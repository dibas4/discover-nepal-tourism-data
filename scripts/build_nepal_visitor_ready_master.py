#!/usr/bin/env python3
"""Build Nepal-wide visitor-ready JSON/CSV from district research + enrichment files.

Canonical place rows come from province/district inventory Markdown tables. Visitor-ready
files add routing/geometry/permit hints. Missing enrichment never deletes a canonical row;
it becomes ROUTING_HOLD/HUB_ONLY until verified.
"""
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
PROVINCES = {
    "bagmati": ("Bagmati", 13, 328),
    "koshi": ("Koshi", 14, 302),
    "madhesh": ("Madhesh", 8, 153),
    "gandaki": ("Gandaki", 11, 237),
    "lumbini": ("Lumbini", 12, 318),
    "karnali": ("Karnali", 10, 284),
    "sudurpashchim": ("Sudurpashchim", 9, 270),
}
EXPECTED_DISTRICTS = 77
EXPECTED_RECORDS = 1892
OUT_DIR = ROOT / "data" / "master" / "generated"


def clean(s: str | None) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


def norm(s: str | None) -> str:
    s = unicodedata.normalize("NFKD", clean(s)).lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return clean(s)


def slug(s: str) -> str:
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", norm(s)))


def strip_md(s: str) -> str:
    s = re.sub(r"\[(.*?)\]\([^)]*\)", r"\1", s)
    return clean(s.replace("**", "").replace("__", "").replace("`", ""))


def split_table_row(line: str) -> list[str]:
    return [strip_md(x) for x in line.strip().strip("|").split("|")]


def is_sep_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells)


def extract_tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    lines = text.splitlines()
    tables = []
    i = 0
    while i + 1 < len(lines):
        if "|" in lines[i] and "|" in lines[i + 1]:
            headers = split_table_row(lines[i])
            sep = split_table_row(lines[i + 1])
            if len(headers) >= 2 and len(sep) == len(headers) and is_sep_row(sep):
                rows = []
                i += 2
                while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
                    cells = split_table_row(lines[i])
                    if len(cells) == len(headers):
                        rows.append(cells)
                    i += 1
                tables.append((headers, rows))
                continue
        i += 1
    return tables


def choose_col(headers: list[str], terms: tuple[str, ...]) -> int | None:
    nh = [norm(h) for h in headers]
    for term in terms:
        for i, h in enumerate(nh):
            if term in h:
                return i
    return None


def parse_inventory(path: Path, province: str) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    out = []
    for headers, rows in extract_tables(text):
        name_i = choose_col(headers, ("place tourism entity", "place landscape", "place destination", "place", "destination", "tourism entity", "site"))
        if name_i is None:
            # Some inventories begin with # then the name column.
            name_i = 1 if headers and norm(headers[0]) in {"#", "no", "sn", "s n"} and len(headers) > 1 else 0
        cat_i = choose_col(headers, ("category",))
        area_i = choose_col(headers, ("municipality area", "municipality", "location area", "area"))
        pri_i = choose_col(headers, ("priority",))
        status_i = choose_col(headers, ("research status", "verification status", "status"))
        note_i = choose_col(headers, ("identification", "notes", "note"))
        for row in rows:
            name = clean(row[name_i]) if name_i < len(row) else ""
            if not name or norm(name) in {"place", "destination", "total"}:
                continue
            out.append({
                "province": province,
                "district": district_from_filename(path),
                "name": name,
                "category": row[cat_i] if cat_i is not None else "",
                "municipality_or_area": row[area_i] if area_i is not None else "",
                "priority": row[pri_i] if pri_i is not None else "",
                "research_status": row[status_i] if status_i is not None else "",
                "research_note": row[note_i] if note_i is not None else "",
                "canonical_source_file": str(path.relative_to(ROOT)),
            })
    # De-duplicate within a district by normalized name while preserving first authoritative row.
    dedup = {}
    for r in out:
        dedup.setdefault(norm(r["name"]), r)
    return list(dedup.values())


def district_from_filename(path: Path) -> str:
    s = path.stem
    s = re.sub(r"(_visitor_ready|-visitor-ready)$", "", s)
    aliases = {"western-rukum": "Western Rukum", "eastern-rukum": "Eastern Rukum", "nawalparasi-west": "Nawalparasi West", "kavrepalanchok": "Kavrepalanchok"}
    return aliases.get(s, s.replace("-", " ").replace("_", " ").title())


def visitor_dir(pdir: Path) -> Path | None:
    for n in ("visitor_ready", "visitor-ready"):
        d = pdir / n
        if d.is_dir():
            return d
    return None


def find_visitor_file(pdir: Path, district: str) -> Path | None:
    vd = visitor_dir(pdir)
    if not vd:
        return None
    ds = slug(district)
    candidates = []
    for f in vd.iterdir():
        if f.is_file() and f.suffix.lower() in {".md", ".yaml", ".yml"} and f.stem.lower() not in {"readme", "complete"}:
            score = 0
            if slug(f.stem) == ds: score += 10
            if ds in slug(f.stem) or slug(f.stem) in ds: score += 4
            candidates.append((score, f))
    candidates.sort(key=lambda x: (-x[0], x[1].name))
    return candidates[0][1] if candidates and candidates[0][0] > 0 else None


def parse_md_enrichment(path: Path) -> dict[str, dict]:
    text = path.read_text(encoding="utf-8")
    m = {}
    rx = re.compile(r"^\s*-\s*\*\*(.+?)\s+[—-]\s+([^:*]+):?\*\*:?\s*(.*)$")
    for line in text.splitlines():
        hit = rx.match(line)
        if not hit:
            continue
        names, gtype, desc = map(clean, hit.groups())
        # Keep grouped bullet as aliases too; individual canonical names can substring-match it.
        rec = {"label": names, "geometry_hint": gtype, "description": desc, "raw": line.strip()}
        m[norm(names)] = rec
        for part in re.split(r",|/|\band\b", names):
            if clean(part):
                m.setdefault(norm(part), rec)
    return m


def flatten_yaml_places(obj) -> list[dict]:
    found = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in {"visitor_areas", "places", "destinations", "visitor_places", "records"} and isinstance(v, list):
                for item in v:
                    if isinstance(item, dict): found.append(item)
            found.extend(flatten_yaml_places(v))
    elif isinstance(obj, list):
        for v in obj: found.extend(flatten_yaml_places(v))
    return found


def parse_yaml_enrichment(path: Path) -> dict[str, dict]:
    if yaml is None:
        return {}
    obj = yaml.safe_load(path.read_text(encoding="utf-8"))
    out = {}
    for item in flatten_yaml_places(obj):
        name = clean(str(item.get("name") or item.get("place") or item.get("title") or item.get("id") or ""))
        if name:
            out[norm(name)] = item
    return out


def infer_geometry(category: str, name: str, hint: str = "") -> str:
    s = norm(" ".join([category, name, hint]))
    if "hold" in s: return "HOLD"
    if any(x in s for x in ("national park", "conservation area", "wildlife reserve", "hunting reserve")): return "PROTECTED_AREA"
    if any(x in s for x in ("lake", "pond", "wetland", "tal ")): return "WATER"
    if any(x in s for x in ("river", "corridor", "valley")): return "CORRIDOR"
    if any(x in s for x in ("trek", "trail", "route", "circuit", "parikrama")): return "ROUTE"
    if any(x in s for x in ("landscape", "village", "town", "bazaar", "ridge", "hill", "forest", "area", "region", "plateau", "highland")): return "AREA"
    return "POINT"


def infer_permits(text: str, geom: str) -> list[str]:
    s = norm(text)
    p = []
    if "restricted" in s: p.append("RESTRICTED_AREA_PERMIT")
    if geom == "PROTECTED_AREA" or any(x in s for x in ("national park", "conservation area", "wildlife reserve")): p.append("PROTECTED_AREA_ENTRY")
    if "climbing permit" in s or "mountaineering permit" in s: p.append("CLIMBING_PERMIT")
    if any(x in s for x in ("border", "customs", "immigration")): p.append("BORDER_CONTROL")
    if any(x in s for x in ("operator", "boating", "rafting", "paragliding", "safari", "cable car")): p.append("OPERATOR_DEPENDENT")
    if any(x in s for x in ("fee", "ticket", "entry")): p.append("ENTRY_FEE")
    if any(x in s for x in ("dynamic", "current", "seasonal", "verify", "check")): p.append("DYNAMIC")
    return list(dict.fromkeys(p)) or ["NONE"]


def best_enrichment(name: str, emap: dict[str, dict]) -> dict | None:
    n = norm(name)
    if n in emap: return emap[n]
    candidates = []
    for k, v in emap.items():
        if n and (n in k or k in n):
            candidates.append((min(len(n), len(k)), v))
    return max(candidates, key=lambda x: x[0])[1] if candidates else None


def enrichment_text(e: dict | None) -> str:
    if not e: return ""
    return clean(" ".join(str(v) for v in e.values() if isinstance(v, (str, int, float, bool))))


def build() -> tuple[list[dict], dict]:
    records = []
    district_seen = set()
    province_stats = {}
    for pslug, (pname, expected_districts, expected_records) in PROVINCES.items():
        pdir = ROOT / "provinces" / pslug
        ddir = pdir / "districts"
        if not ddir.is_dir():
            raise RuntimeError(f"Missing canonical district directory: {ddir}")
        inventory_files = [f for f in sorted(ddir.glob("*.md")) if "visitor_ready" not in f.stem and "visitor-ready" not in f.stem]
        province_records = []
        for f in inventory_files:
            parsed = parse_inventory(f, pname)
            if not parsed: continue
            district = parsed[0]["district"]
            key = (pname, district)
            if key in district_seen: continue
            district_seen.add(key)
            vf = find_visitor_file(pdir, district)
            emap = {}
            if vf:
                emap = parse_yaml_enrichment(vf) if vf.suffix.lower() in {".yaml", ".yml"} else parse_md_enrichment(vf)
            for r in parsed:
                e = best_enrichment(r["name"], emap)
                et = enrichment_text(e)
                hint = clean(str((e or {}).get("geometry_hint") or (e or {}).get("type") or ""))
                geom = infer_geometry(r["category"], r["name"], hint)
                access = "ROUTING_HOLD" if geom == "HOLD" or not e else ("DYNAMIC_CHECK_REQUIRED" if "dynamic" in norm(et) else "ROUTABLE")
                desc = clean(str((e or {}).get("description") or (e or {}).get("intro") or (e or {}).get("short") or ""))
                rec = {
                    "id": f"np-{slug(pname)}-{slug(district)}-{slug(r['name'])}",
                    **r,
                    "introduction": desc or None,
                    "things_to_do": (e or {}).get("things_to_do", []) if isinstance((e or {}).get("things_to_do", []), list) else [],
                    "geometry_type": geom,
                    "access_status": access,
                    "permit_layers": infer_permits(" ".join([r["category"], r["research_note"], et]), geom),
                    "parent_entity_id": None,
                    "visitor_ready_source_file": str(vf.relative_to(ROOT)) if vf else None,
                    "source_record_key": clean(str((e or {}).get("id") or (e or {}).get("name") or "")) or None,
                }
                province_records.append(rec)
        records.extend(province_records)
        province_stats[pname] = {"districts": len({r['district'] for r in province_records}), "records": len(province_records), "expected_districts": expected_districts, "expected_records": expected_records}

    # Parent entity assignment is conservative: normalized name match only.
    registry = json.loads((ROOT / "data/master/nepal_shared_entities.json").read_text(encoding="utf-8"))
    parents = {norm(e["name"]): e["id"] for e in registry["entities"]}
    for r in records:
        if norm(r["name"]) in parents:
            r["parent_entity_id"] = parents[norm(r["name"])]

    qa = {
        "province_stats": province_stats,
        "district_count": len(district_seen),
        "record_count": len(records),
        "expected_district_count": EXPECTED_DISTRICTS,
        "expected_record_count": EXPECTED_RECORDS,
        "district_count_ok": len(district_seen) == EXPECTED_DISTRICTS,
        "record_count_ok": len(records) == EXPECTED_RECORDS,
        "routing_hold_count": sum(r["access_status"] == "ROUTING_HOLD" for r in records),
        "with_visitor_ready_match": sum(bool(r["visitor_ready_source_file"] and r["access_status"] != "ROUTING_HOLD") for r in records),
    }
    return records, qa


def write(records: list[dict], qa: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "nepal_master_visitor_ready.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    columns = ["id","province","district","name","category","municipality_or_area","priority","research_status","geometry_type","access_status","permit_layers","parent_entity_id","canonical_source_file","visitor_ready_source_file"]
    with (OUT_DIR / "nepal_master_visitor_ready.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columns)
        w.writeheader()
        for r in records:
            row = {k: r.get(k) for k in columns}
            row["permit_layers"] = ";".join(r.get("permit_layers") or [])
            w.writerow(row)
    (OUT_DIR / "validation_report.json").write_text(json.dumps(qa, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    records, qa = build()
    write(records, qa)
    print(json.dumps(qa, indent=2))
    if not qa["district_count_ok"] or not qa["record_count_ok"]:
        print("VALIDATION FAILED: canonical counts do not match national integration manifest", file=sys.stderr)
        return 2
    print("VALIDATION PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

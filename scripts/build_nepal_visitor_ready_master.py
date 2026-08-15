#!/usr/bin/env python3
"""Build route-planner-safe Nepal JSON/CSV from the 77 district inventories.

Canonical records always come from researched district inventory tables. Visitor-ready files
only enrich those rows; an enrichment miss never deletes a canonical tourism record. Routing
fails closed: explicit holds and unmatched records remain ROUTING_HOLD. Compact visitor-ready
Markdown can confirm canonical records through conservative name aliases without inventing copy.
"""
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/master/generated"
DISTRICTS = {
    "bagmati": ["bhaktapur", "chitwan", "dhading", "dolakha", "kathmandu", "kavrepalanchok", "lalitpur", "makwanpur", "nuwakot", "ramechhap", "rasuwa", "sindhuli", "sindhupalchok"],
    "koshi": ["bhojpur", "dhankuta", "ilam", "jhapa", "khotang", "morang", "okhaldhunga", "panchthar", "sankhuwasabha", "solukhumbu", "sunsari", "taplejung", "tehrathum", "udayapur"],
    "madhesh": ["bara", "dhanusha", "mahottari", "parsa", "rautahat", "saptari", "sarlahi", "siraha"],
    "gandaki": ["baglung", "gorkha", "kaski", "lamjung", "manang", "mustang", "myagdi", "nawalpur", "parbat", "syangja", "tanahun"],
    "lumbini": ["arghakhanchi", "banke", "bardiya", "dang", "eastern-rukum", "gulmi", "kapilvastu", "nawalparasi-west", "palpa", "pyuthan", "rolpa", "rupandehi"],
    "karnali": ["dailekh", "dolpa", "humla", "jajarkot", "jumla", "kalikot", "mugu", "salyan", "surkhet", "western-rukum"],
    "sudurpashchim": ["achham", "baitadi", "bajhang", "bajura", "dadeldhura", "darchula", "doti", "kailali", "kanchanpur"],
}
PROVINCE_NAMES = {
    "bagmati": "Bagmati",
    "koshi": "Koshi",
    "madhesh": "Madhesh",
    "gandaki": "Gandaki",
    "lumbini": "Lumbini",
    "karnali": "Karnali",
    "sudurpashchim": "Sudurpashchim",
}
EXPECTED = {"Bagmati": 328, "Koshi": 302, "Madhesh": 153, "Gandaki": 237, "Lumbini": 318, "Karnali": 284, "Sudurpashchim": 270}
EXPECTED_TOTAL = 1892
YAML_RECORD_KEYS = {"visitor_areas", "visitor_records", "places", "destinations", "visitor_places", "records"}
GENERIC_NAME_TOKENS = {
    "area", "attraction", "bazaar", "center", "centers", "centre", "centres", "circuit",
    "community", "complex", "conservation", "corridor", "craft", "danda", "destination",
    "durbar", "falls", "forest", "fort", "ghar", "gumba", "heritage", "hill", "homestay",
    "jharana", "landscape", "lake", "mandir", "monastery", "museum", "national", "park",
    "peak", "place", "point", "precinct", "region", "reserve", "route", "settlement", "site",
    "statue", "stupa", "temple", "tourism", "tower", "town", "trail", "valley", "village",
    "view", "viewpoint", "waterfall", "wetland", "wildlife",
}


def clean(value):
    return re.sub(r"\s+", " ", str(value or "").strip())


def norm(value):
    value = unicodedata.normalize("NFKD", clean(value)).lower()
    return clean(re.sub(r"[^a-z0-9]+", " ", value))


def slug(value):
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", norm(value)))


def strip_md(value):
    return clean(re.sub(r"\[(.*?)\]\([^)]*\)", r"\1", value).replace("**", "").replace("__", "").replace("`", ""))


def pretty(slug_name):
    aliases = {"western-rukum": "Western Rukum", "eastern-rukum": "Eastern Rukum", "nawalparasi-west": "Nawalparasi West"}
    return aliases.get(slug_name, slug_name.replace("-", " ").title())


def pretty_key(value):
    return clean(str(value).replace("_", " ").replace("-", " ")).title()


def table_row(line):
    return [strip_md(item) for item in line.strip().strip("|").split("|")]


def separator(cells):
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def tables(text):
    lines = text.splitlines()
    found = []
    index = 0
    while index + 1 < len(lines):
        if "|" in lines[index] and "|" in lines[index + 1]:
            headers = table_row(lines[index])
            divider = table_row(lines[index + 1])
            if len(headers) >= 2 and len(divider) == len(headers) and separator(divider):
                rows = []
                index += 2
                while index < len(lines) and lines[index].strip().startswith("|") and "|" in lines[index]:
                    row = table_row(lines[index])
                    if len(row) == len(headers):
                        rows.append(row)
                    index += 1
                found.append((headers, rows))
                continue
        index += 1
    return found


def column(headers, *terms):
    normalized = [norm(value) for value in headers]
    for term in terms:
        for index, header in enumerate(normalized):
            if term in header:
                return index
    return None


def canonical_file(province_slug, district_slug):
    directory = ROOT / f"provinces/{province_slug}/districts"
    for filename in (f"{district_slug}.md", f"{district_slug.replace('-', '_')}.md"):
        path = directory / filename
        if path.exists():
            return path
    raise FileNotFoundError(f"Missing canonical inventory for {province_slug}/{district_slug}")


def parse_inventory(path, province, district):
    records = []
    for headers, rows in tables(path.read_text(encoding="utf-8")):
        name_index = column(headers, "place tourism entity", "place landscape", "place destination", "place", "destination", "tourism entity", "site")
        if name_index is None:
            name_index = 1 if headers and norm(headers[0]) in {"#", "no", "sn", "s n"} else 0
        category_index = column(headers, "category")
        area_index = column(headers, "municipality area", "municipality", "location area", "area")
        priority_index = column(headers, "priority")
        status_index = column(headers, "research status", "verification status", "status")
        note_index = column(headers, "identification", "notes", "note")
        for row in rows:
            name = clean(row[name_index]) if name_index < len(row) else ""
            if not name or norm(name) in {"place", "destination", "total"}:
                continue
            records.append({
                "province": province,
                "district": district,
                "name": name,
                "category": row[category_index] if category_index is not None else "",
                "municipality_or_area": row[area_index] if area_index is not None else "",
                "priority": row[priority_index] if priority_index is not None else "",
                "research_status": row[status_index] if status_index is not None else "",
                "research_note": row[note_index] if note_index is not None else "",
                "canonical_source_file": str(path.relative_to(ROOT)),
            })
    deduped = {}
    for record in records:
        deduped.setdefault(norm(record["name"]), record)
    return list(deduped.values())


def visitor_file(province_slug, district_slug):
    province_dir = ROOT / f"provinces/{province_slug}"
    for folder in ("visitor_ready", "visitor-ready"):
        directory = province_dir / folder
        if not directory.is_dir():
            continue
        for extension in (".yaml", ".yml", ".md"):
            path = directory / f"{district_slug}{extension}"
            if path.exists():
                return path
    return None


def name_variants(name):
    variants = []

    def add(value):
        value = norm(value)
        if not value or value in variants:
            return
        if len(value.split()) == 1 and len(value) < 5:
            return
        variants.append(value)

    raw_parts = [clean(name)] + [clean(part) for part in re.split(r"\s*/\s*|\s+\bor\b\s+", clean(name), flags=re.I) if clean(part)]
    for raw in raw_parts:
        normalized = norm(raw)
        if not normalized:
            continue
        add(normalized)
        tokens = normalized.split()
        filtered = [token for token in tokens if token not in GENERIC_NAME_TOKENS]
        if filtered and filtered != tokens:
            add(" ".join(filtered))
        trailing = tokens[:]
        while len(trailing) > 1 and trailing[-1] in GENERIC_NAME_TOKENS:
            trailing.pop()
            add(" ".join(trailing))
    return sorted(variants, key=lambda value: (-len(value.split()), -len(value)))


def first_distinctive_token(name):
    for token in norm(name).split():
        if token not in GENERIC_NAME_TOKENS and len(token) >= 7:
            return token
    return ""


def paragraph_context(text, name):
    paragraphs = [clean(part) for part in re.split(r"\n\s*\n", text) if clean(part)]
    variants = name_variants(name)
    if not variants:
        return ""
    for variant in variants:
        for paragraph in paragraphs:
            if variant not in norm(paragraph):
                continue
            clauses = [clean(part) for part in re.split(r";|(?<=[.!?])\s+", paragraph) if clean(part)]
            for clause in clauses:
                if variant in norm(clause):
                    return clause
            return paragraph
    return ""


def md_enrichment(path, canonical_names=()):
    text = path.read_text(encoding="utf-8")
    out = {}

    bullet_pattern = re.compile(r"^\s*-\s*\*\*(.+?)\s+[—-]\s+([^:*]+):?\*\*:?\s*(.*)$")
    for line in text.splitlines():
        match = bullet_pattern.match(line)
        if not match:
            continue
        names, geometry_type, description = map(clean, match.groups())
        record = {"label": names, "geometry_hint": geometry_type, "description": description, "raw": line.strip()}
        out[norm(names)] = record
        for part in re.split(r",|/|\band\b", names):
            if clean(part):
                out.setdefault(norm(part), record)

    heading_pattern = re.compile(r"^###\s+(?:\d+\.\s*)?(.+?)\s*$")
    field_pattern = re.compile(r"^\*\*(.+?):\*\*\s*(.*)$")
    current = None
    for line in text.splitlines() + ["### __END__"]:
        heading = heading_pattern.match(line.strip())
        if heading:
            if current and current.get("name"):
                name = clean(current["name"])
                record = {
                    "name": name,
                    "type": current.get("type"),
                    "geometry_hint": current.get("geometry"),
                    "intro": current.get("introduction"),
                    "things_to_do": [item.strip() for item in re.split(r",|;", current.get("things to do", "")) if item.strip()],
                    "permit_entry": current.get("permit / entry") or current.get("permit entry"),
                    "how_to_visit": current.get("how to visit"),
                    "status": current.get("status") or current.get("routing note"),
                }
                out.setdefault(norm(name), record)
                for part in re.split(r"\s*/\s*", name):
                    if clean(part):
                        out.setdefault(norm(part), record)
            current = {"name": clean(heading.group(1))} if heading.group(1) != "__END__" else None
            continue
        if not current:
            continue
        field = field_pattern.match(line.strip())
        if field:
            current[norm(field.group(1))] = clean(field.group(2))

    distinctive_roots = [first_distinctive_token(name) for name in canonical_names]
    root_counts = Counter(root for root in distinctive_roots if root)
    for name in canonical_names:
        key = norm(name)
        if not key or key in out:
            continue
        context = paragraph_context(text, name)
        match_method = "mention"
        if not context:
            root = first_distinctive_token(name)
            if root and root_counts[root] == 1:
                context = paragraph_context(text, root)
                match_method = "root-mention"
        if not context:
            continue
        out[key] = {
            "name": name,
            "geometry_hint": context,
            "status": context,
            "raw": context,
            "mention_only": True,
            "mention_match_method": match_method,
        }
    return out


def yaml_nodes(value):
    found = []
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in YAML_RECORD_KEYS and isinstance(nested, list):
                found += [item for item in nested if isinstance(item, dict)]
                continue
            found += yaml_nodes(nested)
    elif isinstance(value, list):
        for nested in value:
            found += yaml_nodes(nested)
    return found


def yaml_enrichment(path):
    if yaml is None:
        raise RuntimeError("PyYAML is required: pip install PyYAML")
    out = {}
    for record in yaml_nodes(yaml.safe_load(path.read_text(encoding="utf-8"))):
        names = []
        primary = clean(record.get("name") or record.get("place") or record.get("title") or record.get("id"))
        if primary:
            names.append(primary)
        aliases = record.get("aliases") or record.get("alternate_names") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        if isinstance(aliases, list):
            names += [clean(value) for value in aliases if isinstance(value, (str, int, float)) and clean(value)]
        record_id = clean(record.get("id"))
        if record_id:
            names.append(record_id)
        for name in names:
            out.setdefault(norm(name), record)
    return out


def best_match(name, enrichment_map):
    target = norm(name)
    if target in enrichment_map:
        record = enrichment_map[target]
        if record.get("mention_only"):
            return record, record.get("mention_match_method") or "mention"
        return record, "exact"
    candidates = [(min(len(target), len(key)), key, record) for key, record in enrichment_map.items() if target and (target in key or key in target)]
    if not candidates:
        return None, None
    _, _, record = max(candidates, key=lambda item: (item[0], -abs(len(target) - len(item[1]))))
    return record, "fuzzy"


def flat_text(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (str, int, float)):
        return clean(value)
    if isinstance(value, dict):
        return clean(" ".join(flat_text(nested) for nested in value.values()))
    if isinstance(value, list):
        return clean(" ".join(flat_text(nested) for nested in value))
    return ""


def readable(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, (str, int, float)):
        return clean(value)
    if isinstance(value, list):
        return "; ".join(filter(None, (readable(nested) for nested in value)))
    if isinstance(value, dict):
        parts = []
        for key, nested in value.items():
            rendered = readable(nested)
            if rendered:
                parts.append(f"{pretty_key(key)}: {rendered}")
        return "; ".join(parts)
    return ""


def public_access_text(value):
    if isinstance(value, str):
        text = clean(value)
        if re.search(r"\b(routing hold|do not route|do not publish)\b", text, re.I):
            return ""
        return text
    if not isinstance(value, dict):
        return ""
    blocked = re.compile(r"(^|_)(do_not|navigation_rule|routing|route_status|coordinate|exact_pin|exact_departure)", re.I)
    parts = []
    for key, nested in value.items():
        if blocked.search(str(key)) or not isinstance(nested, str):
            continue
        text = clean(nested)
        if not text or re.search(r"\b(routing hold|do not route|do not publish)\b", text, re.I):
            continue
        parts.append(f"{pretty_key(key)}: {text}")
    return "; ".join(parts)


def first_value(record, *keys):
    for key in keys:
        if key in record and record[key] not in (None, "", [], {}):
            return record[key]
    return None


def activity_strings(value):
    if not isinstance(value, list):
        return []
    activities = []
    for item in value:
        if isinstance(item, (str, int, float)):
            label = clean(item)
        elif isinstance(item, dict):
            label = clean(first_value(item, "activity", "name", "title", "label"))
        else:
            label = ""
        if label and label not in activities:
            activities.append(label)
    return activities


def geometry_hint(enrichment):
    if not enrichment:
        return ""
    parts = [clean(enrichment.get("geometry_hint")), clean(enrichment.get("geometry_type")), clean(enrichment.get("type"))]
    geometry_value = enrichment.get("geometry")
    if isinstance(geometry_value, str):
        parts.append(clean(geometry_value))
    elif isinstance(geometry_value, dict):
        for key in ("type", "geometry_type", "coordinate_status", "coordinate_quality"):
            parts.append(clean(geometry_value.get(key)))
    return clean(" ".join(filter(None, parts)))


def geometry(category, name, hint=""):
    specific = norm(f"{hint} {name}")
    fallback = norm(f"{name} {category}")
    if "hold" in specific:
        return "HOLD"
    if any(token in specific for token in ("national park", "conservation area", "wildlife reserve", "hunting reserve", "protected area")):
        return "PROTECTED_AREA"
    if any(token in specific for token in ("lake", "pond", "wetland", "ramsar")):
        return "WATER"
    if any(token in specific for token in ("point", "waterfall", "falls", "jharana", "temple", "monastery", "stupa", "museum", "statue", "facility", "fort", "cave", "gufa")):
        return "POINT"
    if any(token in specific for token in ("route", "trail", "circuit", "parikrama")):
        return "ROUTE"
    if "corridor" in specific:
        return "CORRIDOR"
    if any(token in specific for token in ("area", "landscape", "village", "town", "bazaar", "ridge", "hill", "forest", "region", "plateau", "highland", "valley", "settlement", "danda", "peak", "summit", "viewpoint", "pass")):
        return "AREA"
    if any(token in fallback for token in ("national park", "conservation area", "wildlife reserve", "hunting reserve")):
        return "PROTECTED_AREA"
    if any(token in fallback for token in ("lake", "pond", "wetland")):
        return "WATER"
    if any(token in fallback for token in ("waterfall", "falls", "jharana", "cave", "gufa")):
        return "POINT"
    if any(token in fallback for token in ("trek", "trail", "route", "circuit", "parikrama")):
        return "ROUTE"
    if any(token in fallback for token in ("river", "corridor")):
        return "CORRIDOR"
    if any(token in fallback for token in ("landscape", "village", "town", "bazaar", "ridge", "hill", "forest", "area", "region", "plateau", "highland", "valley", "danda", "peak", "viewpoint", "pass")):
        return "AREA"
    return "POINT"


def explicit_routing_hold(enrichment, text):
    status = norm(flat_text(first_value(enrichment or {}, "status", "routing_status", "route_status", "access_status", "coordinate_status")))
    combined = norm(f"{status} {text}")
    return bool(re.search(r"\b(routing hold|do not route|route hold|status hold|geometry hold)\b", combined))


def dynamic_access(text):
    normalized = norm(text)
    return any(token in normalized for token in (
        "dynamic", "current conditions", "check locally", "verify locally", "seasonal", "pending current",
        "current operation", "gis verification", "verification before navigation", "verified access node",
        "exact entrance", "exact trailhead", "pin require", "entrance level gis", "access to be checked",
    ))


def permits(text, geometry_type):
    normalized = norm(text)
    layers = []
    no_restricted = bool(re.search(r"\b(no|false|not required|does not require)\b.{0,24}\b(restricted|special).*permit\b|\brestricted.*permit\b.{0,16}\b(no|false|not required)\b", normalized))
    if "restricted" in normalized and "permit" in normalized and not no_restricted:
        layers.append("RESTRICTED_AREA_PERMIT")
    if geometry_type == "PROTECTED_AREA" or any(token in normalized for token in ("national park", "conservation area", "wildlife reserve")):
        layers.append("PROTECTED_AREA_ENTRY")
    if "climbing permit" in normalized or "mountaineering permit" in normalized:
        layers.append("CLIMBING_PERMIT")
    if any(token in normalized for token in ("border", "customs", "immigration")):
        layers.append("BORDER_CONTROL")
    if any(token in normalized for token in ("operator", "boating", "rafting", "paragliding", "safari", "cable car")):
        layers.append("OPERATOR_DEPENDENT")
    if any(token in normalized for token in ("fee", "ticket", "entry")) and not re.search(r"\b(no|none|false)\b.{0,16}\b(entry fee|ticket|fee)\b", normalized):
        layers.append("ENTRY_FEE")
    if any(token in normalized for token in ("dynamic", "current", "seasonal", "verify", "check")):
        layers.append("DYNAMIC")
    return list(dict.fromkeys(layers)) or ["NONE"]


def record_fields(enrichment):
    enrichment = enrichment or {}
    if enrichment.get("mention_only"):
        return None, [], None, None
    introduction = clean(first_value(enrichment, "description", "intro", "short")) or None
    activities = activity_strings(enrichment.get("things_to_do", []))
    permit_value = first_value(enrichment, "permit", "permits", "permit_entry", "permit_entry_text", "permits_and_entry", "permits_entry", "permit_framework")
    access_value = first_value(enrichment, "how_to_visit", "access", "access_guidance")
    permit_text = readable(permit_value) or None
    how_to_visit = public_access_text(access_value) or None
    return introduction, activities, permit_text, how_to_visit


def build():
    records = []
    province_stats = {}
    districts = []
    registry = json.loads((ROOT / "data/master/nepal_shared_entities.json").read_text(encoding="utf-8"))
    parent_ids = {norm(item["name"]): item["id"] for item in registry["entities"]}

    for province_slug, district_slugs in DISTRICTS.items():
        province = PROVINCE_NAMES[province_slug]
        before = len(records)
        for district_slug in district_slugs:
            district = pretty(district_slug)
            districts.append((province, district))
            canonical_path = canonical_file(province_slug, district_slug)
            canonical_records = parse_inventory(canonical_path, province, district)
            visitor_path = visitor_file(province_slug, district_slug)
            enrichment_map = {}
            if visitor_path:
                enrichment_map = yaml_enrichment(visitor_path) if visitor_path.suffix.lower() in {".yaml", ".yml"} else md_enrichment(visitor_path, [record["name"] for record in canonical_records])

            for canonical in canonical_records:
                enrichment, match_method = best_match(canonical["name"], enrichment_map)
                enrichment_text = flat_text(enrichment)
                geometry_type = geometry(canonical["category"], canonical["name"], geometry_hint(enrichment))
                matched = bool(enrichment)
                introduction, activities, permit_text, how_to_visit = record_fields(enrichment)
                routing_hold = geometry_type == "HOLD" or not matched or explicit_routing_hold(enrichment, enrichment_text)
                access_status = "ROUTING_HOLD" if routing_hold else ("DYNAMIC_CHECK_REQUIRED" if dynamic_access(enrichment_text) else "ROUTABLE")
                source_routing_status = "routing_hold" if routing_hold else ("dynamic_check_required" if access_status == "DYNAMIC_CHECK_REQUIRED" else "routable")
                source_key = clean(first_value(enrichment or {}, "id", "name", "place", "title")) or None

                records.append({
                    "id": f"np-{slug(province)}-{slug(district)}-{slug(canonical['name'])}",
                    **canonical,
                    "introduction": introduction,
                    "things_to_do": activities,
                    "geometry_type": geometry_type,
                    "source_routing_status": source_routing_status,
                    "access_status": access_status,
                    "permit_layers": permits(f"{canonical['category']} {canonical['research_note']} {permit_text or ''} {enrichment_text}", geometry_type),
                    "parent_entity_id": parent_ids.get(norm(canonical["name"])),
                    "visitor_ready_label": clean(first_value(enrichment or {}, "name", "place", "title", "id")) or None,
                    "match_method": match_method,
                    "permit_entry_text": permit_text,
                    "how_to_visit": how_to_visit,
                    "visitor_ready_source_file": str(visitor_path.relative_to(ROOT)) if visitor_path else None,
                    "source_record_key": source_key,
                })
        province_stats[province] = {"districts": len(district_slugs), "records": len(records) - before, "expected_records": EXPECTED[province]}

    explicit_hold_routed = [record for record in records if record.get("source_routing_status") == "routing_hold" and record.get("access_status") != "ROUTING_HOLD"]
    routable_without_match = [record for record in records if record.get("access_status") != "ROUTING_HOLD" and not record.get("match_method")]
    waterfall_corridors = [record for record in records if "waterfall" in norm(record.get("name")) and record.get("geometry_type") == "CORRIDOR"]
    kavre = [record for record in records if record["province"] == "Bagmati" and record["district"] == "Kavrepalanchok"]
    kavre_matches = sum(bool(record.get("match_method")) for record in kavre)
    unmatched = [record for record in records if not record.get("match_method")]

    qa = {
        "province_stats": province_stats,
        "district_count": len(districts),
        "record_count": len(records),
        "expected_district_count": 77,
        "expected_record_count": EXPECTED_TOTAL,
        "district_count_ok": len(districts) == 77,
        "record_count_ok": len(records) == EXPECTED_TOTAL,
        "province_record_counts_ok": all(value["records"] == value["expected_records"] for value in province_stats.values()),
        "routing_hold_count": sum(record["access_status"] == "ROUTING_HOLD" for record in records),
        "visitor_ready_match_count": sum(bool(record.get("match_method")) for record in records),
        "unmatched_visitor_ready_count": len(unmatched),
        "unmatched_visitor_ready_examples": [f"{record['province']}/{record['district']}/{record['name']}" for record in unmatched[:25]],
        "routable_record_count": sum(record["access_status"] != "ROUTING_HOLD" for record in records),
        "explicit_hold_routed_count": len(explicit_hold_routed),
        "explicit_hold_routed_ok": not explicit_hold_routed,
        "routable_without_match_count": len(routable_without_match),
        "routable_without_match_ok": not routable_without_match,
        "waterfall_corridor_count": len(waterfall_corridors),
        "waterfall_geometry_ok": not waterfall_corridors,
        "kavrepalanchok_visitor_ready_match_count": kavre_matches,
        "kavrepalanchok_expected_visitor_ready_match_count": 32,
        "kavrepalanchok_visitor_ready_ok": kavre_matches == 32,
    }
    return records, qa


def write(records, qa):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "nepal_master_visitor_ready.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    columns = [
        "id", "province", "district", "name", "category", "municipality_or_area", "priority", "research_status",
        "geometry_type", "source_routing_status", "access_status", "permit_layers", "parent_entity_id", "visitor_ready_label",
        "match_method", "permit_entry_text", "how_to_visit", "canonical_source_file", "visitor_ready_source_file",
    ]
    with (OUT / "nepal_master_visitor_ready.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for record in records:
            row = {key: record.get(key) for key in columns}
            row["permit_layers"] = ";".join(record.get("permit_layers") or [])
            writer.writerow(row)
    (OUT / "validation_report.json").write_text(json.dumps(qa, indent=2) + "\n", encoding="utf-8")


def main():
    records, qa = build()
    write(records, qa)
    print(json.dumps(qa, indent=2))
    valid = (
        qa["district_count_ok"]
        and qa["record_count_ok"]
        and qa["province_record_counts_ok"]
        and qa["explicit_hold_routed_ok"]
        and qa["routable_without_match_ok"]
        and qa["waterfall_geometry_ok"]
        and qa["kavrepalanchok_visitor_ready_ok"]
    )
    print("VALIDATION PASSED" if valid else "VALIDATION FAILED", file=sys.stdout if valid else sys.stderr)
    return 0 if valid else 2


if __name__ == "__main__":
    raise SystemExit(main())

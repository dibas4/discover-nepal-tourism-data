#!/usr/bin/env python3
"""Build route-planner-safe Nepal JSON/CSV from the 77 district inventories.

Canonical records always come from the researched district inventory tables. Visitor-ready
files only enrich those rows; an enrichment miss never deletes a canonical tourism record.
"""
from __future__ import annotations
import csv, json, re, sys, unicodedata
from pathlib import Path
try:
    import yaml  # type: ignore
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/master/generated"
DISTRICTS = {
 "bagmati": ["bhaktapur","chitwan","dhading","dolakha","kathmandu","kavrepalanchok","lalitpur","makwanpur","nuwakot","ramechhap","rasuwa","sindhuli","sindhupalchok"],
 "koshi": ["bhojpur","dhankuta","ilam","jhapa","khotang","morang","okhaldhunga","panchthar","sankhuwasabha","solukhumbu","sunsari","taplejung","tehrathum","udayapur"],
 "madhesh": ["bara","dhanusha","mahottari","parsa","rautahat","saptari","sarlahi","siraha"],
 "gandaki": ["baglung","gorkha","kaski","lamjung","manang","mustang","myagdi","nawalpur","parbat","syangja","tanahun"],
 "lumbini": ["arghakhanchi","banke","bardiya","dang","eastern-rukum","gulmi","kapilvastu","nawalparasi-west","palpa","pyuthan","rolpa","rupandehi"],
 "karnali": ["dailekh","dolpa","humla","jajarkot","jumla","kalikot","mugu","salyan","surkhet","western-rukum"],
 "sudurpashchim": ["achham","baitadi","bajhang","bajura","dadeldhura","darchula","doti","kailali","kanchanpur"]
}
PROVINCE_NAMES = {"bagmati":"Bagmati","koshi":"Koshi","madhesh":"Madhesh","gandaki":"Gandaki","lumbini":"Lumbini","karnali":"Karnali","sudurpashchim":"Sudurpashchim"}
EXPECTED = {"Bagmati":328,"Koshi":302,"Madhesh":153,"Gandaki":237,"Lumbini":318,"Karnali":284,"Sudurpashchim":270}
EXPECTED_TOTAL = 1892


def clean(s): return re.sub(r"\s+"," ",str(s or "").strip())
def norm(s):
    s=unicodedata.normalize("NFKD",clean(s)).lower(); return clean(re.sub(r"[^a-z0-9]+"," ",s))
def slug(s): return re.sub(r"^-|-$","",re.sub(r"[^a-z0-9]+","-",norm(s)))
def strip_md(s): return clean(re.sub(r"\[(.*?)\]\([^)]*\)",r"\1",s).replace("**","").replace("__","").replace("`",""))
def pretty(slug_name):
    aliases={"western-rukum":"Western Rukum","eastern-rukum":"Eastern Rukum","nawalparasi-west":"Nawalparasi West"}
    return aliases.get(slug_name,slug_name.replace("-"," ").title())

def table_row(line): return [strip_md(x) for x in line.strip().strip("|").split("|")]
def sep(cells): return bool(cells) and all(re.fullmatch(r":?-{3,}:?",c.replace(" ","")) for c in cells)
def tables(text):
    ls=text.splitlines(); out=[]; i=0
    while i+1<len(ls):
        if "|" in ls[i] and "|" in ls[i+1]:
            h=table_row(ls[i]); s=table_row(ls[i+1])
            if len(h)>=2 and len(s)==len(h) and sep(s):
                rows=[]; i+=2
                while i<len(ls) and ls[i].strip().startswith("|") and "|" in ls[i]:
                    r=table_row(ls[i]);
                    if len(r)==len(h): rows.append(r)
                    i+=1
                out.append((h,rows)); continue
        i+=1
    return out

def col(headers,*terms):
    hs=[norm(x) for x in headers]
    for t in terms:
        for i,h in enumerate(hs):
            if t in h: return i
    return None

def canonical_file(pslug,dslug):
    d=ROOT/f"provinces/{pslug}/districts"
    for name in (f"{dslug}.md",f"{dslug.replace('-','_')}.md"):
        p=d/name
        if p.exists(): return p
    raise FileNotFoundError(f"Missing canonical inventory for {pslug}/{dslug}")

def parse_inventory(path,province,district):
    rows=[]
    for h,rs in tables(path.read_text(encoding="utf-8")):
        ni=col(h,"place tourism entity","place landscape","place destination","place","destination","tourism entity","site")
        if ni is None: ni=1 if h and norm(h[0]) in {"#","no","sn","s n"} else 0
        ci=col(h,"category"); ai=col(h,"municipality area","municipality","location area","area")
        pi=col(h,"priority"); si=col(h,"research status","verification status","status"); xi=col(h,"identification","notes","note")
        for r in rs:
            name=clean(r[ni]) if ni<len(r) else ""
            if not name or norm(name) in {"place","destination","total"}: continue
            rows.append({"province":province,"district":district,"name":name,"category":r[ci] if ci is not None else "","municipality_or_area":r[ai] if ai is not None else "","priority":r[pi] if pi is not None else "","research_status":r[si] if si is not None else "","research_note":r[xi] if xi is not None else "","canonical_source_file":str(path.relative_to(ROOT))})
    dedup={}
    for r in rows: dedup.setdefault(norm(r["name"]),r)
    return list(dedup.values())

def visitor_file(pslug,dslug):
    pdir=ROOT/f"provinces/{pslug}"
    # Integrated Bagmati normalized the three Valley files to .md and other Bagmati files retain YAML.
    for folder in ("visitor_ready","visitor-ready"):
        d=pdir/folder
        if not d.is_dir(): continue
        for ext in (".yaml",".yml",".md"):
            p=d/f"{dslug}{ext}"
            if p.exists(): return p
    return None

def md_enrichment(path):
    out={}; rx=re.compile(r"^\s*-\s*\*\*(.+?)\s+[—-]\s+([^:*]+):?\*\*:?\s*(.*)$")
    for line in path.read_text(encoding="utf-8").splitlines():
        m=rx.match(line)
        if not m: continue
        names,gtype,desc=map(clean,m.groups()); rec={"label":names,"geometry_hint":gtype,"description":desc,"raw":line.strip()}
        out[norm(names)]=rec
        for part in re.split(r",|/|\band\b",names):
            if clean(part): out.setdefault(norm(part),rec)
    return out

def yaml_nodes(obj):
    found=[]
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k in {"visitor_areas","places","destinations","visitor_places","records"} and isinstance(v,list): found += [x for x in v if isinstance(x,dict)]
            found += yaml_nodes(v)
    elif isinstance(obj,list):
        for v in obj: found += yaml_nodes(v)
    return found

def yaml_enrichment(path):
    if yaml is None: raise RuntimeError("PyYAML is required: pip install -r requirements-data.txt")
    out={}
    for x in yaml_nodes(yaml.safe_load(path.read_text(encoding="utf-8"))):
        name=clean(x.get("name") or x.get("place") or x.get("title") or x.get("id"))
        if name: out[norm(name)]=x
    return out

def best(name,emap):
    n=norm(name)
    if n in emap: return emap[n]
    c=[(min(len(n),len(k)),v) for k,v in emap.items() if n and (n in k or k in n)]
    return max(c,key=lambda z:z[0])[1] if c else None

def etext(e): return clean(" ".join(str(v) for v in (e or {}).values() if isinstance(v,(str,int,float,bool))))
def geometry(category,name,hint=""):
    s=norm(f"{category} {name} {hint}")
    if "hold" in s:return "HOLD"
    if any(x in s for x in ("national park","conservation area","wildlife reserve","hunting reserve")):return "PROTECTED_AREA"
    if any(x in s for x in ("lake","pond","wetland")):return "WATER"
    if any(x in s for x in ("river","corridor","valley")):return "CORRIDOR"
    if any(x in s for x in ("trek","trail","route","circuit","parikrama")):return "ROUTE"
    if any(x in s for x in ("landscape","village","town","bazaar","ridge","hill","forest","area","region","plateau","highland")):return "AREA"
    return "POINT"
def permits(text,g):
    s=norm(text); p=[]
    if "restricted" in s:p.append("RESTRICTED_AREA_PERMIT")
    if g=="PROTECTED_AREA" or any(x in s for x in ("national park","conservation area","wildlife reserve")):p.append("PROTECTED_AREA_ENTRY")
    if "climbing permit" in s or "mountaineering permit" in s:p.append("CLIMBING_PERMIT")
    if any(x in s for x in ("border","customs","immigration")):p.append("BORDER_CONTROL")
    if any(x in s for x in ("operator","boating","rafting","paragliding","safari","cable car")):p.append("OPERATOR_DEPENDENT")
    if any(x in s for x in ("fee","ticket","entry")):p.append("ENTRY_FEE")
    if any(x in s for x in ("dynamic","current","seasonal","verify","check")):p.append("DYNAMIC")
    return list(dict.fromkeys(p)) or ["NONE"]

def build():
    records=[]; stats={}; districts=[]
    registry=json.loads((ROOT/"data/master/nepal_shared_entities.json").read_text(encoding="utf-8"))
    parents={norm(x["name"]):x["id"] for x in registry["entities"]}
    for pslug,dslugs in DISTRICTS.items():
        pname=PROVINCE_NAMES[pslug]; before=len(records)
        for dslug in dslugs:
            district=pretty(dslug); districts.append((pname,district))
            cf=canonical_file(pslug,dslug); vf=visitor_file(pslug,dslug)
            emap={}
            if vf: emap=yaml_enrichment(vf) if vf.suffix.lower() in {".yaml",".yml"} else md_enrichment(vf)
            for r in parse_inventory(cf,pname,district):
                e=best(r["name"],emap); text=etext(e); hint=clean((e or {}).get("geometry_hint") or (e or {}).get("type"))
                g=geometry(r["category"],r["name"],hint); matched=bool(e)
                rec={"id":f"np-{slug(pname)}-{slug(district)}-{slug(r['name'])}",**r,
                     "introduction":clean((e or {}).get("description") or (e or {}).get("intro") or (e or {}).get("short")) or None,
                     "things_to_do":(e or {}).get("things_to_do",[]) if isinstance((e or {}).get("things_to_do",[]),list) else [],
                     "geometry_type":g,"access_status":"ROUTING_HOLD" if g=="HOLD" or not matched else ("DYNAMIC_CHECK_REQUIRED" if "dynamic" in norm(text) else "ROUTABLE"),
                     "permit_layers":permits(f"{r['category']} {r['research_note']} {text}",g),
                     "parent_entity_id":parents.get(norm(r["name"])),
                     "visitor_ready_source_file":str(vf.relative_to(ROOT)) if vf else None,
                     "source_record_key":clean((e or {}).get("id") or (e or {}).get("name")) or None}
                records.append(rec)
        stats[pname]={"districts":len(dslugs),"records":len(records)-before,"expected_records":EXPECTED[pname]}
    qa={"province_stats":stats,"district_count":len(districts),"record_count":len(records),"expected_district_count":77,"expected_record_count":EXPECTED_TOTAL,
        "district_count_ok":len(districts)==77,"record_count_ok":len(records)==EXPECTED_TOTAL,
        "province_record_counts_ok":all(v["records"]==v["expected_records"] for v in stats.values()),
        "routing_hold_count":sum(r["access_status"]=="ROUTING_HOLD" for r in records),
        "visitor_ready_match_count":sum(r["access_status"]!="ROUTING_HOLD" for r in records)}
    return records,qa

def write(records,qa):
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"nepal_master_visitor_ready.json").write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    cols=["id","province","district","name","category","municipality_or_area","priority","research_status","geometry_type","access_status","permit_layers","parent_entity_id","canonical_source_file","visitor_ready_source_file"]
    with (OUT/"nepal_master_visitor_ready.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
        for r in records:
            x={k:r.get(k) for k in cols};x["permit_layers"]=";".join(r.get("permit_layers") or []);w.writerow(x)
    (OUT/"validation_report.json").write_text(json.dumps(qa,indent=2)+"\n",encoding="utf-8")

def main():
    records,qa=build();write(records,qa);print(json.dumps(qa,indent=2))
    ok=qa["district_count_ok"] and qa["record_count_ok"] and qa["province_record_counts_ok"]
    print("VALIDATION PASSED" if ok else "VALIDATION FAILED",file=sys.stdout if ok else sys.stderr)
    return 0 if ok else 2
if __name__=="__main__": raise SystemExit(main())

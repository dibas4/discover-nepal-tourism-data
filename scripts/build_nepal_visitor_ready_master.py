#!/usr/bin/env python3
"""Build route-planner-safe Nepal JSON/CSV from the 77 district inventories.

Canonical records always come from the researched district inventory tables. Visitor-ready
files only enrich those rows; an enrichment miss never deletes a canonical tourism record.
The generated master fails closed for routing: unmatched records and explicit routing holds
remain ROUTING_HOLD, while traveler-facing enrichment is preserved for downstream apps.
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
YAML_RECORD_KEYS = {"visitor_areas","visitor_records","places","destinations","visitor_places","records"}


def clean(s): return re.sub(r"\s+"," ",str(s or "").strip())
def norm(s):
    s=unicodedata.normalize("NFKD",clean(s)).lower(); return clean(re.sub(r"[^a-z0-9]+"," ",s))
def slug(s): return re.sub(r"^-|-$","",re.sub(r"[^a-z0-9]+","-",norm(s)))
def strip_md(s): return clean(re.sub(r"\[(.*?)\]\([^)]*\)",r"\1",s).replace("**","").replace("__","").replace("`",""))
def pretty(slug_name):
    aliases={"western-rukum":"Western Rukum","eastern-rukum":"Eastern Rukum","nawalparasi-west":"Nawalparasi West"}
    return aliases.get(slug_name,slug_name.replace("-"," ").title())
def pretty_key(value): return clean(str(value).replace("_"," ").replace("-"," ")).title()

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
    for folder in ("visitor_ready","visitor-ready"):
        d=pdir/folder
        if not d.is_dir(): continue
        for ext in (".yaml",".yml",".md"):
            p=d/f"{dslug}{ext}"
            if p.exists(): return p
    return None

def md_enrichment(path):
    text=path.read_text(encoding="utf-8")
    out={}; rx=re.compile(r"^\s*-\s*\*\*(.+?)\s+[—-]\s+([^:*]+):?\*\*:?\s*(.*)$")
    for line in text.splitlines():
        m=rx.match(line)
        if not m: continue
        names,gtype,desc=map(clean,m.groups()); rec={"label":names,"geometry_hint":gtype,"description":desc,"raw":line.strip()}
        out[norm(names)]=rec
        for part in re.split(r",|/|\band\b",names):
            if clean(part): out.setdefault(norm(part),rec)

    # Bagmati's longer visitor-ready Markdown uses numbered H3 sections and bold fields.
    # Parse those sections without treating unrelated prose as a routable record.
    heading_rx=re.compile(r"^###\s+(?:\d+\.\s*)?(.+?)\s*$")
    field_rx=re.compile(r"^\*\*(.+?):\*\*\s*(.*)$")
    current=None
    for line in text.splitlines()+["### __END__"]:
        heading=heading_rx.match(line.strip())
        if heading:
            if current and current.get("name"):
                name=clean(current["name"])
                rec={
                    "name":name,
                    "type":current.get("type"),
                    "geometry_hint":current.get("geometry"),
                    "intro":current.get("introduction"),
                    "things_to_do":[x.strip() for x in re.split(r",|;",current.get("things to do", "")) if x.strip()],
                    "permit_entry":current.get("permit / entry") or current.get("permit entry"),
                    "how_to_visit":current.get("how to visit"),
                    "status":current.get("status") or current.get("routing note"),
                }
                out.setdefault(norm(name),rec)
                for part in re.split(r"\s*/\s*",name):
                    if clean(part): out.setdefault(norm(part),rec)
            current={"name":clean(heading.group(1))} if heading.group(1)!="__END__" else None
            continue
        if not current: continue
        field=field_rx.match(line.strip())
        if field:
            current[norm(field.group(1))]=clean(field.group(2))
    return out

def yaml_nodes(obj):
    found=[]
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k in YAML_RECORD_KEYS and isinstance(v,list):
                found += [x for x in v if isinstance(x,dict)]
                continue
            found += yaml_nodes(v)
    elif isinstance(obj,list):
        for v in obj: found += yaml_nodes(v)
    return found

def yaml_enrichment(path):
    if yaml is None: raise RuntimeError("PyYAML is required: pip install -r requirements-data.txt")
    out={}
    for x in yaml_nodes(yaml.safe_load(path.read_text(encoding="utf-8"))):
        names=[]
        primary=clean(x.get("name") or x.get("place") or x.get("title") or x.get("id"))
        if primary: names.append(primary)
        aliases=x.get("aliases") or x.get("alternate_names") or []
        if isinstance(aliases,str): aliases=[aliases]
        if isinstance(aliases,list): names += [clean(v) for v in aliases if isinstance(v,(str,int,float)) and clean(v)]
        record_id=clean(x.get("id"))
        if record_id: names.append(record_id)
        for name in names:
            out.setdefault(norm(name),x)
    return out

def best_match(name,emap):
    n=norm(name)
    if n in emap: return emap[n],"exact"
    candidates=[(min(len(n),len(k)),k,v) for k,v in emap.items() if n and (n in k or k in n)]
    if not candidates: return None,None
    _,_,value=max(candidates,key=lambda z:(z[0],-abs(len(n)-len(z[1]))))
    return value,"fuzzy"

def flat_text(value):
    if value is None: return ""
    if isinstance(value,bool): return "true" if value else "false"
    if isinstance(value,(str,int,float)): return clean(value)
    if isinstance(value,dict): return clean(" ".join(flat_text(v) for v in value.values()))
    if isinstance(value,list): return clean(" ".join(flat_text(v) for v in value))
    return ""

def readable(value):
    if value is None: return ""
    if isinstance(value,bool): return "yes" if value else "no"
    if isinstance(value,(str,int,float)): return clean(value)
    if isinstance(value,list): return "; ".join(filter(None,(readable(v) for v in value)))
    if isinstance(value,dict):
        parts=[]
        for k,v in value.items():
            rendered=readable(v)
            if rendered: parts.append(f"{pretty_key(k)}: {rendered}")
        return "; ".join(parts)
    return ""

def first_value(record,*keys):
    for key in keys:
        if key in record and record[key] not in (None,"",[],{}): return record[key]
    return None

def activity_strings(value):
    if not isinstance(value,list): return []
    out=[]
    for item in value:
        if isinstance(item,(str,int,float)):
            label=clean(item)
        elif isinstance(item,dict):
            label=clean(first_value(item,"activity","name","title","label"))
        else:
            label=""
        if label and label not in out: out.append(label)
    return out

def geometry_hint(e):
    if not e: return ""
    parts=[clean(e.get("geometry_hint")),clean(e.get("geometry_type")),clean(e.get("type"))]
    geometry_value=e.get("geometry")
    if isinstance(geometry_value,str): parts.append(clean(geometry_value))
    elif isinstance(geometry_value,dict):
        for key in ("type","geometry_type","coordinate_status","coordinate_quality"):
            parts.append(clean(geometry_value.get(key)))
    return clean(" ".join(filter(None,parts)))

def geometry(category,name,hint=""):
    specific=norm(f"{hint} {name}")
    fallback=norm(f"{name} {category}")
    if "hold" in specific:return "HOLD"
    if any(x in specific for x in ("national park","conservation area","wildlife reserve","hunting reserve","protected area")):return "PROTECTED_AREA"
    if any(x in specific for x in ("lake","pond","wetland","ramsar")):return "WATER"
    if any(x in specific for x in ("point","waterfall","falls","jharana","temple","monastery","stupa","museum","statue","facility","fort")):return "POINT"
    if any(x in specific for x in ("route","trail","circuit","parikrama")):return "ROUTE"
    if "corridor" in specific:return "CORRIDOR"
    if any(x in specific for x in ("area","landscape","village","town","bazaar","ridge","hill","forest","region","plateau","highland","valley","settlement")):return "AREA"
    if any(x in fallback for x in ("national park","conservation area","wildlife reserve","hunting reserve")):return "PROTECTED_AREA"
    if any(x in fallback for x in ("lake","pond","wetland")):return "WATER"
    if any(x in fallback for x in ("waterfall","falls","jharana")):return "POINT"
    if any(x in fallback for x in ("trek","trail","route","circuit","parikrama")):return "ROUTE"
    if any(x in fallback for x in ("river","corridor")):return "CORRIDOR"
    if any(x in fallback for x in ("landscape","village","town","bazaar","ridge","hill","forest","area","region","plateau","highland","valley")):return "AREA"
    return "POINT"

def explicit_routing_hold(e,text):
    status=norm(flat_text(first_value(e or {},"status","routing_status","route_status","access_status","coordinate_status")))
    full=norm(f"{status} {text}")
    return bool(re.search(r"\b(routing hold|do not route|route hold|status hold|geometry hold)\b",full))

def dynamic_access(text):
    s=norm(text)
    return any(x in s for x in ("dynamic","current conditions","check locally","verify locally","seasonal","pending current","current operation"))

def permits(text,g):
    s=norm(text); p=[]
    no_restricted=bool(re.search(r"\b(no|false|not required|does not require)\b.{0,24}\b(restricted|special).*permit\b|\brestricted.*permit\b.{0,16}\b(no|false|not required)\b",s))
    if "restricted" in s and "permit" in s and not no_restricted:p.append("RESTRICTED_AREA_PERMIT")
    if g=="PROTECTED_AREA" or any(x in s for x in ("national park","conservation area","wildlife reserve")):p.append("PROTECTED_AREA_ENTRY")
    if "climbing permit" in s or "mountaineering permit" in s:p.append("CLIMBING_PERMIT")
    if any(x in s for x in ("border","customs","immigration")):p.append("BORDER_CONTROL")
    if any(x in s for x in ("operator","boating","rafting","paragliding","safari","cable car")):p.append("OPERATOR_DEPENDENT")
    if any(x in s for x in ("fee","ticket","entry")) and not re.search(r"\b(no|none|false)\b.{0,16}\b(entry fee|ticket|fee)\b",s):p.append("ENTRY_FEE")
    if any(x in s for x in ("dynamic","current","seasonal","verify","check")):p.append("DYNAMIC")
    return list(dict.fromkeys(p)) or ["NONE"]

def record_fields(e):
    e=e or {}
    introduction=clean(first_value(e,"description","intro","short")) or None
    things=activity_strings(e.get("things_to_do",[]))
    permit_value=first_value(e,"permit","permits","permit_entry","permit_entry_text","permits_and_entry","permits_entry","permit_framework")
    access_value=first_value(e,"how_to_visit","access","access_guidance")
    permit_text=readable(permit_value) or None
    how_to_visit=readable(access_value) or None
    return introduction,things,permit_text,how_to_visit

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
                e,match_method=best_match(r["name"],emap)
                text=flat_text(e); hint=geometry_hint(e); g=geometry(r["category"],r["name"],hint); matched=bool(e)
                introduction,things,permit_text,how_to_visit=record_fields(e)
                routing_hold=(g=="HOLD" or not matched or explicit_routing_hold(e,text))
                access_status="ROUTING_HOLD" if routing_hold else ("DYNAMIC_CHECK_REQUIRED" if dynamic_access(text) else "ROUTABLE")
                source_routing_status="routing_hold" if routing_hold else ("dynamic_check_required" if access_status=="DYNAMIC_CHECK_REQUIRED" else "routable")
                source_key=clean(first_value(e or {},"id","name","place","title")) or None
                rec={"id":f"np-{slug(pname)}-{slug(district)}-{slug(r['name'])}",**r,
                     "introduction":introduction,
                     "things_to_do":things,
                     "geometry_type":g,
                     "source_routing_status":source_routing_status,
                     "access_status":access_status,
                     "permit_layers":permits(f"{r['category']} {r['research_note']} {permit_text or ''} {text}",g),
                     "parent_entity_id":parents.get(norm(r["name"])),
                     "visitor_ready_label":clean(first_value(e or {},"name","place","title","id")) or None,
                     "match_method":match_method,
                     "permit_entry_text":permit_text,
                     "how_to_visit":how_to_visit,
                     "visitor_ready_source_file":str(vf.relative_to(ROOT)) if vf else None,
                     "source_record_key":source_key}
                records.append(rec)
        stats[pname]={"districts":len(dslugs),"records":len(records)-before,"expected_records":EXPECTED[pname]}
    explicit_hold_routed=[r for r in records if r.get("source_routing_status")=="routing_hold" and r.get("access_status")!="ROUTING_HOLD"]
    routable_without_match=[r for r in records if r.get("access_status")!="ROUTING_HOLD" and not r.get("match_method")]
    kavre=[r for r in records if r["province"]=="Bagmati" and r["district"]=="Kavrepalanchok"]
    kavre_matches=sum(bool(r.get("match_method")) for r in kavre)
    qa={"province_stats":stats,"district_count":len(districts),"record_count":len(records),"expected_district_count":77,"expected_record_count":EXPECTED_TOTAL,
        "district_count_ok":len(districts)==77,"record_count_ok":len(records)==EXPECTED_TOTAL,
        "province_record_counts_ok":all(v["records"]==v["expected_records"] for v in stats.values()),
        "routing_hold_count":sum(r["access_status"]=="ROUTING_HOLD" for r in records),
        "visitor_ready_match_count":sum(bool(r.get("match_method")) for r in records),
        "routable_record_count":sum(r["access_status"]!="ROUTING_HOLD" for r in records),
        "explicit_hold_routed_count":len(explicit_hold_routed),
        "explicit_hold_routed_ok":not explicit_hold_routed,
        "routable_without_match_count":len(routable_without_match),
        "routable_without_match_ok":not routable_without_match,
        "kavrepalanchok_visitor_ready_match_count":kavre_matches,
        "kavrepalanchok_expected_visitor_ready_match_count":32,
        "kavrepalanchok_visitor_ready_ok":kavre_matches==32}
    return records,qa

def write(records,qa):
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"nepal_master_visitor_ready.json").write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    cols=["id","province","district","name","category","municipality_or_area","priority","research_status","geometry_type","source_routing_status","access_status","permit_layers","parent_entity_id","visitor_ready_label","match_method","permit_entry_text","how_to_visit","canonical_source_file","visitor_ready_source_file"]
    with (OUT/"nepal_master_visitor_ready.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
        for r in records:
            x={k:r.get(k) for k in cols};x["permit_layers"]=";".join(r.get("permit_layers") or []);w.writerow(x)
    (OUT/"validation_report.json").write_text(json.dumps(qa,indent=2)+"\n",encoding="utf-8")

def main():
    records,qa=build();write(records,qa);print(json.dumps(qa,indent=2))
    ok=(qa["district_count_ok"] and qa["record_count_ok"] and qa["province_record_counts_ok"]
        and qa["explicit_hold_routed_ok"] and qa["routable_without_match_ok"] and qa["kavrepalanchok_visitor_ready_ok"])
    print("VALIDATION PASSED" if ok else "VALIDATION FAILED",file=sys.stdout if ok else sys.stderr)
    return 0 if ok else 2
if __name__=="__main__": raise SystemExit(main())

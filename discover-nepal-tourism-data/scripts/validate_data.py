#!/usr/bin/env python3
import csv, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
errors=[]
for csv_path in root.glob("provinces/*/*_master_inventory.csv"):
    rows=list(csv.DictReader(csv_path.open(encoding="utf-8-sig")))
    json_path=csv_path.with_suffix(".json")
    if not json_path.exists(): errors.append(f"Missing JSON: {json_path}"); continue
    data=json.loads(json_path.read_text(encoding="utf-8"))
    if len(rows)!=len(data): errors.append(f"Count mismatch: {csv_path} ({len(rows)}) vs {json_path} ({len(data)})")
    required=["province","district","place_name","category","municipality_or_area","priority","research_status"]
    for i,row in enumerate(rows,2):
        for key in required:
            if not row.get(key,"").strip(): errors.append(f"{csv_path}:{i} missing {key}")
if errors:
    print("VALIDATION FAILED")
    print("\n".join(errors)); raise SystemExit(1)
print("Validation passed.")

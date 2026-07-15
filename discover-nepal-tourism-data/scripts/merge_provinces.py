#!/usr/bin/env python3
import csv, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
all_rows=[]
for p in sorted(root.glob('provinces/*/*_master_inventory.json')):
    all_rows.extend(json.loads(p.read_text(encoding='utf-8')))
(root/'master/nepal_master_inventory.json').write_text(json.dumps(all_rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
fields=['index','province','district','place_name','category','municipality_or_area','priority','research_status','notes']
with (root/'master/nepal_master_inventory.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
    for i,r in enumerate(all_rows,1): w.writerow({'index':i,**r})
print(f'Merged {len(all_rows)} records.')

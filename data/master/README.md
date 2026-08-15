# Nepal Visitor-Ready Master Data

This directory is the national integration layer for Discover Nepal Hub.

## Files

- `nepal_master_visitor_ready.json` — national source index and normalization contract.
- `nepal_master_visitor_ready.schema.json` — normalized record schema.
- `nepal_shared_entities.json` — shared parks, restricted areas, river corridors, pilgrimage systems and other cross-district parents.
- `quality_flags.md` — routing/publication safety rules.
- `generated/` — deterministic JSON/CSV outputs created by the builder.

## Build

```bash
python -m pip install -r requirements-data.txt
python scripts/build_nepal_visitor_ready_master.py
```

The builder reads exactly the 77 canonical district inventories, enriches them from the integrated visitor-ready files, assigns stable IDs, normalizes geometry/access/permit layers, links exact-name shared parent entities, writes JSON + CSV, and exits non-zero unless the result matches the national checkpoint: **7 provinces / 77 districts / 1,892 records**.

The canonical district research remains the source of truth. Visitor-ready enrichment may improve routing and visitor meaning, but it cannot delete an existing canonical tourism record.

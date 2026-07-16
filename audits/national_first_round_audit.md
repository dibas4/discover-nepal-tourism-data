# National First-Round Tourism Inventory Audit

Audit status: **first-round reconciliation and path normalization complete**

This file records repository-level checks after completing the first-round district inventories. Git files, not chat messages, are the source of truth.

## Province indexes verified

| Province | Districts | Organized entries | Index path | Status |
|---|---:|---:|---|---|
| Koshi | 14 | 302 | `provinces/koshi/province_index.md` | Reconciled and normalized |
| Madhesh | 8 | 153 | `provinces/madhesh/province_index.md` | Reconciled and normalized |
| Bagmati | 13 | 328 | `provinces/bagmati/province_index.md` | Reconciled and normalized from actual expanded district files |
| Lumbini | 12 | 318 | `provinces/lumbini/province_index.md` | Reconciled |
| Gandaki | 11 | 217 | `provinces/gandaki/province_index.md` | Reconciled |
| Karnali | 10 | 284 | `provinces/karnali/province_index.md` | Reconciled |
| Sudurpashchim | 9 | 270 | `provinces/sudurpashchim/province_index.md` | Reconciled |

**National first-round total: 77 districts and 1,872 organized records.**

## Structural status

All seven provinces now have normalized working paths:

```text
provinces/<province>/province_index.md
provinces/<province>/districts/<district>.md
```

The older nested Koshi, Madhesh and Bagmati copies remain temporarily as a safety archive. They are not the source of truth and should not be used for new edits. Remove them only after CSV/JSON regeneration and hash-level migration review.

## Important reconciliation finding

The former Bagmati index reported 153 records, but several district files had already been expanded without updating that index. The normalized district-file counts reconcile to **328 Bagmati records**, increasing the national total from the earlier reported 1,697 to **1,872**.

## Audit findings

1. All 77 district inventories are represented in normalized province structures.
2. Province index arithmetic reconciles to 1,872 records.
3. Gandaki is intentionally conservative at 217 records and should not be inflated from earlier chat estimates.
4. Province CSV/JSON exports may be older than their district Markdown source files and require regeneration.
5. Cross-district entities must become relationship records rather than unrelated duplicates.
6. Exact coordinates must not be published for archaeological boundaries, seasonal natural features, uncertain mapped sites, or sensitive border locations without verification.
7. Living-culture records require community consent and respectful representation.
8. Roads, flights, trails, bridges, boating, safari operations, permits, entry fees, border access, and accommodation must carry a `last_verified` date.

## Next audit actions

- Regenerate province CSV/JSON files from normalized district Markdown files.
- Generate the national master CSV/JSON from normalized province sources.
- Identify districts below the minimum first-round depth threshold.
- Detect likely duplicate names and cross-district landscapes.
- Create a national `quality_flags.md`.
- Remove the legacy nested archive only after generated outputs and content hashes are checked.

## Proposed normalized record fields

```text
id
place_name
alternate_names
province
district
municipality
ward
category
priority
verification_status
source_type
source_url
latitude
longitude
coordinate_status
seasonality
operational_status
last_verified
image_status
cross_district_entity_id
notes
```
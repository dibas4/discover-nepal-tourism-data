# National First-Round Tourism Inventory Audit

Audit status: **in progress**

This file records repository-level checks after completing the first-round district inventories. Git files, not chat messages, are the source of truth.

## Province indexes directly verified

| Province | Districts verified | Organized entries | Index path | Status |
|---|---:|---:|---|---|
| Lumbini | 12 | 318 | `provinces/lumbini/province_index.md` | Reconciled |
| Gandaki | 11 | 217 | `provinces/gandaki/province_index.md` | Reconciled |
| Karnali | 10 | 284 | `provinces/karnali/province_index.md` | Reconciled |
| Sudurpashchim | 9 | 270 | `provinces/sudurpashchim/province_index.md` | Reconciled |

**Verified subtotal:** 42 districts and 1,089 organized entries.

## Older province structures requiring reconciliation

The current standardized path `provinces/<province>/province_index.md` was not found for:

- Koshi
- Madhesh
- Bagmati

These provinces were researched earlier, but their files may use an older folder layout or naming convention. They must be located and normalized before a reliable national total is published.

## Audit findings

1. Province folder structure is inconsistent between earlier and later research phases.
2. The four standardized province indexes above reconcile correctly with their district counts.
3. Gandaki is intentionally conservative at 217 records and should not be inflated from earlier chat estimates.
4. Cross-district entities must become relationship records rather than unrelated duplicates.
5. Exact coordinates must not be published for archaeological boundaries, seasonal natural features, uncertain mapped sites, or sensitive border locations without verification.
6. Living-culture records require community consent and respectful representation.
7. Roads, flights, trails, bridges, boating, safari operations, permits, entry fees, border access, and accommodation must carry a `last_verified` date.

## Next audit actions

- Locate and normalize Koshi, Madhesh, and Bagmati province indexes.
- Recalculate the true national record total from all seven Git indexes.
- Check every province table for arithmetic errors.
- Identify districts below the minimum first-round depth threshold.
- Detect likely duplicate names and cross-district landscapes.
- Create a national `quality_flags.md`.
- Generate province and national CSV/JSON only after schema normalization.

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

# National First-Round Tourism Inventory Audit

Audit status: **first-round reconciliation complete**

This file records repository-level checks after completing the first-round district inventories. Git files, not chat messages, are the source of truth.

## Province indexes verified

| Province | Districts | Organized entries | Index path | Status |
|---|---:|---:|---|---|
| Koshi | 14 | 302 | `discover-nepal-tourism-data/provinces/koshi/province_index.md` | Reconciled; legacy nested path |
| Madhesh | 8 | 153 | `discover-nepal-tourism-data/provinces/madhesh/province_index.md` | Reconciled; legacy nested path |
| Bagmati | 13 | 153 | `discover-nepal-tourism-data/provinces/bagmati/province_index.md` | Reconciled; legacy nested path |
| Lumbini | 12 | 318 | `provinces/lumbini/province_index.md` | Reconciled |
| Gandaki | 11 | 217 | `provinces/gandaki/province_index.md` | Reconciled |
| Karnali | 10 | 284 | `provinces/karnali/province_index.md` | Reconciled |
| Sudurpashchim | 9 | 270 | `provinces/sudurpashchim/province_index.md` | Reconciled |

**National first-round total: 77 districts and 1,697 organized records.**

## Structural finding

The first three provinces are stored below an accidental extra top-level directory:

```text
discover-nepal-tourism-data/provinces/
```

The later four provinces use:

```text
provinces/
```

This is a repository-layout problem, not missing data. Do not create duplicate province files before migrating the legacy tree.

## Safe migration plan

1. Copy Koshi, Madhesh, and Bagmati province indexes, district files, quality flags, CSV, and JSON into `provinces/<province>/`.
2. Verify file counts and content hashes after copying.
3. Update references in README, scripts, and audit files.
4. Delete the legacy nested copies only after the normalized paths are verified.
5. Regenerate province CSV/JSON files where district Markdown files are newer than the existing exports.

## Audit findings

1. All 77 district inventories are represented by the seven province indexes.
2. Province index arithmetic reconciles to 1,697 records.
3. Gandaki is intentionally conservative at 217 records and should not be inflated from earlier chat estimates.
4. Madhesh district Markdown files are the current source of truth; its province CSV/JSON require regeneration.
5. Cross-district entities must become relationship records rather than unrelated duplicates.
6. Exact coordinates must not be published for archaeological boundaries, seasonal natural features, uncertain mapped sites, or sensitive border locations without verification.
7. Living-culture records require community consent and respectful representation.
8. Roads, flights, trails, bridges, boating, safari operations, permits, entry fees, border access, and accommodation must carry a `last_verified` date.

## Next audit actions

- Normalize the three legacy province paths without duplicating records.
- Check district files against province-index counts.
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

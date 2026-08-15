# Nepal Visitor-Ready Tourism Integration

Status: NATIONAL_INTEGRATION_COMPLETE
Provinces: 7/7
Districts: 77/77
Canonical visitor records covered: 1892

## Province coverage
- Bagmati — 13 districts — 328 records
- Koshi — 14 districts — 302 records
- Madhesh — 8 districts — 153 records
- Gandaki — 11 districts — 237 records
- Lumbini — 12 districts — 318 records
- Karnali — 10 districts — 284 records
- Sudurpashchim — 9 districts — 270 records

## Integration policy
- Preserve completed province/district visitor-ready enrichment as the research source of truth.
- Use point geometry only for verified visitor entrances/POIs; areas, lakes, parks, rivers and trekking systems remain area/corridor/route objects.
- Keep permits separate from protected-area entry fees, tickets, operator charges and border controls.
- Never hard-code changing fees, road/flight status, trail closures, boating, safari operation, border access or seasonal conditions without a dated recheck.
- Keep ROUTING_HOLD where exact public access is not strong enough.
- Cross-district parks, rivers, pilgrimage landscapes and trekking systems must resolve through one shared parent entity with district-specific access relationships.

## Next data-build phase
Generate a normalized Nepal master visitor-ready inventory from these integrated source files, deduplicate shared parent entities, validate 7 provinces / 77 districts, and produce route-planner-safe JSON/CSV outputs.

# Sindhupalchok Deep Research — Batch 03 (Entries 16–25)

Branch: `research/sindhupalchok-deep-research`
Canonical inventory: `provinces/bagmati/districts/sindhupalchok.md`
Coverage: entries 16–25 of 31

## 16. Kodari–Tatopani border landscape
**Disposition:** ESTABLISHED — historical/international border corridor.
- Historic Nepal–Tibet/China trade landscape at the northern end of the Arniko Highway in Bhotekoshi Rural Municipality.
- Keep as a corridor/border-landscape record, not a generic unrestricted sightseeing POI.
- Current border opening, immigration eligibility, customs access and highway condition are dynamic and must be checked live.
- 2026 road-collapse/landslide reporting demonstrates why current access must not be hard-coded.

## 17. Bhote Koshi rafting corridor
**Disposition:** ESTABLISHED — major adventure corridor.
- Nepal Tourism Board identifies Bhote Koshi in Sindhupalchok as a world-famous steep-gradient rafting/kayaking river.
- NTB describes rapids around class 4–5 at high flow and class 3 at lower levels.
- Model as a river/adventure corridor; launch/take-out points, operator availability, river flow and safety conditions belong in dynamic data.

## 18. Bhote Koshi canyoning areas
**Disposition:** ESTABLISHED AS AN ACTIVITY CORRIDOR; exact commercial sites dynamic.
- Canyoning is established in the Bhote Koshi/Arniko Highway adventure landscape and is paired with rafting, bungee and other gorge activities.
- Do not assign one invented coordinate to the whole canyoning product.
- Individual canyon sites/operators should become separate records only when exact location, operator and operating status are verified.

## 19. Bhote Koshi bungee and canyon swing site
**Disposition:** ESTABLISHED — major commercial adventure POI.
- Nepal Tourism Board identifies Nepal's first bungee at The Last Resort along the Arniko Highway over the Bhote Koshi River.
- NTB describes the steel suspension bridge over the river canyon and also notes canyoning/rafting/rock-climbing activity in the area.
- Keep the physical jump site distinct from the broader Bhote Koshi river corridor.
- Pricing, age/weight restrictions, booking status and operating days are dynamic commercial fields.

## 20. Sukute Beach and Sunkoshi rafting corridor
**Disposition:** ESTABLISHED — major river recreation/tourism cluster.
- Sukute is an established Sindhupalchok rafting, camping and resort destination along the Sunkoshi/Bhote Koshi river tourism corridor.
- 2026 reporting documents strong current tourism activity and rafting demand in Sukute.
- Treat “Sukute Beach” as the tourism cluster/riverfront identity, not literally as a coastal beach.
- Individual resorts should remain separate commercial entities rather than being baked into the destination record.

## 21. Balephi–Sunkoshi river landscape
**Disposition:** ESTABLISHED AS LANDSCAPE/CORRIDOR; visitor nodes need verification.
- Retain as a river-valley/confluence landscape associated with Balephi and the Sunkoshi system.
- Evidence supports the wider river-tourism corridor, but this pass does not justify inventing a single canonical attraction pin or guaranteed recreation facility.
- Future GIS/local research should identify exact viewpoints, access points, beaches/camps and safe river nodes.

## 22. Gaurati Bhimsen Temple
**Disposition:** ESTABLISHED — major religious/cultural POI.
- Gaurati/Gaurati Bhimeshwar is repeatedly identified as an important Sindhupalchok religious destination near the Chautara area.
- Retain spelling aliases such as Gaurati Bhimsen / Gaurati Bhimeshwar for search and deduplication.
- Festival timing, ritual schedules, vehicle access and facilities require current/local verification.

## 23. Chautara
**Disposition:** ESTABLISHED — district headquarters and tourism gateway.
- Chautara is the district-headquarters hill town and a useful service/gateway node for central Sindhupalchok.
- It should not be marketed as one monument; model the town as a gateway/community destination linked to Gaurati and surrounding hill routes.
- Lodging, transport schedules and municipal attractions belong in later operational/local layers.

## 24. Tauthali Tripura Sundari Temple
**Disposition:** ESTABLISHED — religious/cultural destination.
- Retain as the principal goddess shrine associated with Tauthali/Tripurasundari and local festival traditions.
- Link to the Tauthali heritage-village record but do not merge them: temple = specific religious POI; village = broader cultural landscape.
- Exact festival dates and ritual schedules should be refreshed annually/local-source verified.

## 25. Tauthali heritage village
**Disposition:** ESTABLISHED WITH LOCAL-DETAIL FLAG.
- Retain as a broader historical/cultural village landscape associated with Tripura Sundari temple, settlement traditions and hill scenery.
- Do not invent a formal heritage-zone polygon or architectural inventory without municipality/field documentation.
- Link the temple as a component attraction rather than duplicating its religious description.

## Batch QA / modeling decisions
- Entries researched/dispositioned after this batch: **25/31**.
- Kodari–Tatopani is explicitly modeled as a controlled international-border landscape; current crossing/access must be live-verified.
- Bhote Koshi rafting, canyoning and bungee remain separate tourism products because they require different geometry, safety information and commercial/operational data.
- Sukute is modeled as a river-tourism cluster, not a literal coastal beach.
- Balephi–Sunkoshi remains a corridor/landscape until exact visitor nodes are verified.
- Gaurati spelling aliases should be normalized to avoid duplicate CMS records.
- Tauthali temple and Tauthali village remain linked but distinct objects.

## Key sources
- Nepal Tourism Board — Bagmati Province / Bhote Koshi: https://ntb.gov.np/en/bagmati-province
- Nepal Tourism Board — Bungee Jumping: https://ntb.gov.np/things-to-do/bungee-jumping
- Sindhu Sukute Tourism Business Association: https://sindhusukutetourism.org/
- Kathmandu Post, 22 Apr 2026 — Tourism regains momentum in Sukute.
- Kathmandu Post, 2 May 2026 — Tatopani border point shut following road collapse (used as evidence that border/highway status is dynamic).

## Next batch
Entries 26–31: Sunkoshi Kafeshwar Mahadev Temple → Kshemadevi Temple → Melamchi Valley → Indrawati River valley → Bahrabise hill and river gateway → Listikot cultural landscape. Then run full district QA.
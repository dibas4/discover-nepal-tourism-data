# Rasuwa District Deep-Research QA

Branch: `research/rasuwa-deep-research`
Canonical inventory: `provinces/bagmati/districts/rasuwa.md`
Inventory size: **34 entries**
Research batches: **7**

## QA verdict

**PASS WITH FLAGS — 34/34 canonical entries researched/dispositioned.**

Rasuwa's district-level destination discovery/research phase can be closed. The remaining flags are deliberately preserved for the later GIS, operations, permits, and field-verification layers rather than filled with guessed precision.

## Coverage audit

- Entries 1–5: Langtang National Park, Langtang Valley, Langtang Village, Kyanjin Gompa Village, Kyanjin Gompa monastery.
- Entries 6–10: Kyanjin Ri, Tserko Ri, Langshisha Kharka, Ganja La Pass trekking route, Yala Peak approach area.
- Entries 11–15: Gosainkunda Lake, Gosainkunda lake system, Saraswati Kunda, Bhairav Kunda (Rasuwa), Surya Kunda.
- Entries 16–20: Lauribina Pass/ridge, Cholangpati, Sing Gompa/Chandanbari, Dhunche, Syabrubesi.
- Entries 21–25: Tamang Heritage Trail, Gatlang, Parvati Kunda/Chhodingmo Kunda, Goljung, Tatopani.
- Entries 26–30: Nagthali Danda, Thuman, Briddim, Chilime Valley, Bhote Koshi–Trishuli headwater corridor.
- Entries 31–34: Rasuwagadhi Fort, Rasuwagadhi border/old trade route, Naukunda lake area, Uttargaya Dham/Betrawati confluence.

**Coverage result: 34/34. No canonical inventory entry is missing from the batch sequence.**

## Identity / duplicate QA

### Keep separate
- **Kyanjin Gompa Village** vs **Kyanjin Gompa monastery** — settlement/visitor base vs religious site.
- **Gosainkunda Lake** vs **Gosainkunda lake system** — principal named lake vs wider sacred/Ramsar wetland complex.
- **Rasuwagadhi Fort** vs **Rasuwagadhi border and old trade route** — historical structure vs historical corridor/controlled international gateway.
- **Chilime Valley** vs **Bhote Koshi–Trishuli headwater corridor** — local landscape record vs broader river corridor.

### Alias normalization
- **Sing Gompa / Singh Gomba / Chandanbari** should resolve to one canonical settlement/monastery-area record, not duplicate destinations.
- Preserve spelling variants such as Syabrubesi/Syafrubesi as aliases where source spelling differs.

### Cross-district disambiguation
- **Bhairav Kunda, Rasuwa** must never be merged with the separate Bhairav Kunda destination in Sindhupalchok.
- **Uttargaya Dham / Betrawati** is a boundary landscape connected with both Rasuwa and Nuwakot; use one canonical destination with cross-district metadata rather than contradictory duplicates.

## Source-confidence QA

Strong primary/official grounding exists for the district's major tourism backbone:

- Langtang National Park officially covers a large share of Rasuwa and provides the protected-area framework for Langtang Valley, Gosainkunda and associated trekking landscapes.
- Nepal Tourism Board identifies Langtang, Kyanjin, Gosainkunda and the Tamang Heritage Trail, including the Dhunche/Syabrubesi and village sequence.
- Gosainkunda is independently documented as a major Rasuwa pilgrimage destination and high-altitude lake system.
- Official/local-government and government-linked evidence supports the main municipal, border and heritage relationships used in the batches.

Lower-confidence/local records were not upgraded beyond their evidence.

## Flags that remain intentionally open

### HOLD / field or local verification
1. **Naukunda lake area** — do not publish an exact lake pin, definitive lake inventory, visitor route, facilities or access time until municipality/GIS/field evidence verifies them.
2. **Tatopani, Rasuwa** — historical hot-spring identity is retained, but current bathing/visitor operation must be checked locally before promising access.
3. **Goljung Village** — cultural settlement is retained; do not claim an active formal homestay programme without current local confirmation.

### Dynamic operational verification
4. **Rasuwagadhi border** — crossing status, eligibility, checkpoint/bridge access, road status and immigration requirements are dynamic; never infer present access from historical trade-route evidence.
5. **Langtang National Park / trekking permits** — fees, permit rules, TIMS/restricted-area requirements and office procedures must be sourced from current authorities at product runtime/publication refresh.
6. **High routes** — Ganja La, Yala approach, Tserko/Kyanjin high hikes, Lauribina and other alpine routes require seasonal/weather/technical-condition checks; static research is not a live safety clearance.
7. **Festival/pilgrimage timing** — Gosainkunda and Uttargaya event dates should come from a current calendar/local source rather than be hard-coded indefinitely.

### GIS layer still required
8. Confirm coordinates/entrances for all records before route-planner production use.
9. Store routes/corridors as geometry, not misleading single POI pins, for Ganja La, Tamang Heritage Trail, Bhote Koshi–Trishuli corridor and the old Rasuwagadhi trade route.
10. Verify ward-level attribution where the research only establishes municipality/area.

## Planner-model QA

Recommended object types:

- `protected_area`: Langtang National Park
- `destination_area`: Langtang Valley, Chilime Valley, Naukunda lake area (held)
- `settlement`: Langtang Village, Kyanjin Village, Cholangpati, Dhunche, Syabrubesi, Gatlang, Goljung, Thuman, Briddim
- `religious_site`: Kyanjin Gompa monastery, Sing Gompa/Chandanbari, Uttargaya Dham
- `lake/wetland`: Gosainkunda, associated lake system, Saraswati Kunda, Bhairav Kunda Rasuwa, Surya Kunda, Parvati/Chhodingmo Kunda
- `viewpoint/pass`: Kyanjin Ri, Tserko Ri, Nagthali, Lauribina
- `route/corridor`: Ganja La route, Tamang Heritage Trail, Bhote Koshi–Trishuli corridor, Rasuwagadhi old trade route
- `mountaineering_approach`: Yala Peak approach
- `heritage_structure`: Rasuwagadhi Fort
- `natural_site`: Tatopani (operation flagged)

This separation prevents the future planner from treating a national park, a village, a monastery, a lake, a pass and a multi-day trail as interchangeable map pins.

## Final district status

**Rasuwa: CLOSED FOR DESTINATION RESEARCH — 34/34, QA PASS WITH FLAGS.**

Do not reopen destination discovery merely to chase generic viewpoints, picnic areas or unverified temples. Future Rasuwa work should focus on structured enrichment: authoritative coordinates, route geometry, live access, permits, current fees/hours, accommodation readiness, imagery/attribution and local field verification for flagged records.

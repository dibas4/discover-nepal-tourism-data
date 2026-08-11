# Nuwakot District Research QA — 2026-08-11

## Scope

- Canonical inventory: **27 entries**
- Research branch: `research/nuwakot-deep-research`
- Deep-researched/dispositioned: **27 / 27**
- QA purpose: verify modeling consistency, duplicate/cross-district handling, confidence flags, dynamic operating data, protected-area claims and publication readiness.

## QA result

**PASS WITH VERIFICATION FLAGS.**

The district research is complete enough to close the deep-research pass, but several records must remain non-public or partially published until GIS/local/live checks are completed.

## Major destination clusters

### Nuwakot heritage cluster

Keep these linked but distinct:

- Nuwakot Durbar complex — parent heritage cluster
- Saat Tale Durbar — individual palace structure
- Bhairabi Temple — religious site
- Taleju Temple — religious/royal temple
- Nuwakot old town — settlement/heritage area

Do not collapse them into one POI and do not duplicate the same palace coordinate across all records.

### Devighat heritage/pilgrimage cluster

Keep **Devighat** separate from the **Prithvi Narayan Shah memorial area**. One is the broader sacred confluence/pilgrimage landscape; the other is a historical memorial record.

### Betrawati cluster

Keep **Betrawati settlement** separate from the **Betrawati treaty area**. The treaty-related record remains partial until a precise public interpretation/monument site is authoritatively confirmed.

## Verification holds / partial records

### Samari Bhanjyang

- Keep as **HOLD / LOCAL-GIS VERIFICATION REQUIRED**.
- Do not publish a precise municipality, coordinate or viewpoint pin based only on generic map labels.

### Chhahare waterfall area

- Keep as **HOLD / LOCAL VERIFICATION REQUIRED**.
- Exact waterfall identity, access route, coordinates, seasonal safety and visitor infrastructure remain unresolved.

### Langtang National Park sector — Nuwakot

- Keep as **BOUNDARY VERIFICATION HOLD**.
- Do not claim a Nuwakot park-sector intersection until authoritative park/district GIS proves the overlap.
- If no intersection exists, remove the district linkage rather than preserving a false cross-district record.

### Northern Tamang villages

- Valid as a broad cultural/community-tourism landscape.
- Not valid as one POI.
- Create child village records only after settlement-level name, ward, coordinate, access and tourism-operation verification.

### Ghale village landscapes

- Keep distinct from Ghalegaun in Lamjung.
- Treat as a Nuwakot village cluster/community-landscape record until individual villages are verified.

## Route/corridor modeling

These must remain route/area objects rather than single POIs:

- Trishuli River rafting corridor
- Tadi River valley
- Likhu River valley
- Kakani–Nuwakot heritage trail
- Dupcheshwar pilgrimage trail
- Tadi valley cycling route

Do not publish static travel times, difficulty, surface condition, launch points, rafting grades for every segment, or fixed GPX geometry without current route/operator/GIS verification.

## Protected-area modeling

### Shivapuri–Nagarjun National Park buffer sector

- Keep as a cross-district protected-area/buffer object.
- Use authoritative park/buffer polygons rather than a tourism POI centroid.
- Entry rules, fees and opening conditions are dynamic and must be checked at publication time.

### Langtang National Park

- Maintain one canonical park destination globally.
- Nuwakot linkage remains conditional on GIS confirmation.

## Dynamic data that must not be hard-coded

Before traveler-facing publication, recheck:

- Palace/temple public access and restoration status
- Entry fees and opening hours
- Sindure Jatra and pilgrimage dates
- Trishuli rafting operators, launch/take-out points and river safety
- Road/trail conditions, especially monsoon/landslide impacts
- Homestay and community-tourism operating status
- Park/buffer rules and fees

## Coordinate confidence rules

- No coordinate should be published merely because a place name appears on a consumer map.
- Heritage clusters should use parent polygons/centroids plus separately verified child POIs.
- River valleys, protected areas and route concepts require line/polygon geometry.
- HOLD records remain without invented pins.

## Publication disposition

### Publication-ready after ordinary GIS/live checks

Major established records such as Nuwakot Durbar cluster, Devighat, Dupcheshwar Mahadev, Kakani, Suryachaur, Trishuli corridor, Tadi/Likhu valleys, Kispang and Shivapuri-linked landscape records.

### Publish only with caveats / partial status

- Betrawati treaty area
- Ghale village landscapes
- Kakani–Nuwakot heritage trail
- Dupcheshwar pilgrimage trail
- Tadi valley cycling route
- Northern Tamang villages

### Hold from standalone traveler routing

- Samari Bhanjyang
- Chhahare waterfall area
- Langtang National Park sector in Nuwakot until boundary proof

## Final status

- **Inventory coverage:** 27 / 27
- **Deep research:** complete
- **QA:** PASS WITH FLAGS
- **District status:** **CLOSED for deep-research phase**
- **Next future layer:** GIS geometry, exact coordinates, live access/fees/operations, route segmentation and publication enrichment.

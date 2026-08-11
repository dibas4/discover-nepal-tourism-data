# Kathmandu District Research QA — 2026-08-11

## Scope

QA checkpoint after completing deep research for all 19 Kathmandu inventory entries.

- Inventory entries: 19
- Deep-researched: 19 / 19
- Research batches: 4
- Status: district research complete; suitable to move to the next district while GIS/operational freshness tasks remain tracked below.

## Naming and alias normalization

- Use **Gokarneshwor Municipality** as the canonical municipality spelling because this is the municipality's own English spelling; preserve `Gokarneshwar` as a search alias where older tourism material uses it.
- Preserve both **Kopan Monastery** and **Kapan Monastery**; monastery-owned material uses Kopan while Nepal Tourism Board has used Kapan.
- Preserve **Bagdwar** and **Baghdwar** as aliases.
- Preserve Kathmandu Durbar Square aliases: **Hanuman Dhoka Durbar Square** and **Basantapur Durbar**.
- Preserve **Swayambhunath / Swayambhu** and **Boudhanath / Bauddhanath** aliases.
- Preserve **National Museum of Nepal / National Museum, Chauni / Chhauni Museum** for search matching, subject to final institution-name confirmation once its official site is fully available.

## Composite destinations that must not become single misleading POIs

1. **Pharping heritage and monastery circuit** — multi-stop destination. Store settlement/circuit metadata separately from individual monasteries, caves and temples.
2. **Indra Daha and Dahachok** — area-level destination. Indra Daha, Kalu Pande memorial and Dahachok View Tower need individual attraction pins.
3. **Shivapuri-Nagarjun National Park** — protected-area polygon/region, not a single attraction coordinate.
4. **Nagarjun-Jamacho hike** — route object requiring at minimum trailhead + summit/destination geometry.
5. **Sundarijal** — destination/gateway containing municipal attractions plus protected-area access; do not apply one fee or one opening time to the whole area.
6. **Gokarna forest and temple area** — split public Gokarneshwor Mahadev religious POI from private/commercial forest-resort/golf facilities.
7. **Chandragiri Hills** — distinguish cable-car bottom station, top station/hill destination and Bhaleshwor Mahadev Temple when route-planner geometry is created.

## Coordinate QA classes

### Strong / usable reference coordinates already present
- Kathmandu Durbar Square — UNESCO component coordinate
- Swayambhunath — UNESCO component coordinate
- Boudhanath — UNESCO component coordinate
- Pashupatinath — UNESCO component coordinate

### Usable but should receive attraction-level confirmation
- Budhanilkantha Temple
- Kopan Monastery
- Pharping settlement
- Dakshinkali Temple
- Chandragiri Hill

### GIS pass required before route-planner publication
- Indra Daha
- Kalu Pande memorial / Dahachok View Tower
- Shivapuri-Nagarjun gates and internal POIs
- Nagarjun-Jamacho trailhead and summit
- Sundarijal visitor point / park gate
- Bagdwar spring/source
- Taudaha lake centroid + visitor access
- Gokarneshwor Mahadev entrance
- Narayanhiti visitor entrance
- National Museum visitor entrance

## Time-sensitive data flags

Recheck immediately before publishing traveler-facing information:

- all entrance fees
- museum opening hours and closure days
- Chandragiri cable-car fares and operating hours
- Shivapuri-Nagarjun park tariffs, gate hours and route/security rules
- Kopan day-visitor access policy
- religious access/photography restrictions
- local festival dates

Do not treat a fee/hours value found for one facility as applying to an entire destination area.

## Route-planner object types

- `heritage_poi`: Kathmandu Durbar Square, Swayambhunath, Boudhanath, Pashupatinath, Budhanilkantha, Dakshinkali, museums
- `living_heritage_area`: Kirtipur
- `religious_poi`: individual temples/monasteries
- `multi_stop_circuit`: Pharping
- `viewpoint_recreation_complex`: Chandragiri Hills
- `area_destination`: Dahachok
- `protected_area`: Shivapuri-Nagarjun National Park
- `hiking_route`: Nagarjun-Jamacho
- `gateway_natural_area`: Sundarijal
- `trail_destination`: Bagdwar
- `wetland_poi`: Taudaha
- `composite_needs_split`: Gokarna forest and temple area

## Publication readiness

- **Research completeness:** PASS — 19/19 entries have deep-research records.
- **Source discipline:** PASS WITH FLAGS — primary/government/NTB sources dominate; Wikidata coordinates used in several records require later GIS confirmation.
- **Alias normalization:** PASS — known spelling variants documented.
- **Operational freshness:** PENDING — intentionally deferred for time-sensitive values.
- **GIS/route-planner readiness:** PARTIAL — strong coordinates exist for major heritage POIs, but trails, gateways and composite destinations require geometry work.

## District decision

Kathmandu's place-level research phase is complete. Do **not** continue expanding Kathmandu place names during the current national enrichment pass. Move to the next Bagmati district and return to Kathmandu later for the dedicated GIS + live-operations layer.

# Lalitpur District Research QA — 2026-08-11

## Scope

QA checkpoint after completing deep research for all 14 Lalitpur inventory entries.

- Inventory entries: 14
- Deep-researched: 14 / 14
- Status: district place-level research complete

## Alias normalization

- Patan = Lalitpur historic city context; preserve both names.
- Hiranya Varna Mahavihar = Golden Temple.
- Mahaboudha / Mahabuddha — preserve both transliterations until canonical local English usage is locked.
- Kumbeshwar / Kumbheshwar — preserve both.
- Karya Binayak / Karyabinayak / Karya Vinayak — preserve for search.
- Phulchowki / Phulchoki — preserve both.
- Lakuri Bhanjyang / Lakhuri Bhanjyang — preserve both.
- Nag Daha / Nagdaha — preserve both.

## Composite destinations needing split objects

1. Patan Durbar Square vs Patan Museum — heritage-zone object plus facility-level museum POI.
2. Bajrabarahi Temple and forest — temple POI plus sacred-forest geometry.
3. Tika Bhairab and Lele valley — temple POI plus area/scenic-route object.
4. Karya Binayak + Bungamati — separate temple POI linked to settlement heritage area.
5. Bungamati — living heritage settlement with multiple internal POIs.
6. Khokana — living heritage settlement with oil-mill, temple and chowk sub-POIs.
7. Godavari Botanical Garden vs Phulchowki — facility POI vs hiking/hill destination.
8. Lakuri Bhanjyang — viewpoint/area object, not one undifferentiated point.
9. Nagdaha — wetland polygon plus Naga temple/festival sub-objects if published separately.

## Coordinate readiness

Strong official coordinate already captured:
- Tika Bhairab Temple — municipality attraction coordinate.

GIS QA still required for:
- Patan Museum entrance
- Golden Temple entrance
- Mahabuddha entrance
- Kumbheshwar entrance
- Bajrabarahi temple/forest boundary
- Lele valley route geometry
- Karya Binayak entrance
- Bungamati settlement geometry / visitor access
- Khokana settlement geometry / visitor access
- Godavari Botanical Garden gate
- Phulchowki trailhead and summit
- Lakuri Bhanjyang viewpoint/access
- Nagdaha lake centroid and visitor access

## Time-sensitive publication checks

Recheck before traveler-facing publication:
- Patan heritage fees
- museum hours/fees
- temple visitor rules where relevant
- festival dates
- botanical-garden hours/fees
- road/trail access conditions for Phulchowki and Lakuri Bhanjyang

## Route-planner object types

- `heritage_zone`: Patan Durbar Square
- `museum_poi`: Patan Museum
- `religious_poi`: Golden Temple, Mahabuddha, Kumbheshwar, Bajrabarahi, Tika Bhairab, Karya Binayak
- `living_heritage_area`: Bungamati, Khokana
- `scenic_area_route`: Lele valley, Lakuri Bhanjyang
- `botanical_garden_poi`: Godavari Botanical Garden
- `hiking_hill`: Phulchowki
- `wetland_poi`: Nagdaha

## District decision

Lalitpur's place-level research phase is complete. Move to the next Bagmati district; return later for GIS and live-operations enrichment.

# Dolakha District Research QA — 2026-08-11

## Scope

QA checkpoint after completing deep research/disposition for all 29 Dolakha inventory entries.

- Inventory entries: 29
- Deep-researched / dispositioned: 29 / 29
- Status: district place-level research complete

## Alias normalization

- Bhimeshwar / Bhimeshwor — use municipality's current canonical English spelling where available and preserve the alternate spelling for search.
- Sailung / Shailung — preserve both; municipality uses Shailung.
- Bigu Gompa / Bigu Nunnery — preserve both where locally appropriate; final canonical institution name still needs direct institution/local confirmation.
- Tsho Rolpa / Tsho Rolpa Lake — preserve both.
- Tony Hagen Park / Ramite Danda — retain as combined alias set until local verification resolves whether these are identical or adjacent POIs.

## Composite or route-based destinations

1. Charikot — gateway/service area, not a single attraction pin.
2. Charikot viewpoints — viewpoint cluster pending individual POI verification.
3. Gaurishankar Conservation Area — protected-area polygon.
4. Rolwaling Valley — trekking corridor with villages and route stages.
5. Tsho Rolpa — lake plus approach trail object.
6. Gaurishankar mountain viewpoints — cluster, not one invented pin.
7. Lapchi Valley — remote trekking/pilgrimage corridor.
8. Lapchi Monastery and Milarepa meditation sites — sacred-site cluster pending exact naming and geometry.
9. Tamakoshi River valley — river/corridor object.
10. Bigu valley landscapes — area object.
11. Cherdung Danda — hiking route/high ridge object.
12. Kalo Bhir — route feature / emerging viewpoint candidate.
13. Jiri Buddhist heritage circuit — multi-stop circuit; Buddha Park is a verified sub-POI.
14. Sailung/Shailung — cross-district highland landscape shared with Ramechhap.
15. Chaughara heritage area — heritage-cluster candidate on hold.

## Strong verified coordinates already captured

- Dolakha Bhimsen Temple — 27.677941, 86.076433 from Bhimeshwor Municipality.
- Jiri Buddha Park — 27.638216, 86.218009 from Jiri Municipality.

## GIS pass required

- Kalinchowk temple, Kuri and cable-car stations
- Historic Dolakha town geometry
- Charikot gateway/service points
- Gaurishankar Conservation Area boundary
- Rolwaling route, Beding, Na, Yalung Ri and Tsho Rolpa
- Gaurishankar viewpoint cluster
- Lamabagar and Lapchi route/sacred sites
- Bigu Gompa and Bigu valley objects
- Tamakoshi river line
- Cherdung trail, Kalo Bhir and Jiri local viewpoint/recreation records
- Sailung district-boundary-aware polygon and access points
- Kalinag Temple
- Chaughara heritage cluster

## High-altitude / restricted-area data rules

- Treat all conservation-area fees, restricted-area permits, trekking permits, mountaineering classifications and border-zone rules as time-sensitive.
- The Department of Tourism currently lists restricted-area permit requirements for Gaurishankar Rural Municipality Ward 9 and Bigu Rural Municipality Ward 1 in Dolakha; these must be checked immediately before traveler-facing publication because official rules can change.
- Do not infer technical climbing permission from a trekking-area name. Yalung Ri and other high-altitude objectives require current official classification before route-planner exposure.
- Border-near Lamabagar/Lapchi routes require live immigration/local-access verification.

## Operational freshness flags

Recheck before publication:
- Kalinchowk cable-car fares and operating hours
- conservation-area entry fees and check-post requirements
- restricted-area permits
- trail/bridge/road condition in Rolwaling, Lamabagar and Lapchi
- snow/monsoon access
- local festival dates
- local park/pond/viewpoint facilities around Jiri
- Sailung entry fee and route-specific collection rules

## Weak / hold records

- Kalo Bhir — partial/local verification required
- Tony Hagen Park / Ramite Danda — canonical relationship unresolved
- Jiri Fish Pond and Linkan area — local facilities unverified
- Jiri Buddhist heritage circuit — circuit retained; only Buddha Park currently strongly verified as a sub-POI
- Lapchi Monastery and Milarepa sites — exact site names/geometry require local verification
- Bigu Gompa — final formal English institution naming still needs local confirmation
- Kalinag Temple — partial/local verification required
- Chaughara heritage area — HOLD / do not publish yet

## Route-planner object types

- `gateway_service_area`: Charikot, Jiri
- `religious_poi`: Kalinchowk Bhagwati, Dolakha Bhimsen, Kalinag candidate
- `living_heritage_area`: Historic Dolakha Town
- `cable_car_facility`: Kalinchowk Cable Car
- `protected_area`: Gaurishankar Conservation Area
- `trekking_valley`: Rolwaling, Lapchi
- `trekking_route`: Cherdung and other verified route objects
- `high_altitude_lake`: Tsho Rolpa
- `community_village`: Kuri, Beding, Na, Lamabagar
- `viewpoint_cluster`: Charikot viewpoints, Gaurishankar viewpoints
- `river_corridor`: Tamakoshi
- `cross_district_highland`: Sailung/Shailung
- `multi_stop_cultural_circuit`: Jiri Buddhist heritage circuit
- `emerging_local_record`: Kalo Bhir, Jiri Fish Pond, Kalinag
- `hold_heritage_cluster`: Chaughara

## District decision

Dolakha's place-level research phase is complete at 29/29. Do not expand minor local POIs during the current national enrichment pass. Return later for GIS geometry, live permits/access, current operations and local verification of flagged records.

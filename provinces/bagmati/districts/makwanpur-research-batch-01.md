# Makwanpur Verified Research Batch 01 — 2026-08-11

> Deep-research sidecar for canonical Makwanpur inventory entries 1–5. The canonical inventory was recovered on `main` with 31 entries, so no reconstruction/replacement was needed.

## 1. Daman

- **District:** Makwanpur
- **Municipality:** Thaha Municipality
- **Destination type:** Hill station / Himalayan viewpoint / highland tourism hub
- **Official tourism status:** Thaha Municipality's dedicated tourism portal lists Daman as one of the municipality's principal destinations.
- **Elevation:** Nepal Film Development Board's official destination profile gives Daman at approximately **2,322 m**.
- **Visitor value:** Himalayan panorama, highland climate, forest/ridge scenery and seasonal winter conditions are the core tourism values.
- **Religious context:** The government filming-site profile notes religious significance associated with Mahadev in Hindu tradition and Guru Padmasambhava in Buddhist tradition in the Daman landscape.
- **Seasonality:** Government destination material notes snowfall can occur in the Daman area in winter, but traveler-facing copy must never guarantee snow on a specific date.
- **Route-planner modeling:** Daman should be an area/gateway object with the View Tower area, Sim Bhanjyang, religious sites, ridge trails, lodging and road-access nodes modeled separately.
- **Primary sources:**
  - https://tourism.thahamun.gov.np/
  - https://www.film.gov.np/destination/21
- **Verification status:** PASS — established municipality-promoted destination; exact GIS boundary and current individual-facility operations remain later enrichment.

## 2. Sim Bhanjyang / Simbhanjyang

- **District:** Makwanpur
- **Municipality:** Thaha Municipality
- **Destination type:** High road pass / viewpoint / ridge landscape
- **Alias normalization:** Preserve `Sim Bhanjyang` and `Simbhanjyang` for search.
- **Destination relationship:** Closely linked to Daman but should remain a separate pass/ridge object rather than being merged into the Daman town record.
- **Official context:** Thaha Municipality tourism material explicitly promotes snowfall in the `Daman Simbhanjang` area, supporting its identity as part of the municipality's highland tourism landscape.
- **Visitor value:** Ridge scenery, road-trip stopping point, forest/highland environment and weather-dependent mountain views.
- **Safety/seasonality:** Fog, rain, winter ice/snow and road conditions can affect travel. Do not publish guaranteed snow or visibility claims.
- **Coordinates:** Exact pass/high-point and safe public stopping geometry require GIS verification.
- **Primary source:** https://tourism.thahamun.gov.np/
- **Verification status:** PASS for destination identity; exact viewpoint/parking geometry pending.

## 3. Daman View Tower area

- **District:** Makwanpur
- **Municipality:** Thaha Municipality
- **Destination type:** Himalayan panorama point / viewpoint facility area
- **Official evidence:** Nepal Film Development Board's government destination profile states that the Himalayas can be seen from the view tower at Daman.
- **Critical operations rule:** Historic/official references establish the viewpoint identity, but the **current physical condition, opening status, access and any ticketing must be checked live** before traveler-facing publication.
- **Modeling:** Store the viewpoint area separately from Daman. If the tower itself is not operational, retain the surrounding viewpoint landscape without falsely advertising tower access.
- **Weather caution:** Panorama quality is entirely weather-dependent.
- **Coordinates:** Exact tower/viewpoint entrance pin requires GIS verification.
- **Primary source:** https://www.film.gov.np/destination/21
- **Verification status:** PASS for historic/official viewpoint identity; CURRENT OPERATIONS CHECK REQUIRED.

## 4. Chitlang Village

- **District:** Makwanpur
- **Municipality:** Thaha Municipality
- **Destination type:** Historic village / cultural landscape / rural tourism destination
- **Official tourism status:** Thaha Municipality's tourism portal lists Chitlang under religious and historical heritage and promotes village life/agriculture as tourism themes.
- **Government destination description:** Nepal Film Development Board describes Chitlang Valley as a north-south valley with chaityas, traditional houses, farmland, trout farms, Taleju Bhawani, Sat Dhara and Shivalaya among its attractions.
- **Community context:** The same government source identifies Newar, Tamang, Chhetri, Bahun and Balami communities in the village. Traveler copy should present these as living communities, not staged attractions.
- **Route-planner modeling:** Chitlang should be a settlement/heritage-area object linked to separate records for Satdhara, religious sites, historic structures, farms and the Chitlang–Markhu hiking route.
- **Coordinates:** Settlement polygon plus verified individual POIs required during GIS pass.
- **Primary sources:**
  - https://tourism.thahamun.gov.np/
  - https://www.film.gov.np/destination/21
- **Verification status:** PASS — strong municipality/government tourism evidence.

## 5. Tistung heritage area

- **District:** Makwanpur
- **Municipality:** Thaha Municipality
- **Destination type:** Historic settlement / agricultural-cultural landscape / old-route corridor
- **Official tourism status:** Thaha Municipality's dedicated tourism portal lists Tistung among its main visitor areas.
- **Destination role:** Treat Tistung as a heritage/agricultural settlement area rather than one POI. Individual temples, old-route structures, farms and public heritage sites require separate verification.
- **Route-planner modeling:** Settlement polygon with road/trail heritage connections to Palung, Daman and the broader Thaha landscape.
- **Evidence caution:** This batch verifies Tistung's municipality tourism identity, but does not invent exact dates, monuments or trade-route structures without record-level sources.
- **Coordinates:** Settlement/heritage-area geometry pending GIS verification.
- **Primary source:** https://tourism.thahamun.gov.np/
- **Verification status:** PASS for destination identity; detailed heritage inventory remains later enrichment.

# Makwanpur progress

- **Canonical inventory entries:** 31
- **Deep-researched / dispositioned:** 5 / 31
- **Next entries:** 6–10 — Kulekhani Reservoir / Indra Sarovar; Markhu; Kulekhani Dam viewpoint; Mohini Jharana; Makwanpurgadhi Fort.

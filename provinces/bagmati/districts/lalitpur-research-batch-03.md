# Lalitpur Verified Research Batch 03 — 2026-08-11

> Completes deep research for Lalitpur inventory entries 11–14. Time-sensitive fees/hours remain publication-time checks.

## 11. Godavari Botanical Garden / National Botanical Garden

- **District:** Lalitpur
- **Municipality:** Godawari Municipality
- **Destination type:** Botanical garden / plant-conservation and education attraction / natural recreation area
- **Municipality verification:** Godawari Municipality's official profile explicitly states that Godawari is famous for its botanical garden.
- **Destination relationship:** Keep the botanical garden as a facility-level POI separate from the broader Godawari forest/settlement area and from the Phulchowki hiking destination.
- **Visitor value:** Suitable future CMS themes include botany, plant conservation, nature walks, family visits, environmental education and bird/nature observation.
- **Coordinates:** Exact public entrance/gate coordinate should be captured during GIS QA rather than using a Godawari settlement centroid.
- **Permit requirement:** No separate travel permit identified for ordinary garden visitation in the sources reviewed.
- **Fee / hours:** Treat as time-sensitive. Recheck against the responsible government botanical-garden/plant-resources authority immediately before publication.
- **Primary sources:**
  - https://www.godawarimun.gov.np/en/content/nagar-profile
  - https://godawarimun.gov.np/en/node/4
- **Verification status:** Municipality and botanical-garden identity verified from Godawari Municipality; facility-level GIS and current operations pending.

## 12. Phulchowki / Phulchoki Hill

- **District:** Lalitpur
- **Municipality:** Godawari Municipality
- **Destination type:** Highest Kathmandu Valley hill / hiking destination / viewpoint / forest and biodiversity area
- **Alias normalization:** Preserve `Phulchowki` and `Phulchoki`; Godawari Municipality currently uses “Phulchowki” in its English profile.
- **Elevation context:** Godawari Municipality identifies Phulchowki as the highest peak in Kathmandu Valley. The municipality's current profile gives its municipal elevation range up to about 2,831 m, consistent with the Phulchowki high point.
- **Tourism context:** The municipality describes Godawari as a popular hiking destination because of wildlife and its environment and specifically locates Phulchowki in Godawari.
- **Route-planner modeling:** Store `Phulchowki hike` as a route/trail object with trailhead, summit/high point and access-road conditions separately. Do not model the entire hill with one generic municipality coordinate.
- **Environmental context:** Future traveler content should account for forest sensitivity, weather/fog and seasonal trail/road conditions rather than presenting it only as a viewpoint.
- **Coordinates:** Summit/high-point and trailhead coordinates require authoritative GIS confirmation during the route layer.
- **Permit / fee / hours:** No authoritative live visitor tariff or gate schedule captured in this pass; recheck locally before publication, especially if access controls or forest rules apply.
- **Primary sources:**
  - https://www.godawarimun.gov.np/en/content/nagar-profile
  - https://www.godawarimun.gov.np/
  - https://www.godawarimun.gov.np/sites/godawarimunlalitpur.gov.np/files/documents/godawari%20nagar%20profile%20%2C2078.pdf
- **Verification status:** Municipality, hiking identity and highest-valley-peak status verified; trail geometry and live access rules pending.

## 13. Lakuri Bhanjyang / Lakhuri Bhanjyang

- **District:** Lalitpur
- **Municipality:** Mahalaxmi Municipality
- **Destination type:** Hill pass / viewpoint / scenic-road and hiking destination
- **Alias normalization:** Preserve both `Lakuri Bhanjyang` and `Lakhuri Bhanjyang`; Mahalaxmi Municipality's English tourism list uses Lakuri while procurement documents also show Lakhuri transliteration.
- **Municipality verification:** Mahalaxmi Municipality explicitly lists Lakuri Bhanjyang among its religious and tourist destinations.
- **Scenic significance:** The municipality homepage itself features a view of Mahalaxmi Municipality from Lakuri Bhanjyang, supporting its viewpoint identity.
- **Access/infrastructure context:** A 2025 municipality procurement notice records road construction from Lakhuri Bhanjyang toward Manmohan Park. Road condition should therefore be treated as dynamic and checked close to travel rather than assumed from older guide material.
- **Route-planner modeling:** Use an area/viewpoint object plus road-access geometry; if individual viewpoints, parks or trailheads are published later, store them as separate POIs.
- **Coordinates:** Exact publication-grade viewpoint/access coordinate requires GIS QA.
- **Permit requirement:** No separate tourism permit identified.
- **Entry fee / hours:** No universal official entry fee or opening schedule identified; individual facilities may have their own conditions.
- **Primary sources:**
  - https://www.mahalaxmimun.gov.np/en/node/4
  - https://www.mahalaxmimun.gov.np/en
  - https://mahalaxmimun.gov.np/sites/mahalaxmimunlalitpur.gov.np/files/mAHALAXMI%20LOI%202082-1-11.pdf
- **Verification status:** Municipality and tourism/viewpoint identity verified; exact viewpoint geometry and current road conditions pending.

## 14. Nag Daha / Nagdaha

- **District:** Lalitpur
- **Municipality / ward:** Lalitpur Metropolitan City, Ward 23, Dhapakhel
- **Destination type:** Lake / wetland / religious-cultural destination
- **Alias normalization:** Preserve `Nag Daha` and `Nagdaha`.
- **Administrative verification:** Lalitpur Metropolitan City's intangible-heritage documentation identifies Nagdaha at Dhapakhel, Ward 23.
- **Religious context:** LMC documentation connects the lake with the Naga tradition and identifies Nagdaha as associated with Karkotak, the king of serpents in local tradition.
- **Festival:** A major Nag Panchami mela is held at Nagdaha, drawing devotees to the Naga temple and lake area. Exact Gregorian festival dates must be derived from the relevant year's religious calendar/local notice.
- **Destination relationship:** Model lake/wetland geometry separately from the Naga temple and festival-event object if the CMS later supports sub-POIs/events.
- **Conservation note:** As a lake/wetland in an urbanizing area, future traveler content should avoid encouraging littering, feeding/disturbance or activities that conflict with local conservation management.
- **Coordinates:** Exact lake centroid and principal visitor access point require GIS QA.
- **Permit requirement:** No separate tourism permit identified.
- **Entry fee / hours:** No reliable universal official entry tariff or schedule identified in this pass.
- **Primary sources:**
  - https://www.lmc.gov.np/sites/lalitpurmun.gov.np/files/documents/Report%20On%20Intangible%20Heritage%20of%20Lalitpur.pdf
- **Verification status:** Dhapakhel/Ward 23 location and Nag Panchami cultural significance verified from Lalitpur Metropolitan City documentation; GIS and live operations pending.

# Lalitpur research completion

- **Inventory entries:** 14
- **Deep-researched:** 14 / 14
- **Status:** Place-level deep research complete.
- **Next step:** Lalitpur district QA for aliases, composite destinations, authoritative coordinates, route-planner object types and time-sensitive operations; then move to the next Bagmati district.

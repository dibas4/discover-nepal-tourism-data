# Dolakha Verified Research Batch 02 — 2026-08-11

> Deep-research sidecar for Dolakha inventory entries 6–10. High-altitude route conditions, permits, conservation fees and operational details must be rechecked against current authorities before traveler-facing publication.

## 6. Charikot

- **District:** Dolakha
- **Municipality:** Bhimeshwor Municipality
- **Destination type:** District-headquarters hill town / transport and trekking gateway / service hub
- **Administrative role:** Charikot is the principal urban and administrative center used as the gateway for destinations across Dolakha, including historic Dolakha, Kalinchowk and northern trekking routes.
- **Tourism role:** For the route planner, Charikot is more useful as a gateway/service-area object than as one isolated attraction. Lodging, transport, hospitals/clinics, fuel, markets and onward-road junctions should later be modeled separately.
- **Relationship to historic Dolakha:** Do not merge Charikot with historic Dolakha town. They are distinct visitor areas within Bhimeshwor Municipality.
- **Coordinates:** Use an urban/service-area geometry plus verified bus/road junctions rather than one generic municipality coordinate.
- **Permit requirement:** No town-wide tourism permit identified.
- **Entry fee / hours:** None for the town itself.
- **Primary sources:**
  - https://bhimeshwormun.gov.np/
  - https://bhimeshwormun.gov.np/en/touristic-destination
- **Verification status:** Municipality/gateway role established; service-level POIs and exact gateway geometry remain later enrichment.

## 7. Charikot viewpoints

- **District:** Dolakha
- **Municipality:** Bhimeshwor Municipality
- **Destination type:** Hill viewpoints / Himalayan panorama cluster
- **Destination relationship:** Treat this as a cluster around the Charikot hill landscape rather than one invented viewpoint pin.
- **View context:** The Charikot/Bhimeshwor hill setting is used for views toward the surrounding Dolakha mountains and valleys; individual named public viewpoints need record-level verification before publication.
- **Object-modeling rule:** Keep as `viewpoint_cluster` until specific viewpoints are supported by municipality/local sources with coordinates and access details.
- **Weather caution:** Mountain visibility is conditional on season, cloud and haze and should never be guaranteed in traveler copy.
- **Coordinates:** Individual viewpoint pins pending GIS/local verification.
- **Permit requirement:** No area-wide tourism permit identified.
- **Primary source:**
  - https://bhimeshwormun.gov.np/en/touristic-destination
- **Verification status:** Cluster retained as first-round researched; individual viewpoint objects remain pending.

## 8. Gaurishankar Conservation Area

- **District context:** Northern Dolakha and adjoining mountain districts
- **Destination type:** Protected mountain landscape / biodiversity conservation area / trekking region
- **Protected-area role:** Gaurishankar Conservation Area is the governing conservation landscape for major northern Dolakha trekking destinations including Rolwaling and approaches toward high Himalayan valleys.
- **Route-planner modeling:** Store the conservation area as a protected-area polygon and separately store entry/check posts, trekking routes, settlements, lakes and peaks. Do not use a single centroid as the visitor destination.
- **Permit/fee rule:** Conservation-area entry requirements and fees are time-sensitive. Before publication, verify current rules directly with the responsible conservation authority/Nepal government and distinguish conservation entry from any immigration/TIMS/trekking or mountaineering requirements that may separately apply.
- **Environmental rule:** Traveler content should emphasize waste control, trail discipline, wildlife protection and local regulations because this is a protected landscape.
- **Coordinates:** Authoritative protected-area boundary geometry required in GIS layer.
- **Primary sources:**
  - https://ntnc.org.np/project/gaurishankar-conservation-area-project
  - https://dnpwc.gov.np/
- **Verification status:** Protected-area identity and northern-Dolakha trekking relationship established; current fee/permit table intentionally left for live verification.

## 9. Rolwaling Valley

- **District:** Dolakha
- **Municipality:** Gaurishankar Rural Municipality
- **Protected-area context:** Gaurishankar Conservation Area
- **Destination type:** Remote Himalayan trekking valley / Sherpa cultural landscape / high-altitude route system
- **Core route relationship:** Rolwaling is the parent valley for settlements such as Beding and Na and for the approach to Tsho Rolpa. These should remain separate records linked to the valley route.
- **Route-planner modeling:** Store Rolwaling as a trekking-corridor/valley object with staged settlements, trail segments, bridges, check posts and altitude points. Never represent the trek as a straight line to a valley centroid.
- **Access character:** Remote mountain access means roadhead and trail conditions can change; landslides, monsoon damage, snow and bridge status require current verification.
- **Permit rule:** Do not publish a static permit formula from secondary trekking sites. Resolve current conservation-area and any trekking/immigration requirements from official authorities before launch.
- **Safety:** High altitude and remoteness make acclimatization, weather and emergency planning important traveler-facing fields.
- **Coordinates:** Valley/trail geometry plus settlement coordinates required during GIS pass.
- **Primary sources:**
  - https://ntnc.org.np/project/gaurishankar-conservation-area-project
  - https://gaurishankarmun.gov.np/
- **Verification status:** Valley, municipality and protected-area relationships verified; route geometry and live permit/access conditions pending.

## 10. Tsho Rolpa Lake

- **District:** Dolakha
- **Municipality:** Gaurishankar Rural Municipality
- **Area:** Upper Rolwaling Valley, Gaurishankar Conservation Area
- **Destination type:** High-altitude glacial lake / trekking destination / glacial-hazard landscape
- **Route relationship:** Tsho Rolpa is reached through the Rolwaling trekking system and should be linked to Beding, Na and the upper-valley trail rather than treated as a drive-up lake.
- **Glacial context:** The lake is a major glacial lake and has long been associated with glacial-lake-outburst-flood monitoring and risk-management work. Traveler copy should present it as a sensitive high-mountain environment, not only a photo stop.
- **Route-planner modeling:** Lake polygon/centroid plus approach trail, safe visitor areas and altitude profile should be separate data layers.
- **Permit rule:** Current conservation/trekking requirements must be checked live from official authorities before publication.
- **Access/safety:** Weather, snow, trail damage, altitude and seasonal conditions materially affect access. Static travel-time claims should be avoided until route segments are verified.
- **Coordinates:** Publication-grade lake geometry should come from authoritative GIS/hydrological data.
- **Primary sources:**
  - https://ntnc.org.np/project/gaurishankar-conservation-area-project
  - https://gaurishankarmun.gov.np/
  - https://www.icimod.org/
- **Verification status:** High-altitude lake, Rolwaling and protected-area relationships established; exact GIS, current access and operational safety information remain live checks.

# Dolakha progress

- **Inventory entries:** 29
- **Deep-researched:** 10 / 29
- **Next entries:** 11–15 — Beding Village; Na Village; Yalung Ri trekking area; Gaurishankar mountain viewpoints; Lamabagar.

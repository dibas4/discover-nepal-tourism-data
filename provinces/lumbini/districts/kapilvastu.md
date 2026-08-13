# Kapilvastu District — Visitor-Ready Tourism Enrichment

## Introduction
Kapilvastu is one of Nepal's most important Buddhist archaeological districts. Its tourism identity is centered on the ancient Shakya landscape around Tilaurakot, Kudan, Gotihawa, Niglihawa, Sagarhawa and related sites, alongside Jagadishpur Reservoir, Taulihawa and the northern Chure belt.

## History
The district preserves the archaeological landscape traditionally associated with ancient Kapilavastu and the Shakya polity. Tilaurakot is the principal fortified urban site, while nearby stupas, Ashokan pillar sites, monasteries and settlement mounds form a wider Buddhist heritage circuit. Taulihawa later developed as the modern district gateway.

## Main visitor hubs
- **Taulihawa** — best base for Tilaurakot, Kudan, Gotihawa and Niglihawa.
- **Tilaurakot** — archaeological hub; use the official visitor entrance rather than a generic site centroid.
- **Jagadishpur** — wetland/birding access hub; route to a verified shoreline/observation access point.

## Places to visit and map behavior
| Place | Visitor introduction | Geometry | Things to do | Permit / entry | How to visit | Routing status |
|---|---|---|---|---|---|---|
| Tilaurakot archaeological site | Fortified ancient urban landscape linked with the Shakya capital tradition and Siddhartha Gautama's early life. | AREA / archaeological polygon | archaeology, interpretation, heritage walk | Heritage entry/visitor rules dynamic; no district travel permit | From Taulihawa by local road/taxi; route to official visitor entrance | READY_AREA |
| Tilaurakot eastern gate | Excavated gate complex on the eastern side of the ancient city. | POINT after GIS | archaeology, fortification study | Inherit Tilaurakot rules | Walk inside/around Tilaurakot heritage zone | GIS_PIN_PENDING |
| Tilaurakot western gate | Western gate remains and approach to the ancient fortified settlement. | POINT after GIS | archaeology, walking | Inherit Tilaurakot rules | From official Tilaurakot visitor route | GIS_PIN_PENDING |
| Tilaurakot fortification ramparts and moat | Defensive earthworks defining the ancient city boundary. | AREA / LINE | heritage walk, archaeology | Inherit Tilaurakot rules | Explore only on designated paths | READY_AREA |
| Kapilvastu Museum | Museum near Tilaurakot displaying archaeological finds from the wider Kapilavastu landscape. | POINT | museum, history | Museum hours/fee dynamic | From Taulihawa or Tilaurakot by local road | PIN_VERIFY |
| Kudan / Nigrodharama | Monastic and stupa landscape associated with Buddha's return to Kapilavastu. | AREA | pilgrimage, archaeology | Site rules dynamic | Short road transfer from Taulihawa/Tilaurakot | READY_AREA |
| Gotihawa Ashoka Pillar | Ashokan pillar site associated in Buddhist tradition with Kakusandha Buddha. | POINT + small precinct | pilgrimage, archaeology | No district permit; site operations dynamic | Road from Taulihawa | PIN_VERIFY |
| Gotihawa archaeological mound and stupa area | Archaeological landscape surrounding the pillar. | AREA | archaeology, walking | Inherit site rules | Same trip as Gotihawa pillar | READY_AREA |
| Niglihawa Ashoka Pillar | Ashokan pillar associated with Konagamana Buddha. | POINT + precinct | pilgrimage, history | No district permit | Road from Taulihawa; combine with Nigali Sagar | PIN_VERIFY |
| Nigali Sagar | Historic pond beside the Niglihawa heritage area. | WATER_AREA | landscape, photography | No special permit | Same road approach as Niglihawa | READY_AREA |
| Araurakot archaeological site | Fortified archaeological settlement in the Greater Lumbini heritage landscape. | AREA | archaeology | Heritage access dynamic | Use Taulihawa as hub; final local road/track must be checked | AREA_ACCESS_CHECK |
| Sagarhawa archaeological site | Large archaeological/commemorative landscape associated with the ancient Shakya region. | AREA | archaeology, heritage | Site rules dynamic | From Taulihawa via local road; verify final access | AREA_ACCESS_CHECK |
| Sagarhawa reservoir / Lumbusagar | Waterbody adjoining the archaeological landscape. | WATER_AREA | scenery, birding where appropriate | No special permit identified; access seasonal | Use verified shoreline access, not water centroid | ROUTE_TO_SHORE |
| Sisaniya archaeological site | Archaeological site within the ancient Kapilavastu cultural landscape. | AREA | archaeology | Dynamic site access | From Taulihawa; final route requires local verification | ACCESS_VERIFY |
| Kanthak Stupa | Stupa traditionally linked with Siddhartha's horse Kanthaka and the Great Departure narrative. | POINT / small precinct | pilgrimage, heritage | No district permit | Combine with Tilaurakot circuit | PIN_VERIFY |
| Twin Stupas | Pair of ancient stupas in the Tilaurakot archaeological circuit. | POINTS / small area | archaeology | Inherit heritage-zone rules | Visit from Tilaurakot | PIN_VERIFY |
| Lohasariya archaeological site | Excavated settlement area south of Tilaurakot. | AREA | archaeology | Access dynamic | From Tilaurakot/Taulihawa; verify public entrance | ACCESS_VERIFY |
| Piprahawa / Pipari stupa landscape, Nepal sector | Nepal-side archaeological name requiring precise identity separation from Piprahwa in India. | HOLD | none until identity verified | — | Do not route publicly yet | ROUTING_HOLD |
| Jagadishpur Reservoir | Major reservoir and internationally important wetland for migratory waterbirds. | WATER_POLYGON | birdwatching, wetland viewing, photography | No district permit; local/management rules dynamic | From Taulihawa/Banganga side to a verified observation/shore access point | READY_AREA |
| Jagadishpur birdwatching area | Visitor-facing birding product around the reservoir. | AREA / observation nodes | birdwatching | Seasonal and local access rules dynamic | Route to verified birding access, not reservoir center | ACCESS_NODE_REQUIRED |
| Banganga River corridor | Major river landscape crossing central Kapilvastu. | CORRIDOR | riverscape, rural scenery | No special permit; monsoon safety dynamic | Use named bridges/riverfronts only | ROUTE_NODE_REQUIRED |
| Arghakhanchi–Kapilvastu Chure foothill forest belt | Forest transition landscape in northern Kapilvastu. | AREA | nature, scenery | Forest access rules dynamic | Only route to verified public trails/roads | ROUTING_HOLD_FOR_TRAILS |
| Tauleshwor Nath Temple | Important Shiva temple in Taulihawa. | POINT / precinct | pilgrimage | Temple access/donations dynamic | Easy local access from Taulihawa | PIN_VERIFY |
| Ramghat and Banganga riverside religious area | Local riverside pilgrimage landscape. | AREA | pilgrimage, riverside visit | No district permit; local ritual access dynamic | Exact public access still needs verification | ROUTING_HOLD |
| Shivagadhi / local Chure religious-hill sites | Cluster of local hill shrines in northern Kapilvastu. | HOLD / cluster | pilgrimage after verification | Unknown site-specific rules | Do not publish as one pin | ROUTING_HOLD |
| Tharu cultural villages of western Kapilvastu | Living Tharu settlement landscape in the western rural belt. | MULTI_AREA | culture, food, community visits | Community consent/active products required | Route only to verified active community programs | PRODUCT_VERIFY |
| Taulihawa historic bazaar and Buddhist-circuit gateway | District headquarters and practical base for the Kapilvastu archaeological circuit. | TOWN_AREA | local market, food, trip staging | No permit | Main road hub for district visits | READY_AREA |

## Permit and entry model
Kapilvastu does **not** require a district-wide tourism permit. Archaeological-site tickets, museum hours, site closures, religious etiquette and local wetland rules are operational fields and must be refreshed before traveler publication.

## Things-to-do routing
- **Buddhist archaeology:** Taulihawa → Tilaurakot → Kudan → Gotihawa → Niglihawa; extend to Araurakot/Sagarhawa only with verified road access.
- **Birding:** route to a verified Jagadishpur observation/shore node.
- **Hindu pilgrimage:** Tauleshwor Nath and verified local shrines.
- **Community culture:** only active, consent-based Tharu tourism products.

## Safety / dynamic data
Monsoon road conditions, wetland water levels, excavation-zone closures, museum hours, festival crowds and local vehicle access are dynamic. Exact pins remain unpublished where the visitor entrance has not been verified.

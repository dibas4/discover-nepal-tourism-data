# Dolpa — Visitor-Ready Tourism Enrichment

## Introduction
Dolpa is one of Nepal's most remote trans-Himalayan destinations, centered on Shey Phoksundo National Park, Phoksundo Lake, Upper Dolpo's Tibetan-influenced villages and monasteries, Tarap Valley, high passes and long-distance trekking corridors. **Juphal** and **Dunai** are the practical access hubs.

## History and cultural context
Dolpa preserves Bon and Tibetan Buddhist traditions, historic trade routes and high-altitude settlements shaped by seasonal agriculture, pastoralism and pilgrimage. Visitor content must distinguish protected-area entry, restricted-area permits and ordinary village/route access.

## Permit and entry profile
- **Upper Dolpa restricted-area permit:** applies only to the current Immigration-defined covered wards; fee/rules must be refreshed from Immigration before publication.
- **Lower Dolpa restricted-area permit:** separate rule and geography from Upper Dolpa.
- **Shey Phoksundo National Park entry:** separate protected-area requirement; use current DNPWC rules/fees.
- Climbing/expedition authorization, where relevant, is separate again.
- Flights, checkpoints, bridges, lodges, weather and trail closures are always dynamic.

## Canonical visitor records
| Place | Visitor meaning / things to do | Map model | Access / routing |
|---|---|---|---|
| Shey Phoksundo National Park | Protected trans-Himalayan landscape | PROTECTED_AREA | Route to official checkpoint/gateway, never park centroid |
| Phoksundo Lake | Flagship high-altitude lake | WATER_POLYGON | Route to Ringmo/verified shoreline viewpoints, not lake center |
| Ringmo Village | Main visitor settlement beside Phoksundo | AREA | Reach on Suligad–Phoksundo trail |
| Tshowa Bon Monastery | Bon heritage above Ringmo | POINT/HOLD | Exact public entrance after local verification |
| Phoksundo Waterfall | Major outlet waterfall | POINT/AREA | Use verified trail viewpoint; seasonal safety applies |
| Suligad Valley and Trail | Main lower approach to Phoksundo | ROUTE/CORRIDOR | Trail conditions/checkpoints refreshed before routing |
| Shey Gompa | Major Upper Dolpo monastery/pilgrimage site | POINT/AREA | Restricted-area route; seasonal expedition logistics |
| Crystal Mountain / Shelri | Sacred circumambulation landscape | AREA/ROUTE | Sacred route, not summit pin; local rules required |
| Shey Festival Landscape | Periodic pilgrimage event | EVENT/AREA | Dates and visitor arrangements dynamic |
| Upper Dolpo Cultural Landscape | Broad Tibetan-influenced highland region | AREA | Parent system containing villages/routes, not a destination pin |
| Lower Dolpo Trekking Region | Multi-route trekking region | ROUTE_NETWORK | Use exact itinerary segments and checkpoints |
| Dho Tarap Village | Major high-altitude settlement | AREA | Reach via Tarap route; restricted-area rule depends on covered geography |
| Tarap Valley | Agricultural/cultural trekking landscape | AREA/CORRIDOR | Route through named settlements |
| Saldang Village | Upper Dolpo heritage settlement | AREA | Remote restricted-area access |
| Yangjer Gompa | Monastery near Saldang | POINT/HOLD | Official spelling/location pending |
| Tinje Village | Eastern Upper Dolpo route settlement | AREA | High-altitude route hub |
| Chharka Bhot Village | Remote trekking/trade settlement | AREA | Route toward passes/Mustang only with current itinerary data |
| Mukot Village and Valley | Remote mountain settlement/valley | AREA/HOLD | Accommodation and approach require local verification |
| Dunai Bazaar | District headquarters and overland organization hub | AREA | Main lower-Dolpa service hub |
| Juphal | Air gateway | POINT/AREA | Flights are dynamic; connect onward to Dunai/trails |
| Tripurasundari Temple | Major district pilgrimage site | AREA/POINT | Road/trail from lower Dolpa hub; festival status dynamic |
| Tripurakot Heritage Settlement | Historic settlement near temple | AREA | Pair with Tripurasundari visit |
| Kaike Cultural Landscape | Indigenous cultural region | AREA | Publish specific villages only after local verification |
| Tichurong Valley | Distinct lower-Dolpo cultural/trekking region | AREA/CORRIDOR | Route-network entity |
| Num La Pass | High trekking pass | ROUTE_NODE | Seasonal snow/altitude rule |
| Baga La Pass | High pass between Tarap/Phoksundo systems | ROUTE_NODE | Seasonal hazard checks mandatory |
| Kang La Pass (Dolpo) | High pass on Shey approach | ROUTE_NODE | Disambiguate from other Kang La passes |
| Jeng La Pass | Remote Upper Dolpo pass | ROUTE_NODE/HOLD | Alignment and naming require specialist verification |
| Thuli Bheri River Corridor | Main river and access landscape | CORRIDOR | Named road/trail viewpoints only |
| Kanjiroba Himal Landscape | Mountain/wilderness massif | AREA | Trek/climb routes need separate authorization checks |
| Snow Leopard and Blue Sheep Habitat | Conservation habitat | HABITAT_AREA | Never present as guaranteed sighting point |
| Yarsagumba Collection Landscapes | Seasonal livelihood/pasture areas | AREA/HOLD | Do not promote without community approval/current rules |

## Planner defaults
For Phoksundo trips use **Juphal → Dunai/Suligad → Ringmo** as a conceptual access chain, but every flight, road, checkpoint and trail segment must be refreshed. Upper Dolpo routes must never be generated without the correct current restricted-area permit logic.
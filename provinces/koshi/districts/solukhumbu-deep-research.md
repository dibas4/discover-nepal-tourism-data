# Solukhumbu District Deep Research + QA — 2026-08-12

> Canonical inventory: 34 records. This pass uses Sagarmatha National Park and Nepal Tourism Board rules as the primary backbone, separates protected-area features from settlements and mountaineering objectives, and treats current trekking/permit rules as dynamic data.

## Authoritative source backbone
- Sagarmatha National Park official site: https://snp.gov.np/
- Nepal Tourism Board TIMS/trekking pages: https://ntb.gov.np/
- Relevant Solukhumbu local governments for lower-Solu cultural/religious destinations.

## Record dispositions
|#|Record|Status|Decision|
|---|---|---|---|
|1|Ama Dablam|VERY STRONG PASS|Sagarmatha National Park officially lists Ama Dablam; mountain/expedition object. Climbing permits and route conditions are dynamic.|
|2|Cho La Pass|VERY STRONG PASS|Core Three Passes/Gokyo–EBC route node. Current NTB TIMS rule covers Chho/Cho La trekking; weather/closure/ice conditions dynamic.|
|3|Dharmadanda|PASS-PARTIAL|Sacred/viewpoint hill in lower Solu border landscape. Exact summit, local religious meaning and route need Sotang/Thulung local verification.|
|4|Dingboche|VERY STRONG PASS|Established Imja Valley Sherpa settlement and acclimatization/trek hub within Everest route system. Settlement/service object.|
|5|Dudhkunda Lake|VERY STRONG PASS|Major sacred alpine lake/pilgrimage-trek destination in Solududhkunda. Lake/route object; festival/trail/season conditions dynamic.|
|6|Everest Base Camp|VERY STRONG PASS|Sagarmatha National Park officially features EBC. High-altitude trekking destination; current NTB TIMS/guide rule applies. Route, weather and campsite conditions dynamic.|
|7|Gokyo Lakes|VERY STRONG PASS|Official Sagarmatha National Park: Gokyo and associated lakes designated Ramsar wetland in 2007. Wetland system/area object rather than single lake pin.|
|8|Gokyo Ri|VERY STRONG PASS|Official park-highlighted panorama point. Viewpoint/trek node; weather visibility dynamic.|
|9|Gorakshep|VERY STRONG PASS|High-altitude settlement/staging node for EBC/Kala Patthar. Settlement/service object; accommodation capacity/current operations dynamic.|
|10|Hinku Valley|STRONG PASS|Major trekking valley in Mahakulung/Mera corridor. Valley/route landscape; exact trail conditions and seasonal access dynamic.|
|11|Imja Tsho|VERY STRONG PASS|Sagarmatha National Park documents Imja glacial-lake system in Imja catchment. Glacial-lake landscape; hazard/access data require current scientific/park sources.|
|12|Island Peak / Imja Tse|VERY STRONG PASS|Established climbing/trekking peak in Imja Valley. Expedition/climbing object; permits/guides/conditions dynamic.|
|13|Junbesi Village|VERY STRONG PASS|NTB’s historic Jiri–Lukla/Everest approach explicitly includes Junbesi. Sherpa cultural/trek settlement; living-community object.|
|14|Kala Patthar|VERY STRONG PASS|Official park material features Everest view from Kalapathar. Viewpoint/trek node; not a separate settlement.|
|15|Khiraule Monastery|STRONG PASS-PARTIAL|Important Mahakulung Buddhist cultural site. Exact monastery name, visitor etiquette/access and current operation require local verification.|
|16|Khumbu Glacier|VERY STRONG PASS|Official park physical-features page identifies Khumbu Glacier. Natural/glacial feature; no unrestricted walking-access implication.|
|17|Khumbu Icefall|VERY STRONG PASS-EXPEDITION|Official Everest expedition landscape. Technical climbing hazard, not a general tourist attraction; route access restricted to expedition context.|
|18|Khumjung Village|VERY STRONG PASS|Official park recognizes Khumjung as major Sherpa settlement/monastery landscape. Village/heritage object.|
|19|Kongma La Pass|VERY STRONG PASS|Core Three Passes route node. High-altitude trekking pass; weather/trail conditions and current guide/TIMS requirements dynamic.|
|20|Mera Peak|VERY STRONG PASS|Major trekking peak in Mahakulung/Hinku landscape. NTB TIMS list includes Mera Peak Trek; climbing permit requirements handled separately/currently.|
|21|Mount Everest / Sagarmatha|VERY STRONG PASS|Official park lists elevation 8,848.80 m and World Heritage park context. Mountain/expedition parent object, not ordinary sightseeing pin.|
|22|Namche Bazaar|VERY STRONG PASS|Official park identifies Namche as main settlement and visitor hub. Settlement/service gateway; live lodging/transport/business data separate.|
|23|Ngozumpa Glacier|VERY STRONG PASS|Official park physical-features page identifies Ngozumpa Glacier and its relation to Gokyo lakes. Natural feature/area object.|
|24|Panch Pokhari, Mahakulung|STRONG PASS-PARTIAL|Sacred glacial-lake cluster in Mahakulung retained. Exact lake count/geometry, pilgrimage route and local ritual context require municipality/GIS verification.|
|25|Pikey Peak|VERY STRONG PASS|Established lower-Solu Himalayan viewpoint/trek. Route/viewpoint object; exact trailheads and seasonal condition current.|
|26|Renjo La Pass|VERY STRONG PASS|Official Sagarmatha National Park highlights Renjo La; NTB TIMS list includes Gokyo Renjo La route. High pass/route node.|
|27|Sagarmatha National Park|VERY STRONG PASS|Official: established 19 July 1976, 1,148 km²; UNESCO World Heritage 1979; buffer zone 275 km² from 2002. Protected-area parent object.|
|28|Taksindu Monastery|VERY STRONG PASS|Historic Buddhist monastery on the classic lower-Solu/Jiri–Lukla approach. Living religious POI; exact visitor etiquette/hours current.|
|29|Tengboche Monastery|VERY STRONG PASS|Official park specifically recognizes Tengboche as renowned monastery and festival gathering place. Religious/cultural POI within Khumbu route system.|
|30|Thupten Chholing Monastery|STRONG PASS|Major monastery in Junbesi area. Living religious/community site; access/retreat/visitor rules require current local verification.|
|31|Lukla|VERY STRONG PASS-GATEWAY|Primary air/trek gateway into Khumbu; park buffer extends toward Lukla. Flight schedules/weather/airport operations dynamic.|
|32|Pangboche Monastery and Village|VERY STRONG PASS|Official park identifies Pangboche among famous monastery settlements. Separate village/monastery child nodes during GIS/CMS refinement.|
|33|Phaplu|VERY STRONG PASS-GATEWAY|Lower-Solu air/road/service gateway in Solududhkunda. Flight schedules and road conditions dynamic.|
|34|Thame Village and Monastery|VERY STRONG PASS|Official park recognizes Thame as famous monastery settlement. Village/monastery/valley cluster; trail/weather status dynamic.|

## QA decisions
- Sagarmatha National Park is the parent protected landscape; glaciers, lakes, passes, villages and monasteries are child features/nodes.
- Gokyo Lakes is a Ramsar wetland system; Gokyo Ri, Renjo La and Ngozumpa Glacier remain separate but linked.
- Everest Base Camp, Kala Patthar, Gorakshep and Khumbu Glacier/Icefall are distinct route/natural/settlement objects, avoiding one bloated ‘Everest’ record.
- Khumbu Icefall is expedition-only technical terrain and should never be promoted as a normal tourist walk.
- Current NTB rules list Everest Basecamp, Gokyo, Chho La, Gokyo-Renjo La, Three Passes and Mera Peak among routes requiring licensed guide + agency-issued TIMS; regulations must be refreshed before traveler-facing use.
- Mountaineering permits, park fees, local-entry fees, flight schedules and trail closures are dynamic operational data.
- Monasteries are living religious institutions; visitor access/etiquette belongs in current/local fields.

## QA result
**34 / 34 records dispositioned.**

Solukhumbu deep research and district QA are complete. Remaining work is GIS/current-operations/permit/media enrichment.
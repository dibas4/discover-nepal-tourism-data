# Bhojpur District Deep Research + QA — 2026-08-12

> Canonical inventory: 30 records. This pass verifies destination identity, normalizes route/area/POI modeling, preserves uncertainty, and avoids inventing coordinates or live operations.

## Source backbone

Primary/authoritative sources used in this pass:
- Nepal Tourism Board, Mundhum Trail: https://ntb.gov.np/en/mundhum-trail-nepals-hidden-cultural-ridge-trek-in-2025
- Nepal Tourism Board, Mundum Trail Visit Year: https://trade.ntb.gov.np/?p=14746
- Nepal Film Development Board, Temke/Mundhum destination profile: https://www.film.gov.np/destination/49
- Temkemaiyung Rural Municipality: https://www.tyamkemaiyummun.gov.np/
- Bhojpur Municipality introduction/tourism list: https://www.bhojpurmun.gov.np/ne/node/3
- Salpasilichho Rural Municipality, Salpa Pokhari: https://salpasilichhomun.gov.np/content/salpa-pokhari
- Salpasilichho Ward 5 profile: https://salpasilichhomun.gov.np/content/%E0%A4%B5%E0%A4%A1%E0%A4%BE-%E0%A4%A8%E0%A5%AB-%E0%A4%B5%E0%A4%A1%E0%A4%BE-%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%B2%E0%A4%AF
- Koshi Province tourism/forest ministry wetland page: https://tourism.koshi.gov.np/%E0%A4%B8%E0%A4%BF%E0%A4%AE%E0%A4%B8%E0%A4%BE%E0%A4%B0/
- Shadananda Municipality: https://shadanandamun.gov.np/en
- Hatuwagadhi Rural Municipality: https://www.hatuwagadhimun.gov.np/

## Record dispositions

| # | Record | Status | Route-planner / CMS decision |
|---|---|---|---|
| 1 | Arun River Corridor | PASS-LANDSCAPE | Keep as linear river/valley landscape, not a single pin. Exact recreation/access nodes require GIS and safety verification. |
| 2 | Bhojpur Khukuri Craft Centres | PARTIAL | Bhojpur/Taksar craft identity is credible, but publish individual workshops only after current business/visitor-access verification. Model as craft cluster. |
| 3 | Hatuwagadhi Durbar | PASS-PARTIAL | Hatuwagadhi municipality explicitly identifies the area as historic Kirat land. Keep fort/durbar heritage record, but exact surviving structures, ward, entrance and interpretation require local heritage/GIS pass. |
| 4 | Maiyung Danda | STRONG PASS | NTB Mundhum Trail explicitly includes Maiyung/Mayung on the route. Model as highland ridge/viewpoint landscape. |
| 5 | Mundhum Trail | VERY STRONG PASS | NTB-supported multi-district cultural trekking route across Bhojpur, Khotang, Solukhumbu and Sankhuwasabha. Store as route object; do not assign the entire route to Bhojpur. |
| 6 | Salpa Pokhari | VERY STRONG PASS | Salpasilichho municipality confirms the lake in Ward 5 and publishes a reference coordinate 27.4463127, 86.9316548. Sacred lake + trekking/pilgrimage node. |
| 7 | Silichung Peak | VERY STRONG PASS | NTB identifies Silichung as the highest/high-point objective of the Mundhum route (published values vary slightly around 4,110–4,153 m). Keep altitude as source-qualified until GIS/topographic normalization. |
| 8 | Temke Danda | VERY STRONG PASS | Government film destination profile verifies Temke, mountain views, temple/cave context and Mundhum connection. Area/viewpoint object. |
| 9 | Bhojpur Bazaar | PASS | District town/gateway object. Use as service/cultural hub, not a single attraction pin. |
| 10 | Bidhya Pokhari | HOLD | Inventory identity retained, but no strong primary destination-level evidence captured in this pass. Do not publish coordinates/history yet. |
| 11 | Chakhewa Danda | VERY STRONG PASS | NTB identifies Chakhewa Bhanjyang as the Mundhum Trail start/base gateway around 2,300 m. Normalize search aliases Chakhewa/Chekhwa. |
| 12 | Chamere Gufa | HOLD | Local inventory candidate; exact cave identity/access/safety not sufficiently verified from primary sources. |
| 13 | Dimalung Park | HOLD / LOCAL | Keep as local candidate only. Current public visitor facilities and exact site identity require municipality verification. |
| 14 | Dingla Bazaar | STRONG PASS | Shadananda Municipality is centered at Dingla Bazaar and officially showcases the historic market/culture. Settlement/heritage-market object. |
| 15 | Dobhane | PASS-GATEWAY | Salpasilichho Ward 5 profile confirms the former Dobhane area and Salpa access context. Model as settlement/gateway, not a standalone attraction. |
| 16 | Hans Pokhari | STRONG PASS | NTB Mundhum material identifies Maiyung/Hans Pokhari on the trail. Wetland/highland trail node; exact lake geometry pending. |
| 17 | Indreni Jharna | STRONG PASS | Hatuwagadhi municipality currently showcases Indreni Waterfall. Exact approach, swimming/canyoning safety and coordinates remain current/GIS fields. |
| 18 | Mahavir Waterfall | PARTIAL | Retain as Temkemaiyung local waterfall candidate; exact identity/access needs primary municipality or field confirmation before publication. |
| 19 | Maluwa Pokhari | PARTIAL | Retain as local highland pond candidate; geometry and visitor relevance need local confirmation. |
| 20 | Ramchandra Temple | STRONG PASS | Shadananda Municipality currently features the Ramchandra Temple premises. Treat as living religious POI; hours/ritual access remain dynamic. |
| 21 | Rawa Dhap | VERY STRONG PASS | Explicit NTB Mundhum Trail stop. Model as highland wetland/meadow trail node. |
| 22 | Sahid Samadhi Sthal | HOLD / LOCAL | Memorial identity needs exact official name, ward and public-access verification. |
| 23 | Salpa Bhanjyang | VERY STRONG PASS | Explicit NTB Mundhum Trail pass between Maiyung/Rawa Dhap and Salpa/Silichung landscape. Route/pass object. |
| 24 | Sawa Waterfall | PARTIAL | Local waterfall candidate; no sufficiently strong record-level primary source captured. Safety and location HOLD. |
| 25 | Selme Danda | PARTIAL | Local viewpoint/hike candidate; retain but do not publish exact claims/coordinates until municipality/GIS confirmation. |
| 26 | Shila Sutkeri | HOLD | Name/significance too weakly sourced for traveler-facing publication. Preserve candidate only. |
| 27 | Siddhakali Temple | VERY STRONG PASS | Bhojpur Municipality explicitly lists Siddhakali Temple, Ward 5, among religious tourism sites. Exact entrance pin still requires GIS. |
| 28 | Suntale Danda | VERY STRONG PASS | Bhojpur Municipality explicitly lists Suntale Danda in Ward 3 and describes its Arun/Temke/Chakhewa views. |
| 29 | Taksar Bazaar | PASS-PARTIAL | Established historical/craft settlement context; treat as heritage settlement/craft cluster. Individual craft businesses need current verification. |
| 30 | Tawa Bhanjyang | PARTIAL | Plausible Temkemaiyung trail/viewpoint node, but exact record-level primary evidence is insufficient in this pass. Keep pending GIS/local confirmation. |

## Key modeling and data-quality decisions

- `Mundhum Trail` is one cross-district route object. Maiyung, Hans Pokhari, Rawa Dhap, Salpa Bhanjyang and Silichung are child/stage destinations rather than duplicate full routes.
- `Arun River Corridor` is a linear landscape. Do not assign one arbitrary coordinate.
- `Bhojpur Khukuri Craft Centres` and `Taksar Bazaar` should support a craft/heritage cluster; individual commercial workshops require live verification before recommendation.
- Salpa Pokhari has a municipality-published reference coordinate; other uncertain records do not inherit guessed map coordinates.
- Waterfalls require access/season/safety fields. No swimming or canyoning claim is assumed safe by default.
- Cultural/Kirat sacred landscapes should be described as living heritage, not staged attractions.

## QA result

**30 / 30 records dispositioned.**

Strong/pass records: 18
Partial/local records requiring further verification: 8
Hold records: 4

Bhojpur is complete at the deep-research + district-QA level. Remaining work is the separate GIS/current-operations/media layer.
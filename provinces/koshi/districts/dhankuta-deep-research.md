# Dhankuta District Deep Research + QA — 2026-08-12

> Canonical inventory: 26 records. This pass verifies the established destination backbone, distinguishes clusters from POIs, and preserves uncertain local records as PARTIAL/HOLD.

## Authoritative source backbone
- Nepal Tourism Board, Dhankuta attractions/community tourism: https://ntb.gov.np/
- Nepal Film Development Board, Bhedetar destination profile: https://www.film.gov.np/
- District Administration Office Dhankuta district profile: https://daodhankuta.moha.gov.np/
- Dhankuta Municipality tourism pages: https://dhankutamun.gov.np/
- Sangurigadhi Rural Municipality: https://sangurigadhimun.gov.np/
- Pakhribas Municipality: https://pakhribasmun.gov.np/
- Mahalaxmi Municipality, Dhankuta: https://mahalaxmimundhankuta.gov.np/

## Record dispositions
| # | Record | Status | Decision |
|---|---|---|---|
|1|Bhedetar|VERY STRONG PASS|Major hill-station/gateway. Municipality office is itself at Bhedetar; NTB/government destination profiles strongly confirm tourism identity. Area object, not one viewpoint pin.|
|2|Charles Point|STRONG PASS|Verified as the principal Bhedetar lookout/Charles Danda tradition. Keep viewpoint POI; exact safe viewing platform geometry requires GIS/current check.|
|3|Hile Bazaar|VERY STRONG PASS|Dhankuta Municipality officially classifies Hile Bazaar as religious/cultural/tourism area and publishes reference coordinate 27.0380439, 87.3046982. Settlement/gateway object.|
|4|Kopche Heritage Trail|STRONG PASS|NTB-backed Kopche heritage/community tourism context. Model as walking route through heritage settlement, not a single pin.|
|5|Namaste Jharana|VERY STRONG PASS|NTB/government destination material confirms Simsuwa/Namaste waterfall near Bhedetar. Waterfall safety/access/season fields remain dynamic.|
|6|Namje Village|VERY STRONG PASS|Government and municipality material confirms Namje as tourism/community settlement; link to Thumki and community facilities.|
|7|Namje–Thumki Community Homestay|PASS-CURRENT CHECK|Community-homestay identity strongly supported, but individual operating homes/capacity/prices require live verification. Treat as community-stay cluster.|
|8|Rajarani Wetland|STRONG PASS|District/official tourism sources establish Rajarani as major Dhankuta destination. Model wetland landscape separately from settlement/valley.|
|9|Rani Tal / Rani Lake|PASS|Lake/wetland node within Rajarani landscape. Do not duplicate the whole Rajarani destination; exact lake geometry required.|
|10|Aathpahariya Baunna Chulo Ghar|PASS-PARTIAL|Aathpahariya cultural heritage in Dhankuta is strongly documented; exact visitor facility/operating status needs municipality confirmation before publication.|
|11|Banjhakri Park|PARTIAL|Retain as Mahalaxmi local cultural/recreation candidate; exact current public operation and coordinates not strongly verified.|
|12|Chintang Devi Temple|STRONG PASS|District sources identify Chintang/Panchakanya religious-historical landscape. Living religious POI; exact entrance/ritual access pending.|
|13|Chuliban View Tower|PARTIAL-CURRENT CHECK|Known Dhankuta viewpoint facility; exact tower condition/opening and safe access require current municipality verification.|
|14|Dhankuta Bazaar|VERY STRONG PASS|Historical district town and primary cultural/service hub; NTB and municipality sources support. Settlement object.|
|15|Jitpur Bazaar|PASS|Mahalaxmi municipal headquarters at Jitpur confirms settlement importance. Treat as historical/service settlement; specific heritage structures need local verification.|
|16|Kopche Heritage Settlement|STRONG PASS|Keep as heritage neighbourhood/area; link Kopche Heritage Trail as route child rather than duplicate destination.|
|17|Latibhanjyang Shiva Statue|PARTIAL|Religious/viewpoint candidate retained; exact statue identity, completion/current access and coordinate need first-party record-level confirmation.|
|18|Leguwa–Arun River Confluence Area|PASS-LANDSCAPE|Valid river/road landscape in Mahalaxmi/Leguwa corridor. Linear/area object; no arbitrary point.|
|19|Nageshwar Temple|PARTIAL|Leguwa religious candidate; exact official identity/access needs municipality-level verification before traveler publication.|
|20|Pakhribas Agricultural Research Centre|VERY STRONG PASS|Pakhribas Municipality officially identifies the agricultural research centre and agro-tourism/education value. Facility-level POI; visitor access may be restricted/dynamic.|
|21|Pakhribas Bazaar|STRONG PASS|Municipality seat/scenic hill settlement; use as gateway/service town.|
|22|Pathibhara Temple near Hile|STRONG PASS|Government destination material confirms Pathibhara religious attraction in the Bhedetar/Hile corridor. Preserve locality qualifier to avoid confusion with Taplejung Pathibhara.|
|23|Rajarani Valley|STRONG PASS|Keep as broader settlement/valley landscape, separate from wetland and Rani Tal.|
|24|Sadam Tourism Area|HOLD/EMERGING|Retain emerging Chaubise candidate; current facilities, exact boundaries and visitor readiness require local verification.|
|25|Syaule–Sipting Aathpahariya Community Homestay|PARTIAL-CURRENT CHECK|Community/cultural-tourism concept credible; verify active homestay households and booking/visitor operations before recommendation.|
|26|Thumki Hill|STRONG PASS|Sangurigadhi has formally invested in Thumki/Namje tourism infrastructure. Hill/viewpoint object linked to Namje cluster; exact trail/parking geometry pending.|

## QA decisions
- Bhedetar is the destination/gateway; Charles Point is a child viewpoint, not a duplicate page.
- Namje, Thumki and the homestay form one community-tourism cluster with separate settlement/viewpoint/stay object types.
- Rajarani Valley, Rajarani Wetland and Rani Tal remain linked but distinct area/wetland/lake records.
- Kopche Settlement and Kopche Heritage Trail remain area + route, not duplicate POIs.
- Hile and Dhankuta Bazaar are settlement hubs; services/businesses should not be frozen as permanent attractions.
- Current homestay operation, view-tower condition, entry fees and road conditions remain live-data tasks.
- Do not use invalid placeholder coordinates found on some municipal pages; only authoritative, plausible record-level coordinates are accepted.

## QA result
**26 / 26 records dispositioned.**

Deep research and district QA are complete. Remaining work belongs to GIS/current-operations/media enrichment.
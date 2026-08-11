# Kavrepalanchok Verified Research Batch 02 — 2026-08-11

> Deep-research sidecar for Kavrepalanchok inventory entries 6–10. Time-sensitive operations and GIS geometry remain publication-time checks.

## 6. Panauti sacred confluence / Triveni Ghat

- **District:** Kavrepalanchok
- **Municipality:** Panauti Municipality
- **Destination type:** Sacred river confluence / pilgrimage landscape / ritual-ghat heritage area
- **Municipality context:** Panauti Municipality's official site prominently features `Triveni Ghat Parisar` and describes Panauti as a cultural city noted for jatras, the 12-year Makar Mela and major temples including Indreshwar Mahadev.
- **Hydrological-cultural identity:** The sacred confluence is traditionally associated with the Roshi and Punyamata river system and forms a core ritual landscape of historic Panauti. Because the site is a river/ghat complex rather than one monument, it should be modeled as an area object.
- **Festival context:** Panauti Municipality identifies Makar Mela as one of the city's defining traditions; exact Gregorian dates and event-access arrangements must be taken from the relevant year's municipal/local notices.
- **Route-planner modeling:** Store the confluence/ghat area separately from Indreshwar Mahadev Temple and Panauti Museum. Use riverbank/ghat geometry plus verified access points rather than a single town centroid.
- **Permit requirement:** No separate tourism permit identified.
- **Entry fee / hours:** No universal official fee or opening schedule identified for the public confluence area.
- **Primary sources:**
  - https://panautimun.gov.np/en
- **Verification status:** Municipality, Triveni Ghat identity and ritual/festival significance verified; detailed river-confluence geometry pending GIS QA.

## 7. Dhulikhel

- **District:** Kavrepalanchok
- **Municipality:** Dhulikhel Municipality
- **Destination type:** Hill town / tourism gateway / Himalayan-view destination
- **Elevation:** Dhulikhel Municipality places the city at about 1,550 m above sea level.
- **Access context:** Municipality states Dhulikhel is roughly 30 km southeast/east of Kathmandu and lies on the Arniko Highway; both Arniko Highway and B.P. Highway pass through the municipality.
- **View significance:** The municipality states that on clear days more than 20 Himalayan peaks can be seen from different points around Dhulikhel, including major central/eastern Himalayan ranges.
- **Tourism context:** Nepal Tourism Board describes Dhulikhel as an important former trade post and a hill destination with Himalayan panoramas, sunrise walks and links to Namo Buddha.
- **Cultural identity:** Dhulikhel Municipality describes the city as rich in ancient traditions, with a strong Newar presence and multiple historic temples. The older Buddhist name `Shrikhandapur` is also retained in municipality material.
- **Route-planner modeling:** Treat Dhulikhel as an area/town destination with linked hotel, old-town, viewpoint and trail POIs; do not use one city-centroid coordinate for all experiences.
- **Permit requirement:** No area-wide tourism permit identified.
- **Primary sources:**
  - https://www.dhulikhelmun.gov.np/en/node/4
  - https://trade.ntb.gov.np/tourist-destination/hill-stations/
- **Verification status:** Municipality, elevation, highway access, tourism role and Himalayan-view identity verified.

## 8. Dhulikhel old town

- **District:** Kavrepalanchok
- **Municipality:** Dhulikhel Municipality
- **Core wards:** Municipality records identify Ward 6 as the main Dhulikhel city/old-city area and Ward 7 as another historic core with temples and long-standing Newar settlement.
- **Destination type:** Historic Newar settlement / heritage streets / temple and courtyard area
- **Ward 6 context:** Dhulikhel Municipality describes Ward 6 as the main Dhulikhel city and an old city, with important religious heritage including Bhagawati Temple.
- **Ward 7 context:** Municipality states Ward 7 contains historic temples including Harisiddhi, Shesh Narayan, Lankhanamai, Garud and Manabinayak and traces organized settlement back to the medieval period.
- **Modeling note:** Old Dhulikhel should be a multi-block heritage-area object, not a single POI. Individual temples, chowks and heritage streets can later be mapped as sub-POIs.
- **Coordinates:** Capture historic-core polygon(s) and walkable access points during GIS QA; do not use the municipal office coordinate.
- **Permit requirement:** No town-wide heritage permit identified.
- **Entry fee / hours:** No universal old-town fee or opening schedule.
- **Primary sources:**
  - https://dhulikhelmun.gov.np/en/node/808
  - https://dhulikhelmun.gov.np/en/node/809
  - https://www.dhulikhelmun.gov.np/en/node/4
- **Verification status:** Historic-core ward context and temple heritage verified from municipality sources.

## 9. Dhulikhel viewpoints

- **District:** Kavrepalanchok
- **Municipality:** Dhulikhel Municipality
- **Destination type:** Sunrise/Himalayan panorama viewpoints / ridge walking destinations
- **Municipality view context:** Dhulikhel Municipality states that major Himalayan peaks can be viewed from different points throughout the city on clear days.
- **NTB viewpoint guidance:** Nepal Tourism Board identifies an early-morning roughly 30-minute hike to Bhagawati Temple as a sunrise viewpoint and notes ridge trails north of town.
- **Object-modeling rule:** Do not store `Dhulikhel viewpoints` as one point. Future route-planner data should split specific public viewpoints, ridge walks and temple-based viewpoints into distinct POIs/routes.
- **Potential anchor:** Bhagawati Temple sunrise point is a confirmed tourism anchor from NTB; other popular named viewpoints should be individually verified before being added.
- **Season/weather caution:** Himalayan visibility is weather-dependent; traveler-facing content should present views as conditional rather than guaranteed.
- **Permit requirement:** No area-wide tourism permit identified.
- **Entry fee / hours:** No universal viewpoint fee or schedule identified; facility-specific points may differ.
- **Primary sources:**
  - https://www.dhulikhelmun.gov.np/en/node/4
  - https://trade.ntb.gov.np/tourist-destination/hill-stations/
- **Verification status:** Dhulikhel panorama/sunrise identity and Bhagawati hiking anchor verified; viewpoint-level GIS mapping remains pending.

## 10. Banepa old town

- **District:** Kavrepalanchok
- **Municipality:** Banepa Municipality
- **Destination type:** Historic Newar trading town / religious-cultural heritage area
- **Municipality identity:** Banepa Municipality describes Banepa as an ancient town with historical and religious importance and as a major commercial center of Kavrepalanchok.
- **Setting:** Municipality material places old Banepa between surrounding forests/hills and notes the Punyamata river corridor around the town.
- **Name/trade context:** Banepa Municipality explains the place-name through the ideas of commerce/trading settlement and emphasizes the town's long-standing role as a market center.
- **Heritage modeling:** Store old Banepa as a heritage-area object, with Chandeshwari Temple and other individually verified monuments as separate POIs. Avoid treating the modern municipality's entire urban footprint as `old town`.
- **Coordinates:** Historic-core polygon and pedestrian access points require GIS QA; use municipality resource maps later for ward-level geometry.
- **Permit requirement:** No town-wide tourism permit identified.
- **Entry fee / hours:** No universal old-town admission fee or opening schedule.
- **Primary sources:**
  - https://www.banepamun.gov.np/ne/node/3
  - https://www.banepamun.gov.np/en/content/%E0%A4%AC%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE-%E0%A4%A8%E0%A4%97%E0%A4%B0%E0%A4%AA%E0%A4%BE%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A4%BE-%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%A4-%E0%A4%A8%E0%A4%95%E0%A5%8D%E0%A4%B6%E0%A4%BE
- **Verification status:** Ancient-town, religious/historical and trading-center identity verified from Banepa Municipality; exact heritage-core geometry pending.

# Kavrepalanchok progress

- **Inventory entries:** 32
- **Deep-researched:** 10 / 32
- **Next entries:** 11–15 — Chandeshwari Temple; Palanchok Bhagwati Temple; Panchkhal Valley; Bethanchok Narayanthan; Bethanchok Hill.

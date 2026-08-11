# Dolakha Verified Research Batch 01 — 2026-08-11

> Deep-research sidecar for Dolakha inventory entries 1–5. Current fares, operating hours and mountain-road conditions are time-sensitive and must be rechecked before traveler-facing publication.

## 1. Kalinchowk Bhagwati Temple

- **District:** Dolakha
- **Municipality / ward:** Kalinchowk Rural Municipality–1 (per canonical inventory; ward-level local-government confirmation still needed in the later admin/GIS pass)
- **Destination type:** High-altitude Hindu pilgrimage shrine / mountain viewpoint / conservation-area destination
- **Altitude:** About 3,842 m above sea level according to Nepal Tourism Board and the cable-car operator.
- **Protected-area relationship:** Nepal Tourism Board and Kalinchowk Darshan both place the temple inside Gaurishankar Conservation Area.
- **Religious significance:** NTB lists Kalinchowk Bhagwati among Bagmati Province's key religious destinations and describes it as a highly revered goddess shrine.
- **Access context:** Government film-location guidance and the operator describe the classic access as Kathmandu–Charikot by road, Charikot–Kuri by mountain road/jeep, then either cable car or roughly one hour on foot from Kuri.
- **Viewpoint context:** The operator highlights wide Himalayan views from the summit area; mountain visibility is weather-dependent and must not be guaranteed in traveler copy.
- **Route-planner modeling:** Store the temple as a religious POI, with separate Kuri trailhead/cable-car base, upper cable-car station and walking route objects.
- **Permit / conservation rule:** Because the temple lies within Gaurishankar Conservation Area, protected-area entry rules may apply depending on route/access. Current GCA rules and fees must be checked before publication.
- **Primary sources:**
  - https://ntb.gov.np/en/bagmati-province
  - https://kalinchowkdarshan.com.np/
  - https://www.film.gov.np/destination/45
- **Verification status:** Altitude, district, pilgrimage identity, Gaurishankar Conservation Area relationship and Kuri access context verified from NTB/operator/government sources.

## 2. Kuri Village / Kuri Bazar

- **District:** Dolakha
- **Municipality / area:** Kalinchowk Rural Municipality, below Kalinchowk summit
- **Destination type:** Mountain visitor settlement / accommodation base / cable-car and hiking gateway
- **Operator context:** Kalinchowk Darshan describes Kuri Village as the main gateway settlement for Kalinchowk Bhagwati Temple.
- **Facilities:** Government film-location guidance lists hotels, local transport, hospital/health support, electricity, internet and cable-car access at Kuri/Kalinchowk.
- **Road relationship:** The same government source describes Charikot–Kuri as roughly 17 km by jeep, while the operator describes about 18 km off-road from Charikot. Treat this as an approximate road-distance range until route geometry is measured directly.
- **Visitor experience:** Kuri functions as the accommodation, food and staging base for temple pilgrims, snow-season visitors, hikers and cable-car users.
- **Route-planner modeling:** Store Kuri as a settlement/visitor-base object with separate hotel, parking, health facility, cable-car station and trailhead POIs when individually verified.
- **Seasonality:** Snow and monsoon conditions can materially change road accessibility; current road status should be checked before trip planning.
- **Primary sources:**
  - https://kalinchowkdarshan.com.np/
  - https://www.film.gov.np/destination/45
- **Verification status:** Gateway role, facilities and Charikot–Kuri road relationship verified; exact settlement geometry and seasonal road status pending GIS/live checks.

## 3. Kalinchowk Cable Car / Kalinchowk Darshan

- **District:** Dolakha
- **Location:** Kuri Village to Kalinchowk summit/top-station area
- **Destination type:** Cable-car transport attraction / pilgrimage-access facility
- **Operator:** Kalinchowk Darshan Limited
- **Line length:** Operator currently states about 2.5 km.
- **Ride duration:** Operator ticket page states roughly 6 minutes.
- **Cabin capacity:** 8 passengers per cabin according to the operator.
- **Current fares (source checked 2026-08-11):** Regular/Nepali one-way NPR 400 and return NPR 600; student return NPR 500; senior citizen return NPR 500; differently abled return NPR 500; Indian citizen one-way NPR 640 and return NPR 960; foreigner one-way NPR 760 and return NPR 1,300. Child rules are based on height; operator says children up to 3 ft do not require a ticket and children above 3 ft up to 4 ft qualify for child fare. All fares are explicitly subject to change.
- **Ticket-policy notes:** Operator states student/senior discounts apply to Nepali nationals with ID; passengers age 60+ qualify for senior fare; tickets are valid for seven days; passenger insurance and baggage rules are also published by the operator.
- **Operating-hours conflict (source checked 2026-08-11):** The operator's main page shows Sun–Fri 05:00–16:00 and Sat/holidays 03:30–16:30, while a current ticket page shows Sun–Fri 06:00–16:00 and Sat/holidays 05:00–16:00. Because two official pages conflict, **do not publish a definitive schedule without same-day operator confirmation**.
- **Advance booking:** One operator ticket page states that advance booking is currently unavailable and tickets must be purchased at Kuri, Dolakha. Recheck before publication because this can change.
- **Route-planner modeling:** Separate bottom station, top station and cable-car line geometry.
- **Primary sources:**
  - https://kalinchowkdarshan.com.np/
  - https://kalinchowkdarshan.com.np/ticket
  - https://kalinchowkdarshan.com.np/tickets
  - https://kalinchowkdarshan.com.np/management
- **Verification status:** Operator, line length, ride time, cabin capacity and current fare table verified directly from the operator; hours explicitly flagged due to official-source conflict.

## 4. Dolakha Bhimsen Temple / Bhimeshwor Temple

- **District:** Dolakha
- **Municipality / ward:** Bhimeshwor Municipality, Ward 2
- **Destination type:** Major Hindu pilgrimage temple / historic Dolakha religious landmark
- **Canonical aliases:** Dolakha Bhimsen Temple; Dolakha Bhimeshwor Temple; Bhimsen/Bhimeshwar spelling variants should be preserved for search.
- **Official municipality coordinate:** 27.677941, 86.076433
- **Coordinate status:** Bhimeshwor Municipality tourist-destination coordinate.
- **Municipality relationship:** Bhimeshwor Municipality states that the municipality is named after this ancient and sacred temple.
- **NTB religious context:** Nepal Tourism Board identifies the temple as one of Bagmati Province's key pilgrimage destinations and notes its strong traditional association with traders.
- **Temple tradition:** NTB relates the shrine to Bhimsen of the Mahabharata and documents the widely known local belief that the idol may “sweat” before major national events. Traveler-facing content should present this clearly as religious/local belief, not scientific prediction.
- **Festival context:** NTB notes large pilgrim gatherings during Chaitra Dashain and Bhim Ekadashi in Magh. Exact Gregorian dates must be taken from the relevant year's calendar/local notice.
- **Route-planner modeling:** Facility-level religious POI linked to Historic Dolakha Town heritage area and nearby municipal attractions.
- **Primary sources:**
  - https://bhimeshwormun.gov.np/en/touristic-destination
  - https://bhimeshwormun.gov.np/en/node/26
  - https://bhimeshwormun.gov.np/en/node/4
  - https://ntb.gov.np/en/dolakha-bhimsen--dolakha
- **Verification status:** Ward 2, exact municipality coordinate, municipality naming relationship and pilgrimage significance verified from Bhimeshwor Municipality + NTB.

## 5. Historic Dolakha Town

- **District:** Dolakha
- **Municipality:** Bhimeshwor Municipality
- **Destination type:** Historic Newar settlement / religious-cultural heritage town / traditional trade settlement
- **Relationship to Bhimsen:** Dolakha Bhimsen Temple is a core heritage anchor inside the historic Dolakha settlement and should remain a separate POI linked to the town-area record.
- **Municipal tourism context:** Bhimeshwor Municipality identifies multiple visitor assets in Ward 2 around the Bhimsen area, including Bhimeshwor Temple, Champuja Hariyali Park and Manjushree Park, demonstrating a broader visitor cluster rather than a temple-only destination.
- **NTB context:** NTB treats Dolakha itself as one of Bagmati Province's major tourism areas and separately highlights Dolakha Bhimsen as a major religious site.
- **Heritage-modeling rule:** Store Historic Dolakha Town as an area/polygon object. Temples, old streets, traditional houses, courtyards, parks and museums/interpretive facilities should be separate sub-POIs as they are individually verified.
- **Evidence caution:** This research pass confirms the historic-town tourism cluster but does not yet provide a publication-grade polygon or a complete structure-level heritage inventory. Those should come from municipal heritage mapping/local verification rather than inferred web-map boundaries.
- **Coordinates:** Historic-core geometry pending GIS/local heritage mapping.
- **Permit requirement:** No town-wide tourism permit identified.
- **Primary sources:**
  - https://bhimeshwormun.gov.np/en/touristic-destination
  - https://bhimeshwormun.gov.np/en/content/tourist-destination
  - https://ntb.gov.np/en/bagmati-province
  - https://ntb.gov.np/en/dolakha-bhimsen--dolakha
- **Verification status:** Heritage-tourism cluster and Bhimsen relationship verified; structure-level old-town mapping remains pending.

# Dolakha progress

- **Inventory entries:** 29
- **Deep-researched:** 5 / 29
- **Next entries:** 6–10 — Charikot; Charikot viewpoints; Gaurishankar Conservation Area; Rolwaling Valley; Tsho Rolpa Lake.

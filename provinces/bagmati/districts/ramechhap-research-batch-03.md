# Ramechhap Verified Research Batch 03 — 2026-08-11

> Deep-research sidecar for canonical inventory entries 11–15. Transport operations, river activities and exact GIS geometry remain publication-time checks.

## 11. Manthali

- **District:** Ramechhap
- **Municipality:** Manthali Municipality
- **Destination type:** District-headquarters town / road-air gateway / visitor service hub
- **Administrative context:** Manthali is the principal administrative and transport center of Ramechhap District. Manthali Municipality lists its office at Manthali-01.
- **Airport relationship:** Ramechhap Airport lies in/alongside Manthali and must remain a separate transport-infrastructure record rather than being merged into the town destination.
- **Tourism role:** For Discover Nepal Hub, Manthali is primarily a gateway/service-area object: airport transfers, road connections, lodging, food, fuel, health/emergency services and onward transport are more useful than treating the town as one sightseeing POI.
- **River relationship:** Manthali sits beside the Tamakoshi corridor; riverbank recreation should remain a separate inventory object.
- **Route-planner modeling:** Urban/service-area geometry plus airport, bus/road junctions and river access as separate POIs.
- **Primary sources:**
  - https://www.manthalimun.gov.np/en/locationmap
  - https://www.manthalimun.gov.np/en/node/449
  - https://caanepal.gov.np/storage/app/media/RAMECHHAP%20AIRPORT-New.pdf
- **Verification status:** Municipality/gateway and airport relationship verified; detailed traveler-service inventory remains later enrichment.

## 12. Ramechhap Airport

- **District:** Ramechhap
- **Municipality:** Manthali Municipality
- **Destination type:** Domestic airport / seasonal Everest-region air gateway
- **Official CAAN identity:** Civil Aviation Authority of Nepal lists Ramechhap Airport among Nepal's domestic airports in operation.
- **Official location:** CAAN states the airport is in Manthali Municipality, on the bank of the Tamakoshi River and close to the district headquarters.
- **Codes:** IATA `RHP`; location indicator/ICAO `VNRC`.
- **Official aerodrome reference point:** 27°23'38"N, 86°03'41"E.
- **Elevation:** 494 m / 1,620 ft according to CAAN.
- **Everest gateway role:** CAAN states that during tourist-season congestion at Tribhuvan International Airport, many flights bound for Lukla and Phaplu operate from Ramechhap Airport.
- **Operational caution:** Flight schedules, airline use, transfer arrangements and weather disruption are highly time-sensitive. Never hard-code a promise that a particular Lukla flight will depart from Manthali without live airline/CAAN confirmation.
- **Route-planner modeling:** Airport facility POI with terminal/drop-off/parking geometry and transfer relationship to Manthali town.
- **Primary sources:**
  - https://caanepal.gov.np/storage/app/media/RAMECHHAP%20AIRPORT-New.pdf
  - https://caanepal.gov.np/airports/airport-profiles
  - https://ramechhap.caanepal.gov.np/
- **Verification status:** Strong official CAAN verification including coordinates, elevation and gateway role.

## 13. Ramechhap Bazaar

- **District:** Ramechhap
- **Municipality:** Ramechhap Municipality
- **Ward:** Municipality headquarters/contact address identifies Ramechhap Bazaar as Ramechhap-8.
- **Destination type:** Historic hill bazaar / municipal center / former district-center heritage area
- **Administrative verification:** Ramechhap Municipality states its center is at Ramechhap Bazaar, Ward 8, and uses the same location in current official contact information.
- **Historic modeling:** Preserve its historic-bazaar/former-center identity separately from modern Manthali, which now functions as the district's main administrative/transport gateway.
- **Object-modeling rule:** Store Ramechhap Bazaar as a settlement/heritage-area object. Individual temples, markets, civic heritage and viewpoints should become sub-POIs only after record-level verification.
- **Coordinates:** Historic-core polygon and visitor access points require GIS QA; do not substitute the municipality office pin for the entire bazaar.
- **Entry fee / permit:** No town-wide tourism fee or permit identified.
- **Primary sources:**
  - https://www.ramechhapmun.gov.np/en
  - https://ramechhapmun.gov.np/ne/content/%E0%A4%B8%E0%A4%82%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BF%E0%A4%AA%E0%A5%8D%E0%A4%A4-%E0%A4%AA%E0%A4%B0%E0%A4%BF%E0%A4%9A%E0%A4%AF-0?page=4
- **Verification status:** Municipality, Ward 8 and municipal-center identity verified; structure-level heritage mapping pending.

## 14. Tamakoshi River corridor

- **District:** Ramechhap
- **Area:** Manthali and western/central Ramechhap river corridor
- **Destination type:** Major river corridor / valley landscape / recreation and transport geography
- **Official airport relationship:** CAAN confirms Ramechhap Airport is situated on the bank of the Tamakoshi River, providing a strong geospatial anchor at Manthali.
- **Object-modeling rule:** Store Tamakoshi as a river line/corridor object, not a point attraction. Bridges, beaches/riverbanks, rafting put-ins, fishing locations, confluences and hydropower sites require separate verified POIs.
- **Activity caution:** The inventory notes rafting/fishing potential, but specific commercial or safe recreation segments should not be published without operator/local-authority verification of current flow, access and safety.
- **Seasonality:** Monsoon flow, flood risk and road/riverbank conditions can materially change visitor safety and access.
- **Coordinates:** Authoritative hydrological line geometry required during GIS pass.
- **Primary sources:**
  - https://caanepal.gov.np/storage/app/media/RAMECHHAP%20AIRPORT-New.pdf
  - https://www.manthalimun.gov.np/
- **Verification status:** River-Manthali/airport relationship verified; recreation products remain live/local verification items.

## 15. Likhu River valley

- **District:** Ramechhap
- **Area:** Eastern/northeastern Ramechhap; Likhu Tamakoshi and northern approach context
- **Destination type:** River valley / rural access corridor / agricultural and settlement landscape
- **Administrative/GIS evidence:** Likhu Tamakoshi Rural Municipality publishes current ward-level land-use maps that explicitly include riverine/lake zoning and settlement/agricultural land, providing an official GIS base for later valley modeling.
- **Destination role:** Treat the Likhu valley as a corridor/landscape object linking settlements and northern approaches, not as one sightseeing point.
- **Route-planner modeling:** River line + valley/municipality polygons + verified roads, bridges, villages and trail junctions. Avoid assigning a single generic `Likhu Valley` pin.
- **Activity caution:** Do not infer rafting, swimming or fishing safety from the existence of the river. Any activity product requires local/current verification.
- **Coordinates:** Use authoritative hydrography and municipality GIS during the dedicated GIS pass.
- **Primary source:**
  - https://www.likhutamakoshimun.gov.np/sites/likhumunramechhap.gov.np/files/Map.pdf
- **Verification status:** Official municipality/GIS context established; detailed tourism POIs and access conditions remain later enrichment.

# Ramechhap progress

- **Inventory entries:** 29
- **Deep-researched / dispositioned:** 15 / 29
- **Next canonical entries:** 16–20 — Khimti valley; Gumdel Village; Bamti Bhandar; Chuchure; Those.

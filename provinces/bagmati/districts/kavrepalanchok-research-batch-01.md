# Kavrepalanchok Verified Research Batch 01 — 2026-08-11

> Deep-research sidecar for Kavrepalanchok inventory entries 1–5. This batch prioritizes destination identity, administrative context, visitor modeling and publication cautions. Time-sensitive operations should be rechecked before traveler-facing publication.

## 1. Namo Buddha / Namobuddha pilgrimage site

- **District:** Kavrepalanchok
- **Municipality:** Namobuddha Municipality
- **Destination type:** Buddhist pilgrimage landscape / sacred hill / cultural destination
- **Administrative context:** Namobuddha Municipality is the local government unit for the pilgrimage landscape and takes its name from Namo Buddha.
- **Religious significance:** Namo Buddha is one of Nepal's best-known Buddhist pilgrimage destinations, associated with the Jataka tradition in which a bodhisattva prince offers his body to a starving tigress and her cubs.
- **Destination modeling:** Do not collapse the entire pilgrimage landscape into the monastery record. Store `Namo Buddha sacred site` and `Thrangu Tashi Yangtse Monastery` as separate but linked visitor objects.
- **Route-planner role:** Major pilgrimage/day-trip destination that can connect with Dhulikhel and Balthali hiking circuits.
- **Coordinates:** Sacred-site/stupa and monastery coordinates should be captured separately during GIS QA.
- **Permit requirement:** No district-level travel permit identified for ordinary visitation.
- **Entry fee / hours:** Religious-site access practices, donations and monastery visiting hours are time-sensitive and should be confirmed locally before publication.
- **Primary sources:**
  - https://namobuddhamun.gov.np/
  - https://ntb.gov.np/
- **Verification status:** Municipality and major pilgrimage identity verified; attraction-level GIS and live operations pending.

## 2. Thrangu Tashi Yangtse Monastery

- **District:** Kavrepalanchok
- **Municipality:** Namobuddha Municipality
- **Destination type:** Tibetan Buddhist monastery / pilgrimage and study center / hill viewpoint
- **Destination relationship:** Closely linked with the Namo Buddha sacred landscape but should remain a distinct facility-level POI in the CMS and route planner.
- **Visitor context:** The monastery complex is a major modern religious institution overlooking the Namo Buddha landscape and is commonly paired with the sacred stupa/site in day trips.
- **Religious-use note:** Treat as an active monastery, not simply a scenic attraction. Public areas, teaching spaces and monastic residential areas can have different access expectations.
- **Route-planner modeling:** Facility POI with separate road arrival/drop-off and walking links to the sacred Namo Buddha site where verified.
- **Coordinates:** Exact public entrance and principal monastery-complex coordinate require GIS QA.
- **Permit requirement:** No separate regional travel permit identified.
- **Hours / fees:** Visitor schedules, retreat/course arrangements and donation practices should be taken from current monastery-owned information immediately before publication.
- **Primary sources:**
  - https://namobuddhamun.gov.np/
  - https://www.namobuddha.org/
- **Verification status:** Destination identity and Namobuddha context established; current monastery visitor operations require publication-time confirmation.

## 3. Panauti heritage town

- **District:** Kavrepalanchok
- **Municipality:** Panauti Municipality
- **Destination type:** Historic Newar town / living heritage area / temple and courtyard landscape
- **Heritage significance:** Panauti preserves a traditional Newar urban core with temples, public squares, courtyards, water structures and religious landscapes.
- **Destination modeling:** Store Panauti as a `living_heritage_area`, not a single POI. Indreshwar Mahadev Temple, Panauti Museum and the sacred confluence remain separate linked records.
- **Route-planner role:** Major heritage stop that also serves as a gateway for Balthali and surrounding village-hiking circuits.
- **Living-community note:** Traveler-facing copy should frame Panauti as an inhabited town with active religious and community life rather than an open-air museum.
- **Coordinates:** Historic-core polygon/centroid, principal arrival point and individual monuments require separate GIS geometry.
- **Permit requirement:** No town-wide travel permit identified.
- **Entry fee / hours:** Do not assume one universal fee or opening schedule for the entire heritage town; individual facilities may differ.
- **Primary sources:**
  - https://panautimun.gov.np/
  - https://ntb.gov.np/
- **Verification status:** Municipality and heritage-town identity verified; structure-level mapping remains for later GIS enrichment.

## 4. Indreshwar Mahadev Temple

- **District:** Kavrepalanchok
- **Municipality:** Panauti Municipality
- **Destination type:** Historic Shiva temple / religious and architectural heritage POI
- **Destination relationship:** Core monument within the Panauti heritage cluster; keep it as a separate religious/architectural POI linked to the town-level heritage record.
- **Heritage context:** Indreshwar Mahadev is one of the defining temples of historic Panauti and contributes to the town's medieval Newar religious landscape.
- **Religious-use note:** Active worship site. Publication should distinguish visitor sightseeing from ritual access and should locally verify photography/temple-interior practices.
- **Coordinates:** Exact temple entrance/compound geometry requires GIS confirmation.
- **Permit requirement:** No separate regional travel permit identified.
- **Entry fee / hours:** No reliable universal current tourist tariff or complete schedule stored in this pass; recheck from municipality/site management before publication.
- **Primary sources:**
  - https://panautimun.gov.np/
- **Verification status:** Panauti administrative and heritage-cluster identity established; detailed monument operations and GIS pending.

## 5. Panauti Museum

- **District:** Kavrepalanchok
- **Municipality:** Panauti Municipality
- **Destination type:** Local museum / cultural-history interpretation facility
- **Destination relationship:** Facility-level POI within the Panauti heritage town cluster; should link to Indreshwar Mahadev, the sacred confluence and historic-core walking route.
- **Visitor value:** Museum interpretation can provide historical/cultural context before or during exploration of Panauti's built heritage and living traditions.
- **Route-planner modeling:** Store the museum entrance as a precise POI rather than using the Panauti town centroid.
- **Coordinates:** Exact public entrance coordinate requires GIS QA.
- **Permit requirement:** No regional travel permit identified.
- **Entry fee / opening hours:** Museum operations are time-sensitive. Confirm current municipal/museum schedule and tariff immediately before publication rather than relying on old guide listings.
- **Primary sources:**
  - https://panautimun.gov.np/
- **Verification status:** Museum retained as a distinct established Panauti attraction; live operational data and exact GIS point pending.

# Kavrepalanchok progress

- **Inventory entries:** 32
- **Deep-researched:** 5 / 32
- **Next entries:** 6–10 — Panauti sacred confluence; Dhulikhel; Dhulikhel old town; Dhulikhel viewpoints; Banepa old town.
- **Research rule:** Preserve cluster relationships while keeping facilities, settlements, trails and area destinations as separate route-planner object types.

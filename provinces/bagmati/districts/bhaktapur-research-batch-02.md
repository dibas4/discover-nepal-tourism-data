# Bhaktapur Verified Research Batch 02 — 2026-08-11

> Deep-research sidecar for Bhaktapur inventory entries 6–10. Time-sensitive fees and operations must be rechecked before publication.

## 6. Changu Narayan Temple

- **District:** Bhaktapur
- **Municipality:** Changunarayan Municipality
- **Destination type:** UNESCO World Heritage monument zone / Hindu temple / hilltop heritage village
- **UNESCO status:** Changu Narayan is one of the seven monument zones forming the Kathmandu Valley World Heritage property.
- **UNESCO context:** UNESCO describes Changu Narayan as a temple complex on a ridge northeast of Kathmandu, with inscriptions and monuments of high historical value within the Kathmandu Valley property.
- **Municipal context:** Changunarayan Municipality is named after the temple and maintains the heritage destination as one of the municipality's defining cultural assets.
- **Route-planner modeling:** Separate the UNESCO monument-zone / village area from the temple entrance itself. A heritage-area polygon plus temple POI is preferable to a single generic pin.
- **Permit requirement:** No separate travel permit identified; applicable heritage-site entrance arrangements may apply and should be verified from the current official tariff before publication.
- **Coordinates:** Use UNESCO monument-zone geometry / authoritative temple coordinate during GIS QA.
- **Primary sources:**
  - https://whc.unesco.org/en/list/121/
  - https://whc.unesco.org/en/list/121/maps/
  - https://changunarayanmun.gov.np/
- **Verification status:** UNESCO identity and municipality context verified; live fee/hours and exact route geometry pending.

## 7. Kailashnath Mahadev Statue

- **District:** Bhaktapur
- **Municipality / area:** Sanga, Suryabinayak Municipality
- **Destination type:** Monumental Shiva statue / pilgrimage and viewpoint attraction
- **Administrative context:** Suryabinayak Municipality includes the Sanga area in eastern Bhaktapur District; the attraction is commonly identified with Sanga.
- **Attraction identity:** The site is known for the large standing Shiva statue at Sanga and functions as a religious, scenic and roadside tourism stop.
- **Cross-district caution:** Sanga sits near the Bhaktapur–Kavrepalanchok boundary. The statue's exact parcel/entrance must be stored with authoritative GIS data so the route planner does not mis-assign it to Kavrepalanchok.
- **Route-planner modeling:** Use a facility-level POI with road-access and parking/drop-off geometry. Do not model the whole Sanga ridge as the attraction.
- **Permit requirement:** No separate travel permit identified.
- **Entry fee / hours:** Operational details are commercial/facility-level and time-sensitive; recheck from the operator/local authority before publication.
- **Coordinates:** Exact attraction entrance coordinate required during GIS QA.
- **Primary sources:**
  - https://suryabinayakmun.gov.np/
- **Verification status:** Sanga/Suryabinayak administrative context verified; operator-level operational data and precise boundary coordinate pending.

## 8. Suryabinayak Temple

- **District:** Bhaktapur
- **Municipality:** Suryabinayak Municipality
- **Destination type:** Hindu Ganesh temple / pilgrimage site / forest-edge religious POI
- **Municipality relationship:** Suryabinayak Municipality takes its name from Suryabinayak Temple, confirming the site's central local identity.
- **Religious context:** The temple is one of the important Ganesh shrines of the Kathmandu Valley and is an active worship destination rather than a museum-style attraction.
- **Access modeling:** Store the temple as a religious POI and preserve any surrounding forest/road approach as separate access geometry if needed.
- **Festival / crowd caution:** Worship peaks and festival days can change traffic and access conditions; current local notices should be used for event-day traveler guidance.
- **Permit requirement:** No separate travel permit identified.
- **Entry fee / hours:** No universal authoritative tourist fee or complete operating schedule captured in this pass.
- **Coordinates:** Exact temple entrance coordinate required during GIS QA.
- **Primary sources:**
  - https://suryabinayakmun.gov.np/
- **Verification status:** Municipality association and pilgrimage identity verified; detailed operations/GIS pending.

## 9. Siddha Pokhari / Ta-Pukhu

- **District:** Bhaktapur
- **Municipality:** Bhaktapur Municipality
- **Destination type:** Historic pond / urban heritage landscape / religious-cultural gathering site
- **Alias normalization:** Preserve `Siddha Pokhari` and traditional Newar name `Ta-Pukhu` where verified in local heritage material.
- **Municipal context:** Bhaktapur Municipality treats Siddha Pokhari as one of the city's major historic public-water and heritage sites.
- **Urban-heritage value:** The pond should be modeled as a waterbody/heritage-space object, not simply as a point attraction.
- **Festival context:** Local religious and festival activities can center on the pond; exact annual dates should come from current municipality notices.
- **Permit requirement:** No separate travel permit identified.
- **Entry fee / hours:** No universal official general entry tariff or fixed opening schedule identified.
- **Coordinates:** Capture pond polygon/centroid plus primary visitor-access points during GIS QA.
- **Primary sources:**
  - https://bhaktapurmun.gov.np/
- **Verification status:** Municipality and heritage identity verified; detailed cultural-event and GIS layer pending.

## 10. Nagarkot

- **District context:** Cross-district ridge spanning Bhaktapur and Kavrepalanchok; the Bhaktapur inventory should represent the Bhaktapur-side Nagarkot / Changunarayan access context without claiming the entire destination lies in Bhaktapur.
- **Bhaktapur municipality context:** Changunarayan Municipality includes Nagarkot-area wards on the western/southwestern portion of the ridge and is a principal Bhaktapur-side administrative anchor for the destination.
- **Destination type:** Hill station / Himalayan viewpoint / sunrise-sunset destination / resort area
- **Cross-district modeling rule:** Store Nagarkot as a multi-district destination object with district-specific subareas or polygons. Do not duplicate the whole destination independently in Bhaktapur and Kavrepalanchok as if each contained all of Nagarkot.
- **Tourism value:** Nagarkot is widely known for Himalayan panoramas, sunrise/sunset viewing, short hikes and resort stays.
- **Route-planner note:** Route planning should use exact hotel/viewpoint/trail POIs and district polygons rather than one town centroid, especially because users can approach from Bhaktapur or Kavrepalanchok sides.
- **Coordinates:** Area geometry and specific public viewpoints require GIS QA; a single central Nagarkot coordinate is insufficient for district ownership.
- **Permit requirement:** No area-wide tourism permit identified.
- **Entry fee / hours:** No universal destination fee or opening schedule; individual towers, resorts or facilities may have separate charges.
- **Primary sources:**
  - https://changunarayanmun.gov.np/
  - https://ntb.gov.np/
- **Verification status:** Cross-district nature and Bhaktapur-side Changunarayan relationship verified; polygon-level district split and exact viewpoint POIs remain GIS tasks.

# Bhaktapur progress

- **Inventory entries:** 11
- **Deep-researched:** 10 / 11
- **Final remaining entry:** Pilot Baba Ashram viewpoint.
- **After 11/11:** Run Bhaktapur district QA with special focus on Changu Narayan UNESCO geometry, Nagarkot cross-district modeling, Sanga boundary precision and live operational data.

# Lalitpur Verified Research Batch 02 — 2026-08-11

> Deep-research sidecar for Lalitpur inventory entries 6–10. This batch can be normalized into the canonical `lalitpur.md` during the district QA pass.

## 6. Bajrabarahi Temple and forest

- **District:** Lalitpur
- **Municipality:** Godawari Municipality
- **Area context:** Bajrabarahi / Chapagaun area; Godawari Municipality's administrative center is located at Bajrabarahi.
- **Destination type:** Hindu temple / sacred forest / religious-natural attraction
- **Municipality verification:** Godawari Municipality maintains Bajrabarahi Temple, Chapagaun in its official list of religious and tourism areas.
- **Municipal context:** Godawari Municipality describes itself as a tourism city and identifies Bajrabarahi as its municipal center, reinforcing the site's administrative and local prominence.
- **Forest modeling note:** Treat the sacred forest and temple as one destination area but preserve separate geometry if the route planner later distinguishes temple entrance, forest perimeter and walking paths.
- **Coordinates:** Exact temple entrance coordinate was not captured from an authoritative municipal page in this pass; obtain during GIS QA.
- **Permit requirement:** No separate tourism permit identified in municipality sources reviewed.
- **Entry fee / hours:** No reliable current official tariff or complete visitor schedule found; locally recheck before traveler-facing publication.
- **Primary sources:**
  - https://www.godawarimun.gov.np/ne/important-places/%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AE%E0%A4%BF%E0%A4%95-%E0%A4%8F%E0%A4%AC%E0%A4%AE-%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%AF%E0%A4%9F%E0%A4%95%E0%A5%80%E0%A4%AF-%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0
  - https://www.godawarimun.gov.np/en/content/brief-introduction
  - https://godawarimun.gov.np/en/content/nagar-profile
- **Verification status:** Municipality, destination identity and religious-tourism classification verified; exact GIS point and live operations pending.

## 7. Tika Bhairab and Lele valley

- **District:** Lalitpur
- **Municipality:** Godawari Municipality
- **Ward:** Ward 6 for Tika Bhairab; Godawari Municipality's Ward 6 office is officially located at Tikabhairab, Lalitpur.
- **Destination type:** Bhairab temple / valley-edge religious stop / scenic-rural corridor
- **Official temple coordinate:** 27.5746659, 85.3108224
- **Coordinate status:** Godawari Municipality attraction coordinate for Tika Bhairab Temple.
- **Municipality verification:** Godawari Municipality lists Tika Bhairab Temple under religious and tourism areas.
- **Lele context:** Godawari Municipality's official profile confirms that former Lele VDC is now part of the municipality. The inventory item should be modeled as a corridor/area destination rather than pretending the entire Lele valley is one POI.
- **Current infrastructure context:** In June 2026 the municipality published a tender for rehabilitation/reconstruction of the historic Rajkulo section from Tikabhairav to Thecho, evidence that this corridor remains an active municipal landscape with heritage/infrastructure value.
- **Route-planner note:** Separate `Tika Bhairab Temple` as an attraction POI and `Lele valley` as an area/scenic route object.
- **Permit requirement:** No separate tourism permit identified.
- **Fee / hours:** No reliable current official general visitor tariff or opening schedule captured.
- **Primary sources:**
  - https://godawarimun.gov.np/ne/content/%E0%A4%9F%E0%A4%BF%E0%A4%95%E0%A4%BE%E0%A4%AD%E0%A5%88%E0%A4%B0%E0%A4%AC-%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0
  - https://www.godawarimun.gov.np/en/content/%E0%A4%B5%E0%A4%A1%E0%A4%BE-%E0%A4%A8%E0%A4%82-%E0%A5%AC
  - https://godawarimun.gov.np/en/content/nagar-profile
  - https://www.godawarimun.gov.np/ne/content/%E0%A4%97%E0%A5%8B%E0%A4%A6%E0%A4%BE%E0%A4%B5%E0%A4%B0%E0%A5%80-%E0%A4%A8%E0%A4%97%E0%A4%B0%E0%A4%AA%E0%A4%BE%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A4%BE-%E0%A4%B2%E0%A4%B2%E0%A4%BF%E0%A4%A4%E0%A4%AA%E0%A5%81%E0%A4%B0-%E0%A4%85%E0%A4%A8%E0%A5%8D%E0%A4%A4%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%A4-%E0%A4%9F%E0%A4%BF%E0%A4%95%E0%A4%BE%E0%A4%AD%E0%A5%88%E0%A4%B0%E0%A4%B5-%E0%A4%A6%E0%A5%87%E0%A4%96%E0%A4%BF-%E0%A4%A0%E0%A5%87%E0%A4%9A%E0%A5%8B-%E0%A4%B8%E0%A4%AE%E0%A5%8D%E0%A4%AE%E0%A4%95%E0%A5%8B-%E0%A4%96%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%AE%E0%A4%BE-%E0%A4%B0%E0%A4%B9%E0%A5%87%E0%A4%95%E0%A5%8B-%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A4%95%E0%A5%81%E0%A4%B2%E0%A5%8B%E0%A4%95%E0%A5%8B
- **Verification status:** Temple identity, Ward 6 and official temple coordinate verified; Lele valley remains an area object requiring route geometry.

## 8. Karya Binayak Temple / Karyabinayak

- **District:** Lalitpur
- **Municipality / area:** Lalitpur Metropolitan City, Bungamati area
- **Destination type:** Hindu Ganesh temple / pilgrimage POI
- **Name aliases:** Karya Binayak; Karyabinayak; Karya Vinayak. Preserve spelling variants for search until a single canonical English usage is selected from local-authority material.
- **Destination relationship:** The temple should be linked operationally with Bungamati because it is commonly visited within the same southern Lalitpur heritage circuit, but it should remain a separate POI rather than being collapsed into the village record.
- **Municipal/heritage context:** Lalitpur Metropolitan City administers Bungamati as Ward 22, confirming the temple's wider municipal context for the route-planner layer.
- **Religious context:** Treat it as a living worship site rather than a museum-style attraction; festival-day congestion and worship rules should be locally checked before publication.
- **Coordinates:** Exact temple entrance coordinate requires GIS QA.
- **Permit requirement:** No separate travel permit identified.
- **Fee / hours:** No reliable current official general visitor tariff or complete opening schedule found in authoritative sources during this pass.
- **Primary sources:**
  - https://lmc.gov.np/en/%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AE%E0%A4%9A%E0%A4%BE%E0%A4%B0%E0%A5%80-%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3/
  - https://lmc.gov.np/en/%E0%A4%B5%E0%A4%A1%E0%A4%BE-%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%B2%E0%A4%AF%E0%A4%B9%E0%A4%B0%E0%A5%81/
- **Verification status:** Bungamati/LMC administrative context verified; attraction-specific operational and GIS confirmation still required.

## 9. Bungamati heritage village

- **District:** Lalitpur
- **Municipality / ward:** Lalitpur Metropolitan City, Ward 22
- **Destination type:** Historic Newar settlement / living heritage village / religious-cultural destination
- **Administrative verification:** Lalitpur Metropolitan City lists Ward 22 office as Bungamati.
- **Cultural identity:** Nepal Tourism Board identifies Bungamati as an old Kathmandu Valley village and links it directly with Machhindranath/Matsyanath, also called Bung Dhya in Newa usage.
- **Festival significance:** NTB's 2026 Rato Machhindranath festival material identifies Bungamati as the traditional birthplace of Matsyanath and describes the deity's central role in the valley's long-running rain and chariot festival tradition.
- **Living-heritage modeling:** Treat Bungamati as a settlement/heritage-area object with multiple internal POIs, not a single pin. Future sub-POIs should include the Rato Machhindranath temple precinct, Karya Binayak and major traditional squares/courtyards where verified.
- **Visitor context:** Heritage content should emphasize living community, ritual practice, settlement fabric and craft/cultural continuity rather than presenting the village as an open-air museum.
- **Coordinates:** Capture settlement polygon/centroid plus separate visitor drop-off and attraction pins during GIS QA.
- **Permit requirement:** No village-wide tourism permit identified.
- **Entry fee / hours:** No reliable municipality-wide admission fee or universal opening hours found; individual religious sites may have their own access practices.
- **Primary sources:**
  - https://lmc.gov.np/en/%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AE%E0%A4%9A%E0%A4%BE%E0%A4%B0%E0%A5%80-%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3/
  - https://lmc.gov.np/en/%E0%A4%B5%E0%A4%A1%E0%A4%BE-%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%B2%E0%A4%AF%E0%A4%B9%E0%A4%B0%E0%A5%81/
  - https://ntb.gov.np/en/ratharohan-of-rato-machindranath
- **Verification status:** Ward 22, settlement identity and Machhindranath cultural significance verified; detailed sub-POI and GIS mapping pending.

## 10. Khokana heritage village

- **District:** Lalitpur
- **Municipality / ward:** Lalitpur Metropolitan City, Ward 21
- **Destination type:** Historic Newar settlement / living industrial-agricultural heritage village
- **Administrative verification:** Lalitpur Metropolitan City's official staff/ward records identify Ward 21 office at Khokana.
- **UNESCO status:** `Khokana, the vernacular village and its mustard-oil seed industrial heritage` has been on Nepal's UNESCO World Heritage Tentative List since 23 May 1996. It is **not** an inscribed World Heritage Site.
- **UNESCO heritage description:** UNESCO's Tentative List record describes Khokana as a medieval settlement model with drainage and chowk systems, chaityas and a Mother Goddess temple, with mustard-oil seed production as living heritage.
- **Core identity:** The mustard-oil industry is not just a historic footnote; it is the defining heritage theme in Nepal's Tentative List submission and should be a first-class field in future CMS copy and experiences.
- **Living-heritage modeling:** Store Khokana as an area/settlement object with separate POIs for oil mills, temple precincts, chowks and traditional infrastructure when individually verified.
- **Coordinates:** UNESCO's current public Tentative List page identifies the location at Lalitpur District level but does not expose a publication-ready visitor entrance point in the retrieved record; GIS pass required.
- **Permit requirement:** No village-wide tourism permit identified.
- **Entry fee / hours:** No reliable universal village entry fee or operating schedule found in official sources; individual heritage facilities may have separate arrangements.
- **Primary sources:**
  - https://whc.unesco.org/en/tentativelists/844/
  - https://lmc.gov.np/en/%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AE%E0%A4%9A%E0%A4%BE%E0%A4%B0%E0%A5%80-%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3/
  - https://lmc.gov.np/en/%E0%A4%B5%E0%A4%A1%E0%A4%BE-%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%B2%E0%A4%AF%E0%A4%B9%E0%A4%B0%E0%A5%81/
- **Verification status:** Ward 21 and UNESCO Tentative List heritage identity verified; internal POI geometry and live visitor operations pending.

# Lalitpur progress

- **Inventory entries:** 14
- **Deep-researched:** 10 / 14
- **Next entries:** 11–14 — Godavari Botanical Garden; Phulchowki hill; Lakuri Bhanjyang; Nag Daha.
- **After 14/14:** Run Lalitpur district QA for aliases, composite destinations, GIS precision, route-planner object types and time-sensitive operations.

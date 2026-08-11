# Makwanpur Verified Research Batch 04 — 2026-08-11

> Deep-research sidecar for canonical Makwanpur inventory entries 16–20. Official local-government evidence is preferred. Exact visitor operations, fees, opening hours and route access remain live checks where not explicitly published by the responsible authority.

## 16. Hetauda

- **District:** Makwanpur
- **Administrative role:** Hetauda Sub-Metropolitan City; district headquarters and major urban gateway.
- **Destination type:** Urban gateway / service hub / cultural and tourism base.
- **Official context:** Hetauda Sub-Metropolitan City describes the city as lying at the meeting of major national highway corridors and notes its development as Makwanpur district headquarters.
- **Tourism role:** Use Hetauda as a gateway/service-area object connecting city attractions, Makwanpurgadhi, Bhimphedi, the Rapti corridor and southern Makwanpur rather than as one attraction pin.
- **Route-planner modeling:** Separate bus/road arrival nodes, accommodation/service areas, temples, parks and hill viewpoints.
- **Primary source:** https://hetaudamun.gov.np/en/node/10
- **Verification status:** ESTABLISHED.

## 17. Bhutandevi Temple

- **District:** Makwanpur
- **Municipality:** Hetauda Sub-Metropolitan City
- **Destination type:** Hindu temple / pilgrimage and cultural site.
- **Official evidence:** Makwanpur District Coordination Committee identifies Bhutandevi Temple in central Hetauda and notes regular Hindu devotees/internal visitors, with larger crowds around Bada Dashain and special worship periods.
- **Municipal coordinate:** Hetauda Sub-Metropolitan City's tourism-place record publishes latitude **27.424** and longitude **85.023**.
- **Route-planner modeling:** Use the municipality coordinate as an official-source point but perform map/GIS QA before production routing to confirm the entrance rather than merely the site centroid.
- **Festival caution:** Do not hard-code annual Gregorian festival dates; derive Dashain dates from the relevant Nepali calendar/year.
- **Primary sources:**
  - https://dccmakwanpur.gov.np/detail/4
  - https://hetaudamun.gov.np/en/node/666
- **Verification status:** ESTABLISHED; unusually strong municipality-level coordinate evidence available.

## 18. Manakamana Temple, Hetauda

- **District:** Makwanpur
- **Municipality:** Hetauda Sub-Metropolitan City
- **Destination type:** Hill temple / city viewpoint / religious site.
- **Official evidence:** Hetauda Sub-Metropolitan City's official website surfaces `Manakamana Danda` as a city view/tourism feature, supporting the hill/viewpoint identity associated with the temple area.
- **Disambiguation:** Always label this record `Manakamana Temple, Hetauda` so it is not confused with the famous Manakamana Temple in Gorkha District.
- **Visitor value:** Religious visit plus elevated views over Hetauda where weather/visibility permits.
- **Evidence caution:** Current official pages reviewed do not provide a publication-grade temple entrance coordinate, opening hours or fee schedule.
- **Route-planner modeling:** Temple and hill/viewpoint may later need separate geometry if local GIS confirms distinct access points.
- **Primary source:** https://hetaudamun.gov.np/en/node
- **Verification status:** ESTABLISHED identity; exact entrance/GIS and operations require local verification.

## 19. Pashupatinath Temple, Hetauda

- **District:** Makwanpur
- **Municipality:** Hetauda Sub-Metropolitan City
- **Destination type:** Urban Shiva temple / religious complex.
- **Disambiguation:** Canonical CMS/search title must include `Hetauda`; never route this record to Kathmandu's Pashupatinath Temple.
- **Evidence status:** The Makwanpur inventory identifies this as an established Hetauda religious site, but the current authoritative web sources reviewed do not provide enough specific evidence for a reliable entrance coordinate, operating hours, fee, or detailed historical narrative.
- **Publication rule:** Retain the destination record but do not invent a founding date, architecture history, festival schedule or visitor operations.
- **Coordinates:** LOCAL/GIS VERIFICATION REQUIRED.
- **Verification status:** PARTIAL — identity retained, detailed publication fields on hold.

## 20. Risheshwar Mahadev

- **District:** Makwanpur
- **Area:** Daman / Thaha–Bhimphedi boundary context
- **Destination type:** Cave-temple / Hindu pilgrimage site with associated Buddhist sacred landscape.
- **Location caution:** Public reporting places the famous Risheshwar Mahadev/Tarebhir sacred landscape around the boundary context of **Bhimphedi Rural Municipality Ward 9** and the Thaha Municipality side. The inventory's simple `Daman / Thaha Municipality` label should therefore be treated as a tourism-area label, not a final administrative pin.
- **Religious context:** Contemporary reporting associates the site with Risheshwar Mahadev and with Buddhist Guru Padmasambhava traditions in the surrounding Tarebhir landscape.
- **Route-planner modeling:** Keep Risheshwar Mahadev temple/cave, Tarebhir/Padmasambhava feature and road/trail access as separable objects if later local verification confirms distinct visitor nodes.
- **Evidence caution:** Do not copy exact ritual legends, cave coordinates, opening hours or access claims from tourism blogs. Municipality/ward or site-level confirmation is still needed.
- **Sources:**
  - https://thahamun.gov.np/
  - https://ekantipur.com/Art/2025/04/08/en/a-huge-picture-of-guru-rinpoche-was-started-to-be-carved-in-the-taravir-of-makwanpur-55-12.html
- **Verification status:** ESTABLISHED sacred-site identity; administrative boundary, entrance coordinate and live operations require local/GIS verification.

# Makwanpur progress

- **Inventory entries:** 31
- **Deep-researched / dispositioned:** 20 / 31
- **Next canonical entries:** 21–25 — Bajrabarahi Temple, Thaha; Gumba Danda; Rapti River corridor; Manahari River and forest landscape; Parsa National Park sector.

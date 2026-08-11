# Kavrepalanchok Verified Research Batch 05 — 2026-08-11

> Deep-research sidecar for Kavrepalanchok inventory entries 21–25. Cross-district and GIS-sensitive records are explicitly modeled as area/subarea objects.

## 21. Timal region / Temal cultural landscape

- **District:** Kavrepalanchok
- **Municipality:** Temal Rural Municipality
- **Destination type:** Tamang cultural landscape / monastery-and-village region / ridge tourism area
- **Municipality profile:** Temal Rural Municipality consists of 9 wards and identifies itself as a culturally diverse hill municipality with a majority Tamang population.
- **Religious-tourism anchors:** The municipality's official profile names Pokhari Narayansthan and nearby Buddhist stupas, Tongsum Kund and Santaneshwar Mahadev among important religious-tourism places.
- **Cultural identity:** The municipality specifically notes the strong Buddhist population alongside Hindu and Christian communities, and identifies Tamang as the majority community. Future traveler content should treat Temal as a living cultural region, not a staged ethnic attraction.
- **Landscape/view significance:** Temal Municipality states that high points in the municipality can see Himalayan ranges from Kanchenjunga to Dhaulagiri, along with Kathmandu Valley and Sindhuligadhi in suitable conditions.
- **Route-planner modeling:** Use a regional/cultural-landscape object with separate villages, monasteries, temples and ridge viewpoints as sub-POIs.
- **Coordinates:** Municipality polygon plus individually verified attraction/viewpoint coordinates required; one centroid is insufficient.
- **Primary sources:**
  - https://temalmun.gov.np/content/%E0%A4%A4%E0%A5%87%E0%A4%AE%E0%A4%BE%E0%A4%B2-%E0%A4%97%E0%A4%BE%E0%A4%89%E0%A4%81%E0%A4%AA%E0%A4%BE%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A4%BE%E0%A4%95%E0%A4%BE%E0%A5%87-%E0%A4%B8%E0%A4%82%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BF%E0%A4%AA%E0%A5%8D%E0%A4%A4-%E0%A4%AA%E0%A4%B0%E0%A4%BF%E0%A4%9A%E0%A4%AF
  - https://temalmun.gov.np/content/%E0%A4%A4%E0%A5%87%E0%A4%AE%E0%A4%BE%E0%A4%B2%E0%A4%95%E0%A5%8B-%E0%A4%90%E0%A4%A4%E0%A4%BF%E0%A4%B9%E0%A4%BE%E0%A4%B8%E0%A4%BF%E0%A4%95-%E0%A4%A4%E0%A4%A5%E0%A4%BE-%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%AF%E0%A4%9F%E0%A4%A8-%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BE%E0%A4%B2%E0%A4%B9%E0%A4%B0%E0%A5%81
- **Verification status:** Municipality, Tamang cultural identity, religious anchors and broad Himalayan-view context verified from Temal Rural Municipality.

## 22. Timal ridge viewpoints / Temal ridge viewpoints

- **District:** Kavrepalanchok
- **Municipality:** Temal Rural Municipality
- **Destination type:** Ridge viewpoints / scenic-road and hiking area
- **Municipality evidence:** Temal Rural Municipality states that from its high points visitors can see Himalayan ranges from Kanchenjunga through Dhaulagiri, and can also see Kathmandu Valley and Sindhuligadhi in clear weather.
- **Emerging-site context:** The municipality's 2025 tourism-gallery material documents multiple historic and tourism places in Temal, but not every ridge viewpoint has a separately published official name/coordinate.
- **Object-modeling rule:** Keep `Timal ridge viewpoints` as an area/cluster record until individual public viewpoints are authoritatively named and geolocated. Do not invent multiple viewpoint POIs from map labels alone.
- **Weather caution:** Long-range mountain visibility is highly weather-dependent and should be presented as possible, not guaranteed.
- **Coordinates:** Specific viewpoint coordinates remain pending local/GIS verification.
- **Primary sources:**
  - https://temalmun.gov.np/content/%E0%A4%A4%E0%A5%87%E0%A4%AE%E0%A4%BE%E0%A4%B2-%E0%A4%97%E0%A4%BE%E0%A4%89%E0%A4%81%E0%A4%AA%E0%A4%BE%E0%A4%B2%E0%A4%BF%E0%A4%95%E0%A4%BE%E0%A4%95%E0%A4%BE%E0%A5%87-%E0%A4%B8%E0%A4%82%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BF%E0%A4%AA%E0%A5%8D%E0%A4%A4-%E0%A4%AA%E0%A4%B0%E0%A4%BF%E0%A4%9A%E0%A4%AF
  - https://temalmun.gov.np/photo-gallery
- **Verification status:** Ridge-level panorama identity verified; individual viewpoint pins remain intentionally unverified.

## 23. Sanga ridge

- **District context:** Kavrepalanchok side of the Bhaktapur–Kavrepalanchok gateway ridge
- **Destination type:** Scenic gateway ridge / road-trip viewpoint area
- **Cross-district rule:** Sanga sits on the Bhaktapur–Kavrepalanchok boundary corridor. The inventory should use district-specific subareas or polygons instead of assigning the entire Sanga ridge to one district.
- **Tourism context:** Nepal Tourism Board identifies Sanga as the location of Kailashnath Mahadev and notes its hilltop setting and broad views. This confirms the ridge's tourism value beyond the statue itself.
- **Route-planner modeling:** `Sanga ridge` should be an area/scenic-road object with exact district boundary geometry, while individual attractions such as Kailashnath Mahadev remain separate POIs.
- **Coordinates:** Boundary-aware ridge geometry requires authoritative GIS QA.
- **Permit requirement:** No area-wide tourism permit identified.
- **Primary sources:**
  - https://ntb.gov.np/en/latest-stories/top-5-shiva-temples-in-kathmandu-valley
  - https://ntb.gov.np/plan-your-trip/trip-ideas/pilgrimage-to-doleshwar-mahadev-temple
- **Verification status:** Sanga tourism identity and hilltop/view context verified from NTB; exact Kavrepalanchok-side polygon pending GIS.

## 24. Kailashnath Mahadev Statue / Sanga Shiva

- **District context:** Sanga gateway ridge; exact district parcel must be handled with boundary-aware GIS because Sanga lies at the Bhaktapur–Kavrepalanchok edge.
- **Destination type:** Monumental Shiva statue / pilgrimage and recreation complex
- **Alias:** Kailashnath Mahadev; Sanga Shiva.
- **NTB height/context:** Nepal Tourism Board currently describes Kailashnath Mahadev at Sanga as a 143-foot monument and notes the statue itself as 108 feet high, with the larger complex spread across a hilltop recreation/wellness setting.
- **Inauguration:** NTB states the site was inaugurated on June 21, 2010.
- **Access:** NTB places it about 20 km from Kathmandu and describes it as road-accessible.
- **Facility modeling:** Treat the statue/complex as a facility-level POI. Store entrance, parking/drop-off and hill/viewpoint geometry separately if available.
- **Cross-district caution:** Do not duplicate the same facility as two independent attractions in Bhaktapur and Kavrepalanchok. Use one canonical attraction record with boundary/district metadata and district-specific related links.
- **Fees / hours:** Commercial/facility operations are time-sensitive and should be rechecked with the operator before publication.
- **Primary sources:**
  - https://ntb.gov.np/en/latest-stories/top-5-shiva-temples-in-kathmandu-valley
  - https://ntb.gov.np/plan-your-trip/trip-ideas/pilgrimage-to-doleshwar-mahadev-temple
- **Verification status:** Attraction identity, size, inauguration and road-access context verified from Nepal Tourism Board; exact district parcel and live operations pending.

## 25. Nagarkot eastern ridge

- **District:** Kavrepalanchok
- **Municipality:** Mandan Deupur Municipality
- **Destination type:** Cross-district hill-station subarea / viewpoints / resort and homestay ridge
- **Municipality verification:** Mandan Deupur Municipality explicitly lists Nagarkot among its important parks/picnic/tourism locations.
- **Ward-level verification:** The municipality's Ward 2 profile, formerly associated with Naldum/Baluwapati Deupur, specifically describes Nagarkot tourism as economically important and notes more than 60 hotels, resorts and homestays serving domestic and foreign visitors in the area.
- **Cross-district modeling:** This record represents the Kavrepalanchok/Mandan Deupur side of Nagarkot. The broader Nagarkot destination must remain a shared multi-district object linked with Bhaktapur-side Nagarkot rather than two competing destination pages.
- **Municipality context:** Mandan Deupur's own slogan emphasizes agriculture and tourism, and the municipality describes its mid-hill terrain as highly suitable for tourism.
- **Route-planner modeling:** Use a district-aware Nagarkot polygon/subarea with separate resorts, viewpoints, trails and road approaches. Do not use one town centroid to determine district ownership.
- **Coordinates:** District boundary and viewpoint-level GIS remain pending.
- **Primary sources:**
  - https://mandandeupurmun.gov.np/%E0%A4%AE%E0%A4%B9%E0%A4%A4%E0%A5%8D%E0%A4%B5%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%A3-%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BE%E0%A4%A8%E0%A4%B9%E0%A4%B0%E0%A5%81
  - https://mandandeupurmun.gov.np/ward-no-2
  - https://www.mandandeupurmun.gov.np/
- **Verification status:** Mandan Deupur/Nagarkot relationship and substantial tourism-accommodation context verified from municipality sources; polygon/viewpoint GIS pending.

# Kavrepalanchok progress

- **Inventory entries:** 32
- **Deep-researched:** 25 / 32
- **Next entries:** 26–30 — Roshi Valley; Roshi River corridor; Tindhare Waterfall; Kushadevi forest landscape; Bolde viewpoint.

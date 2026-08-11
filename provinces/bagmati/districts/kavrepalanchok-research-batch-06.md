# Kavrepalanchok Verified Research Batch 06 — 2026-08-11

> Deep-research sidecar for Kavrepalanchok inventory entries 26–30. Strong official evidence was found for Roshi/Tindhare; weaker emerging records remain explicitly flagged rather than overstated.

## 26. Roshi Valley

- **District:** Kavrepalanchok
- **Municipality:** Roshi Rural Municipality
- **Destination type:** River valley / rural road-trip landscape / agriculture-and-nature region
- **Municipality identity:** Roshi Rural Municipality describes itself as a historically and tourism-important hill municipality and uses the slogan `Roshi's vision: tourism and agriculture`.
- **Name origin:** The municipality states that it is named after Roshi Khola, the major river of the area.
- **Landscape context:** Official municipality planning material describes Roshi as a 176+ sq km hill municipality with 12 wards, bordered by Namobuddha and Temal to the north, Sunkoshi to the east, Bethanchok to the west and southern hill municipalities.
- **Cultural context:** Municipality sources identify Tamang as the largest ethnic community, with Hindu and Buddhist populations both significant. Traveler-facing content should treat the valley as a living rural/cultural landscape rather than a generic scenic drive.
- **Route-planner modeling:** Use a valley/region object with settlements, river crossings, waterfalls, ridges and BP Highway access points as separate sub-objects.
- **Coordinates:** Municipality/valley polygon required; one centroid is insufficient.
- **Primary sources:**
  - https://roshimun.gov.np/content/%E0%A4%B8%E0%A4%82%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BF%E0%A4%AA%E0%A5%8D%E0%A4%A4-%E0%A4%AA%E0%A4%B0%E0%A4%BF%E0%A4%9A%E0%A4%AF
  - https://www.roshimun.gov.np/
  - https://www.roshimun.gov.np/sites/roshimun.gov.np/files/Roshi_LOI%20modified.pdf
- **Verification status:** Municipality, tourism identity, river-name relationship and broad valley context verified from Roshi Rural Municipality.

## 27. Roshi River corridor

- **District:** Kavrepalanchok
- **Municipal span:** Roshi Rural Municipality with upstream connections toward central Kavrepalanchok/Panauti-side catchments
- **Destination type:** River corridor / scenic-road landscape / hydrological feature
- **Official hydrology:** Roshi Rural Municipality planning material states that Roshi Khola is the area's major river, originates in the foothills of Kavrepalanchok, runs roughly 55.65 km and ultimately joins the Sunkoshi River.
- **Naming significance:** The rural municipality itself is named after Roshi Khola.
- **Object-modeling rule:** Store the river as a line/corridor object, not a POI. Individual bridges, ghats, picnic sites, confluences and waterfall tributaries require separate verified records.
- **Safety/seasonality:** Monsoon flow, erosion, landslides and road conditions can materially change river-corridor travel. Future route guidance must use current conditions rather than static assumptions.
- **Coordinates:** River line geometry should come from authoritative hydro/GIS data during the dedicated GIS pass.
- **Primary sources:**
  - https://www.roshimun.gov.np/sites/roshimun.gov.np/files/Roshi_LOI%20modified.pdf
  - https://roshimun.gov.np/content/%E0%A4%B8%E0%A4%82%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BF%E0%A4%AA%E0%A5%8D%E0%A4%A4-%E0%A4%AA%E0%A4%B0%E0%A4%BF%E0%A4%9A%E0%A4%AF
- **Verification status:** River identity, municipality-name relationship, approximate length and Sunkoshi connection verified from municipality planning material.

## 28. Tindhare Waterfall

- **District:** Kavrepalanchok
- **Municipality:** Roshi Rural Municipality
- **Destination type:** Waterfall / trekking-nature cluster / emerging municipality tourism project
- **Strong municipality evidence:** Roshi Rural Municipality's official municipal magazine documents a `Tindhare Waterfall Integrated Development Committee` and identifies Tindhare Waterfall as the center of a planned tourism-development area.
- **Associated attractions:** The same official source lists Antarsinghe and Mahabhir waterfalls, an ore-washing cave, Copper Hill, Banjhakri Cave, a Mahabharat-related hill and a plateau suitable for a helipad within the broader development area.
- **Development context:** The municipality states it was studying integrated development around Tindhare, including construction of a trekking trail. This means the record is more than a social-media-only waterfall claim, but infrastructure status must still be checked live.
- **Route-planner modeling:** Use Tindhare as the anchor waterfall POI and model associated falls/caves/trails separately only after exact local verification. Do not automatically publish every named feature from the planning concept as an independently accessible attraction.
- **Coordinates:** Exact waterfall and trailhead coordinates remain for GIS/local verification.
- **Access caution:** Road/trail conditions and development status can change, especially in monsoon.
- **Primary source:**
  - https://roshimun.gov.np/sites/roshimun.gov.np/files/Roshi%20R_Municipality%20Magazine%20%282%29.pdf
- **Verification status:** PASS — municipality tourism-development evidence is strong; exact GIS, trail completion and current visitor operations pending.

## 29. Kushadevi forest landscape

- **District:** Kavrepalanchok
- **Municipality:** Panauti Municipality
- **Destination type:** Forested rural hill landscape / emerging nature destination
- **Administrative verification:** Panauti Municipality's current introduction confirms that the former Kushadevi VDC was incorporated into the restructured Panauti Municipality.
- **Municipal nature context:** Panauti Municipality describes the municipality as having major natural beauty and beautiful hills, with agriculture as a principal livelihood and an elevation range extending to roughly 2,782 m.
- **Evidence caution:** Current municipality sources verify Kushadevi as part of Panauti and support the broader natural/hill context, but this research pass did **not** find a strong official source defining a formally bounded tourism product called `Kushadevi forest landscape`.
- **Publication rule:** Keep as an emerging area record, not a fully established attraction. Before traveler-facing publication, verify exact forest/community-forest names, public access, trails and local tourism use.
- **Route-planner modeling:** Area object only until specific community forests, trailheads or viewpoints are authoritatively identified.
- **Coordinates:** Pending exact forest/landscape boundary verification.
- **Primary sources:**
  - https://panautimun.gov.np/
  - https://panautimun.gov.np/en/node/4
- **Verification status:** PARTIAL — administrative and landscape context verified; attraction identity/access needs local verification.

## 30. Bolde viewpoint

- **District:** Kavrepalanchok
- **Area:** Temal / Bolde area per district inventory
- **Destination type:** Local hill viewpoint / emerging destination
- **Evidence status:** The canonical district inventory already flags this record as `Needs local verification`. This research pass did not find sufficiently strong municipality or tourism-board evidence to promote `Bolde viewpoint` to an established attraction.
- **Data-quality decision:** Preserve the record because it may represent a genuine local viewpoint, but explicitly keep it out of publication-ready routing until its exact local name, ward, coordinate, public access and viewpoint identity are verified.
- **Do-not-invent rule:** Do not assign a coordinate from a generic `Bolde` settlement map pin and do not infer a viewpoint merely from elevation/topography.
- **Route-planner modeling:** `emerging_viewpoint_candidate` until local verification is complete.
- **Coordinates:** Unverified.
- **Entry/access:** Unverified.
- **Verification status:** HOLD / LOCAL VERIFICATION REQUIRED.

# Kavrepalanchok progress

- **Inventory entries:** 32
- **Deep-researched / dispositioned:** 30 / 32
- **Next entries:** 31–32 — Kavre Bhanjyang; Panchkhal agro-tourism belt.
- **After 32/32:** Run district QA, with Bolde retained as a verification hold rather than falsely marked established.

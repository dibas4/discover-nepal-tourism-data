# Ramechhap Verified Research Batch 06 — 2026-08-11

> Final place-level research batch for Ramechhap inventory entries 26–29. Weakly sourced local features remain explicit verification holds rather than being promoted from map/social labels.

## 26. Sailung sunrise viewpoint

- **District context:** Ramechhap side of the cross-district Sailung/Shailung highlands
- **Municipality:** Doramba Sailung Rural Municipality
- **Destination type:** Sunrise viewpoint / high-ridge panorama / hiking objective
- **Canonical relationship:** This is a viewpoint experience within the broader Thulo Sailung destination, not a second independent mountain destination.
- **Local-government context:** Doramba Sailung Rural Municipality explicitly positions tourism as a core development pillar in its current municipal identity.
- **Route-planner modeling:** Link the viewpoint to the canonical Sailung ridge polygon and store the Ramechhap-side trailhead/road approach separately once GIS-verified.
- **Cross-district rule:** Do not duplicate the entire Sailung ridge in both Ramechhap and Dolakha. Use one canonical destination with district-aware access subareas.
- **Weather caution:** Sunrise and Himalayan visibility are weather-dependent and never guaranteed.
- **Coordinates:** Exact safe public sunrise-viewpoint pin requires local/GIS verification.
- **Primary source:** https://dorambamun.gov.np/
- **Verification status:** PASS at destination/municipality level; precise viewpoint geometry pending.

## 27. Numbur alpine meadows

- **District:** Ramechhap
- **Municipality:** Umakunda Rural Municipality
- **Destination type:** Alpine pasture / seasonal grazing landscape / trekking-route natural feature
- **Destination relationship:** These meadows belong to the broader Numbur Himal and Numbur Cheese Circuit landscape and should not be modeled as one invented meadow POI.
- **Cultural-economic context:** High pastures can be associated with seasonal livestock/yak grazing and dairy production, but individual grazing sites and cheese-production stops must be verified before publication.
- **Route-planner modeling:** `alpine_meadow_cluster` linked to verified trekking segments. Individual pasture polygons/camps should only be created from authoritative/local evidence.
- **Seasonality:** Vegetation, livestock presence, snow cover and accessibility vary substantially by season.
- **Coordinates:** No single canonical meadow coordinate should be invented; GIS/trail survey required.
- **Permit/access:** Recheck current trekking/local requirements before publication.
- **Verification status:** PARTIAL — broader Numbur highland landscape is established; specific meadow objects remain field/local verification work.

## 28. Khimti waterfalls and cascades

- **District:** Ramechhap
- **Area:** Gokulganga / Khimti corridor
- **Destination type:** River cascades / seasonal waterfall candidates / emerging natural attractions
- **Strong corridor evidence:** Gokulganga Rural Municipality's environmental assessment confirms Khimti Khola as a major local river corridor and documents multiple riverbank sites within the municipality.
- **Evidence caution:** The official material supports the Khimti river environment, but this pass did not find authoritative evidence defining one canonical tourism attraction called `Khimti waterfalls and cascades` with a verified coordinate.
- **Data-quality decision:** Keep as an emerging cluster record. Do not turn roadside cascades or map labels into independent tourism POIs without local confirmation.
- **Seasonality/safety:** Cascade volume and safety change dramatically with monsoon flow; river-edge access should not be assumed safe.
- **Route-planner modeling:** `waterfall_candidate_cluster`; publish individual waterfalls only after name, ward, coordinate and safe-access verification.
- **Primary source:** https://gokulgangamun.gov.np/sites/gokulgangamun.gov.np/files/IEE-Report.pdf
- **Verification status:** HOLD for attraction-level publication; Khimti river corridor itself is verified.

## 29. Manthali riverbank recreation area

- **District:** Ramechhap
- **Municipality:** Manthali Municipality
- **Destination type:** Emerging riverbank recreation landscape / urban visitor stop
- **Municipal context:** Manthali Municipality actively discusses tourism-development potential and its transport plan documents road/access infrastructure around Manthali, including Paani Ghat and other Ward 1 corridors.
- **Evidence caution:** Current authoritative municipality sources do not establish a single formally named tourism facility matching `Manthali riverbank recreation area` with fixed boundaries, ticketing or visitor operations.
- **Data-quality decision:** Retain as an emerging area record rather than a publication-ready attraction.
- **Related verified local attractions:** Municipality ward pages separately identify established local sites such as Teenlal Park and Nagkanya Temple in Ward 1 and several hill/religious attractions in other wards. These should not be silently merged into the riverbank record.
- **Route-planner modeling:** `emerging_recreation_area`; exact Tamakoshi riverbank segment, public access, flood-safe area and facilities require municipal/GIS verification.
- **Flood/seasonality caution:** Any riverbank routing must account for seasonal Tamakoshi conditions and should use current local safety information.
- **Primary sources:**
  - https://manthalimun.gov.np/en
  - https://manthalimun.gov.np/en/node/1409
  - https://www.manthalimun.gov.np/sites/manthalimun.gov.np/files/Articles/Manthali%20final%20Report%20MTMP%20%281%29.pdf
- **Verification status:** PARTIAL / LOCAL VERIFICATION REQUIRED before attraction-level publication.

# Ramechhap completion status

- **Inventory entries:** 29
- **Deep-researched / dispositioned:** 29 / 29
- **Place-level research:** COMPLETE
- **Next step:** District QA covering aliases, municipality assignments, cross-district Sailung geometry, Numbur route/lake disambiguation, weak local records, GIS precision, live access and permit rules.

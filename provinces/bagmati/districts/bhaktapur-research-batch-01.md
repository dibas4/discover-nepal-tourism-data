# Bhaktapur Verified Research Batch 01 — 2026-08-11

> Deep-research sidecar for Bhaktapur inventory entries 1–5. Time-sensitive fees and operations must be rechecked before publication.

## 1. Bhaktapur Durbar Square

- **District:** Bhaktapur
- **Municipality:** Bhaktapur Municipality
- **Destination type:** UNESCO World Heritage monument zone / former royal palace square / living Newar heritage core
- **UNESCO status:** Bhaktapur Durbar Square is one of the seven monument zones forming the Kathmandu Valley World Heritage property.
- **UNESCO coordinates:** 27°40'20.734"N, 85°25'42.481"E
- **Coordinate status:** UNESCO monument-zone coordinate; use separate visitor-gate/POI pins later for route planning.
- **UNESCO property size:** 3.61 ha core property with a 10.71 ha buffer zone.
- **Tourism context:** Nepal Tourism Board describes the square as the former palace center of Bhaktapur, surrounded by monuments dating from roughly the 13th–18th centuries. Major features include the Palace of 55 Windows, Golden Gate, Lion Gate, King Bhupatindra Malla statue and Batsala Temple.
- **Current entry fee (source checked 2026-08-11):** NTB lists US$18 or NPR 1,800 for foreign nationals; NPR 500 for SAARC nationals; NPR 500 for Chinese nationals; Nepalese free. Children below 10 are free; for groups of 11–20, one tour leader may enter free.
- **Permit requirement:** No separate travel permit identified; heritage-site entrance ticket applies to relevant visitor categories.
- **Fee caution:** NTB language versions have historically shown conflicting older tariff values, so traveler-facing fees must always use the current English fee table or municipality ticket source immediately before publication.
- **Primary sources:**
  - https://whc.unesco.org/en/list/121/
  - https://whc.unesco.org/en/list/121/maps/
  - https://ntb.gov.np/en/bhaktapur
  - https://ntb.gov.np/plan-your-trip/before-you-come/heritage-site-entry-fees
- **Verification status:** UNESCO identity/geometry, tourism significance and current NTB English tariff verified.

## 2. Dattatreya Square / Dattatraya Square

- **District:** Bhaktapur
- **Municipality:** Bhaktapur Municipality
- **Destination type:** Historic square / religious-architectural ensemble / wood-carving heritage area
- **Alias normalization:** Preserve both `Dattatreya` and `Dattatraya`; Bhaktapur Municipality currently uses Dattatraya while NTB uses Dattatreya.
- **Municipality context:** Bhaktapur Municipality identifies Dattatraya Square as the oldest part of the city and describes it as an open museum especially noted for wood carving.
- **Core monuments:** Municipality sources identify Dattatraya Temple, Bhimsen Temple, water spouts, carved windows, maths/monastic structures and the famous Peacock Window among the major features.
- **Museum relationship:** Bhaktapur Municipality also notes the Brass and Bronze Museum and Wood Carving Museum in the square.
- **NTB religious context:** NTB states that Dattatreya Temple is dedicated to the three-headed form combining Brahma, Vishnu and Shiva and records the traditional claim that it was built from the trunk of a single tree.
- **Current museum tariff relationship (source checked 2026-08-11):** NTB's National Art Museum fee is listed as NPR 150 foreign / NPR 50 SAARC / NPR 150 Chinese / NPR 10 students and NPR 25 other Nepalese, with separate camera/video charges. NTB states this ticket includes the Wood Carving Museum and Brass and Bronze Museum in Dattatreya Square. Closed Tuesdays according to the current NTB table.
- **Route-planner modeling:** Store Dattatreya Square as an area/heritage-square object with separate temple and museum POIs.
- **Coordinates:** Exact square centroid and museum/temple entrances require GIS QA.
- **Primary sources:**
  - https://bhaktapurmun.gov.np/en/node/4
  - https://ntb.gov.np/en/bhaktapur
  - https://ntb.gov.np/plan-your-trip/before-you-come/heritage-site-entry-fees
- **Verification status:** Square identity, major monuments and museum relationship verified from municipality + NTB; detailed GIS pending.

## 3. Thimi heritage town / Madhyapur Thimi historic core

- **District:** Bhaktapur
- **Municipality:** Madhyapur Thimi Municipality
- **Destination type:** Historic Newar town / pottery and farming heritage / living cultural settlement
- **Name context:** Use `Thimi` for the historic settlement and `Madhyapur Thimi Municipality` for the modern administrative unit.
- **Tourism context:** Nepal Tourism Board places Thimi about 8 km east of Kathmandu on the way to Bhaktapur and identifies pottery and vegetable farming as defining local activities.
- **Religious anchors:** NTB names Balkumari Temple and Karunamaya as important local deities/shrines.
- **Administrative context:** Madhyapur Thimi Municipality was formed from the former Bode, Nagadesh, Chapacho, Balkumari and Lokanthali local units; current municipal ward structure confirms the historic Thimi/Balkumari/Chapacho core remains within the municipality.
- **Living-heritage modeling:** Treat Thimi as a settlement/heritage-area object with separate pottery neighborhoods, Balkumari Temple, Karunamaya and festival routes as sub-POIs/events.
- **Coordinates:** Use a historic-core area geometry rather than a single municipality-office coordinate; GIS QA required.
- **Permit requirement:** No town-wide tourism permit identified.
- **Entry fee / hours:** No universal heritage-town fee or opening hours identified; individual temples/facilities may differ.
- **Primary sources:**
  - https://ntb.gov.np/en/bhaktapur
  - https://www.madhyapurthimimun.gov.np/en/content/madhyapur-thimi-municipality-ward-no-4-balkumari
  - https://madhyapurthimimun.gov.np/en/content/madhyapur-thimi-municipality-ward-no-6-chapacho
- **Verification status:** Settlement identity, pottery/farming significance and modern municipal context verified.

## 4. Bode and Nil Barahi cultural area

- **District:** Bhaktapur
- **Municipality:** Madhyapur Thimi Municipality
- **Administrative anchors:** Bode is explicitly Ward 8 in current municipal records; Bode-linked institutions and Nilbarahi-named institutions also appear in Ward 9 / Sintitaar-Tigani municipal records, so the cultural area spans more than one simple ward-center concept.
- **Destination type:** Historic Newar settlement / ritual-dance and festival cultural area
- **Bode verification:** Madhyapur Thimi Municipality's Ward 8 page is officially titled `Madhyapur Thimi Municipality Ward No. 8, Bode`.
- **Nil Barahi cultural significance:** The municipality maintains official photo/event documentation for the historical Madhyapur Thimi Bhaila Dance, Nilbarahi Dance and Mahakali Dance, confirming Nil Barahi as an active municipal cultural-heritage tradition rather than only a place-name reference.
- **Modeling note:** Do not collapse `Bode`, `Nil Barahi Temple/ritual area`, and the Nil Barahi dance/festival route into one point. Store settlement, temple/ritual POI and event route separately when verified.
- **Festival-date caution:** Annual ritual/festival dates follow local calendars and should be taken from current municipality notices for the relevant year.
- **Coordinates:** Exact Bode historic-core, Nil Barahi sacred-site and event-route geometry require GIS/local-source QA.
- **Permit requirement:** No area-wide tourism permit identified.
- **Entry fee / hours:** No universal visitor tariff or opening schedule identified.
- **Primary sources:**
  - https://www.madhyapurthimimun.gov.np/en/node/853
  - https://madhyapurthimimun.gov.np/en/content/historical-madhyapur-thimi-bhaila-dance-nilbarahi-dance-and-mahakali-dance-2079080
  - https://madhyapurthimimun.gov.np/en/content/madhyapur-thimi-municipality-ward-no-9-sintitaar
- **Verification status:** Bode administrative identity and Nil Barahi cultural-dance significance verified; exact sacred-site geometry remains pending.

## 5. Nyatapola Temple

- **District:** Bhaktapur
- **Municipality / area:** Bhaktapur Municipality, Taumadhi Square
- **Destination type:** Five-storey pagoda temple / architectural landmark / living religious heritage
- **Name meaning:** Nepal Tourism Board states that `Nyatapola` literally means “five storied.”
- **Municipality context:** Bhaktapur Municipality identifies Nyatapola as one of the principal monuments of Taumadhi Square, together with Bhairabnath Temple, Tilmadhav Narayan Temple and associated historic features.
- **Architectural significance:** NTB describes Nyatapola as a defining Bhaktapur landmark and notes the staged stone guardians/deities/mythical beasts lining the staircase.
- **Earthquake context:** NTB notes that the temple survived the devastating 1933 earthquake; traveler copy should avoid broader resilience claims unless separately sourced for later earthquakes.
- **Relationship to heritage ticket:** Nyatapola lies within Bhaktapur's historic city visitor circuit. Do not assume a standalone Nyatapola ticket; apply the correct heritage-zone/access model based on current municipality entry controls.
- **Route-planner modeling:** Facility-level religious/architectural POI inside Taumadhi Square; keep Taumadhi Square as a separate area object if added later.
- **Coordinates:** Exact temple entrance/foot-of-stair coordinate required during GIS QA.
- **Permit requirement:** No separate travel permit identified.
- **Fee / hours:** No separate authoritative temple tariff or complete schedule captured; recheck local religious-access practices before publication.
- **Primary sources:**
  - https://bhaktapurmun.gov.np/en/node/4
  - https://ntb.gov.np/en/bhaktapur
- **Verification status:** Municipality location, architectural identity and tourism significance verified.

# Bhaktapur progress

- **Inventory entries:** 11
- **Deep-researched:** 5 / 11
- **Next entries:** 6–10 — Changu Narayan Temple; Kailashnath Mahadev Statue; Suryabinayak Temple; Siddha Pokhari; Nagarkot.
- **Final entry after that:** Pilot Baba Ashram viewpoint.
- **After 11/11:** Run Bhaktapur district QA for cross-district Nagarkot geometry, aliases, UNESCO relationships, GIS precision and live operational data.

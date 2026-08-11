# Rasuwa Verified Research Batch 01 — 2026-08-11

> Deep-research sidecar for canonical Rasuwa inventory entries 1–5. Protected-area rules, current fees, trail conditions and precise GIS geometry remain publication-time checks where they are dynamic.

## 1. Langtang National Park

- **District / extent:** Rasuwa with adjoining Nuwakot and Sindhupalchok sectors.
- **Destination type:** National park / Himalayan protected area / trekking and wildlife landscape.
- **Establishment:** Government of Nepal gazetted the park on 22 March 1976.
- **Area:** 1,710 sq km. DNPWC separately lists a 420 sq km buffer zone.
- **Rasuwa share:** The park office states that it covers parts of four rural municipalities in Rasuwa and about 57% of the park's total area lies in Rasuwa.
- **Elevation / ecology:** Official park information describes an elevation range from roughly 1,000 m to above 7,200 m, with subtropical, temperate, subalpine and alpine vegetation zones.
- **Wildlife:** Official sources identify red panda, musk deer, Himalayan black bear, Himalayan tahr, ghoral, serow, wild dog and snow leopard among characteristic fauna.
- **Tourism role:** Nepal Tourism Board identifies Langtang National Park as a major trekking/mountaineering and Tamang-culture destination, with Langtang Valley and Gosainkunda among its key attractions.
- **Current NTB park-entry fee (source checked 2026-08-11):** Nepali NPR 25, SAARC NPR 1,500 and foreign national NPR 3,000 per person per entry. Recheck before publication because tariffs can change.
- **Headquarters / access anchor:** Dhunche is listed as the park headquarters and principal road-access gateway.
- **Modeling rule:** Store the park as a protected-area polygon/region, not a single attraction pin. Village, trail, lake and monastery records remain child/linked objects.
- **Verification status:** **VERIFIED major protected area; live tariff, gate rules and route conditions require freshness checks.**

## 2. Langtang Valley

- **District:** Rasuwa.
- **Municipality:** Gosaikunda Rural Municipality; the municipality itself identifies Langtang as one of its principal tourism areas.
- **Destination type:** Himalayan trekking valley / cultural-natural landscape.
- **Route context:** Nepal Tourism Board describes the Langtang Valley Trek as starting from Syabrubesi and passing through Tamang villages, forests and alpine meadows toward Kyanjin Gompa, Kyanjin Ri and Tserko Ri.
- **Protected-area relationship:** The valley lies inside Langtang National Park; park-entry rules therefore apply to trekking access.
- **Cultural context:** Tourism material consistently links the valley with Tamang settlements, monasteries, yak-based livelihoods and alpine mountain culture.
- **Seasonality:** NTB's Langtang-region guidance identifies March–May and October–November as the main trekking seasons; winter snow and monsoon rain materially affect route conditions.
- **Modeling rule:** Keep `Langtang Valley` as an area/trekking-corridor destination rather than a single POI. Langtang Village, Kyanjin, viewpoints and side hikes are separate nodes.
- **Coordinates:** Use valley geometry/trail corridor in GIS rather than one generic centroid for route planning.
- **Verification status:** **VERIFIED major trekking valley; exact trail geometry and current condition remain dynamic.**

## 3. Langtang Village

- **District:** Rasuwa.
- **Municipality / ward:** Gosaikunda Rural Municipality, Ward 4. The municipality lists Ward 4 as Langtang and maintains a ward office in Langtang.
- **Destination type:** High-mountain village / cultural and trekking stop.
- **Administrative grounding:** Gosaikunda Rural Municipality explicitly identifies Langtang as Ward 4 and includes Langtang among the municipality's major tourism assets.
- **Tourism role:** Langtang Village is a principal settlement on the Langtang Valley trekking route and should be modeled independently from the valley itself.
- **2015-earthquake context:** Traveler-facing historical copy should acknowledge that the village was devastated in the 2015 earthquake and subsequently rebuilt, but current lodging/infrastructure claims must be rechecked locally rather than inferred from older recovery reports.
- **Community sensitivity:** Treat the village as a living community, not a spectacle. Cultural descriptions should foreground local ownership, consent and respectful photography.
- **Coordinates:** Settlement-level centroid may be used only after GIS confirmation; lodging, memorial and trail-junction nodes should have separate points.
- **Verification status:** **VERIFIED settlement and Ward 4 association; current business inventory and exact POI geometry require live/local verification.**

## 4. Kyanjin Gompa Village

- **District:** Rasuwa.
- **Municipality / ward:** Upper Langtang, within Gosaikunda Rural Municipality's Ward 4 Langtang area.
- **Destination type:** High-altitude trekking village / upper-valley base.
- **Tourism role:** Nepal Tourism Board identifies Kyanjin as the upper Langtang destination from which visitors explore the upper valley, Langshisa and nearby viewpoints. Current NTB trekking material explicitly links Kyanjin Gompa with Kyanjin Ri and Tserko Ri.
- **Protected-area relationship:** Village access is through Langtang National Park and therefore depends on park-entry and trail conditions.
- **Modeling rule:** Keep the settlement as a village/base object. The monastery, Kyanjin Ri, Tserko Ri and onward Langshisha route remain separate child attractions/routes.
- **Operational caution:** Teahouse/lodge availability, seasonal closures, power/connectivity and medical support are dynamic high-altitude conditions and must not be hard-coded without a recent local check.
- **Coordinates:** Settlement centroid and individual facilities should be separated during GIS QA.
- **Verification status:** **VERIFIED upper-valley trekking settlement; current operations and precise GIS nodes remain dynamic.**

## 5. Kyanjin Gompa monastery

- **District:** Rasuwa.
- **Municipality / ward:** Kyanjin, Ward 4 Langtang area, Gosaikunda Rural Municipality.
- **Destination type:** Buddhist monastery / religious-cultural POI.
- **Tourism grounding:** Nepal Tourism Board repeatedly identifies Kyanjin Gompa as the spiritual/cultural anchor of the upper Langtang trek and as a principal destination reached from the Langtang Valley route.
- **Important separation:** The monastery must not be conflated with `Kyanjin Gompa Village`; one is a religious POI and the other is the surrounding trekking settlement.
- **Religious etiquette:** Traveler-facing content should emphasize quiet conduct, respectful dress and photography only where permitted locally. Do not invent opening hours, ritual schedules or donation requirements.
- **Coordinates:** Exact monastery entrance/compound coordinate should be captured separately from the village centroid during GIS QA.
- **Verification status:** **VERIFIED religious-cultural site within Kyanjin; operating hours/access details require local confirmation.**

### Sources reviewed

1. Langtang National Park Office — official park profile and geographic/ecological context: https://langtangnationalpark.gov.np/en/
2. Department of National Parks and Wildlife Conservation — Langtang National Park profile: https://dnpwc.gov.np/pages/langtang-national-immigration-office-64/
3. Nepal Tourism Board — Langtang National Park: https://ntb.gov.np/en/langtang
4. Nepal Tourism Board — Langtang Region / trekking destination material: https://trade.ntb.gov.np/tourist-destination/langtang-region/ and https://ntb.gov.np/en/top-trekking-destination-in-nepal-for-the-ultimate-himalayan-experience
5. Gosaikunda Rural Municipality — municipality introduction, ward offices and Langtang tourism listing: https://gosaikundamun.gov.np/introduction ; https://www.gosaikundamun.gov.np/ward-offices ; https://gosaikundamun.gov.np/important-places/%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%AF%E0%A4%9F%E0%A4%95-%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0

# Rasuwa research progress

- **Canonical inventory:** 34 entries
- **Deep-researched/dispositioned:** 5 / 34
- **Remaining:** 29
- **Next canonical entries:** 6. Kyanjin Ri; 7. Tserko Ri; 8. Langshisha Kharka; 9. Ganja La Pass trekking route; 10. Yala Peak approach area.

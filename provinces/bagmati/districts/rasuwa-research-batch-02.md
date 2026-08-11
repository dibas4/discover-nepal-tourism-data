# Rasuwa Verified Research Batch 02 — 2026-08-11

> Deep research for canonical Rasuwa inventory entries 6–10. High-altitude route geometry, current conditions and permit rules must be rechecked before traveler-facing publication.

## 6. Kyanjin Ri
- **Area:** Kyanjin / upper Langtang Valley, Gosaikunda Rural Municipality, Rasuwa
- **Type:** High-altitude viewpoint / acclimatisation day hike
- **Verification:** Nepal Tourism Board explicitly lists Kyanjin Ri among the destinations reached on the Langtang Valley Trek and its official Photo Nepal platform identifies Kyanjin Ri in Langtang Valley.
- **Modeling:** Keep as a viewpoint/trail destination distinct from Kyanjin village and monastery. Store trailhead and summit/viewpoint geometry separately during GIS QA.
- **Safety:** High-altitude mountain conditions are dynamic; do not hard-code a universal duration, difficulty or safe-season guarantee.
- **Sources:** https://ntb.gov.np/en/top-trekking-destination-in-nepal-for-the-ultimate-himalayan-experience ; https://photo.ntb.gov.np/photo/6871/kyanjin-ri-lower-peak
- **Status:** VERIFIED; precise trail geometry pending.

## 7. Tserko Ri
- **Area:** Upper Langtang Valley / Kyanjin area, Rasuwa
- **Type:** High-altitude viewpoint / day-hike objective
- **Verification:** Nepal Tourism Board explicitly names Tserko Ri together with Kyanjin Gompa and Kyanjin Ri as a Langtang Valley Trek destination.
- **Modeling:** Store as a high-altitude viewpoint/trail destination rather than a generic attraction POI. Exact route and summit coordinate require GIS verification.
- **Safety:** Weather, snow, altitude and trail conditions can materially change difficulty; traveler-facing guidance requires current local/park checks.
- **Source:** https://ntb.gov.np/en/top-trekking-destination-in-nepal-for-the-ultimate-himalayan-experience
- **Status:** VERIFIED for tourism identity; geometry/operational conditions pending.

## 8. Langshisha Kharka
- **Area:** Upper Langtang Valley beyond Kyanjin, Rasuwa
- **Type:** Alpine meadow / trekking destination
- **Verification:** Nepal Tourism Board's Langtang Region page states visitors can extend their stay at Kyanjin to explore the upper valley to Langshisa and beyond, supporting the canonical upper-valley destination concept.
- **Name handling:** Preserve `Langshisha` and `Langshisa` as aliases because transliteration varies across tourism sources.
- **Modeling:** Area/trail destination, not a single building POI. Exact kharka centroid, route and camping/use rules require park/GIS verification.
- **Source:** https://trade.ntb.gov.np/tourist-destination/langtang-region/
- **Status:** VERIFIED WITH GIS FLAG.

## 9. Ganja La Pass trekking route
- **Area:** Langtang–Helambu high route
- **Type:** High mountain pass / trekking route
- **Verification:** Nepal Tourism Board identifies Ganja La as a major pass south of the Langtang range and gives an elevation of 5,122 m.
- **Critical modeling rule:** This is a route/pass object, not a normal POI. Do not reduce the entire crossing to one map pin.
- **Safety:** Treat as an advanced high-altitude route. Snow, navigation and seasonal conditions require current professional/local verification before route-planner recommendation.
- **Permit note:** Do not infer a special Ganja La-specific permit from generic Langtang park requirements; current trekking/park requirements must be checked at publication time.
- **Source:** https://trade.ntb.gov.np/tourist-destination/langtang-region/
- **Status:** VERIFIED; route geometry and live safety conditions pending.

## 10. Yala Peak approach area
- **Area:** Upper Langtang / Kyanjin approach, Rasuwa
- **Type:** Mountaineering approach / trekking-peak access area
- **Verification:** Government of Nepal tourism documentation lists **Yala** at 5,732 m in the Langtang range, with the approach described as Kathmandu–Dhunche–Langtang–Kyanjin–base camp. Historical Nepal Tourism Statistics also records climbers permitted for Yala Peak.
- **Critical modeling rule:** Keep the `approach area` separate from the summit/climbing objective. The route planner must not present a mountaineering objective as an ordinary hike.
- **Permit/safety:** Climbing regulation and permit administration are time-sensitive. Recheck the current authorized issuing body, royalty/fee, guide requirements and route conditions before public publication.
- **Sources:** https://www.tourism.gov.np/files/publication_files/TourismIndustryServiceIndustryDirective_1479883437.pdf ; https://www.tourism.gov.np/files/statistics/8.pdf
- **Status:** VERIFIED as a regulated mountaineering objective/approach; current permit operations pending live verification.

# Batch status
- **Canonical entries covered:** 6–10
- **Rasuwa cumulative:** 10 / 34 researched/dispositioned
- **Next canonical entries:** 11. Gosainkunda Lake; 12. Gosainkunda lake system; 13. Saraswati Kunda; 14. Bhairav Kunda, Rasuwa; 15. Surya Kunda.
# Chitwan Deep Research Completion Checkpoint — 2026-08-12

> Deep-research checkpoint for all 14 canonical Chitwan inventory entries. Dynamic fees, park regulations, operators, trail/road conditions and exact visitor-entrance GIS geometry remain current-data tasks.

## 1. Chitwan National Park
- **Status:** VERY STRONG PASS.
- **Model:** Protected-area polygon with separate verified gateways and visitor facilities; never one generic pin.
- **Visitor nodes:** Park material identifies gates/facilities including Sauraha, Kasara, Patihani/Ghatgain, Meghauli/Bhimle and visitor/conservation facilities.
- **Rule:** Park fees, activities and regulations are dynamic.
- **Primary source:** https://chitwannationalpark.gov.np/

## 2. Bish Hajari birdwatching forests
- **Status:** PASS after refinement.
- **Canonical refinement:** `Barandabhar–Beeshazar forest and birdwatching landscape`.
- **Relationship:** Keep separate from entry 4: this record represents the surrounding forest/birdwatching landscape, while entry 4 represents the Ramsar wetland complex.
- **Primary sources:** https://rsis.ramsar.org/ ; https://www.ramsar.org/

## 3. Sauraha
- **Status:** VERY STRONG PASS.
- **Municipality:** Ratnanagar Municipality.
- **Model:** Tourism town / eastern park gateway / accommodation-activity hub. Do not equate Sauraha with Chitwan National Park itself.
- **Primary source:** https://chitwannationalpark.gov.np/

## 4. Beeshazar and Associated Lakes
- **Status:** VERY STRONG PASS.
- **Model:** Ramsar wetland complex / conservation landscape.
- **Ramsar context:** Internationally designated wetland complex in the Chitwan National Park buffer-zone landscape.
- **GIS rule:** Ramsar reference coordinates are not visitor-entrance pins.
- **Aliases:** Preserve Beeshazar/Bish Hazari/Bish Hajari variants for search.
- **Primary source:** https://rsis.ramsar.org/

## 5. Narayani River waterfront
- **Status:** STRONG PASS.
- **Canonical refinement:** `Narayani River waterfront, Bharatpur–Narayangarh`.
- **Model:** Urban riverfront/linear recreation landscape with separate ghats, promenades, viewpoints and regulated boating nodes.
- **Primary source:** https://bharatpurmun.gov.np/

## 6. Rapti River wildlife corridor
- **Status:** STRONG PASS as landscape.
- **Model:** River/wildlife-edge corridor; canoe launches, ghats and viewpoints require separate verified nodes.
- **Safety:** Wildlife and water-risk context must remain explicit.
- **Primary protected-area context:** https://chitwannationalpark.gov.np/

## 7. Jalbire Waterfall
- **Status:** PASS for identity; PARTIAL for current operations.
- **Municipality / area:** Ichchhakamana Rural Municipality area.
- **Model:** Waterfall/adventure site.
- **Rule:** Current canyoning/swimming operations, fees, access and safety require live verification before publication.

## 8. Devghat
- **Status:** VERY STRONG PASS.
- **Model:** Cross-district pilgrimage destination shared with the Tanahun side; use one primary Devghat destination object rather than duplicate full pages by district.
- **Primary sources:** https://ntb.gov.np/en/devghat ; https://devghatmun.gov.np/

## 9. Balmiki Ashram approach
- **Status:** PASS after refinement.
- **Canonical correction:** Primary destination should be `Balmiki Ashram`; the approach/access route belongs in navigation data rather than being the attraction itself.
- **Access:** Current route geometry/conditions remain verification tasks.
- **Primary tourism context:** https://trade.ntb.gov.np/ ; https://www.exploremadi.org/

## 10. Chepang Hill Trail
- **Status:** VERY STRONG PASS.
- **Model:** Cross-district route object. Nepal Tourism Board describes the trail between Hugdi and Shaktikhor and identifies intermediate hill/community points.
- **Rule:** Exact GPX, active homestays and current trail conditions remain separate current/GIS fields.
- **Primary source:** https://ntb.gov.np/en/chepang-hill-trail

## 11. Siraichuli viewpoint
- **Status:** VERY STRONG PASS.
- **Relationship:** Link as a viewpoint/hill destination on the Chepang Hill Trail rather than an isolated generic pin.
- **Primary source:** https://ntb.gov.np/en/chepang-hill-trail

## 12. Upper Dang Gadhi
- **Status:** VERY STRONG PASS.
- **Alias normalization:** Preserve `Uppardang Gadi`, `Uppardang Gadhi`, and `Upper Dang Gadhi` for search.
- **Model:** Historic fort / former administrative center / viewpoint.
- **Primary source:** https://ntb.gov.np/en/chepang-hill-trail

## 13. Meghauli wildlife tourism area
- **Status:** VERY STRONG PASS.
- **Canonical refinement:** `Meghauli wildlife-tourism gateway/cluster`.
- **Model:** Western Chitwan National Park gateway linked to community forests, river landscapes, cultural experiences and verified park entrances.
- **Primary sources:** https://ntb.gov.np/en/meghauli ; https://chitwannationalpark.gov.np/

## 14. Madi valley and Someshwar hills
- **Status:** STRONG PASS after conceptual split.
- **Model:** Separate `Madi Valley` destination/landscape hub from `Someshwar hills/range`; `Someshwor Temple` should be a separate religious POI when individually verified.
- **Primary sources:** https://madimunchitwan.gov.np/ ; https://www.exploremadi.org/

# District QA disposition

- **Canonical inventory:** 14 / 14 researched/dispositioned.
- Separate the Barandabhar forest/birdwatching landscape from the Beeshazar Ramsar wetland complex.
- Treat Chitwan National Park, Beeshazar, Narayani waterfront and Rapti corridor as area/linear objects rather than arbitrary pins.
- Treat Devghat and Chepang Hill Trail as cross-district objects.
- Correct `Balmiki Ashram approach` so Balmiki Ashram is the destination and access is route data.
- Normalize Uppardang Gadi spelling aliases.
- Model Meghauli as a gateway/cluster.
- Split the Madi Valley/Someshwar composite concept into proper landscape and POI layers.
- Keep Jalbire adventure operations, park fees/regulations, canoe/boating access, operators and trail conditions as current-data fields.
- No unverified coordinate should be published as exact and no dynamic operation should be presented as permanent.

# Chitwan research status

**14 / 14 canonical entries researched + district QA complete.**

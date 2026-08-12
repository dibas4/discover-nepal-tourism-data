# Koshi Province Deep Research Completion Checkpoint — 2026-08-12

## Scope
Koshi Province canonical tourism inventory deep-research pass is complete across all 14 districts.

**Total canonical records dispositioned: 302 / 302**

This completion level means every canonical record has received a research disposition and district QA decision. It does **not** mean every coordinate, fee, opening hour, road condition, permit, operator, image or facility status is permanently verified. Those remain separate GIS/current-operations/media enrichment layers.

## District checkpoints
| District | Canonical records | Research branch | Completion commit |
|---|---:|---|---|
| Bhojpur | 30 | `research/bhojpur-deep-research` | `9543e131354aa19d2b0ad12522e1174fc3839d87` |
| Dhankuta | 26 | `research/dhankuta-deep-research` | `fd5ed2308f86cda51a36c4147ca7ef9ed76b362d` |
| Ilam | 37 | `research/ilam-deep-research` | `b00014a19e7750e675c3ae5d51faf55d38626a3b` |
| Jhapa | 23 | `research/jhapa-deep-research` | `e213dcdb81a27d27d8aa3a3a76d6553b6db1c42e` |
| Khotang | 19 | `research/khotang-deep-research` | `9f6cb8992c9bb96f8a5f8b853dd7cca2ba34325c` |
| Morang | 17 | `research/morang-deep-research` | `b7d7c26cfb94bb50226fc299b9ca03b542499b29` |
| Okhaldhunga | 14 | `research/okhaldhunga-deep-research` | `8c7f48891558336f5c77785cd79d07d4fce52ae6` |
| Panchthar | 18 | `research/panchthar-deep-research` | `599190eafb72553aa8899461fa4b446b6eae761a` |
| Sankhuwasabha | 18 | `research/sankhuwasabha-deep-research` | `331b3caef2b48c110e90881f24e3af831dd13799` |
| Solukhumbu | 34 | `research/solukhumbu-deep-research` | `cb71906990c3cbe8f03a488b633f70e6a932f3f0` |
| Sunsari | 18 | `research/sunsari-deep-research` | `42a02ed2ed6ca74c95487555ee77c7b42814dd73` |
| Taplejung | 21 | `research/taplejung-deep-research` | `19145bf9d4a4ffdaf9b68b447329cecdbcf0a622` |
| Tehrathum | 13 | `research/tehrathum-deep-research` | `ada76f89a46610acb2fe3b21936025ea3be6224c` |
| Udayapur | 14 | `research/udayapur-deep-research` | `e2c4973386138678e81594da6cff52d05fc1b6eb` |

## Province-wide QA rules applied
- Official/primary sources are preferred: Nepal Tourism Board, DNPWC/protected-area offices, municipalities/rural municipalities and other government heritage/tourism sources.
- Records are explicitly allowed to remain `PARTIAL`, `HOLD`, `CURRENT CHECK`, `DEVELOPING` or `CORRECTION` when evidence is insufficient.
- No guessed coordinates are promoted as verified.
- River corridors, wetlands, valleys, protected areas, ridge systems and trekking routes are modeled as area/linear/route objects rather than arbitrary single pins.
- Settlement/gateway records are kept separate from child temples, museums, viewpoints, monasteries, parks and transport facilities.
- Cross-district landscapes such as Tinjure–Milke–Jaljale, Mundhum Trail and protected/wetland systems are not duplicated as independent full destinations in every district.
- Trekking guides/TIMS, protected-area entry, climbing permits, border permissions, fees, hours, flight schedules, road/trail closures and operator availability are treated as dynamic/current data.
- Religious and Indigenous/Kirat/Limbu/Sherpa cultural narratives are attributed as living belief/tradition rather than converted into unsupported archaeological fact.
- Waterfalls, caves, cliffs, glaciers, high passes and river destinations carry explicit safety/current-access requirements.

## Important corrections / deduplication flags
1. **Udayapur — `Koshi Tappu Wildlife Reserve – Udayapur section`: HOLD/CORRECTION.** Current DNPWC material describes the reserve itself in Sunsari and Saptari. Do not publish an Udayapur reserve section without official boundary GIS evidence. The broader Belaka/Sapta Koshi floodplain landscape remains valid.
2. **Ilam — `Siddhithumka Chuli` vs `Siddhi Thumka`: deduplication/name-normalization review required** before separate CMS pages.
3. **Khotang — Halesi Cave Complex / Halesi Mahadev / Maratika:** retain one parent sacred complex with separate religious nodes, avoiding duplicate destination copy.
4. **Sunsari — Vijayapur Hill:** use as parent historic/religious landscape linking Budhasubba, Dantakali, Pindeshwar and Vijayapur Gadhi.
5. **Taplejung/Sankhuwasabha/Tehrathum — Tinjure–Milke–Jaljale:** one cross-district corridor object.
6. **Bhojpur and adjoining districts — Mundhum Trail:** one cross-district trekking/cultural route with stage destinations, not separate duplicate trails.
7. **High Himalaya:** mountains/technical expedition features such as Everest, Makalu, Kanchenjunga, Khumbu Icefall and climbing peaks are not modeled as ordinary sightseeing POIs.

## Completion statement
**Koshi deep research: COMPLETE — 14 / 14 districts, 302 / 302 canonical records dispositioned and district-QA’d.**

Next possible layer: merge/integrate these research sidecars into a consolidated master enrichment dataset, or proceed to the next province using the same large-pass workflow.
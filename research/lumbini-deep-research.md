# Lumbini Province Deep Research Completion Checkpoint

Status: COMPLETE for province-wide deep-research + district-QA phase.

## Province coverage

12 districts, 277 canonical research objects dispositioned.

- Arghakhanchi — 24 — research/arghakhanchi-deep-research — QA complete
- Banke — 25 — research/banke-deep-research — QA complete
- Bardiya — 30 — research/bardiya-deep-research — QA complete
- Dang — 30 — research/dang-deep-research — QA complete
- Eastern Rukum — 26 — research/eastern-rukum-deep-research — QA complete
- Gulmi — 25 — research/gulmi-deep-research — QA complete
- Pyuthan — 23 — research/pyuthan-deep-research — QA complete
- Rolpa — 28 — research/rolpa-deep-research — QA complete
- Kapilvastu — 14 — research/kapilvastu-deep-research — rebuilt missing inventory + QA complete
- Rupandehi — 24 — research/rupandehi-deep-research — rebuilt missing inventory + QA complete
- Nawalparasi (Bardaghat Susta West / Parasi) — 10 — research/nawalparasi-west-deep-research — rebuilt missing inventory + QA complete
- Palpa — 18 — research/palpa-deep-research — rebuilt missing inventory + QA complete

Total: 277

## Important repository finding

At the start of this pass, `provinces/lumbini/districts/` on `main` contained only eight district inventory files: Arghakhanchi, Banke, Bardiya, Dang, Eastern Rukum, Gulmi, Pyuthan and Rolpa. Kapilvastu, Rupandehi, Nawalparasi West and Palpa were absent. Their research inventories were therefore rebuilt on dedicated research branches from authoritative sources rather than being falsely marked complete.

## Province-level QA rules

- Lumbini is the UNESCO World Heritage parent landscape; Sacred Garden, Maya Devi Temple, Ashoka Pillar, Puskarini, monastic zones and other components are linked child objects.
- Greater Lumbini is a cross-district Buddhist heritage/pilgrimage route covering Rupandehi, Kapilvastu and Nawalparasi; do not duplicate it as a single attraction in each district.
- Tilaurakot, Kudan, Gotihawa, Niglihawa, Sagarhawa, Araurakot and Sisaniya are separate Kapilvastu archaeological nodes.
- Devdaha is a parent Koliya heritage landscape with Bhawanipur, Kanyamai, Bairimai, Khayardada and associated wetlands/river context as child nodes.
- Ramagrama Stupa is the canonical Nawalparasi sacred archaeological POI; Panditpur is a separate Koliya archaeological node.
- Tansen is the Palpa heritage-town parent; Rani Mahal, Shreenagar and major temples/craft clusters remain distinct.
- Banke and Bardiya national parks are protected-area parent objects; safari zones, gates, buffer communities and wildlife activities are child/current-operation records.
- Dhorpatan, Ruru/Ridi, major rivers, Chure belts and other cross-district landscapes are modeled as shared entities.
- Fees, hours, park/safari operations, road/landslide status, border procedures, flights, festival dates, homestays and commercial services are dynamic fields.
- Small wetlands, caves, fort remains, generic viewpoints and community-tourism clusters remain PARTIAL/HOLD where current authority/GIS evidence is insufficient.
- No guessed coordinates or wildlife-sighting guarantees are treated as verified.

## Authoritative anchors used

- UNESCO World Heritage Centre: Lumbini, Birthplace of the Lord Buddha; Tentative List context for Tilaurakot and Ramagrama.
- Government of Nepal / Lumbini Development Trust: Greater Lumbini Area, Lumbini, Devdaha, Ramagrama, Kapilvastu archaeological sites.
- Nepal Tourism Board: Tansen/Palpa, Bageshwari/Banke, Swargadwari/Pyuthan and national pilgrimage references.
- Department of National Parks and Wildlife Conservation: Banke National Park and Bardiya protected-area management sources.

This checkpoint completes the research/QA layer only. Integration into `main`, exact GIS geometry, media rights/attribution, and current-operation refreshes remain separate downstream work.

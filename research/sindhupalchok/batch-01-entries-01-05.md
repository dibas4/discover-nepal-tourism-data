# Sindhupalchok Deep Research — Batch 01 (Entries 1–5)

Branch: `research/sindhupalchok-deep-research`
Canonical inventory: `provinces/bagmati/districts/sindhupalchok.md`
Coverage: entries 1–5 of 31

## 1. Helambu trekking region

**Disposition:** ESTABLISHED — retain as a regional trekking product.

- Nepal Tourism Board describes Helambu as a scenic highland destination in Sindhupalchok extending from the Lauribina La area toward the Melamchi valley and accessible by trekking approaches from around Kathmandu.
- Langtang National Park tourism material identifies Helambu as one of the park region's three principal trekking routes/areas and notes locally operated teahouses, hotels and campsites along trekking routes.
- NTB's current TIMS guidance explicitly lists the Helambu Trek under the Helambu Region.

**Planner treatment:** regional route/landscape object, not a single POI. Trail geometry, weather, landslide condition, accommodation availability and permit/TIMS rules must be treated as dynamic operational fields.

**Sources:** Nepal Tourism Board Bagmati Province; Nepal Tourism Board Langtang/Natural Treasures; Nepal Tourism Board TIMS Card guidance.

## 2. Tarkeghyang Village

**Disposition:** ESTABLISHED — retain as a distinct Helambu cultural village.

- Nepal Tourism Board material identifies Tarkeghyang among the significant cultural sites of the Langtang/Helambu landscape.
- NTB rural-tourism material describes a gompa on the ridge above Tarkeghyang with Himalayan views toward Ganja La, Dorje Lakpa and surrounding peaks.
- Keep the settlement record separate from any monastery/gompa sub-record until a later site-level pass verifies formal monastery names, exact coordinates and access.

**Planner treatment:** village/cultural stop on Helambu itineraries; do not invent a single attraction pin for the whole settlement.

## 3. Sermathang Village

**Disposition:** ESTABLISHED — retain as a distinct Helambu cultural village.

- Nepal Tourism Board's Langtang National Park material lists Shermathang/Sermathang among cultural sites worth visiting in the wider protected-area/Helambu landscape.
- The canonical record's role as a scenic Yolmo settlement and trekking stop is consistent with established Helambu route structure.
- Spelling variants should be normalized as aliases (`Sermathang`, `Shermathang`) rather than duplicated.

**Planner treatment:** village/cultural trekking stop. Current lodging, road access and individual monastery details remain dynamic/local-verification fields.

## 4. Melamchi Ghyang

**Disposition:** ESTABLISHED — retain as a historic Helambu settlement/monastery area.

- NTB protected-area material lists Melamchighyang among significant cultural sites.
- NTB rural-tourism material describes Melamchigaun above a tributary of the Melamchi Khola, with stone houses, terraced fields and an old gompa.
- Normalize spelling variants such as `Melamchi Ghyang`, `Melamchighyang`, and `Melamchigaun` cautiously; do not automatically merge unrelated modern administrative labels without local GIS confirmation.

**Planner treatment:** settlement + cultural/monastery area; exact gompa geometry should wait for site-level verification.

## 5. Ama Yangri

**Disposition:** ESTABLISHED AS A MAJOR HELAMBU RIDGE/PILGRIMAGE DESTINATION; precise route geometry requires local/GIS verification.

- Ama Yangri is retained as a high ridge/pilgrimage/viewpoint destination above the Helambu settlements and as a distinct excursion from the village records.
- The broader Helambu region and its Himalayan ridge trekking context are strongly established by Nepal Tourism Board sources.
- This pass does not hard-code an exact summit elevation, trailhead, trail geometry, shrine coordinates, or current road approach because sufficiently strong first-party site-level evidence was not recovered for those precise fields.

**Planner treatment:** hiking/pilgrimage viewpoint object. Require local/GIS confirmation for exact summit pin and route; weather and trail status are dynamic.

## Batch QA / modeling decisions

- Entries researched/dispositioned after this batch: **5/31**.
- Helambu remains a region/trek product while Tarkeghyang, Sermathang and Melamchi Ghyang remain distinct settlement records.
- Individual monasteries inside the villages are not split into separate POIs until formal names and exact sites are verified.
- `Sermathang` / `Shermathang` and Melamchi Ghyang spelling variants should be handled through aliases to prevent duplicates.
- Ama Yangri is retained but exact elevation/route claims are withheld pending stronger site-level evidence.
- Current TIMS/guide requirements, permits, trail condition, road access, lodging and weather belong in the operational layer rather than being frozen into static destination research.

## Next batch

Entries 6–10: Palchok Bhagwati Temple → Larke Ghyang religious area → Panch Pokhari → Panch Pokhari trekking route → Bhotang Village.

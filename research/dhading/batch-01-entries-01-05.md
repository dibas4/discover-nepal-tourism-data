# Dhading Deep Research — Batch 01 (Entries 1–5)

Branch: `research/dhading-deep-research`
Canonical inventory: `provinces/bagmati/districts/dhading.md`
Coverage: entries 1–5 of 31

## 1. Ruby Valley trekking region

**Disposition:** ESTABLISHED — retain as a regional trekking/cultural destination.

- Nepal Tourism Board identifies Ruby Valley in Dhading as a trekking destination known for Tamang and Gurung culture, ruby/mineral associations, herbs, shaman traditions and varied trekking landscapes.
- Government Film Development Board material describes the Ruby Valley circuit through Somdang, Pangsang Bhanjyang, Tipling, Chalish, Hindung/Ganesh Himal Base Camp, Borang and Jharlang.
- The region should be modeled as a broad trekking product, not pinned to one arbitrary village coordinate.
- Accommodation and road/trail conditions vary strongly by segment and should remain dynamic fields.

**Planner treatment:** multi-day trekking region with route segments and village child records.

**Sources:**
- Nepal Tourism Board, Bagmati Province: https://ntb.gov.np/en/bagmati-province
- Film Development Board Nepal, Ruby Valley: https://film.gov.np/destination/12

## 2. Ganesh Himal trekking region

**Disposition:** ESTABLISHED — retain as a mountain trekking landscape overlapping the Ruby Valley product.

- Nepal Tourism Board maintains a dedicated Ganesh Himal Trek product and describes the route through the Ruby Valley landscape.
- NTB identifies Pangsang Kharka/Pass on the Rasuwa–Dhading boundary and Tipling as a principal village stage.
- Government Film Development Board material also identifies Ganesh Himal Base Camp as an extension from the Ruby Valley circuit, reached from Hindung.
- Do not model technical Ganesh Himal summits as ordinary POIs; this record represents the trekking region/approach landscape.

**Planner treatment:** trekking-region parent record; technical peak/climbing data belongs in a regulated mountaineering layer.

**Sources:**
- Nepal Tourism Board, Ganesh Himal Trek: https://ntb.gov.np/plan-your-trip/trip-ideas/ganesh-himal-trek
- Film Development Board Nepal, Ruby Valley: https://film.gov.np/destination/12

## 3. Pangsang Pass

**Disposition:** ESTABLISHED — high ridge/pass and viewpoint.

- Ruby Valley Rural Municipality's tourism publication places Pangsang Pass in Ruby Valley Ward 1, Dhading, at about 3,850 m and describes access via Somdang/Rasuwa and Dhading-side routes.
- The municipality identifies views of Ganesh Himal, Annapurna, Manaslu, Paldor and Langtang and notes the area's seasonal pasture and ruby-crystal associations.
- Government Film Development Board material likewise gives about 3,850 m for Pangsang Bhanjyang and places it on the Ruby Valley circuit.
- NTB's Ganesh Himal itinerary gives a higher figure for Pangsang Kharka on its route; because published elevations vary, the website should avoid false single-meter precision until authoritative GIS/topographic validation.

**Planner treatment:** pass/viewpoint; elevation displayed as approximate pending GIS QA; weather/snow exposure warning required.

**Sources:**
- Ruby Valley Rural Municipality tourism publication: https://rubivalleymun.gov.np/sites/rubivalleymun.gov.np/files/Book_Final_0.pdf
- Film Development Board Nepal, Ruby Valley: https://film.gov.np/destination/12
- Nepal Tourism Board, Ganesh Himal Trek: https://ntb.gov.np/plan-your-trip/trip-ideas/ganesh-himal-trek

## 4. Somdang Village

**Disposition:** ESTABLISHED AS TREKKING STAGE — retain, with boundary/access nuance.

- Government tourism material uses Somdang as the northern starting/staging point for the Ruby Valley circuit, followed by Pangsang Bhanjyang and Tipling.
- NTB's Ganesh Himal trek describes the Somdang valley/camp area before the climb toward Pangsang.
- Government electricity-development records for Somdang Khola reference Tipling (Dhading) and Gatlang (Rasuwa), reinforcing that this is a boundary landscape where careless district pinning can be misleading.
- Treat the visitor record as the established Somdang trekking settlement/stage and verify its exact administrative point/ward through GIS/local records before publishing a precise district-level pin.

**Planner treatment:** trekking stage/gateway; exact administrative coordinate flagged for GIS verification.

**Sources:**
- Film Development Board Nepal, Ruby Valley: https://film.gov.np/destination/12
- Nepal Tourism Board, Ganesh Himal Trek: https://ntb.gov.np/plan-your-trip/trip-ideas/ganesh-himal-trek
- Department of Electricity Development records, Somdang Khola HPP location context: https://doed.gov.np/pages/canceled_hydro/

## 5. Tipling Village

**Disposition:** ESTABLISHED — retain as a major Tamang cultural/trekking village.

- NTB describes Tipling as an old village inhabited mostly by Tamang people and a principal stage of the Ganesh Himal trek.
- Government Film Development Board material places Tipling directly on the Ruby Valley circuit.
- Government procurement documentation explicitly locates Tipling Health Post in Ruby Valley Rural Municipality, Dhading District, providing administrative confirmation.
- Current homestay/lodge inventory should not be assumed from historical trekking descriptions; accommodation availability needs local/current verification.

**Planner treatment:** community/cultural trekking destination; verify live lodging inventory separately.

**Sources:**
- Nepal Tourism Board, Ganesh Himal Trek: https://ntb.gov.np/plan-your-trip/trip-ideas/ganesh-himal-trek
- Film Development Board Nepal, Ruby Valley: https://film.gov.np/destination/12
- Government of Nepal e-GP / Tipling Health Post documentation: https://bolpatra.gov.np/egp/

## Batch QA / modeling decisions

- Entries researched/dispositioned after this batch: **5/31**.
- Ruby Valley and Ganesh Himal remain regional trekking objects rather than duplicate point POIs.
- Pangsang elevation is marked approximate because official/official-adjacent sources report differing values.
- Somdang requires exact boundary/GIS verification before a precise administrative pin is published.
- Tipling's cultural/route identity is strong, but live accommodation remains a dynamic verification field.
- Nepal Tourism Board currently lists **Ganesh Himal–Ruby Valley Trek** among routes for which trekkers should check applicable guide/TIMS requirements; permit/TIMS rules must be sourced dynamically rather than frozen into the destination record.

## Next batch

Entries 6–10: Sertung Village; Chalish Village; Borang Village; Lapa Village; Jharlang Village.

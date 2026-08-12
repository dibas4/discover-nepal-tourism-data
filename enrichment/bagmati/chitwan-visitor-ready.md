# Chitwan Visitor-Ready Tourism Enrichment

Status: first visitor-ready enrichment pass

## District introduction

Chitwan is an Inner Terai district of south-central Nepal where subtropical forest, grassland, wetlands, the Rapti and Narayani river systems, Tharu communities, pilgrimage landscapes and the Mahabharat foothills meet. Its strongest tourism identity is Chitwan National Park, but the district also includes Sauraha and Meghauli wildlife gateways, Bharatpur/Narayangarh urban riverfronts, Devghat pilgrimage, Beeshazar wetlands, Madi Valley and the Chepang hill country.

## Short history

The Chitwan valley was historically a forested, malaria-prone Inner Terai landscape with long-established Indigenous communities, especially Tharu settlements. Nepal created Chitwan National Park in 1973 as the country's first national park; the protected area later became a UNESCO World Heritage Site. Modern roads, migration and the growth of Bharatpur transformed the district into a major transport and commercial centre while conservation and community tourism developed around the park. Older layers remain visible at Devghat, Uppardang Gadi and the Chepang hill settlements.

## Mapping rules for Chitwan

- Large settlement or tourism zone: use an approximate centre plus an area radius/polygon.
- National park, wetland complex, valley or forest: polygon/area object; never a single visitor pin.
- River: corridor/polyline.
- Trail: route/polyline with start/end and intermediate nodes.
- Museum, temple, visitor centre, gate, fort or cave entrance: point POI when coordinates are verified.
- Current fees, safari operators, boating availability, opening hours and trail conditions remain dynamic fields.

## Main visitor areas and places

### Sauraha

**Type:** tourism settlement / wildlife gateway  
**Map geometry:** area  
**Approximate centre:** 27.5802, 84.5023  
**Suggested first-pass radius:** ~2.0 km  

Sauraha is the best-known tourism settlement on the eastern edge of Chitwan National Park. It is the main concentration of accommodation, restaurants, safari services, riverside activity and visitor information for the eastern park gateway.

**Things to do tied to locations**
- Rapti riverside sunset and wildlife viewing -> Sauraha riverfront area.
- Park entry / ticketing -> Sauraha park gateway and official visitor/ticket offices.
- Learn about wildlife and conservation -> Chitwan National Park Visitor Center, Sauraha.
- Learn about Tharu culture -> Tharu Cultural Museum and verified cultural programmes.
- Canoe activities -> verified departure points on the Rapti; current operator/season must be checked.

#### Chitwan National Park official visitor/ticket area, Sauraha
**Type:** visitor/ticket facility  
**Map geometry:** point  
**Approximate mapped coordinate:** 27.57391, 84.49533  
**Coordinate status:** mapped POI; field/official GIS recheck recommended  

Visitor-facing park information and ticketing area associated with the Sauraha gateway. Use this as a practical navigation node, not as the coordinate for the entire national park.

#### Tharu Cultural Museum, Sauraha/Bachhauli
**Type:** museum  
**Map geometry:** point  
**Approximate mapped coordinate:** 27.58144, 84.50849  
**Coordinate status:** mapped POI; duplicate map nodes need final GIS reconciliation  

A local museum focused on Tharu material culture and community heritage. It is useful for visitors who want context on traditional tools, household life, clothing, customs and the local Tharu cultural landscape rather than only a wildlife experience.

### Chitwan National Park

**Type:** protected landscape  
**Map geometry:** polygon  
**Do not use:** one centre pin as the visitor destination  

Nepal's first national park and the district's primary wildlife destination. The park protects subtropical sal forest, grasslands, riverine habitats and important populations of one-horned rhinoceros, Bengal tiger, crocodilians and many bird species.

**Visitor nodes should be separate POIs:**
- Sauraha gate via Tandi/Ratnanagar
- Kasara headquarters/gateway
- Ghatgain via Patihani
- Bhimle via Meghauli
- other officially listed gates
- Gharial Breeding Center near Kasara
- park museum at Kasara
- Elephant Breeding Center at Khorsor

**Things to do:** jungle drives, permitted jungle walks, wildlife observation, birdwatching, canoeing where operated, conservation interpretation and buffer-zone cultural experiences. Each activity must resolve to an operating gateway/launch point rather than the park polygon itself.

### Meghauli

**Type:** tourism settlement / western wildlife gateway  
**Map geometry:** area  
**Approximate centre:** 27.5812, 84.2349  
**Suggested first-pass radius:** ~3 km  

Meghauli is a western gateway to Chitwan National Park on the Rapti-Narayani landscape. It is quieter and more spread out than Sauraha, with community-forest access, wildlife tourism, birdwatching, Tharu cultural experiences and river sunsets.

**Things to do tied to locations**
- Wildlife/birdwatching -> verified community forest and park gateway nodes.
- Tharu cultural experience -> verified village/homestay locations.
- Sunset -> Golaghat/Golghat river-confluence area after exact GIS verification.

#### Meghauli Community Forest entrance
**Type:** park/community-forest access node  
**Map geometry:** point  
**Approximate mapped coordinate:** 27.57471, 84.21994  
**Coordinate status:** mapped POI; management/access status needs current check  

A practical access node for the community-forest side of the Meghauli tourism landscape. It should not be confused with a Chitwan National Park entrance unless current authority signage confirms that function.

### Beeshazar and Associated Lakes

**Type:** Ramsar wetland complex  
**Map geometry:** polygon/area  
**Coordinate style:** use Ramsar/site reference as an area reference, not visitor entrance  

Beeshazar is a wetland complex in the Chitwan buffer-zone landscape, surrounded by the Barandabhar forest system. It is valuable for birdwatching, wetland ecology and wildlife habitat.

**Things to do:** birdwatching, nature observation and wetland photography from verified public access routes. Do not publish one lake-centre pin as the entrance.

### Barandabhar-Beeshazar forest and birdwatching landscape

**Type:** forest/buffer-zone landscape  
**Map geometry:** polygon/area  

The forest surrounding the Beeshazar wetland system should be modeled separately from the Ramsar wetland itself. It provides the wider ecological and birdwatching setting rather than being treated as a duplicate 'Bish Hajari' attraction.

### Narayani River waterfront, Bharatpur-Narayangarh

**Type:** urban riverfront / river corridor  
**Map geometry:** line/area with verified access nodes  

The Narayani forms the western edge of Bharatpur/Narayangarh and is one of Chitwan's most important urban landscapes. Visitors use specific ghats, promenades and riverbank spaces for sunsets, festivals and recreation.

**Things to do:** riverside walking, sunset viewing, photography and seasonal cultural events at verified public-access sections. Boating/swimming must not be inferred from the river record itself.

### Rapti River - Sauraha / park-edge corridor

**Type:** river corridor  
**Map geometry:** polyline/river area  

The Rapti River forms a major scenic and ecological edge between tourism settlements and sections of Chitwan National Park. Around Sauraha it is central to sunsets, canoe departures and wildlife observation.

**Things to do:** riverside sunset, birdwatching, crocodile/wildlife observation and authorized canoe trips from verified departure nodes.

### Devghat pilgrimage landscape

**Type:** cross-district pilgrimage area  
**Map geometry:** area  
**Chitwan-side approximate centre:** 27.7392, 84.4254  
**Suggested first-pass radius:** ~1.5-2 km across the broader confluence landscape  

Devghat is a major Hindu pilgrimage landscape around the confluence where the Kali Gandaki and Trishuli systems form the Narayani. Temples, ashrams, ghats and religious institutions extend across both the Chitwan and Tanahun sides, so the destination must be a shared cross-district object rather than duplicated as unrelated places.

**Things to do:** visit temples and ashrams, observe the sacred river confluence, attend pilgrimage periods such as Makar Sankranti and use verified ghats. Individual temples and ghats should receive separate pins.

### Jalbire Waterfall

**Type:** waterfall / adventure site  
**Map geometry:** point plus approach trail/road if verified  
**Coordinate status:** exact public-access POI still requires GIS verification  

A waterfall in Ichchhakamana Rural Municipality known for its dramatic rock-and-water setting and adventure use. Canyoning and swimming conditions must be treated as current/safety-sensitive activities rather than guaranteed features.

### Balmiki Ashram

**Type:** religious/heritage destination  
**Map geometry:** point/compound once exact entrance is verified  

A forest pilgrimage site associated with the Ramayana tradition and sage Valmiki/Balmiki, located in the southwestern protected landscape near the Tribeni river system. The destination is the ashram itself; its access route should be modeled separately as navigation data.

### Chepang Hill Trail

**Type:** cross-district trekking route  
**Map geometry:** polyline  
**Primary endpoints:** Hugdi (Dhading side) <-> Shaktikhor (Chitwan side)  

A cultural hill trail linking Chepang and other mid-hill communities with forest walking, village stays, birdwatching and Himalayan viewpoints. Important nodes include Hattibang, Siraichuli, Jyandala, Chisapanitar and Uppardang Gadi.

### Siraichuli

**Type:** hill viewpoint  
**Map geometry:** point/summit plus trail access  

One of the high points on the Chepang Hill Trail, known for sunrise/sunset and broad Himalayan views. Because the approach is a trekking route, the map should pair the summit/viewpoint POI with its trail connection rather than route drivers directly to the summit.

### Uppardang Gadi

**Aliases:** Uppardang Gadi, Uppardang Gadhi, Upper Dang Gadhi  
**Type:** historic fort / viewpoint  
**Map geometry:** point/fort area  

A historic hill fort on the Chepang Hill Trail landscape and the former headquarters area of Chitwan. The visitor value combines surviving fort remains, historic context and hill views. Exact fort footprint and approach path still require GIS verification.

### Madi Valley

**Type:** valley / destination region  
**Map geometry:** broad area/polygon  

Madi is a large valley south of the main Bharatpur-Sauraha urban corridor, bordered by protected forest and the Someshwar range. It should be treated as a destination region containing many separate religious, natural and community-tourism POIs rather than as one pin.

### Someshwar hills / range

**Type:** ridge/mountain landscape  
**Map geometry:** line/area  

The Someshwar hills form the southern highland edge of the Madi landscape. Individual trails, viewpoints and Someshwor religious sites should become child POIs only after access and coordinates are verified.

## District-wide things-to-do index

- **Wildlife safari:** route user to an operating Chitwan National Park gateway, not to the park centre.
- **Birdwatching:** Beeshazar/Barandabhar, Meghauli community-forest landscape, Rapti/Narayani wetlands, Chepang hill forest sites.
- **Canoeing:** only from verified current departure points on permitted river sections.
- **Tharu culture:** verified museums, villages, cultural centres and active homestays around Sauraha, Meghauli and other buffer-zone communities.
- **Hiking/trekking:** Chepang Hill Trail, Siraichuli/Uppardang Gadi connections, verified Madi/Someshwar routes.
- **Pilgrimage:** Devghat, Balmiki Ashram and verified Madi-area religious sites.
- **Waterfall/adventure:** Jalbire, with current safety/operator checks.
- **Urban riverfront:** Narayani waterfront at verified Bharatpur/Narayangarh public-access nodes.

## Sources used in this first pass

- Chitwan National Park official website: facilities, gateways, visitor nodes, regulations and park history.
- Nepal Tourism Board: Chitwan, Chitwan National Park, Meghauli, Devghat and Chepang Hill Trail destination pages.
- Bharatpur Metropolitan City: Bharatpur/Narayani urban context.
- Ramsar sources for Beeshazar and Associated Lakes.
- OpenStreetMap/GeoNames-derived map references for approximate locality centres and selected mapped POIs; all such coordinates are flagged for final GIS reconciliation rather than treated as authoritative survey coordinates.

## Next enrichment work

1. Add exact or area-centre coordinates for every remaining child POI.
2. Build verified boundaries/radii for Sauraha, Meghauli, Devghat and Madi.
3. Add specific Sauraha riverfront, canoe departure, park gateway, museum and cultural POIs.
4. Add Kasara, Gharial Breeding Center, park museum, Khorsor Elephant Breeding Center and verified gate coordinates.
5. Resolve Golaghat/Golghat spelling and exact confluence geometry.
6. Add Madi Valley child POIs rather than leaving Madi as one broad destination.
7. Add current access/season/safety fields separately from permanent place descriptions.

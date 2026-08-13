# Madhesh Province — Visitor-ready tourism enrichment

Status: COMPLETE PROVINCE PASS (8/8 districts)

Districts: Saptari, Siraha, Dhanusha, Mahottari, Sarlahi, Rautahat, Bara, Parsa.

This layer converts the completed district inventories into planner-ready tourism data. Required model for every canonical record:
- short visitor introduction and identity
- things to do tied to the actual site/area
- geometry: POINT for verified small POIs; AREA/POLYGON for settlements, wetlands, forests and heritage precincts; CORRIDOR/ROUTE for rivers and pilgrimage routes
- practical access from the nearest main hub
- permit/entry classification separated from ticket/operational fees
- dynamic flags for festivals, floods, wetlands, park operations, border procedures and road conditions
- ROUTING_HOLD wherever a precise entrance, public access point or current operating condition is not sufficiently verified

Province access model: Janakpurdham is the primary cultural/pilgrimage hub; Birgunj is the western gateway; East–West Highway towns provide east-west access; Indian-border gateways are treated as controlled transport nodes, not attractions with guaranteed crossing conditions.

Cross-district parent systems: Koshi Tappu/Saptakoshi floodplain; Kamala River; Bagmati/Nunthar; Mithila Madhya Parikrama; Parsa National Park; Chure forest belt. These must be represented once as parent systems and linked to district sectors rather than duplicated as unrelated attractions.

Permit policy: Madhesh has no blanket tourism permit. Protected-area entry (Parsa National Park, Koshi Tappu Wildlife Reserve sectors) is separate from ordinary district travel. Temple/festival/boating/safari charges are operational entry/service fees, not trekking permits. Border formalities are dynamic and nationality/document dependent.

Safety policy: river islands, sandbars, floodplains, Chure streams and wetlands are seasonal. Never route to a waterbody centroid, river midpoint, arbitrary forest coordinate or unverified archaeological point. Route to a verified public entrance/ghat/trailhead/roadside access node only.

District files in this directory carry the canonical record list and district-specific access/permit/geometry rules.
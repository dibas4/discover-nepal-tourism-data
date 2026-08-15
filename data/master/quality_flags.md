# Nepal Visitor-Ready Master — Quality Flags

## Publication rules

- `ROUTABLE`: visitor-ready enrichment matched the canonical place and no explicit hold was detected.
- `DYNAMIC_CHECK_REQUIRED`: route/operation data is usable only after a current check for roads, flights, borders, trail closures, tickets, operators or seasonal conditions.
- `ROUTING_HOLD`: keep the record searchable/content-visible but do not send a route planner to an unverified exact location.
- `HUB_ONLY`: route only to the nearest verified gateway until the final public access point is confirmed.

## Geometry rules

Exact `POINT` geometry is only for verified public POIs/entrances. Towns, villages, ridges and cultural landscapes use `AREA`; rivers and valleys use `CORRIDOR`; treks and pilgrimage systems use `ROUTE`; lakes/wetlands use `WATER`; parks/reserves/conservation areas use `PROTECTED_AREA`; uncertain access remains `HOLD`.

## Permit rules

Restricted-area permits, protected-area entry, climbing permits, normal entrance tickets, operator charges and border controls are separate layers. Never infer a district-wide permit from one restricted ward or protected sector.

## Dynamic fields

Do not publish as timeless facts: permit/entry prices, flights, helicopter services, road/bridge condition, border openings, trail closures, boating, rafting, safari, cable-car operation, festival dates, accommodation availability, snowfall/high-pass safety or community access.

## National validation gate

The generated master must fail validation unless it contains exactly **7 provinces, 77 districts and 1,892 canonical records**, and each province matches its integration checkpoint count.

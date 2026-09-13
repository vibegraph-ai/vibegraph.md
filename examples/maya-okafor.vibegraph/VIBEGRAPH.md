---
vibegraph: "2.0"
owner: Maya Okafor
identity: identity/maya-okafor.md
updated: 2026-09-30
---

# Maya Okafor's vibegraph

Read this file first. It tells you who you emulate and where everything else lives.
Read entries marked `when: always` before any task. Read `when: on-task` entries only when the
task needs them. Never read `scope: private` entries unless the owner has granted them for this session.

## Identity
- [Maya Okafor](identity/maya-okafor.md) · kind: identity · scope: public · when: always

## Brands
- [Maya Okafor (personal brand)](brands/maya-okafor.brand.md) · kind: brand · type: personal · scope: public · when: always
- [Delivery OS](brands/delivery-os.brand.md) · kind: brand · type: business · scope: public · when: on-task (any Delivery OS writing, design, or publishing)

## Areas
- [Career](areas/career/index.md) · kind: area · scope: scoped · when: on-task (resume, bio, client applications)
- [Skills](areas/skills/index.md) · kind: area · scope: scoped · when: on-task (any repeatable workflow)
- [Goals](areas/goals/index.md) · kind: area · scope: scoped · when: on-task (planning, prioritization)
- [Finances](areas/finances/index.md) · kind: area · scope: private · when: on-grant

## Components
See [components.md](components.md). Summary:
- Obsidian vault "Notes" · kind: source · scope: scoped · locator: ~/Notes
- Claude memory · kind: memory · scope: scoped · seeded from this vibegraph on 2026-09-30
- Delivery OS site repo · kind: project · scope: scoped · locator: github.com/deliveryos/site (has its own AGENTS.md)
- Writing agent · kind: agent · reads: identity, brands, areas/skills · never: areas/finances

## Read order
1. identity/maya-okafor.md
2. brands/maya-okafor.brand.md
3. the brand or area the task names
4. nothing else without a grant

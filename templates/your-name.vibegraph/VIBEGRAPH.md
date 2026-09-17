---
vibegraph: "3.0"
owner: Your Name
role: owner
identity: identity/your-name.md
updated: 2026-10-10
---

# Your Name's vibegraph

Read this file first. It tells you who you emulate and where everything else lives.
Read entries marked `when: always` before any task. Read `when: on-task` entries only when the
task needs them. Never read `scope: private` entries unless the owner has granted them for this session.
Context sources are where context lives; areas are what it is about, and an area's entries point into sources.

## Identity
- [Your Name](identity/your-name.md) · kind: identity · scope: public · when: always

## Brands
- [Your Name (personal brand)](brands/your-name.brand.md) · kind: brand · type: personal · scope: public · when: always
- [Your Business](brands/your-business.brand.md) · kind: brand · type: business · scope: public · when: on-task (any Your Business writing, design, or publishing)

## Context Sources
See [context-sources.md](context-sources.md). Summary:
- Notes app "Your vault" · kind: source · scope: scoped · locator: ~/Notes

## Areas
- [Career](areas/career/index.md) · kind: area · scope: scoped · when: on-task (resume, bio, applications)

## Read order
1. identity/your-name.md
2. brands/your-name.brand.md
3. the brand or area the task names
4. nothing else without a grant

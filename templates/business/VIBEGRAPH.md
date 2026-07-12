---
vibegraph_version: "1.0"
type: business
owner: "Your Company"
updated: "2026-01-01"
default_visibility: private
summary: >
  One paragraph a tool can read to orient itself: what the company does, who it serves,
  and the single most important thing about how the brand sounds. Replace this.
---

# Your Company — Vibegraph

> Replace this blockquote with a one- or two-sentence statement of what the company is.
> Example: "A boutique studio that helps B2B founders turn expertise into demand. This
> is our codified brand and operating context for use with AI tools and agents."

This is our **business vibegraph** — a structured, portable statement of our brand and
how we operate, for AI tools and agents to consume. Read this manifest first, then load
whatever the task needs.

## Core Identity — *who we are*  (visibility: public)

Safe to load in any interaction. Paste this into a chat to calibrate an AI to our brand.

- [`core/brand-personality.md`](core/brand-personality.md) — Aaker dimensions + archetype
- [`core/purpose.md`](core/purpose.md) — Why / How / What; mission, vision, values
- [`core/brand-positioning.md`](core/brand-positioning.md) — positioning, voice, messaging
- [`core/brand-design.md`](core/brand-design.md) — design system + templates

## Knowledge Base — *how we operate*

Private or scoped unless stated otherwise. These are the systems that make the business
repeatable — the material an operator or agent needs to produce consistent output.

- [`modules/playbooks.md`](modules/playbooks.md) — SOPs & playbooks *(visibility: scoped)*
- `modules/…` — add your own (CRM, finances, operations, goals, brand-templates…)

## How to use this vibegraph

1. **Calibrate any AI:** paste this file plus the four `core/` files into a chat, or
   attach them to a shared Project or custom GPT the team uses.
2. **Respect privacy:** `private` items (financials, customer data, internal ops) should
   never be shared with a tool. `scoped` items are for named agents only.
3. **Keep it current:** update the `updated` dates as the brand and operations evolve.

*Built with the open Vibegraph framework — https://vibegraph.md*

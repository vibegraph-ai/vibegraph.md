# Areas

Areas are the domains of knowledge and working context an owner adds when a real use case demands one. Each area is a folder with an `index.md` and its own scope, so it can be granted as a unit. Areas are where depth and sensitivity live, so they are scoped or private by default and stay home when the core travels.

This example registers three areas. Their content lives in Maya's Obsidian vault; each index lists its entries with a route to reach them.

## Add an area

1. Create `areas/<area-slug>/index.md`.
2. Give it front matter:

   ```yaml
   ---
   kind: area
   area: Health
   scope: private
   when: on-grant
   updated: 2026-10-10
   ---
   ```

3. In the body, say what the area covers.
4. Under `## Entries`, list each file, link, or location that holds the area's content, one line per entry: a `scope`, a `when`, and one `access`: `file` (a path), `link` (a URL), `mcp` (a named connector), or `ask` (ask the owner; nothing is stored). Add `in:` naming a context source's slug when the entry lives in one.
5. Add one line under `## Areas` in `VIBEGRAPH.md`:

   ```
   - [Health](areas/health/index.md) · kind: area · scope: private · when: on-grant
   ```

Suggested personal areas: Health, Relationships, Career, Money, Play, Time, Tech, Goals, Library. Suggested business areas: Finance, Relationships and CRM, Marketing, Content and Brand, Operations. `area:` is free text; an owner may name areas outside the list.

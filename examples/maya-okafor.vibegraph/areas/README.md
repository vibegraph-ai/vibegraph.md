# Areas

Areas are the domains of knowledge and working context an owner adds when a real use case demands one. Each area is a folder with an `index.md` and its own scope, so it can be granted as a unit. Areas are where depth and sensitivity live, so they are scoped or private by default and stay home when the core travels.

This example registers four areas. Their content lives in Maya's Obsidian vault; the index files say what belongs in each and where it is.

## Add an area

1. Create `areas/<area-slug>/index.md`.
2. Give it front matter:

   ```yaml
   ---
   kind: area
   area: Health
   scope: private
   when: on-grant
   updated: 2026-09-30
   ---
   ```

3. In the body, say what the area covers and link or locate its contents.
4. Add one line under `## Areas` in `VIBEGRAPH.md`:

   ```
   - [Health](areas/health/index.md) · kind: area · scope: private · when: on-grant
   ```

Suggested personal areas: career, skills, goals, finances, health, relationships, notes and ideas. Suggested business areas: relationships and CRM, operations, playbooks and SOPs, management routines, templates, goals.

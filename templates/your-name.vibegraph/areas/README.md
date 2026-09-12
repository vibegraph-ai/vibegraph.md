# Areas

Areas are the domains of knowledge and working context you add when a real use case demands one. Each area is a folder with an `index.md` and its own scope, so it can be granted as a unit. Areas are scoped or private by default and stay home when the core travels. Add one only when an agent actually needs it.

## Add an area

1. Create `areas/<area-slug>/index.md`.
2. Give it front matter:

   ```yaml
   ---
   kind: area
   area: Finances
   scope: private
   when: on-grant
   updated: 2026-09-30
   ---
   ```

3. In the body, say what the area covers and link or locate its contents.
4. Add one line under `## Areas` in `VIBEGRAPH.md`:

   ```
   - [Finances](areas/finances/index.md) · kind: area · scope: private · when: on-grant
   ```

Suggested personal areas: career, skills, goals, finances, health, relationships, notes and ideas. Suggested business areas: relationships and CRM, operations, playbooks and SOPs, management routines, templates, goals.

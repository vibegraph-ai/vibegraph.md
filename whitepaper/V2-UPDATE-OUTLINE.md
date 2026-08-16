# Vibegraph Whitepaper v1.5: Update Outline

Working outline for revising The-Vibegraph-Whitepaper-v1.0 (July 11, 2026).
v1.0 was written before the app existed. The build changed the structure, the
naming, the instruments, and several product claims. v1.5 brings the paper
back in line with what shipped, and upgrades "planned" language to "built"
language where the app now proves the framework. v2.0 follows after the
business builder lands, right before product launch, with Section 5 moved to
present tense.

Status: decisions resolved Aug 11 (Ryan) and folded in below. One open item:
the public name for the third part (see Section 8). Drafting can start
everywhere that name does not touch.

---

## 1. The headline structural change: three phases, not two parts

v1.0 describes a two-part architecture: Core Identity + Knowledge Base.
The app as built organizes the same material as a three-phase journey, and
v2.0 should present that as the canonical structure:

DECIDED (Ryan, Aug 11): a vibegraph has THREE parts.

| Part | Name | Contents |
|---|---|---|
| 1 | **Core Identity** | Personality (Big Five + Enneagram, one assessment in two complementary instruments, plus the integrated reading) + Ikigai |
| 2 | **Branding** | Brand Context (12 elements) + Brand Visuals (8 elements) |
| 3 | **Orbits** (DECIDED Aug 11; app renames from "Spheres" to follow) | The gated life/business deep-context part; v1.0's Knowledge Base concept intact. The name is the architecture: they revolve around the core, and they stay home when the core travels. |

The two-part philosophy (small shareable core, gated deep modules) is still
true and still the right story: parts 1 and 2 are the shareable core, part 3
is the gated depth. Only the presentation and names moved.

## 2. Global naming changes (apply everywhere, including diagrams)

| v1.0 term | v2.0 term | Source of truth |
|---|---|---|
| Brand Positioning | **Brand Context** | App section, 12 elements |
| Brand Aesthetics | **Brand Visuals** | App section, 8 elements |
| Knowledge Base | **Orbits** | Decided Aug 11; app rename to follow |
| "personality profile" (Big Five only) | **Personality** = Big Five + Enneagram + the integrated reading | App Identity phase |
| Ikigai 2.0 "the corrected framework (Kowalski)" | Ikigai grounded in the four-pillar structure, **inspired by** Kowalski's Ikigai 2.0 | Grounding decision: inspired, not adopted wholesale; talents not skills, money as byproduct |
| modules | orbits / elements as appropriate | |

Also standardize "element" as the unit inside a section (the app treats the
12 + 8 elements as first-class: each has its own guidance, examples, and
generation). v1.0 has no word for this level.

## 3. Section-by-section plan against v1.0

**Intro + Section 1 (The Problem): keep, light touch.**
Still accurate and the strongest writing in the paper. Update only the
frameworks list in the intro (add the Enneagram; fix the Ikigai attribution
phrasing) and refresh the AGENTS.md adoption number if a current one exists.

**Section 2 (What Is a Vibegraph) + Design Principles: keep, one addition.**
Add a design principle the app taught us: **guided, not blank** (structured
elicitation with an AI coach beats empty templates; the demo persona and
per-element examples exist because blank pages kill these documents).

**Section 3 (Architecture): rewrite.**
Present the three-phase structure from Section 1 of this outline. Keep the
"why the split matters" arguments; they transfer cleanly.

**Section 4 (The Personal Vibegraph): rewrite. Biggest section change.**
- 4.1 Personality: DECIDED framing (Ryan, Aug 11): one full personality
  assessment in two parts, the Big Five (IPIP-NEO-120) and the Enneagram,
  which assess personality with different methods of questioning; the
  integrated reading reconciles the two. The Enneagram does not appear
  anywhere in v1.0. Include the import fast-track (bring results from
  elsewhere) since it is a real adoption path.
- 4.2 Ikigai: the four pillars (what you love, what the world needs, what
  you are good at, what you can be paid for), the "where they meet"
  synthesis, and the Ikigai statement as the hero artifact. Fix attribution
  per Section 2 table.
- 4.3 Brand Context: name the actual 12 elements: Brand Name, Slogans &
  Taglines, Unique Value Proposition, Purpose-Vision-Mission, Core Values,
  Tone & Voice, Messaging & Narratives, Keywords & Phrases, Bio
  (Short/Long), Achievements & Awards, Inspiration & Influence, Online
  Presence.
- 4.4 Brand Visuals: name the actual 8: Symbols & Logos, Color Palette,
  Typography, Iconography, Brand Imagery, Illustration Style, Visual
  Elements, Photography. Keep v1.0's "concrete artifacts, not vague
  direction" framing; it is exactly how the app behaves (hex values, type
  pairings, a brand board).
- 4.5 Orbits: the v1.0 module table survives here nearly as-is, marked
  clearly as the extensible frontier rather than shipped surface.
- Update Figure 1 to match all of the above.

**Section 5 (The Business Vibegraph): revise and re-stage.**
The instrument-swap story (Aaker, archetypes, Golden Circle) remains the
design. But v1.0 reads as if it exists on equal footing with the personal
framework; as of today the business builder is sold (the Personal + Business
tier) and arriving, not shipped. v2.0 should describe the business framework
as specified, note the shared spine with the personal graph honestly, and
align the element list with the business template (tagline, talking points,
origin story, category point of view, boilerplates) once the business build
locks. Update Figure 2. Consider flagging this section "specification ahead
of implementation" the way v1.0 flagged the Vibeclone.

**Section 6 (How AI Systems Consume): revise tenses.**
Mode 1 (paste) and mode 2 (workspace context) are true today and now backed
by a real export: name the actual artifact (a zip with a VIBEGRAPH.md
manifest that tells the reading AI where to start, one file per element,
assets included). Mode 3 (MCP) and mode 4 (memory seeding) are still
roadmap: keep them, but phrase as direction, not current capability.

**Section 7 (Security and Privacy): the honesty pass. Highest stakes.**
See Section 5 of this outline. The threat model (7.1) holds up and needs no
change. 7.2 must be re-staged to match reality.

**Section 8 (Use Cases): keep, add one.**
All six hold up. Add the one the build proved: the app itself generates
every launch asset from the founder's own vibegraph ("every launch asset
came from a vibegraph" is both a use case and the marketing story).

**Section 9 (The Vibeclone): keep, near zero changes.**
Already correctly framed as future. Check whether the "dedicated paper
forthcoming" promise still stands.

**Section 10 (The Open Framework & Application): rewrite the app half.**
- The Claudia companion is now the defining feature of the app and v1.0
  never mentions her: guided element-by-element building, one continuous
  conversation across the whole vibegraph, craft playbooks per element
  (distilled brand-strategy frameworks that steer both coaching and
  generation), generate-from-what-you-have, upload-and-generate from an
  existing document, and a final review that reads the whole brand for gaps
  and contradictions.
- Pricing: DECIDED (Ryan, Aug 11): no dollar amounts in the paper; point
  at the pricing page. Additionally the app's total footprint in the paper
  shrinks: the paper is about the framework, and the app appears only in
  Section 10 as the reference implementation (a few paragraphs: guided
  build with Claudia, free assessment start, one-time unlock shape, link),
  plus wherever the build is evidence that the framework works. No feature
  tour.
- Keep the closing principle sentence; it is load-bearing: "a convenience
  layered on the open framework, never a gate in front of it."

**Section 11 (Summary): light rewrite** after everything above settles.

**Versioning: DECIDED (Ryan, Aug 11): this revision publishes as v1.5**,
now, ahead of the Sept 1 launch. v2.0 follows once the business builder
ships (Section 5 to present tense), timed right before product launch.

**Glossary: update.**
Revise Core Identity and Knowledge Base entries per the new structure. Add:
Orbits, Claudia, element, playbook (if the term appears in Section 10),
Brand Context, Brand Visuals. Keep Vibeclone.

**References: extend.**
Add: an Enneagram source (choose the edition actually leaned on for the
instrument), and the IPIP-NEO-120 citation specifically (v1.0 cites IPIP
generally). Verify every URL still resolves. Trademark footer: confirm
Raizen Labs entity line and the feedback address still correct.

## 3.5 Cover description (DECIDED Aug 11)

The cover description is final, replacing v1.0's "An open framework for
codifying personal and brand identity as portable context for AI tools and
agents.":

> An open framework for codifying human identity and personal brand as
> structured, portable AI context: digital DNA any AI can read today, and
> the protocol for an agent that operates as its creator's clone, a
> Vibeclone.

Carries the "digital DNA" idea and puts the Vibeclone endgame on the cover.
Deliberately NOT claimed: "agentic knowledge graph" (it is neither,
strictly) and "open source" ("open framework" matches the license claim).
The tagline "Your Vibes, Codified." stays above it unchanged.

## 4. New material v2.0 should add

1. **A "from framework to product" section or sidebar**: the framework was
   specified first, then a real app was built on it; what the build
   validated (element granularity, guided elicitation, generation from
   assessments) and what it changed (the re-cuts this outline documents).
   This is the paper's credibility upgrade: v1.0 was a proposal, v2.0 is a
   report.
2. **The export contract**, briefly, as the reference implementation of the
   spec: manifest-first reading order, one file per element, final copy vs
   draft copy semantics (what you pushed is what exports), staleness
   warning when answers moved after the last push.
3. **Version block + changelog**: v2.0, date, and a short "changes since
   v1.0" list. The spec repo has a CHANGELOG.md; the paper should reference
   the spec version it describes.

## 5. Honesty fixes (claims in v1.0 the product does not yet back)

These are the must-fix items; each currently reads as shipped:

1. **Zero-knowledge encryption for hosted vibegraphs (7.2 and Section 10).**
   The hosted app today uses server-readable storage with a no-train
   inference posture. ZK client-side encryption is deferred (v2 hosted
   tier). The v1.0 line "shipping proven encryption today beats promising
   novel cryptography tomorrow" must be re-staged: keep the design as the
   stated destination, state plainly what the hosted app does today, and
   keep the local-first open framework as the strong-privacy path that
   exists right now.
2. **Scoped, logged agent access over MCP (7.2, 6.3).** No MCP serving is
   shipped. Move fully to roadmap voice.
3. **"Optional ongoing maintenance, monitoring, agent connections" (10).**
   None of these exist as products yet. Cut or mark as planned.
4. **Per-item visibility settings ("every element carries its own
   visibility setting").** The schema anticipates visibility levels; the
   shipped app does not yet expose per-element visibility controls. Soften
   to design-level language until it ships.
5. **Business vibegraph parity (Section 5).** See section-by-section notes.

## 6. Style and mechanics for the v2.0 pass

- **No em dashes.** v1.0 uses them throughout; house style now uses ":" or
  "|" (the same rule enforced in the app's copy). This alone touches nearly
  every page.
- Keep the v1.0 voice: plain, direct, confident, specific. The rewrite
  should read like the same author on a later draft, not a new author.
- Diagrams: Figures 1 and 2 both redraw (new names, new structure, Claudia
  and the export in the consumption column).
- Footer: bump version and date; keep the running title.
- Decide the canonical casing once: "vibegraph" lowercase in prose, "The
  Vibegraph" as title, VIBEGRAPH.md for the manifest (v1.0 is already
  mostly consistent; codify it).

## 7. Companion work (not the paper, but must move with it)

1. **SPEC.md**: same re-cut (three phases, Brand Context/Brand Visuals
   element lists, Spheres naming, manifest example). The paper cites the
   spec; publish them together so they cannot disagree.
2. **App copy audit**: the pricing page, export manifest blurbs, and
   marketing pages should use the v2.0 names exactly. The app is already
   the source of the names, so this is mostly a verification pass.
3. **vibegraph.md and vibegraph.ai sites**: whichever pages quote the paper
   or the element lists.

## 8. Decisions (resolved Aug 11 except one)

1. **DECIDED (Aug 11): the third part is named "Orbits."** Chosen for the
   structural metaphor (they revolve around the core; the core travels,
   the orbits stay home), pronounceability, and the radial dashboard already
   drawing it. The app renames from "Spheres" after the paper locks. Add a
   follow-up task: rename the journey phase, nav, and copy in the app.
2. **Core Identity** = Personality + Ikigai (part 1 of three). Branding is
   part 2. The third part is part 3. The two-part Core/Knowledge-Base
   vocabulary retires.
3. **No prices in the paper**; point at the pricing page. App coverage
   shrinks to Section 10 as reference implementation.
4. **Enneagram**: one full personality assessment in two parts with
   different questioning methods; the paper explains the pairing in one
   honest paragraph (dimensional scores for calibration, the Enneagram's
   motivational typing for depth, the integrated reading reconciling them).
5. **This revision is v1.5, published now.** v2.0 lands after the business
   builder, right before launch.

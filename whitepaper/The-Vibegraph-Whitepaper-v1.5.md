# The Vibegraph™

*Your Vibes, Codified.*

An open framework for codifying human identity and personal brand as structured, portable AI context: digital DNA any AI can read today, and the foundation for an agent that operates as its creator, a Vibeclone.

**Version 1.5 · August 2026 · Ryan Charleston · vibegraph.ai · vibegraph.md**

---

## Introduction

Every AI tool you use starts from zero. It doesn't know your voice, your values, your goals, or your taste. So it guesses, and it guesses toward the statistical average. The result is output that could belong to anyone, which is another way of saying it belongs to no one.

The vibegraph fixes the input instead of endlessly editing the output. It is a structured, portable, human-owned system that codifies who you are: your personality, your purpose, your brand positioning, and your visual identity, plus optional orbits covering the working context of your life and/or business. Any AI tool, agent, or memory system can consume it. None of them own it.

Two design decisions separate the vibegraph from the wave of AI memory products. First, it is grounded in established frameworks rather than passive data collection: the Big Five "OCEAN" personality model paired with the Enneagram as a two-part personality assessment, an Ikigai-based structure for purpose and meaning, and industry best practices and standards in brand strategy for positioning and aesthetics (with organizational equivalents for business brands, drawn from Aaker's brand personality dimensions, Jungian brand archetypes, and the Golden Circle). Second, it works today, with zero platform adoption required. Paste a vibegraph into Claude, ChatGPT, Grok, or Gemini and the next output sounds like you.

> Memory layers remember what happened. A vibegraph defines who you are.

This paper describes the problem, the three-part architecture, how business brands nest inside their owner's vibegraph, how AI systems consume a vibegraph, the security model such a concept demands, and the open specification at vibegraph.md. Since version 1.0, the framework has also been proven in software: a working application at vibegraph.ai now builds complete vibegraphs, and the revisions in this version reflect what that build taught us.

---

## 1. The Problem: AI Doesn't Know Who You Are

Large language models are trained on the written output of millions of people and optimized to produce the most probable response. Probable means average. When a model knows nothing about you, the average is the best it can do.

Anyone who uses AI for real work has felt the consequences:

**You repeat yourself constantly.** Every new chat, every new tool, every new agent begins with the same ritual: here's who I am, here's what I do, here's how I write, here's what I'm working on. The context you type into one tool is gone the moment you open another.

**The output is generic.** "AI slop" became a household term for a reason. Ask ten professionals in the same field to generate a LinkedIn post on the same topic and the results are nearly interchangeable, because the model is drawing on the same averaged prior for all ten. The people who complain loudest are exactly the people with the most to lose: creators, coaches, consultants, and founders whose personal brand is their business. Their differentiation is their voice or unique "vibes", and generic output erodes that brand with every post.

**Platform memory doesn't solve this, and creates a new problem.** ChatGPT remembers some things about you. Claude remembers other things. Neither can see the other's memory, you can't fully inspect either one, and none of it transfers when a better tool ships next quarter. Memory features are useful, but they are fragmented, passive, and platform-locked. What they accumulate is a history of what you did, filtered through what a model happened to notice. That is not the same as a deliberate statement of who you are, today, nor does it keep track of who you are becoming.

**Agents raise the stakes.** A chatbot that misreads your tone wastes a prompt. An autonomous agent that misreads your intent takes actions on your behalf: it sends the email, books the meeting, publishes the post. The gap between "AI that knows you" and "AI that guesses" stops being a quality issue and becomes a trust issue.

The software industry has already solved a version of this problem for code. AGENTS.md, an open markdown convention that tells coding agents how a project works, spread to more than 60,000 repositories in about a year because the payoff was immediate: write the file once, and every agent that touches your codebase gets better on the next task. No committee, no SDK, no permission from anyone.

There is no equivalent for a human being. That is the gap the vibegraph fills.

---

## 2. What Is a Vibegraph?

A vibegraph is a structured collection of documents that codifies one person's identity and working context in a format AI systems can consume. It is natively human-shaped: a vibegraph represents a unique individual, holding exactly one personal brand, and one or more business brands that person owns beside it. Plain markdown at its simplest. A permissioned, encrypted data vault at its most complete. You own it, you host it where you choose, and you decide which parts any given tool or agent can see.

The name is literal. Your "vibes" (personality, taste, voice, values, purpose, aesthetic) are the things AI gets wrong about you by default, because they were never written down anywhere a machine could read them. The vibegraph writes them down and keeps them up-to-date.

### Design Principles

**Human-authored, not scraped.** A vibegraph is built deliberately, through structured self-assessment and brand-strategy work, not inferred from your inbox. Passive inference produces a model's opinion of you. A vibegraph is your statement of record. (The two can coexist; a vibegraph makes an excellent seed and correction layer for passive memory systems.)

**Useful on day one, with zero adoption required.** This is the load-bearing principle. A vibegraph delivers its value the moment its owner pastes it into any AI tool, LLM, or agent. Although welcomed, it's not dependent on third-party platforms to support it as a standard. Proposed web standards that depended on platform adoption have a poor track record; the ones that win give individual users an immediate payoff with tools they already have and use. The vibegraph is designed for the second pattern.

**Guided, not blank.** The hard part of a document like this is not the format; it is the blank page. The framework assumes a guided build: structured questions, worked examples for every element, and an AI coach that elicits real material in conversation rather than waiting for the owner to fill in a template. This principle was learned in software: the reference application's entire building experience exists because blank templates kill documents like these.

**Portable and sovereign.** The vibegraph is a framework and system that can be exported to a document/file format. It moves with you across tools, models, and vendors. If a platform shuts down or a better one launches, your vibegraph comes along unchanged.

**Grounded in established frameworks.** The identity layer is not improvised. It uses instruments and frameworks with decades of practice behind them, so the output is structured, comparable, and complete rather than a freeform "about me" essay.

**Private by default, shared by choice.** The parts of a vibegraph differ in sensitivity by design, and the framework's permission model (Section 7) treats visibility as a per-part, deny-by-default decision.

**Extensible.** A minimal vibegraph is the Core Identity and Branding: a few documents. From there, owners add orbits for whatever domains matter to them, at whatever depth they choose and feel comfortable documenting.

### Glossary

**Vibegraph: your vibes, codified.**
A portable, structured identity and context framework that codifies personality, purpose, and brand so AI tools and agents act in alignment with their owner's goals, voice, and taste. A vibegraph represents one unique person, and carries that person's brands: one personal, and optionally one or more business.

**Core Identity: who you are.**
The first of a vibegraph's three parts: personality (a two-part assessment: the Big Five and the Enneagram, reconciled in an integrated reading) and Ikigai (purpose). Small, stable, and safe to share with any AI tool.

**Branding: how you show up.**
The second part: one or more brands, each made of Brand Context (twelve positioning elements, from brand name to bios) and Brand Visuals (eight visual elements, from logos to photography direction). The personal brand is built from the Core Identity; business brands are built beside it. This is the part that keeps generated work on-brand.

**Element.**
The unit inside Brand Context and Brand Visuals: a single named artifact such as Core Values or Color Palette. Elements are first-class: each carries its own guidance, examples, and craft standards.

**Orbits: what you know and how you operate.**
The third part: self-defined modules containing the documents, data, and working context of your life or business, revolving around the core. Creators often call this their second brain; businesses call it a knowledge base or wiki. Orbits are gated and permissioned based on owner preferences, and they stay home when the core travels.

**Claudia.**
The AI coach in the reference application at vibegraph.ai. She guides the build: asking, drafting, and generating from what the owner has already established.

**Vibeclone: you, digitally remastered.**
An AI agent powered by a vibegraph that thinks, writes, and acts in its owner's likeness. Covered briefly in Section 9; a dedicated paper will follow.

---

## 3. Architecture: Three Parts

Every vibegraph has the same three-part structure, anchored to one person.

The **Core Identity** answers the question every AI tool silently asks and never gets answered: who is this person? It contains the personality profile and the purpose work. It is deliberately small, because it is meant to travel everywhere. It is the part you paste into a chat, attach to a project, or expose to an agent without a second thought.

**Branding** answers the next question: how does this person show up? It holds one or more brands, each with its words (Brand Context) and its look (Brand Visuals). The personal brand is built from the Core Identity; business brands the owner operates sit beside it as full brand documents of their own (Section 5). Together with the core, Branding forms the shareable half of a vibegraph: the core and a brand fit comfortably inside a single model context window.

The **Orbits** answer the follow-up question: what is this person working with? They are a set of self-defined modules (health, finances, relationships, career, notes, time management, skills, goals, or anything else the owner wants to include) each containing documents, files, data, and protocols. The orbits are where depth lives, and where sensitivity lives, which is why every orbit and every item within it carries its own access controls.

The structure matters for three reasons.

First, it matches how AI consumption actually works. Identity and brand context belong in every interaction; domain context belongs only in relevant ones. A model writing your newsletter needs your voice and positioning, not your medical history. Separating the always-relevant from the sometimes-relevant keeps context windows lean and permission decisions simple.

Second, it matches how trust works. The Core Identity and Branding are shareable by design. The Orbits are gated by design. A clean architectural line is easier to secure and easier to reason about than a single blob with per-paragraph exceptions.

Third, it scales in both directions. A minimal vibegraph (Core Identity and Branding only) is genuinely useful and can be built quickly with proper tools. A maximal vibegraph, with a dozen orbits maintained over years, approaches something like a personal operating system. Both are valid. The framework doesn't force anyone up the curve.

---

## 4. Inside the Vibegraph

### 4.1 Personality: a two-part assessment

The foundation is a full personality assessment in two parts, using two instruments that approach the same person with different methods of questioning.

**Part one: the Big Five (OCEAN).** A Big Five assessment measuring Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism, administered through the IPIP-NEO-120, a public-domain, research-grade inventory. The Big Five anchors the assessment for a simple reason: it is the model with the strongest empirical support in personality psychology, and it produces dimensional scores rather than type labels. Dimensional data is exactly what a machine consumer can use: "high openness, moderate extraversion, low neuroticism" gives a model calibration that a four-letter type does not. The vibegraph stores the scores, the facet breakdown, and a written interpretation in the owner's own words.

**Part two: the Enneagram.** The Enneagram asks a different kind of question: not how you behave, but why. Where the Big Five measures traits, the Enneagram surfaces core motivations, fears, and the characteristic patterns a person falls into under stress and growth. It is a typology rather than a dimensional instrument, and the framework uses it with that understanding: not as a replacement for dimensional rigor, but as a second angle of questioning that dimensional scores alone do not capture.

**The integrated reading.** The two instruments are reconciled in a single written interpretation: where they agree, where they tension, and what the combination means for how this person works, decides, and communicates. This reading, in the owner's own words after review, is what most AI consumers actually use; the underlying scores remain available for tools that want them. Owners who have already taken either assessment elsewhere can import their results rather than retaking them.

### 4.2 Purpose: Ikigai

The second layer codifies meaning and direction through a four-pillar Ikigai structure, inspired by Kyle Kowalski's "Ikigai 2.0" treatment of the concept: what you love, what the world needs from you, what you are naturally good at, and what you can be paid for. Where the pop-culture ikigai Venn diagram reduces purpose to a career sweet spot, this treatment keeps the pillars distinct, examines where they genuinely meet, and produces a richer artifact: four honest self-statements, a synthesis of their intersections, and a single Ikigai statement, the sentence the rest of the vibegraph builds on. For an AI consumer, this layer is what turns "write a post about productivity" into a post about productivity *that connects to what its author actually cares about.*

### 4.3 Brand Context: the brand in words

The third layer begins the Branding part: twelve positioning elements that define the brand's language.

1. Brand Name
2. Slogans & Taglines
3. Unique Value Proposition
4. Purpose-Vision-Mission
5. Core Values
6. Tone & Voice
7. Messaging & Narratives
8. Keywords & Phrases
9. Bio (Short/Long)
10. Achievements & Awards
11. Inspiration & Influence
12. Online Presence

Each element is a small, opinionated artifact with a defined shape: core values as decision filters with the behavior that proves them, a value proposition in a single tested sentence, messaging as repeatable statements each paired with the story that makes it believable. The shapes matter because the consumer is a machine: a model handed twelve well-formed elements writes like the owner; a model handed an essay writes like a model that read an essay.

### 4.4 Brand Visuals: the brand in pictures

Eight visual elements complete the Branding part:

1. Symbols & Logos
2. Color Palette
3. Typography
4. Iconography
5. Brand Imagery
6. Illustration Style
7. Visual Elements
8. Photography

The visuals layer produces concrete artifacts rather than vague direction: hex color values, typography pairings, logo and symbol options, iconography, imagery guidelines, and photography direction. When an AI tool generates a slide, a thumbnail, or a landing page for you, this is the layer that keeps it on-brand without a design review.

Together, the Core Identity and Branding give any AI system what a great ghostwriter, a great designer, and a great strategist would each need a dozen sessions to absorb.

### 4.5 Orbits

The Orbits are organized into modules. The framework suggests a starting taxonomy; owners rename, merge, split, and invent orbits freely. The default suggested personal set:

| Orbit | Typical contents |
|---|---|
| Health & Wellness | Sleep, nutrition, fitness, habits and rituals, health records and documents |
| Relationships | Family, friends, coworkers, partners and clients, audience |
| Finances | Budget, savings and investments, wealth and tax documents |
| Career | Résumé/CV and career history, current role, current business info |
| Notes & Ideas | Quick notes, brain dumps, bookmarks and read-later queues, journals |
| Time Management | Principles, routines and schedules, planner, calendar conventions |
| Skills | Methods, protocols, skills written for AI consumption, reference docs |
| Tech Stack | Tools and hardware/software, current/intended use, access and privileges |
| Goals | Short- and long-term, with daily/weekly/monthly/yearly cadence |

A note on method: readers who maintain a second brain will recognize that this is a life-domain taxonomy, closer to Johnny Decimal or the "Areas" of PARA than to Zettelkasten's emergent linking. That is deliberate. Systems optimized for human creative recall reward loose association; systems optimized for machine retrieval reward stable, addressable domains an agent can be granted access to, one at a time. The vibegraph does not replace your PKM practice. It sits in front of it as the permissioned, machine-facing layer, and it can happily link out to an Obsidian vault, Notion workspace, or a folder of markdown files.

The most common failure mode of personal knowledge systems is well documented: capture everything, retrieve nothing, abandon the system. The vibegraph's defense is the core/orbit split itself. The Core Identity and Branding alone deliver the headline value. Orbits are added when a real use case demands one, not because an empty template exists.

*[Figure 1, redrawn for v1.5: one person's vibegraph as a master file over three parts (Core Identity, Branding with the personal brand and business brands beside it, Orbits), consumed by AI chats and tools, agents, memory layers, and the Vibeclone.]*

---

## 5. Business Brands

*This section describes the business framework as specified. The rest of the vibegraph is implemented in full in the reference application; the business brand builder is in active development on the same architecture, and this section will move to the present tense in version 2.0.*

A vibegraph represents one human being, and that is the design, not a limitation. The audience this framework serves first (solopreneurs, creators, founders) does not experience their business as a separate self; they experience it as something they own and express. The vibegraph models that reality directly: business brands live inside their owner's vibegraph, one full brand document per business, beside the personal brand.

The sequence is deliberate, and the reference application enforces it: business brands are built after the owner's identity and personal brand, because the founder's material is the business brand's raw material. A brand for a business still cannot take a personality test, and ikigai does not describe a company, so the business brand swaps the identity instruments for organizational equivalents while keeping the same Context and Visuals structure.

### 5.1 The Business Brand's Foundations

**Brand personality: Aaker's five dimensions.** In place of the Big Five, the business brand uses Jennifer Aaker's brand personality framework (Sincerity, Excitement, Competence, Sophistication, Ruggedness), the closest thing brand research has to an empirically derived trait model for organizations. Like OCEAN, it produces dimensional, machine-usable calibration rather than a slogan.

**Brand character: the twelve archetypes.** Aaker's dimensions describe a brand's personality; a Jungian archetype (Hero, Sage, Creator, Outlaw, Caregiver, and the rest) gives it a coherent character to write and design from. In practice the two work together: choose the archetype, then use the dimensions to describe and measure how it shows up. Both live in the business brand's foundation.

**Purpose: the Golden Circle, mission, vision, values.** In place of Ikigai, the business brand codifies purpose through Simon Sinek's Why/How/What structure alongside conventional mission, vision, and values statements. (Small businesses running on EOS can drop their Vision/Traction Organizer in here nearly unchanged.) Usefully, Sinek designed the Golden Circle to apply to individuals as well as organizations, which gives the personal and business brands inside one vibegraph a shared spine: the founder's personal Why and their company's Why are written in the same shape and checked against each other, in the same graph.

**Visuals.** The visual half carries over from the personal brand with one adjustment in emphasis: it becomes a full design system (design principles, symbols and logos, palette, typography, iconography, imagery, and templates for the assets a business produces repeatedly, such as social posts, decks, email signatures, landing pages, and media kits).

### 5.2 Business Orbits

A business brand brings its own orbits, and they shift from life domains to operating systems: the things that make delegation and consistency possible.

| Orbit | Typical contents |
|---|---|
| Relationships (CRM) | Employees, advisors, investors, partners, vendors, customers, audience |
| Finances | Budget, P&L, payroll, investments, valuation |
| Operations | Business entity, HR, legal |
| Skills | Playbooks, SOPs, workflows, skills written for AI, reference docs |
| Management | Principles, routines, planning, calendar systems |
| Brand Templates | Post templates, decks, email templates, lead magnets, landing pages, media kits |
| Goals | Short- and long-term, with cadence |
| Notes & Ideas | Capture, bookmarks, journals/logs |
| Tech Stack | Tools, access and privilege protocols |

The structural difference from the personal orbits is worth stating plainly, because it explains why the module lists diverge. A personal knowledge system optimizes for one person's recall and creative output. A business knowledge system optimizes for *repeatability*: any operator (teammate, contractor, or agent) following the same playbook should produce the same result. That is why SOPs and templates, which barely appear in personal systems, are the center of gravity in business ones. It is also why the business side of a vibegraph is unusually well suited to agents: an SOP written clearly enough for a new hire is most of the way to being a protocol an agent can execute.

### 5.3 What maps, what doesn't

| Personal brand | Business brand | Relationship |
|---|---|---|
| Big Five + Enneagram | Aaker's five dimensions + archetype | Replaced: same job (personality calibration), different instruments |
| Ikigai | Golden Circle + mission/vision/values | Replaced: same job (purpose), shared Why structure |
| Brand Context | Brand Context | Carries over nearly intact |
| Brand Visuals | Brand design system + templates | Carries over, deepens |
| Life-domain orbits | Operating-system orbits | Restructured around repeatability |

A solopreneur, usefully, needs both, and the vibegraph holds them side by side by design: the personal brand governs voice and identity; the business brand governs the machine that sells and delivers. One person, one graph, every brand they own.

### 5.4 The organizational vibegraph, someday

A standalone organizational vibegraph (a company as first-class owner, with no single human anchor: the multi-founder startup, the agency-managed brand, the institution) is a plausible future extension of the framework, and nothing in the format precludes it. It is deliberately not part of this version. The person-anchored model is shipped, coherent, and serves the framework's first audience; an organization-anchored variant deserves its own careful treatment rather than a premature parallel.

*[Figure 2, redrawn for v1.5: business brands inside one person's vibegraph, the instruments swapped for organizational equivalents and the business orbits restructured around repeatability.]*

---

## 6. How AI Systems Consume a Vibegraph

A vibegraph is only as good as the ways it can be used. There are four, in increasing order of sophistication, and the first one requires nothing from anyone.

**1. Direct context.** Paste the Core Identity and Branding into any chat, or attach the exported files to any tool that accepts them. This works today, in every AI product on the market, and it is the canonical consumption mode. The reference application exports a vibegraph as a portable archive: a master file that tells the reading AI where to start and links every document in read order, one file per document (personality, ikigai, and each brand), and the visual assets alongside. For AI builders, the corollary: a vibegraph is structured markdown, so if your product accepts text, it already supports vibegraphs. The feedback loop is immediate: the very next response is calibrated to its owner. This is the same loop that drove AGENTS.md through the developer ecosystem: write the file once, watch every tool get better. VIBEGRAPH.md applies the same idea to a person instead of a codebase.

**2. Persistent workspace context.** Most serious AI tools now have a persistent-context surface: Claude's Projects, ChatGPT's custom GPTs and project instructions, and their equivalents elsewhere. A vibegraph exports cleanly into all of them. Set it once per workspace and every conversation in that workspace starts calibrated.

**3. Live access over MCP (roadmap).** The Model Context Protocol gives agents a standard way to request data from external sources at runtime. A vibegraph served over MCP lets an agent ask for exactly the orbit it needs, when it needs it, subject to the owner's permissions: your writing agent reads Core Identity and the Brand Templates orbit; your finance agent reads Finances and nothing else. This is where the per-item permission model (Section 7) does its real work, and it is the consumption mode that turns a vibegraph from a document into critical infrastructure. It is a design target of the framework, not a shipped capability of the reference application today.

**4. Seeding memory layers.** AI memory systems, the platform-native ones and the dedicated memory infrastructure used by agent builders, all face a cold-start problem: they know nothing until they've watched you for weeks, and what they learn is inference, not fact. A vibegraph solves this cold start. Loaded as seed context, it gives a memory layer a verified, owner-authored foundation that passive observation can then extend. This is the intended relationship between the vibegraph and the well-funded memory category: they are the substrate, the vibegraph is the schema. Memory layers remember what happened. A vibegraph defines who you are. The two compose.

One relationship worth making explicit: the vibegraph is to a person what AGENTS.md is to a repository. Same medium (plain, human-readable markdown), same philosophy (a predictable place for the context machines need), same adoption physics (individual users get instant value; ecosystem support compounds it but is never required).

> Where AGENTS.md tells an agent how to work on your code, a vibegraph tells an agent how to work as, and for, you.

---

## 7. Security and Privacy

A complete vibegraph is a concentrated dossier: personality profile, purpose, finances, health, relationships, goals. In the wrong hands it is a toolkit for impersonation, social engineering, and targeted fraud. Any honest presentation of this framework has to treat security as architecture, not a policy page. This section describes the threat model and the design that answers it, and it is equally honest about which parts of that design are shipped and which are the committed destination.

### 7.1 Threat Model

The realistic attack surfaces, roughly in order of likelihood:

**Compromised or over-permissioned AI tool access.** The newest and most distinctive risk. Prompt-injection attacks that exfiltrate data through AI tool integrations moved from theory to documented incidents in 2025, including zero-click exfiltration through enterprise AI assistants and data theft through poisoned MCP tool descriptions. The security community's consensus position is sobering: prompt injection cannot currently be fully eliminated, only contained. Any system that exposes personal data to AI tools must therefore assume that some tool, someday, will be manipulated, and must limit what that tool can access in the first place.

**Server breach.** If vibegraphs are stored on a provider's servers in readable form, the provider is a honeypot. One breach exposes every customer's most sensitive self-description at once.

**Account takeover.** Credential stuffing and phishing against individual accounts.

**Insider access.** Anyone at a hosting provider who can read customer data is a risk, however trustworthy the company.

**Training-data leakage.** Personal context sent to model providers without contractual protection may end up in training corpora.

### 7.2 Design Response

**Private and local by default (shipped: the open framework).** The reference posture for a vibegraph is files on hardware the owner controls. The open framework at vibegraph.md assumes local-first operation: your vibegraph lives on your machine, and only the elements you deliberately expose ever leave it. Owners who self-host accept responsibility for their own device security, and the framework documentation says so plainly rather than pretending a local folder is a vault. This path exists today and is the strong-privacy option.

**The hosted application, today (shipped, stated plainly).** The hosted app at vibegraph.ai currently stores vibegraphs in conventional server-readable form, protected by industry-standard encryption in transit and at rest, row-level access control, and the no-train inference posture below. It does not yet offer zero-knowledge encryption. Owners for whom server-readable hosting is unacceptable should use the local-first framework; that is precisely why the framework ships open and file-based.

**No-train inference, with escalation paths (shipped).** AI features that process vibegraph content run against APIs whose terms exclude customer data from model training, with that policy pinned per-request rather than assumed: the standard posture of major providers' commercial APIs, and the pragmatic baseline for most owners. Owners with stricter requirements can point the framework at local models or privacy-focused inference providers; the vibegraph, being a file format rather than a service, does not care which model reads it.

**Per-item permissions, deny by default (specified; partially shipped).** The framework's permission model gives every orbit, and every item within an orbit, a visibility setting: private (never exposed), scoped (exposed to named tools or agents, for named purposes), or public (freely shareable, like the core). Nothing is exposed by omission. In the reference application today, this model governs the architecture (the shareable core and the gated orbits are structurally separate); the fine-grained per-item controls arrive with the orbits themselves.

**Scoped, logged agent access (design target).** When vibegraphs are served to agents over MCP, access will be granted per-agent and per-orbit, never as a blanket, with every agent read logged so the owner can always answer "what has this tool actually seen?" Given the prompt-injection reality described above, tight scoping is not paranoia; it is the mitigation. An agent that was never granted the Finances orbit cannot leak it, no matter how thoroughly the agent itself is compromised.

**Zero-knowledge encryption for hosted vibegraphs (committed destination).** The endpoint for hosted storage follows the model proven by password managers and encrypted-mail providers: client-side encryption, with keys derived on the owner's device and never transmitted, so the provider stores ciphertext it cannot read. This carries real trade-offs that deserve an honest statement: a zero-knowledge provider cannot search your data server-side, cannot recover it if you lose your keys, and cannot hand over readable data under compulsion, because it never had any. For a document this sensitive, those trade-offs are the point. It is stated here as the destination, not the present: the hosted app will say "zero-knowledge" only when it is true.

**Future consideration of verifiable credentials.** The W3C's Verifiable Credentials standard (v2.0, a formal Recommendation since May 2025) and selective-disclosure techniques point toward a future in which a vibegraph can *prove* an attribute (a credential, an age, a verified identity) without revealing the underlying data. That is a genuinely useful future for a portable identity layer, and the framework is designed not to preclude it. It remains deliberately excluded from this version of the whitepaper, along with blockchain storage of any kind.

### 7.3 The Risk Summary

A vibegraph concentrates risk in exchange for concentrating value; the design's job is to keep the exchange favorable. Local by default, deny by default, scope everything, state plainly what the hosted service can and cannot see today, and log every agent access as that capability ships. No security section can promise safety. This one promises that the sensitivity of the data was the first architectural constraint, not the last, and that the paper will never claim a protection before it exists.

---

## 8. Use Cases

**High-fidelity AI output.** The founding use case. A creator, marketer, or founder with a vibegraph gets output in their voice, aligned with their positioning, styled to their brand, from any AI tool, on the first generation instead of the fifth revision. The people this serves most are those whose personal brand is the business: solopreneurs, founders, coaches, consultants, content creators, educators, agency founders, fractional executives.

**Consistency across the whole stack.** The same Core Identity feeds the chat tool, the writing assistant, the design generator, the email drafter, and the agent that queues social posts. One source of truth ends the drift between tools that each hold a slightly different, slightly stale picture of you.

**Bootstrapping a brand from a vibegraph.** The build proved this one on itself: every launch asset of the vibegraph application (its site copy, its brand board, its founder's own positioning) was generated from vibegraphs built in the app. The vibegraph is not just context for producing content; it is sufficient raw material for producing an entire brand surface.

**Agency client onboarding, upgraded.** Marketing and branding agencies extract a shallow vibegraph from every client today; they just call it a discovery questionnaire, it lives in a Google Doc, and it gets read twice. Rebuilt as a vibegraph, client discovery produces a living, structured client-context file the agency loads into every AI tool it uses for that account, for the life of the engagement. Onboarding output stops being paperwork and becomes reusable infrastructure. For agencies, one intake process yields a per-client asset; for clients, the vibegraph is theirs to keep when the engagement ends.

**Seeding your digital twin.** A vibegraph is the natural training substrate for an AI clone of oneself (see Section 9) and the natural seed for any personal-AI or memory product, giving passive systems a verified foundation instead of weeks of cold-start inference.

**The résumé, replaced.** A résumé is a one-dimensional, self-flattering PDF. A shared slice of a vibegraph (Core Identity plus a Career orbit) gives an employer or client a structured, honest, machine-readable picture of how a person thinks, works, and communicates. Whether hiring processes are ready for this is an open question; the artifact, at least, is finally made possible by the vibegraph.

**Forms, applications, and intake, automated.** Medical intake, loan applications, vendor onboarding, conference speaker forms: tedious, repetitive, and answerable almost entirely from a well-maintained vibegraph. An agent with scoped access to the relevant orbits fills them in seconds and asks the owner only for what's genuinely new. Vibegraph owners save a significant amount of time on the task of filling out forms.

---

## 9. The Vibeclone

In the future, the most ambitious consumer of a vibegraph will be a Vibeclone: an AI agent that runs on a person's vibegraph and operates in their likeness, thinking through their frameworks, writing in their voice, making the calls they would make, within the permissions they've granted.

The distinction between a vibeclone and today's "AI clone" products is the direction of service. Existing clone platforms point outward at an audience: fans and clients talk to a chatbot trained on a creator's content. A vibeclone points inward, working *for* its owner across their actual tools and tasks, with the vibegraph as its persistent, owner-authored source of self. The better the vibegraph, the less the clone has to guess.

The vibeclone raises its own questions (capability boundaries, disclosure norms, delegation limits, identity verification) that deserve more than a subsection. A dedicated Vibeclone paper (forthcoming) will address and answer these questions. For the purposes of this whitepaper, one sentence suffices: the vibegraph is the prerequisite. There is no faithful clone of an uncodified person.

---

## 10. The Open Framework & Application

The vibegraph ships in two forms, deliberately.

**The Open Framework.** The open specification can be found at vibegraph.md. The framework itself (the document structure, the three-part architecture, the element and orbit taxonomy, the schema, and starter templates) is published free under a permissive license, in the same spirit (and the same medium) as AGENTS.md. Anyone can build a vibegraph by hand, with their own tools, their own storage, and their own security posture. Developers and tinkerers can extend it, wrap it, serve it over MCP, and build products that consume it, without asking permission. An identity standard that isn't open isn't a standard; it's a lock-in scheme with a manifesto.

**The Application.** The guided application can be found at vibegraph.ai. Building a vibegraph by hand is real work: a proper personality assessment, honest purpose work, and brand strategy development historically could cost thousands of dollars with a human brand strategist. The application packages that work into a guided build with Claudia, an AI coach who carries the craft: she asks the questions a strategist would ask, drafts every element from what the owner has already established, works from uploaded reference material when there is some, and reads the finished brand back for gaps and contradictions before it ships. The personality assessment is free to start; completing the full build is a one-time unlock (current tiers and prices at vibegraph.ai/pricing), with unlimited edits and re-exports. The vibegraph app is a convenience layered on the open framework, never a gate in front of it.

---

## 11. Summary

The last two years (mid 2024 to mid 2026) settled the question of whether AI can produce competent work. The next two will be about context and whose work it produces. Left uncalibrated, every model regresses to the same mean, average output or "slop", and everyone who relies on it sounds a little more like everyone else. Your unique personal moat in the agentic era will rely on a well-defined vibegraph and the personal brand that exists within it.

The fix is not a smarter model. It is better input and context: a deliberate, structured, portable statement of identity that any AI system can read and no AI platform can own. Small enough to paste into a chat today. Extensible enough to run an agent fleet tomorrow. Private by default, permissioned by design, grounded in frameworks older and sturdier than any of the tools that will consume it, and now proven by a working application that builds it end to end.

> The Vibegraph is your vibes, codified.

Visit **vibegraph.md** to download the open framework or **vibegraph.ai** to start building your vibegraph with the app.

---

## Changes since v1.0

- The architecture is presented as three parts (Core Identity, Branding, Orbits), replacing the two-part Core Identity / Knowledge Base presentation. The concepts are unchanged; the names and grouping now match the reference application.
- A vibegraph now explicitly represents one person. Business brands live inside their owner's vibegraph (Section 5), replacing v1.0's parallel "business vibegraph" framing; the standalone organizational vibegraph is staged as a possible future extension.
- The personality layer is a two-part assessment: the Big Five (IPIP-NEO-120) joined by the Enneagram, reconciled in an integrated reading.
- Brand Positioning and Brand Aesthetics are renamed Brand Context and Brand Visuals, with their twelve and eight elements enumerated.
- The Knowledge Base is renamed Orbits.
- The Ikigai layer's attribution is clarified: inspired by Kowalski's Ikigai 2.0, implemented as the framework's own four-pillar structure.
- Section 7 now states plainly which protections are shipped, which are partial, and which are committed destinations; zero-knowledge hosted encryption is stated as destination, not present capability. MCP serving is stated as roadmap.
- Section 10 describes the application as built, including the guided build with Claudia; pricing details moved to the pricing page.
- A new design principle ("Guided, not blank") and a new use case (bootstrapping a brand from a vibegraph) reflect what the build demonstrated.
- Cover description revised.

---

## References

The vibegraph stands on established frameworks and open standards. The works and authors below inform or are embedded in its architecture.

### Identity & Psychology

1. McCrae, R. R., & Costa, P. T. (1987). "Validation of the Five-Factor Model of Personality Across Instruments and Observers." *Journal of Personality and Social Psychology*, 52(1), 81–90. The foundational validation of the Big Five (OCEAN) model.
2. Goldberg, L. R. (1993). "The Structure of Phenotypic Personality Traits." *American Psychologist*, 48(1), 26–34.
3. Johnson, J. A. (2014). "Measuring thirty facets of the Five Factor Model with a 120-item public domain inventory: Development of the IPIP-NEO-120." *Journal of Research in Personality*, 51, 78–89. The instrument used for the Big Five assessment.
4. International Personality Item Pool (IPIP): public-domain Big Five assessment instruments. ipip.ori.org
5. Riso, D. R., & Hudson, R. (1999). *The Wisdom of the Enneagram*. Bantam. The Enneagram's nine types, levels of development, and stress/growth patterns.
6. Kowalski, K. *Ikigai 2.0: Evolving the Ikigai Diagram for Life Purpose*: the treatment of ikigai that inspired the framework's four-pillar purpose structure. Sloww. sloww.co/ikigai-2-0

### Brand Strategy

7. Aaker, J. L. (1997). "Dimensions of Brand Personality." *Journal of Marketing Research*, 34(3), 347–356. The five-dimension brand personality framework used in the business core.
8. Jung, C. G. (1959). *The Archetypes and the Collective Unconscious*. Princeton University Press. The psychological foundation of archetype theory.
9. Mark, M., & Pearson, C. S. (2001). *The Hero and the Outlaw: Building Extraordinary Brands Through the Power of Archetypes.* McGraw-Hill. The application of Jung's twelve archetypes to brand building.
10. Sinek, S. (2009). *Start with Why: How Great Leaders Inspire Everyone to Take Action.* Portfolio. The Golden Circle (Why/How/What) framework. simonsinek.com
11. Wickman, G. (2011). *Traction: Get a Grip on Your Business.* BenBella Books. The Entrepreneurial Operating System (EOS) and Vision/Traction Organizer. eosworldwide.com

### Knowledge Management

12. Forte, T. (2022). *Building a Second Brain.* Atria Books. The PARA method and the modern "second brain" practice. buildingasecondbrain.com
13. Ahrens, S. (2017). *How to Take Smart Notes.* The Zettelkasten method, after the practice of sociologist Niklas Luhmann.
14. Noble, J. *The Johnny.Decimal System*: a numbered life-domain taxonomy for organizing information. johnnydecimal.com

### AI Standards & Protocols

15. AGENTS.md: an open markdown convention for guiding AI coding agents, stewarded by the Agentic AI Foundation under the Linux Foundation. agents.md
16. Model Context Protocol (MCP): an open protocol for connecting AI applications to external data sources and tools, originated by Anthropic and hosted by the Linux Foundation. modelcontextprotocol.io

### Security & Privacy

17. W3C (2025). *Verifiable Credentials Data Model v2.0.* W3C Recommendation, May 15, 2025. w3.org/TR/vc-data-model-2.0
18. OWASP Foundation. *OWASP Top 10 for Large Language Model Applications*: the reference taxonomy for prompt-injection and related LLM security risks. genai.owasp.org
19. 1Password. *1Password Security Design* white paper: the zero-knowledge, client-side encryption model referenced in Section 7. 1password.com/security

---

*Vibegraph™ and Vibeclone™ are trademarks of Raizen Labs, LLC. Authored by Ryan Charleston. The vibegraph specification is published under a permissive open license at vibegraph.md. Send feedback to whitepaper@vibegraph.ai*

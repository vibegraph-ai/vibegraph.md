# Framework site design

The static GitHub Pages entry is docs/index.html. There is no build step. docs/assets/site.js controls the theme, navigation and optional NET preview. Google Fonts supplies Space Grotesk Medium, Inter Regular/Medium and IBM Plex Mono Regular/Medium.

## Design source

Figma file: https://www.figma.com/design/x48b72CU3Bv4bvgTwtOBH7

Page 12, node 3:88: Desktop dark 20:1549, Desktop light 20:1576, Mobile dark 20:1602, Mobile light 20:1625. Foundations, utility icons, controls, navigation, cards, motion and handoff were inspected on pages 00, 01, 04 through 08, 14 and 15. The existing site-vibegraph implementation and shared prototype handoff were used for component behavior and vendor files.

The header mark is the exact SVG export of the framework instance 21:51. Its path geometry is unchanged. CSS maps its two fills to the foreground and background theme tokens. Utility icons come from the same system's exported assets.

Desktop uses a 1200 px container, 120 px side margins at 1440, an 880 px reading column, 96 px section padding, 48 px section gaps, an 88 px header and a 72/83 px framework display. Mobile uses 20 px margins, 56 px section padding, 32 px gaps, a 76 px header and a 44/51 px display. Between 640 and 1439 the minimum margin is 32 px, with content capped at 1200 px. Navigation and feature columns collapse below 1024. Below 360 the framework display is 40/48 to fit 320 px. Native browser scrollbars consume their normal layout width.

## Preserved content and adapted patterns

The hero, all seven v2.0 sections, metadata and existing resource links remain. Figma's older text was not substituted. Text height follows content, so the result is longer than the four reference frames. Repository links explicitly target v2.0.

- Definition and acceptance test: editorial section, H2, body and divider primitives. The definition's existing pull quote uses H3 with a monochrome rule.
- Roles: the original semantic comparison table uses system labels, body type and dividers. On mobile, each comparison row stacks its three labeled values at readable body size. This table pattern is an adaptation because the target frames have no roles section.
- What: the page 12 three-column framework dimensions pattern, with current Identity, Brands, and Areas and components copy.
- Root and handoff: editorial section plus Code/M, quiet bordered panels and badge/metadata primitives. Code wraps visually without altering its text or clipboard contents. These code panels are adaptations because the target frames omit these sections.
- Start: page 12 vertical 01/02/03 pattern, H3, body, 44 px resource links and dividers.
- Footer: page 12 ecosystem links, synchronized theme toggle and family credit. The original resource navigation and maintainer line are retained beneath it to preserve existing content.

The framework/site name remains lowercase. The locked specification's literal root filename VIBEGRAPH.md stays uppercase, consistent with its explicit case-sensitive filename explanation and the Figma overview rule that repository details govern exact filenames.

## Behavior

First visit follows prefers-color-scheme, as requested, overriding the older Figma dark-first instruction. Explicit choices persist as vibe-theme, matching the marketing site key. Header and footer controls always name the next action. Storage failures do not prevent use. System changes apply until a manual preference exists; storage events synchronize tabs.

Menu controls use native buttons and a labeled navigation landmark. Enter/Space operate controls; Escape closes the menu and restores trigger focus. Below 640 the roles table becomes a labeled stack. Code and path strings wrap; the body does not need horizontal scrolling. Focus uses the shared 2 px ring and 3 px offset. Action targets are at least 44 px, primary/secondary buttons 48 px.

NET is off by default. Opting in lazy-loads pinned local Three.js and Vanta.js from the original prototype, with their MIT license texts. Page 14's reference settings are preserved, with its documented light-theme colors and touchControls:false. Below 640, with reduced motion, or on loading/WebGL failure, a static diagonal mesh appears. Hidden/offscreen pages suspend the effect. Theme changes and page exit destroy existing canvases. Turning the preview off returns to solid monochrome. The effect is decorative and cannot capture page scrolling.

## Verification

Browser review: 1440 and 390 px, dark and light; full-page review images assembled from viewport captures because the browser's built-in full-page capture had stitching artifacts. Breakpoint checks at 320, 359, 390, 639, 640, 768, 1023, 1024, 1280 and 1440 found no horizontal overflow. Keyboard menu and Escape, theme synchronization and reload persistence passed. NET rendered with one canvas, theme changes retained one canvas, and mobile fallback removed the canvas. Browser warning/error log was empty.

A dependency-free VM check additionally verified both system theme defaults, invalid saved preferences, blocked storage, manual override priority, system preference changes, reduced-motion/mobile suppression of library loading, and failed-library static fallback. Reduced motion was checked in that harness; the OS setting was not changed during browser review.

Text contrast: dark foreground 18.32:1, dark muted 9.98:1, light foreground 18.32:1, light muted 4.93:1, light card muted 5.33:1. All seven section text comparisons against the original passed. No em dashes occur in the page. JavaScript syntax and git diff whitespace checks passed.

SPEC.md, templates, example, changelog, GitHub, framework, product domains and whitepaper PDF resolve. The Context Layer at https://contextlayer.vibegraph.ai/ was verified as Home | The Context Layer in the browser; a command-line request returned 403. Vibegraph.ai and Vibeclone.ai currently resolve to public holding pages, not the unpublished marketing implementation. The PDF redirect and CNAME remain untouched.

No push or deployment is part of this change.


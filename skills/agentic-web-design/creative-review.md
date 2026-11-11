# Creative decisions with little designer overhead

Use for full marketing-site builds in Webflow or Astro. The agent researches, prepares visible options, recommends a direction and fixes routine execution problems. The designer makes a small number of consequential choices. Scale narrow changes to their actual scope.

## Three planned touchpoints

Use the [design interview](design-intake.md) across all three touchpoints. Each is a short back-and-forth: prepare a visible proposal, hear the designer's reaction, revise the relevant decision and artifact, then explore the next consequential gap. Continue through section design, assets and rendered refinement. The 21-question bank supplies starting prompts, not a fixed script. Lead with recommendations and invite corrections or exceptions instead of requiring dozens of individual selections.

1. **Direction and voice.** Inspect the brief and existing approvals. When direction is open, show three distinct boards, each with a hero, typography/palette, image treatment and two supporting section references. Recommend one. Show a proposed voice specimen alongside it. Agree direction and voice before drafting the full site.
2. **Complete page and production plan.** Present the full UX/copy outline, visible section options, recommended scrollable storyboard, button/link specimen, motion examples and asset concept cards together. Agree UX/copy before finalizing the storyboard; resolve changes in this same review round. Obtain any uncovered media budget before paid production. Include desktop composition and mobile behavior. A designer can accept the recommended package in one response or identify only the exceptions.
3. **Rendered site.** After self-review and refinement, show the complete site at desktop and phone sizes, a short interaction recording and remaining meaningful decisions. Compare it to the selected references and agreed storyboard.

Intermediate section progress is visible, but does not create a new approval gate for every group. Reopen decisions for material changes, unresolved dependencies or changes to spend. Use explicit existing delegation within its scope; silence never supplies a decision or budget.

## Voice specimen

Read `copywriting-master` before drafting customer-facing website copy. Record audience, positioning, promise, desired action and evidence available. Propose concrete voice attributes with writing examples: a hero headline and supporting sentence, a service paragraph and a CTA. Include wording to avoid so terms such as “confident,” “premium” or “friendly” have an observable meaning.

Agree this specimen before writing the site. Carry the voice into headings, descriptions, forms, navigation and CTA labels. Write specific benefits, differentiation and reasons to act; an orderly explanation of services alone is insufficient sales copy. Keep claims grounded in supplied facts. Preserve a clear early action for visitors already ready to enquire; adapt the copywriting skill's persuasion sequence to the page's visitor task.

## Button, link and navigation specimen

Show actual proposed controls on light and dark surfaces, with their labels and states, before building the site. Default system:

| Role | Required decisions |
| --- | --- |
| Primary CTA | Strong, high-contrast treatment; large hero/closing size; suitable compact size; versions for light and dark surfaces |
| Secondary CTA | Lower emphasis, visibly subordinate when paired with primary; approved surface treatment |
| Text/navigation link | Clear typography and a deliberate hover/active treatment; remains a link rather than automatically becoming a button |

Agree shape, size, typography, spacing, fill, border treatment and optional icon usage. Show default, hover, pressed, keyboard focus and disabled states where applicable. Include desktop navigation, active page, dropdown and mobile-menu behavior. All primary destinations need real actions in the UX outline.

Do not wrap every link or action in an outlined box, pill or surrounding CTA frame. An outlined secondary is an option to show and approve, not the default for every URL. Keep visible keyboard focus distinct from decorative default borders. Carry the approved system across sections and pages.

## Visual richness and repetition

Build an image/icon plan alongside section selection. For each substantial section, name its visual role and asset: photography, product UI, diagram, illustration, coherent icons, editorial typography or a deliberately text-led composition. Provide relevant imagery beyond the hero. Explain text-led exceptions by their content and composition rather than filling every section with decoration. Icons should clarify services, features or steps and belong to one consistent family.

Identify the page's distinctive moments beyond the hero and show the references that support them. Vary composition, scale, image treatment and pacing according to content. Count repeated layout families in the storyboard; reconsider consecutive identical card grids, alternating splits or repeated page sequences unless repetition serves a clear comparison or established page family. Shared headers, buttons and design tokens should remain consistent.

Judge novelty at page and template level: would the design still feel specific with the logo covered? Which lower sections would a designer point to as reasons to choose this template? If the only answers are the hero, colors or clean spacing, revise the storyboard before extending the build. A different animation on an unchanged generic section does not resolve a composition problem.

## Motion plan

Show references or short previews for the proposed motion language before implementation. Record the target element, trigger, intended effect, timing/sequence, mobile behavior and reduced-motion alternative in the storyboard. Cover hero behavior, navigation, CTA hover, cards and relevant section transitions. Choose distinctive moments suited to this site's concept; support them with restrained shared behavior elsewhere.

Use motion to reveal relationships, direct attention or express the brand. Avoid applying the same slide/fade or card effect to every section, or using arbitrary one-off effects merely to increase variety. Transitions should feel related, while different section roles can receive different choreography. Text, controls and content remain accessible without animation; avoid scroll interference and hover-only information.

For Webflow, implement reusable native styles/interactions and editable assets where practical. For Astro, use shared components/tokens and the lightest suitable CSS or motion code, verifying initialization across navigation when relevant. Neither stack changes the visual bar. Follow `asset-direction.md` for generated video/3D and costs; a motion plan does not authorize production spend.

## Review evidence

Review the complete page and representative sibling pages, not only the strongest hero. Check voice and sales argument, image/icon coverage, section and page repetition, button hierarchy, navigation/hover behavior and motion variety against the agreed package. Watch actual motion, including a phone and reduced-motion pass. Fix routine defects before involving the designer.

Clean spacing and correct responsiveness are necessary but insufficient for an impressive template. Record concrete gaps against the references and fix them; do not use a high subjective score to dismiss visible generic composition. Template-store acceptance remains a separate outcome that requires the store's actual review.


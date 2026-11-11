# Design interview

Use throughout discovery, art direction, section design, asset development and refinement whenever a consequential design decision is unresolved. This is the conversational operating method of the web-design workflow: the agent brings design judgment, references and visible proposals; the designer reacts, and that reaction shapes the next question and iteration. The existing filename is retained for compatibility; this resource covers more than initial intake.

## Run a design interview throughout the build

Treat the site as connected design decisions: audience/offer → positioning and voice → art direction and narrative → section composition → assets and interactions → rendered experience. Each answer changes which decisions are ready to explore. An existing project enters at its first unresolved decision.

The three touchpoints organize designer time. Each is a short back-and-forth with visible proposals, not a one-shot presentation. Reuse this method whenever consequential feedback reopens a branch; preserve settled direction elsewhere.

1. Identify the highest-impact unresolved decision whose prerequisites are known. Research factual gaps independently; resolve routine implementation details yourself.
2. Consult the relevant design knowledge below. Prepare a proposal supported by a reference screenshot, voice sample, rough composition, control specimen, motion preview or rendered section.
3. Ask the smallest useful question, recommend a direction and explain its design/visitor consequence. Group independent choices when efficient; ask dependent questions after the prerequisite answer.
4. Wait where a designer decision is required. Interpret what they liked or rejected: composition, density, subject, tone, hierarchy or motion. Clarify ambiguous reactions that would materially change production.
5. Revise the artifact and decision record, then determine the next unresolved branch. A selected reference needs an adaptation for this content; “more premium” needs a visible interpretation. Do not restart the interview.
6. Execute and self-review within settled direction or explicit delegation. Return with evidence when a meaningful choice remains, rather than asking permission for routine adjustments.

Stop a round when its consequential choices are resolved or delegated and the next useful work belongs to the agent. Resume when another human decision becomes ready. Completion depends on decision readiness, not a fixed question count or an exhaustive interview about every pixel.

## Use the design knowledge behind the interview

Bring judgment and recommendations, rather than asking the designer to invent the site. Route unresolved decisions to relevant resources:

| Decision | Design knowledge | Evidence to show |
| --- | --- | --- |
| Positioning, narrative and voice | Project research and `copywriting-master` | Positioning recommendation, voice samples and section copy |
| Art direction and composition | Shared reference library, desktop/mobile captures, gallery and rebuild notes; miner for gaps | Shortlisted screenshots and adaptations using actual content |
| Hero and supporting assets | `asset-direction.md`, brand material and visual references | Distinct concepts, in-layout still/crops and bounded production plan |
| Controls, navigation and motion | `creative-review.md` and observed interaction examples | Light/dark control specimens and behavior previews |
| Coherence and distinctiveness | `section-review.md`, selected references and storyboard | Full-page sequence, cross-page repetition findings and revisions |
| Implementation and refinement | Project's Webflow/Astro conventions and rendered evidence | Editable sections, desktop/mobile checks and interaction recordings |

Webflow and Astro share this design judgment; implementation mechanics follow the chosen platform. If a resource is unavailable, inspect suitable references directly and record the limitation.

Example: the designer says services feel dull. Inspect the content and composition, then show two relevant alternatives: an image-led service index and asymmetric grouping with a featured service. Recommend one based on hierarchy and available imagery. Ask which hierarchy feels right; adapt the section, inspect the page rhythm, and then determine whether new imagery or motion is needed. Adding the same reveal animation to the existing cards does not answer that feedback.

## Choose a response format

These are workflow tradeoffs, not measured time or quality results.

| Mode | Useful when | Cost or weakness | Recommended use |
| --- | --- | --- | --- |
| Fixed 21-question interview | Starting from nothing; designer wants a thorough interview | Repeats known facts and asks taste questions before examples exist | Offer on request; use the bank for coverage internally |
| Adaptive short interview | A few decisions determine the direction | Can hide assumptions if the agent never records them | Default: ask only consequential gaps, with recommendations |
| Visual preference round | Words such as premium, bold or playful remain ambiguous | Attractive references can distract from the offer | Show three distinct boards with the same representative content |
| Prefilled brief to correct | Existing research, brand work or a familiar client provides context | Designer can overlook unsupported assumptions | Default starting artifact; distinguish known facts from proposals |
| Dictated brief / freeform reply | Designer thinks faster aloud than in forms | Answers arrive out of order and can conflict | Accept one response, organize it, return only unresolved decisions |

**Default:** begin with a prefilled brief, then conduct the design interview using short questions and visible proposals as needed. These formats support the same ongoing conversation. Do not ask the designer to select a process before doing useful preparation. Accept their preferred response format when supplied.

## Prepare before asking

Read project research, existing brand work, copy, references, assets, previous feedback and approvals. Use connected sources when relevant and available. Inspect the existing site and the section library. Do not make the designer report facts already accessible to the agent.

Draft one compact brief: audience and offer; visitor action; positioning and voice; creative direction; required page/section jobs; assets; constraints; unresolved decisions. For each consequential item record its source and status: **confirmed, proposed, unresolved or explicitly delegated**. A sourced fact can be known without the proposed creative treatment being approved. Preserve existing choices; stale or conflicting evidence needs resolution.

Use the bank below as a coverage checklist. Skip answered questions. Defer questions that need visual examples until the boards or control specimens exist. Research factual gaps yourself where possible. Recommend reversible details rather than sending every choice to the designer.

## The 21-question bank

Use these as starting prompts and coverage checks. Follow-up questions come from the designer's answers, project evidence and design judgment; the bank neither determines the order nor limits the interview to 21 questions.

| ID | Question | Drives |
| --- | --- | --- |
| Q01 | Who is the most important visitor, and what situation brings them here? | Audience and relevance |
| Q02 | What are we selling, and why should this visitor choose it over the alternatives? | Offer and differentiation |
| Q03 | What is the main action we want, and what should happen immediately after it? | CTA and conversion path |
| Q04 | Which visitor doubts or objections must the page resolve? | Persuasion and section order |
| Q05 | What genuine evidence can we use: work, reviews, results, people or process? | Proof and asset inventory |
| Q06 | Which pages and content jobs are essential for this release? | UX coverage and scope |
| Q07 | Which proposed voice sample sounds right, and what wording feels wrong? | Brand voice; show samples |
| Q08 | How direct should the sales message be, and which claims or promises are off-limits? | Persuasive intensity and boundaries |
| Q09 | Which brand elements must we preserve, and which can we develop? | Identity constraints |
| Q10 | Which of these three direction boards fits best, and which specific parts would you change? | Art direction; show boards |
| Q11 | What visual patterns or past results should we avoid repeating? | Negative preferences |
| Q12 | Where should the site feel familiar, and where can it be more distinctive? | Creative latitude and usability |
| Q13 | What should visitors recognize or feel from the hero before reading the details? | Hero concept and visitor meaning |
| Q14 | Which available assets should lead, and which proposed asset route best fits the brand? | Client/stock/generated/code choice; show options |
| Q15 | What media budget and attempt limit are authorized, including any separate video scope? | Production cap; unresolved means no paid calls |
| Q16 | Which lower sections should be the memorable moments, and which proposed image/icon treatment supports them? | Visual richness beyond the hero |
| Q17 | Which proposed primary, secondary and text-link treatments fit the brand on light and dark backgrounds? | Button system; show specimen |
| Q18 | Which navigation, hover and motion examples feel right, and what feels excessive? | Interaction language; show examples |
| Q19 | What must remain easy to edit, reuse or integrate in Webflow or Astro? | Build constraints and handoff |
| Q20 | What does success for this release mean, and which references establish the visual bar? | Acceptance criteria and finish level |
| Q21 | Which creative decisions do you want to retain, and which may the agent make within the agreed scope? | Delegation and review boundary |

## Ask only the current gaps

Aim for an initial round of three to five consequential questions when feasible; use smaller groups if the question tool requires it. This is a review-load target, not a rule to omit necessary decisions. Ask dependent questions after their prerequisites are settled. Offer a recommended answer and explain its effect briefly. A designer can answer by IDs, accept a recommendation explicitly, correct the prefilled brief or dictate one reply covering several items.

Example: “Q13 — What should the hero communicate? Recommend dependable local service through a branded van arriving at a cared-for home. Alternative: technician-led expertise. This determines the photo brief.” Show corresponding imagery when the distinction is visual. A verbal answer does not replace the section boards or in-layout asset test.

After the reply, update the brief and show a compact decision summary plus remaining gaps. Do not repeat resolved questions or require a second approval of the same answers. If a vague answer would change production, show a concrete option to clarify it. Preserve uncertainty instead of silently converting a proposal into approval.

If the designer requests all 21 questions, present them grouped by audience/offer, copy/voice, visual direction, assets and execution. Prefill known answers so their work is correction. If they request a very short session, prioritize goal, direction, voice, constraints, spend and delegation; propose remaining reversible details visibly. Never treat lack of time, silence or general creative freedom as a spending authorization.

## Keep later reviews fast

At touchpoint two, lead with the recommended complete storyboard and the few consequential decisions. Keep all substantial section references, full copy and alternatives visibly accessible, with stable IDs. The designer may accept the package or respond only with exceptions such as “S03 B; soften the sales tone; keep the primary button.” Do not require them to choose every section individually.

At touchpoint three, the agent has already compared the rendered site with the agreed references, fixed routine defects and watched the interactions. Lead with the complete preview and only meaningful remaining choices. Do not delegate quality assurance to the designer.

Track repeated feedback in the existing project decision record. Offer to reuse an established voice, button family or interaction language on a later related project; do not assume that preference authorizes the same layouts or assets on every site. Maintain visual variety across templates while preserving agreed brand systems.

## Completion and learning

Intake is ready for direction work when audience, offer, action, constraints and voice needs are known, and unresolved creative questions are attached to the boards/specimens that will resolve them. Paid production remains blocked until its concept and budget are covered. Full implementation follows the agreed UX/copy and storyboard. Reversible proposed details can proceed within existing authorization; record them.

Record the number of unanswered questions sent, review rounds, late direction changes and designer corrections after each project. Use actual results to shorten future intake and improve examples; do not promise that 21 answers or three touchpoints guarantee a distinctive site or store acceptance.

## Source note

Matt Pocock's [grilling skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) is a reference for grouping questions whose prerequisite decisions are settled and separating research from human decisions. This web-design adaptation uses the iterative interview principle with references, copywriting, art direction and rendered critique as its domain knowledge. The 21-question bank is our own set of starting prompts.

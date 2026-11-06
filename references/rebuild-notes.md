# Observed section references

Generated from `patterns/*.json` by `render_pattern_gallery.py`.

Screenshots are reference evidence, not reusable client assets. Scores describe editorial judgments of visual impact and conversion clarity, not measured performance. Observed references have not been validated through a complete rebuild.

## Raycast — atmospheric product hero

ID: `raycast-atmospheric-hero` · Type: hero · Observed: 2026-11-06

Source: [Raycast — atmospheric product hero](https://www.raycast.com/)

Status: observed reference; not rebuild-validated.

Borrow: centered white headline over diagonal red abstract imagery, with a floating dark navigation bar

Editorial scores: conversion clarity 6/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/raycast-hero-desktop.jpg)

Mobile: [view 1](shots/raycast-hero-mobile.jpg)

### Use when

A single product or offer with a distinctive visual world and a short promise. Useful for software, creative tools, or a bold brand launch.

### Avoid when

Visitors who need immediate service details, several competing actions, or genuine product proof within the first screen. The mobile capture has no obvious download CTA in the hero; improve that for acquisition briefs.

### Content slots

Floating brand/navigation; a roughly two-line primary promise; one short supporting paragraph; one primary action. The observed mobile treatment also includes a small secondary keyboard-product link.

### Desktop composition

A near-black full-width scene with diagonal red forms behind a narrow centered text column. The large rounded navigation container floats above it. Light text and a restrained white navigation action contrast with the saturated asset.

### Observed mobile behavior

Observed at a requested 390×844 viewport: the navigation collapses to brand and hamburger; the background crops tightly; the headline wraps into two lines and the description into several. A secondary link sits lower in the composition. The screenshot raster is 375×812 because of browser scaling.

### Rebuild recipe

Start with a semantic header and hero containing a constrained text column. Place a separately authored background asset behind it with cover sizing and an adjustable focal point. Define navigation inset, text width, vertical spacing, and crop as tokens. Add a clear primary action in the hero when required by the brief; do not inherit the source's weak mobile action visibility.

### Asset production

Create or license an abstract still with directional depth, texture, and a deliberately quiet text region. The source asset's production technique was not verified; this reference does not establish that it uses Three.js. A still can implement the composition.

### Adaptation decisions

Borrow directional composition and disciplined hierarchy; replace red with the brand's own asset language. Use real product UI nearby if the promise needs explanation. Keep text and actions as HTML.

### Interaction evidence and gaps

Navigation destinations and collapsed mobile menu were observed. Menu behavior, keyboard interaction, reduced motion, and download completion were not tested.

### Verification

Desktop and mobile screenshots inspected. This is a visual reference, not evidence of conversion uplift or a validated reusable component.

## KUBE Saint-Tropez — cinematic destination hero

ID: `kube-cinematic-hero` · Type: hero · Observed: 2026-11-06

Source: [KUBE Saint-Tropez — cinematic destination hero](https://www.kubehotel-saint-tropez.com/en)

Status: observed reference; not rebuild-validated.

Borrow: full-bleed destination video with lower centered serif headline and a pale-lime booking action

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/kube-hero-desktop.jpg)

Mobile: [view 1](shots/kube-hero-mobile.jpg)

### Use when

A destination, venue, retreat, property, or experience whose visual reality is central to the buying decision.

### Avoid when

Offers without relevant high-quality footage, urgent service requests, or situations where generated scenery could misrepresent the actual premises.

### Content slots

Centered brand mark; language control; reservation/menu controls; a short factual category line; one concise emotional headline; booking action.

### Desktop composition

Viewport-scale footage spans edge to edge. A minimal white header overlays the scene. Category and serif headline occupy the lower center, with the lime action immediately beneath on desktop. A darkening treatment keeps white lettering readable against changing footage.

### Observed mobile behavior

The navigation stays minimal with brand centered and reservation/menu at the right. The headline wraps to two lines over vertically cropped footage. The booking control becomes a wide bar near the bottom. The captures show different moments of the moving scene, not matched frames.

### Rebuild recipe

Create a video/poster layer, contrast overlay, semantic header, and a lower-aligned content region. Use a bounded viewport-height composition that allows long text to grow. Keep the booking control visible within the mobile layout and clear of safe-area insets. Test contrast against the lightest and darkest clip frames.

### Asset production

The live page exposed a background Vimeo player and moving location footage was observed after an initial black loading state. Source authentic footage or shoot the destination; for fictional/concept imagery, generated still-to-video is an option. Deliver a compressed loop, poster, mobile crop, and reduced-motion still.

### Adaptation decisions

Borrow the editorial placement and restrained overlay UI. Art-direct horizon and focal subject around the headline. Improve the initial black loading state with a real poster. Do not copy hotel footage or imply synthetic scenes are real property photographs.

### Interaction evidence and gaps

Video changed between observations; only still captures were saved. Booking controls were observed but no booking was submitted. Loop seams, audio state, autoplay failure, and reduced-motion handling were not tested.

### Verification

Live desktop/mobile inspection and saved screenshots. No performance or conversion measurements.

## Apple MacBook Air — product sculpture hero

ID: `apple-product-sculpture-hero` · Type: hero · Observed: 2026-11-06

Source: [Apple MacBook Air — product sculpture hero](https://www.apple.com/macbook-air/)

Status: observed reference; not rebuild-validated.

Borrow: oversized paired product render above a compact left-aligned identity and price block, balanced by a blue purchase button

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/apple-hero-desktop.jpg)

Mobile: [view 1](shots/apple-hero-mobile.jpg)

### Use when

A physical product with a recognizable silhouette, meaningful material/detail, and excellent rendering or photography.

### Avoid when

Service offers with no visual object, products requiring a dense explanation before an image is meaningful, or builds with only low-resolution packshots.

### Content slots

Dominant product image; product name; concise benefit headline; short variant/performance line; price/terms; purchase action.

### Desktop composition

A pale blue-to-white environment and a large paired laptop composition create an almost sculptural shape. The image dominates the upper region. Below, product identity sits left; pricing/terms and the blue pill action share the lower commercial row. Treat the exact rendering as an asset, not generic CSS decoration.

### Observed mobile behavior

The product is recropped across the narrow screen rather than simply shrinking the desktop composition. Identity, benefit, price, and action remain below the image, with the purchase action at the right of the price area. The captured animation frame overlaps part of the product-name line; treat it as a captured transition, not an alignment to reproduce.

### Rebuild recipe

Make an art-directed responsive picture or a short product animation above a constrained information block. Separate identity, message, terms, and action semantically. Tune the image's aspect ratio and crop at mobile widths. Use a stable still or reserved media dimensions so the purchase content never shifts or gets obscured.

### Asset production

Use client CAD renders, licensed 3D models, or high-quality product photography. Preserve exact product geometry and branding; do not rely on generation for factual hardware detail. A static render can achieve this composition without an interactive runtime.

### Adaptation decisions

Borrow the product-as-sculpture approach and proportion of visual to commercial information. Change the scene and camera to emphasize the client's distinguishing detail. Avoid cloning the laptop pairing if the product has a different visual story.

### Interaction evidence and gaps

Animated product framing was observed. Purchase destinations were visible but checkout, keyboard behavior, and reduced motion were not tested.

### Verification

Desktop crop and mobile viewport capture inspected. Prices and device specifications are not reusable client content.

## Raycast Pro — illustrated feature bento

ID: `raycast-pro-feature-bento` · Type: bento · Observed: 2026-11-06

Source: [Raycast Pro — illustrated feature bento](https://www.raycast.com/pro)

Status: observed reference; not rebuild-validated.

Borrow: three bordered feature cards with distinct colored schematic illustrations between wider product-demo rows

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/raycast-pro-bento-desktop.jpg)

Mobile: [view 1](shots/raycast-pro-bento-mobile.jpg)

### Use when

Several capabilities with distinct mechanisms that can each be explained through a small diagram or cropped UI demonstration.

### Avoid when

Three generic benefits with no demonstration, evidence, or visual differentiation. Filling every tile with an unrelated icon loses the strength of the example.

### Content slots

Section intro/action; wide translation demonstration; three compact feature modules with schematic image, short benefit/description, and feature label; wide theme-customization demonstration.

### Desktop composition

Within a near-black section, the translation scene is wider than the supporting cards. Three equal-width rounded bordered cards share consistent image and copy zones. Purple device diagrams, red history blocks, and blue position dots distinguish the mechanisms. The final wide customization demo provides a different visual density.

### Observed mobile behavior

The wide demonstrations recompose and the three cards stack into a single sequence. Illustrations remain above their explanations. Translation leads, then synchronization/history/window controls, then customization. The saved tall mobile crop shows the entire section; desktop and mobile crops were taken from full-page captures.

### Rebuild recipe

Use a three-column grid for supporting cards with full-span demonstration rows above and below. Build each card from illustration, benefit text, and small feature label. Keep common internal padding and image heights. At a content-driven breakpoint switch to one column and change wide demos to stacked media/text. Match the diagram language across tiles.

### Asset production

Create simple original SVG diagrams for device synchronization, history, and positioning; use accurate product UI for the broad demonstrations. Keep text labels in HTML where practical. A little accent color in each visual does more than decorating every card background.

### Adaptation decisions

Assign tile sizes according to the client's content, and omit modules that add no useful distinction. Reuse visual grammar, line weight, and color roles across the custom illustrations rather than copying the Raycast graphics.

### Interaction evidence and gaps

Some visuals exposed controls or animated content, but their complete interaction behavior was not tested. A static diagram is a valid first implementation; assess any motion separately.

### Verification

Desktop and mobile section crops inspected. Structural recipe inferred from visible layout, not copied source CSS.

## KUBE Saint-Tropez — photographic room bento

ID: `kube-photographic-room-bento` · Type: bento · Observed: 2026-11-06

Source: [KUBE Saint-Tropez — photographic room bento](https://www.kubehotel-saint-tropez.com/en)

Status: observed reference; not rebuild-validated.

Borrow: two half-width photographic room tiles above a full-width room tile, separated by fine light gutters with overlaid serif labels

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/kube-rooms-desktop.jpg), [view 2](shots/kube-rooms-desktop-lower.jpg)

Mobile: [view 1](shots/kube-rooms-mobile.jpg), [view 2](shots/kube-rooms-mobile-lower.jpg)

### Use when

A small set of spaces, destinations, projects, or product categories with strong authentic imagery and short labels.

### Avoid when

Categories that require long explanations, a strict side-by-side specification comparison, or weak photos that cannot sustain large crops.

### Content slots

Centered eyebrow and section heading; three category tiles; each tile has full-bleed imagery, short category label, and one exploration link.

### Desktop composition

An off-white introduction leads into an edge-to-edge two-column image grid. Two category tiles occupy the first row; the third spans the full width below. Fine light seams separate the images. White serif labels and compact links sit toward the lower center over darkened imagery. There are no pill-shaped card containers.

### Observed mobile behavior

All three categories become full-width stacked image panels in source order. Labels remain inside the images, with tall crops preserving an immersive view. Separate viewport captures show the first and second panels and the beginning of the third; they are complementary views, not a stitched page.

### Rebuild recipe

Use a two-column semantic list with the third item spanning both columns. Give tiles an explicit aspect ratio and an absolutely positioned image plus readable lower overlay. On narrow widths remove spans and use a one-column sequence with independently chosen crops. Make the meaningful category label the accessible link name.

### Asset production

Source genuine category photographs with enough detail for large panels. The live tiles changed between imagery during inspection; some saved frames contain a crossfade. A single well-chosen image per category is a sound static implementation. Do not use generated room scenes as factual inventory.

### Adaptation decisions

Use the mixed-span photographic composition for a client's projects, services with tangible outcomes, or product families. Define why the third item earns the wide span; change the order if another item has higher priority. Add outside descriptions if labels alone cannot communicate the difference.

### Interaction evidence and gaps

Exploration links and changing imagery were observed; link destinations were not exercised. For a rebuild, verify focus visibility, contrast throughout any image change, touch targets, and static fallback.

### Verification

Live layout and mobile stack inspected. Viewport screenshots replaced a distorted full-page capture caused by the source's scrolling behavior.

## Attio — workflow demonstration bento

ID: `attio-workflow-bento` · Type: bento · Observed: 2026-11-06

Source: [Attio — workflow demonstration bento](https://attio.com/#home-2026-generate-pipeline)

Status: observed reference; not rebuild-validated.

Borrow: a dominant full-width product workflow demonstration above two supporting mechanism cards inside a hairline grid

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/attio-bento-desktop.jpg), [view 2](shots/attio-bento-desktop-lower.jpg)

Mobile: [view 1](shots/attio-bento-mobile.jpg), [view 2](shots/attio-bento-mobile-lower.jpg)

### Use when

A complex product where one workflow can anchor two supporting capabilities. Works when product artifacts provide more meaning than decorative imagery.

### Avoid when

Offers without demonstrable UI or concepts that require all tiny interface text to be legible on mobile. The source scales its product table down substantially on phones.

### Content slots

Workflow navigation; one outcome-led introduction; wide product scene; two supporting cards, each with a benefit/description and illustrative mechanism.

### Desktop composition

A sticky left workflow rail sits beside the main canvas on desktop. The main canvas uses a light background, thin dividers, a large table-and-email demonstration, and two half-width cards beneath. Copy uses a darker leading claim and lighter continuation. Minimal borders provide structure without heavy shadows.

### Observed mobile behavior

The left rail becomes a horizontally arranged sticky workflow navigation under the header. The article is single-column: intro, scaled wide demonstration, then stacked supporting cards. The second mobile capture shows the two supporting mechanisms in their vertical reading order.

### Rebuild recipe

Use an outer navigation/content grid and an article with a full-span demo above a two-column supporting grid. Keep the product scene in its own media container. At mobile widths move navigation to a horizontal row and stack supporting cards. Simplify the demo or provide a closer detail view if understanding depends on tiny table text.

### Asset production

Build original schematic UI from the client's real workflow or capture accurate sanitized product screens. The source demonstration contains sample CRM records and an email composer; do not reuse its customer names or treat them as proof. Lightweight vector or HTML scenes can replace a large video when the mechanism is simple.

### Adaptation decisions

Keep the sequence of context, main mechanism, and supporting details. Adjust border, type, spacing, and accent roles to the site system. Use optional sticky navigation only when there are enough workflows to justify it.

### Interaction evidence and gaps

The Build pipeline anchor was exercised and scrolled to the article. Mobile navigation transformed as described. Demo animations were observed, but no email was sent and demo controls, keyboard behavior, and reduced motion were not tested.

### Verification

Live desktop/mobile inspection and complementary viewport captures. No complete rebuild or conversion measurement.

## Instrument — service rows with directly relevant project proof

ID: `instrument-services` · Type: services · Observed: 2026-11-06

Source: [Instrument — service rows with directly relevant project proof](https://www.instrument.com/services/)

Status: observed reference; not rebuild-validated.

Borrow: a service promise and learn-more route beside two relevant project thumbnails with concise case summaries

Editorial scores: conversion clarity 9/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/instrument-services-desktop.jpg)

Mobile: [view 1](shots/instrument-services-mobile.jpg)

### Use when

A studio with a few clearly differentiated service families and two strong projects for each.

### Avoid when

A new business without relevant work, or a large catalog whose offers require functional comparison rather than repeated editorial rows.

### Content slots

Service name; outcome promise; detail route; two project visuals; client names; short project summaries; case-study destinations.

### Desktop composition

A deep purple section introduces each service in a generous horizontal row. The left column uses a large serif name, short sans promise and pale pill action; the right has two rounded landscape thumbnails with names and descriptions below.

### Observed mobile behavior

The service heading, promise and action precede a vertical sequence of project cards. Project captions remain below imagery and a visible View Case Study action appears in the saved phone view.

### Rebuild recipe

Store each service with its promise, detail destination and selected project records. Use a weighted two-region desktop grid with a two-column proof subgrid. Stack service content before proofs on phones. Keep thumbnail, title and action tied to the same destination without duplicate confusing tab stops.

### Asset production

Use two actual client project posters per service, with consistent crop ratios and color treatment. Supply real project summaries and destinations. Prepare static posters before adding video; source project media is study material.

### Adaptation decisions

Name services in customer language and make the promise distinct. Show only projects that demonstrate that capability. Reduce repetition if several services share the same two projects, and keep any qualification or scope details on the linked service page.

### Interaction evidence and gaps

Service rows and project destinations inspected. The service-detail and case-study routes were not opened from these cards; no hover or media playback behavior was validated.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores describe editorial conversion clarity and visual impact, not measured performance. No complete rebuild validation.

## Humaan — six capability groups in a quiet type-led matrix

ID: `humaan-services` · Type: services · Observed: 2026-11-06

Source: [Humaan — six capability groups in a quiet type-led matrix](https://www.humaan.com/about)

Status: observed reference; not rebuild-validated.

Borrow: six clearly titled capability lists arranged in a three-by-two matrix without decorative card chrome

Editorial scores: conversion clarity 8/9; visual impact 6/9. No measured uplift.

Desktop: [view 1](shots/humaan-services-desktop.jpg)

Mobile: [view 1](shots/humaan-services-mobile.jpg)

### Use when

An established provider with a broad, concrete capability set that buyers need to check.

### Avoid when

A primary offer that needs differentiation or persuasion; the matrix is supporting scope, not a complete service pitch.

### Content slots

Capability introduction; six meaningful group names; short capability labels; relevant next route elsewhere on the page.

### Desktop composition

Six evenly spaced groups sit on a pale blue field in three columns and two rows. Bold dark headings and left-aligned text lists supply hierarchy. Generous gutters and row spacing keep the dense inventory calm.

### Observed mobile behavior

The groups become one vertical column, preserving their reading order. The phone view shows the first two complete groups and the start of the third. The source bottom navigation overlaps lower content at times.

### Rebuild recipe

Model groups and items as semantic heading/list pairs. Use a three-column grid with consistent group gaps; collapse to one column when labels wrap awkwardly. Keep actual list text selectable and avoid individual cards unless the items need navigation.

### Asset production

A considered type system and accurate capability inventory suffice. This pattern requires no decorative stock or generated imagery.

### Adaptation decisions

Use buyer-recognizable group labels, prune overlapping items and distinguish ongoing support from initial delivery. Pair the matrix with a concise offer and proof. Provide a nearby inquiry or service-detail route and keep sticky UI clear of content.

### Interaction evidence and gaps

Static capability groups and responsive reflow inspected. No list interaction exists in the observed matrix; expertise navigation and inquiry routes were not exercised. Initial captures affected by the page's scroll animation were replaced.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores describe editorial conversion clarity and visual impact, not measured performance. No complete rebuild validation.

## ustwo — engagement offers with activities, outcomes and proof

ID: `ustwo-services` · Type: services · Observed: 2026-11-06

Source: [ustwo — engagement offers with activities, outcomes and proof](https://ustwo.com/services/)

Status: observed reference; not rebuild-validated.

Borrow: an outcome-led service module with engagement timing, representative clients, explicit activities, outcomes and a relevant quote

Editorial scores: conversion clarity 9/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/ustwo-services-desktop.jpg)

Mobile: [view 1](shots/ustwo-services-mobile.jpg), [view 2](shots/ustwo-services-mobile-proof.jpg)

### Use when

A considered consulting engagement whose scope and outputs materially affect purchase decisions.

### Avoid when

A quick commodity service or an offer with insufficient evidence to support lengthy scope and proof.

### Content slots

Engagement phase; indicative duration; buyer goal; relevant client marks; short explanation; activities; expected artifacts/outcomes; attributed quote.

### Desktop composition

A restrained white module divides a large goal statement and client marks on the left from explanation and paired activities/outcomes lists on the right. Phase and duration sit above. A large italic testimonial with an orange quotation mark follows.

### Observed mobile behavior

The module becomes phase/duration, goal, marks, explanation, activities, then outcomes in one column. The supporting quote follows with attribution before the next offer begins; complementary phone views capture both portions.

### Rebuild recipe

Create a repeated engagement module with scope and outcome fields separated in the data. Use a two-column desktop layout, then a small internal list grid. Stack in logical reading order on phones. Keep duration as a qualified expectation, not an unexplained guarantee.

### Asset production

Approved client marks, a relevant attributed quote and a precise engagement definition. Typography and spacing carry the visual design; no large hero image is necessary.

### Adaptation decisions

Express the service as the customer's goal. Make activities concrete and outputs useful enough to inform a buying decision. Replace generic outcome promises with deliverables or success criteria that the team can actually commit to.

### Interaction evidence and gaps

Services navigation and cookie dismissal were used. Scope lists, proof links and responsive order inspected; linked client stories, inquiry submission and any sales qualification flow were not tested.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores describe editorial conversion clarity and visual impact, not measured performance. No complete rebuild validation.

## Instrument — filterable work grid with separate display modes

ID: `instrument-portfolio` · Type: portfolio · Observed: 2026-11-06

Source: [Instrument — filterable work grid with separate display modes](https://www.instrument.com/work/grid)

Status: observed reference; not rebuild-validated.

Borrow: category chips and an independent grid/stack switch above large rounded project posters with compact labels

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/instrument-portfolio-desktop.jpg), [view 2](shots/instrument-portfolio-desktop-filter.jpg)

Mobile: [view 1](shots/instrument-portfolio-mobile.jpg)

### Use when

A substantial project archive with a small meaningful set of service categories.

### Avoid when

A small portfolio where filters hide scarce evidence or categories overlap so much that the selection adds little value.

### Content slots

Portfolio introduction; category controls; current selection; display control; project poster; client/project name; category tags; project destination.

### Desktop composition

A large brand heading precedes a thin rule and controls, with filters left and display mode right. In grid mode, two equally sized rounded image blocks sit in each row, with short client names and uppercase category labels below.

### Observed mobile behavior

Grid cards become one column. The filter area condenses to a Filter control plus the selected category and a small Grid control. Project images keep generous size and names remain below them.

### Rebuild recipe

Separate category and display state. Use real links with URL state when filtered pages are addressable; preserve category when changing display. Render project cards from one dataset and reserve image aspect ratios. Provide a meaningful no-results state and selected-control semantics.

### Asset production

Original project posters with consistent crops, current project metadata and actual case-study destinations. Use static imagery as a dependable base; animated previews should have posters and reduced-motion alternatives.

### Adaptation decisions

Choose categories customers can use to assess relevance. Add a one-line project result if client names alone are insufficient. Reduce the source's large control-to-grid gap for a compact homepage version.

### Interaction evidence and gaps

Grid mode was opened from the display control, then the product category selected; the resulting route retained /grid and the product chip was visibly selected. Phone controls were inspected but not opened. Several Vimeo embeds in stack mode were unavailable; grid posters loaded.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores describe editorial conversion clarity and visual impact, not measured performance. No complete rebuild validation.

## Humaan — featured project followed by paired visual cards

ID: `humaan-portfolio` · Type: portfolio · Observed: 2026-11-06

Source: [Humaan — featured project followed by paired visual cards](https://www.humaan.com/work)

Status: observed reference; not rebuild-validated.

Borrow: one wide flagship project leading into paired portrait-like project cards, with captions moved below images on phones

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/humaan-portfolio-desktop.jpg), [view 2](shots/humaan-portfolio-desktop-grid.jpg)

Mobile: [view 1](shots/humaan-portfolio-mobile.jpg)

### Use when

A curated portfolio with one strong lead project and enough distinctive finished work to support varied crops.

### Avoid when

An exhaustive archive where consistent compact scanning matters more than curation, or imagery too weak to carry large cards.

### Content slots

Short work promise; sector/category routes; flagship poster; subsequent project posters; persistent project names; case-study destinations.

### Desktop composition

On a warm light background, a nearly full-width rounded flagship card is followed by two large rounded cards per row. Website mockups and photography are composed as project-specific posters. Names sit at the bottom-left of desktop imagery.

### Observed mobile behavior

Category routes wrap as pills. All projects become one column; the first project's name sits outside the image below, improving readability at small size. Floating bottom navigation can overlap the next card.

### Rebuild recipe

Use a two-column grid with an explicit featured item spanning both columns. Define project-specific desktop and phone crops; move captions into normal flow at the mobile breakpoint. Keep each card a clearly named link with focus treatment independent of image motion.

### Asset production

High-quality finished-work posters combining actual product views, brand graphics or photography. Prepare alternate crops and sufficient contrast behind desktop captions. Avoid manufacturing client work or implying unperformed projects.

### Adaptation decisions

Choose the flagship based on relevance to the buyer, not just visual spectacle. Add discipline or outcome captions where project names lack context. Keep captions visible on touch devices and position persistent navigation away from them.

### Interaction evidence and gaps

Category destinations and project links inspected; category navigation, hover previews and project detail pages were not exercised. Featured remained the active route; the bright Education chip in the phone capture is a pointer-hover treatment.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores describe editorial conversion clarity and visual impact, not measured performance. No complete rebuild validation.

## Locomotive — project index with expandable rich previews

ID: `locomotive-portfolio` · Type: portfolio · Observed: 2026-11-06

Source: [Locomotive — project index with expandable rich previews](https://locomotive.ca/en/work)

Status: observed reference; not rebuild-validated.

Borrow: a scannable name/industry/location index that expands one project into imagery, scope and clear case-study/live-site routes

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/locomotive-portfolio-desktop.jpg), [view 2](shots/locomotive-portfolio-desktop-preview.jpg)

Mobile: [view 1](shots/locomotive-portfolio-mobile.jpg), [view 2](shots/locomotive-portfolio-mobile-preview.jpg)

### Use when

A larger project archive whose industries and geography meaningfully help visitors select work.

### Avoid when

A short portfolio that would be better shown immediately or a gallery where hidden imagery adds unnecessary friction.

### Content slots

Portfolio promise; project count/filter; project name; industry; location; expand/collapse; preview image; scope; summary; year; case-study and live-site destinations.

### Desktop composition

A white typographic index aligns names, industries and locations in three broad columns. Opening a row inserts scope/thumbnail at left, a large project visual in the center and summary/actions at right, with later rows pushed below.

### Observed mobile behavior

Rows show name and industry beside a thumbnail and plus/minus control; location drops from the visible row. The expanded project stacks scope, summary and actions before the large visual. A native category selector appears in the DOM.

### Rebuild recipe

Store row metadata and preview content together. Use explicit disclosure buttons with expanded state, controlled panels and keyboard support. Preserve the row's location during expansion. Build desktop preview grid areas and a deliberate phone order instead of shrinking the desktop layout.

### Asset production

Real project thumbnails and larger preview images, concise scope/summary, year and correct detail/live destinations. Supply optimized small previews and replace loading placeholders with useful posters.

### Adaptation decisions

Use metadata relevant to the buyer; a local contractor might show service/location/year instead of creative discipline. Keep the case-study route distinct from the external live site. Maintain accessible names even when the visual affordance is a plus sign.

### Interaction evidence and gaps

FinalFinal was opened from its row, revealing a named preview and two destination links. Close collapsed it. Filter selection, keyboard behavior and onward links were not tested. Some later phone thumbnails were still low-resolution loading placeholders.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores describe editorial conversion clarity and visual impact, not measured performance. No complete rebuild validation.

## Instrument / Oura — rationale, paired deliverables and a time-bounded impact block

ID: `instrument-case` · Type: case-study · Observed: 2026-11-06

Source: [Instrument / Oura — rationale, paired deliverables and a time-bounded impact block](https://www.instrument.com/work/oura-smart-ring)

Status: observed reference; not rebuild-validated.

Borrow: a case-study sequence that connects design rationale to paired product/site visuals and a concise post-launch impact list

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/instrument-case-desktop-visual.jpg), [view 2](shots/instrument-case-desktop-approach.jpg), [view 3](shots/instrument-case-desktop.jpg)

Mobile: [view 1](shots/instrument-case-mobile.jpg)

### Use when

A substantial redesign with documented research, finished artifacts and credible post-launch evidence.

### Avoid when

A project with attractive mockups but no support for its claimed outcomes, or a case where a simple before/after image is sufficient.

### Content slots

Client and challenge; design rationale; implementation principles; paired deliverable visuals; impact time window; result measures; attributed client proof; project roles.

### Desktop composition

The case uses a dark slate field with light editorial prose in a narrower centered column. Two tall rounded visual panels show the product treatment beside its mobile website context. A later full-width impact heading and large bullet list state results with a post-launch window.

### Observed mobile behavior

The impact heading and large result bullets become a single readable column. The saved phone frame includes the following media container, which failed to load in this environment. Desktop stills provide the usable visual evidence.

### Rebuild recipe

Build the story from distinct context, decision, artifact and impact modules. Alternate reading-width text with wider media pairs. Store result value, unit, definition, period and evidence separately from visual styling. Stack media on phones and use explicit static posters if video cannot play.

### Asset production

Client-owned finished product/site images, original rationale and verified analytics with permission to publish. Prepare paired crops that explain the relationship between product and experience, plus video posters and accessible descriptions.

### Adaptation decisions

Use only the client's actual results. Specify baseline, metric definition and observation period; the source's mobile-performance percentage is ambiguous and should not be copied as a complete measurement. Distinguish correlation from demonstrated causal impact.

### Interaction evidence and gaps

Rationale, paired visuals, impact text and project roles inspected. No video was played, and some embedded media was unavailable. The results are source-reported claims, not independently verified conversion evidence.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores describe editorial conversion clarity and visual impact, not measured performance. No complete rebuild validation.

## ustwo / RVO Health — contextualized impact cards before the deeper story

ID: `ustwo-case` · Type: case-study · Observed: 2026-11-06

Source: [ustwo / RVO Health — contextualized impact cards before the deeper story](https://ustwo.com/work/rvo-health/)

Status: observed reference; not rebuild-validated.

Borrow: an early impact section with three comparable result cards, each keeping its baseline or timeframe next to the headline figure

Editorial scores: conversion clarity 8/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/ustwo-case-desktop-intro.jpg), [view 2](shots/ustwo-case-desktop.jpg)

Mobile: [view 1](shots/ustwo-case-mobile.jpg)

### Use when

A product or service case with a few comparable, well-defined outcomes and a deeper explanation available below.

### Avoid when

Results without denominators, baseline or timeframe, or an engagement story being misrepresented as a validated clinical outcome.

### Content slots

Project identity and deliverable image; plain-language purpose; impact intro/timeframe; three result cards; comparison context; explanation; attributed proof; challenge; partnership; approach; next steps.

### Desktop composition

A large product illustration introduces the case. The later dark impact band uses a centered reading-width heading/introduction, a wider row of three navy cards, then supporting prose. Bright figure labels and larger explanatory text separate the measure from its context.

### Observed mobile behavior

The three impact cards stack in a single column with their comparison text intact. The explanatory narrative follows. The source uses very small condensed metric labels even on desktop; increase their size in an adaptation.

### Rebuild recipe

Use a case-study article with separate context, impact, challenge and approach sections. Render impact cards from value/unit/baseline/period/evidence records. Set a shared desktop card grid and one-column phone layout; use actual text rather than embedding metrics into images.

### Asset production

A real product poster with approved sample content, permissioned customer quote and documented measurement definitions. Protect user data in product captures; use synthetic examples for sensitive content while keeping the actual product design faithful.

### Adaptation decisions

Retain comparison and timeframe beside each number. Treat engagement measures as engagement, and specify the actual outcome being claimed. Review any clinical or regulated assertion with the evidence owner. Update dated future-tense rollout language rather than copying it.

### Interaction evidence and gaps

The case was opened through the studio's work card. Context, impact cards and the challenge/approach structure were inspected. Video and inquiry routes were not exercised. Reported results and rollout claims were not independently verified.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores describe editorial conversion clarity and visual impact, not measured performance. No complete rebuild validation.

## Lime / TOKEN2049 — project facts, before/after evidence and an explained experiment

ID: `lime-case` · Type: case-study · Observed: 2026-11-06

Source: [Lime / TOKEN2049 — project facts, before/after evidence and an explained experiment](https://limestud.io/work/token2049)

Status: observed reference; not rebuild-validated.

Borrow: a concise scope table and visual A/B comparison connected to a result explanation that includes timeframe and sample sizes

Editorial scores: conversion clarity 9/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/lime-case-desktop-visual.jpg), [view 2](shots/lime-case-desktop.jpg), [view 3](shots/lime-case-desktop-outcomes.jpg)

Mobile: [view 1](shots/lime-case-mobile.jpg), [view 2](shots/lime-case-mobile-outcomes.jpg)

### Use when

A design engagement with real strategic tradeoffs, visible deliverables and publishable comparison evidence.

### Avoid when

Uncontrolled projects presented as experiments, or a case with no permission to show the previous design or its performance data.

### Content slots

Project identity; brief; duration/status; category; scope; attributed customer proof; strategic decision and tradeoff; approach; before/after artifact; result method; lasting operational outcome; inquiry route.

### Desktop composition

The white overview uses a serif heading, short context paragraph and thin ruled fact rows with labels left and values right. Dark green proof and visual regions interrupt the narrative. A large side-by-side A/B checkout image provides visual evidence; a later outcome section explains the comparison before the final inquiry band.

### Observed mobile behavior

Overview facts become label/value stacks within ruled rows. Outcome prose becomes a narrow reading column with the reported timeframe and comparison counts kept together. Complementary phone views capture brief and results separately.

### Rebuild recipe

Create a reusable case schema for context, project facts, decisions, artifacts and evidence. Use a definition list for project facts, reading-width narrative sections and a dedicated comparison figure with captions. Keep outcome method next to its claimed result; let phones open or zoom dense comparison artwork.

### Asset production

Approved project artifacts, permission to show earlier/new designs, an actual experiment summary and an attributed quote. Provide legible individual comparison images for phones instead of relying solely on a dense combined screenshot.

### Adaptation decisions

Explain what the team chose and what it gave up. Report dates, sample sizes and outcome definitions when available. Only claim statistical significance when the client can supply the analysis; the source's test and uplift are reported, not independently audited here.

### Interaction evidence and gaps

Overview, strategy, approach, comparison artwork and outcome explanation inspected. No checkout, booking or experiment was executed. The screenshot's image alt describes an older partnership-page visual, while the observed artwork is an A/B checkout comparison; the recipe follows the observed image.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores describe editorial conversion clarity and visual impact, not measured performance. No complete rebuild validation.

## Humaan — staged culture photography and a large purpose statement

ID: `humaan-about` · Type: about · Observed: 2026-11-06

Source: [Humaan — staged culture photography and a large purpose statement](https://www.humaan.com/about)

Status: observed reference; not rebuild-validated.

Borrow: a deliberately art-directed group scene followed by a large purpose statement and varied culture-image rail

Editorial scores: conversion clarity 7/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/humaan-about-desktop.jpg), [view 2](shots/humaan-about-desktop-lower.jpg)

Mobile: [view 1](shots/humaan-about-mobile.jpg), [view 2](shots/humaan-about-mobile-lower.jpg)

### Use when

A people-led service business with a distinctive culture and budget for original photography.

### Avoid when

A company relying on stock team photos, or an urgent lead-generation page where a long introductory scene delays the task.

### Content slots

Short positioning statement; staged group photo; purpose paragraph; highlighted phrase; culture images; client proof below.

### Desktop composition

A pale blue full-width scene places the group against a coordinated set. Oversized introductory type belongs to the opening scene. Below, a large left-aligned purpose paragraph highlights its opening phrase in purple; rounded culture images create an offset horizontal strip.

### Observed mobile behavior

The headline wraps over the upper scene; the group becomes a panoramic band. Purpose text becomes a narrow large-type paragraph, followed by smaller cropped culture images. A floating bottom navigation overlaps the source content at times; it is not required for this section.

### Rebuild recipe

Separate positioning, group scene, purpose and culture media into modules. Use a deliberately composed responsive image rather than absolute-positioning individual people. Set a readable max width and fluid type for the purpose paragraph. Give culture images consistent corner radii but varied ratios, with scrollable overflow on phones.

### Asset production

Commission a real team shoot with a unified backdrop, wardrobe palette and props, plus candid working images. Plan a wide group composition and a mobile-safe crop; generate only supporting abstract artwork, never substitute invented staff for actual employees.

### Adaptation decisions

Tie the culture to a specific client benefit. Keep introductory copy concise and add a route to work/contact nearby if used on a conversion page. Use a static layout and poster when motion is reduced; check that floating UI does not cover text.

### Interaction evidence and gaps

Scroll-triggered scene changes and the culture-image strip were observed. No horizontal dragging, navigation or client links were exercised. Initial captures affected by the changing scene geometry were replaced.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores are editorial judgments, with no measured conversion result or complete rebuild validation.

## Linear — company thesis beside an editorial narrative

ID: `linear-about` · Type: about · Observed: 2026-11-06

Source: [Linear — company thesis beside an editorial narrative](https://linear.app/about)

Status: observed reference; not rebuild-validated.

Borrow: a wide founder-video context above a two-column company thesis and concise supporting narrative

Editorial scores: conversion clarity 8/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/linear-about-desktop.jpg), [view 2](shots/linear-about-desktop-lower.jpg)

Mobile: [view 1](shots/linear-about-mobile.jpg)

### Use when

A product company with a strong thesis and enough real history to support it.

### Avoid when

A company with little substantive narrative, or a short homepage block that cannot support the video and reading length.

### Content slots

Video/poster; thesis heading; opening argument; product purpose; founding/adoption context; team culture; next people section.

### Desktop composition

A wide video sits above the narrative. The lower section places a compact large heading in the left half and a narrower text column on the right. The opening paragraph is larger/brighter than the supporting paragraphs, with generous vertical spacing on black.

### Observed mobile behavior

Heading and narrative stack into one reading column. The selected phone view includes the full thesis and supporting paragraphs; the team heading begins below a faint separator. A sliver of video remains above.

### Rebuild recipe

Use an optional media block followed by a two-column section. Keep heading and prose independent, with a reading width around 50–65 characters for supporting text. Stack heading before text on phones; retain paragraph hierarchy and spacing.

### Asset production

A real founder/product interview with a deliberate poster, captions and transcript; otherwise use a relevant static image or omit media. Supply verified company milestones and proof.

### Adaptation decisions

Lead with the client's actual point of view. Replace adoption counts and named customers with verified evidence. Keep a short version for homepages and route longer history to an about page.

### Interaction evidence and gaps

Video controls were visible in a paused initial state. Playback, audio, captions and hiring/profile links were not tested. The reference records narrative layout, not the truth of every company claim.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores are editorial judgments, with no measured conversion result or complete rebuild validation.

## Stripe — illustrated company manifesto in a narrow reading column

ID: `stripe-about` · Type: about · Observed: 2026-11-06

Source: [Stripe — illustrated company manifesto in a narrow reading column](https://stripe.com/about)

Status: observed reference; not rebuild-validated.

Borrow: a small architectural line drawing above a restrained company essay with evidence linked directly in the prose

Editorial scores: conversion clarity 7/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/stripe-about-desktop.jpg)

Mobile: [view 1](shots/stripe-about-mobile.jpg)

### Use when

An established organization explaining a substantive mission or investment philosophy to partners, recruits and informed buyers.

### Avoid when

A skim-first campaign page or an organization whose mission copy would be generic at essay length.

### Content slots

Original line illustration; concise opening position; purpose; linked customer evidence; operating principles; onward routes for inquiry, documentation and careers.

### Desktop composition

White space surrounds a modest monochrome architectural drawing. A centered narrow text column sits below with even paragraph rhythm and underlined evidence links. The top header retains a sales route; the essay ends with three intent-specific onward links.

### Observed mobile behavior

The illustration shrinks and the reading column expands within phone gutters. Paragraph hierarchy and underlined links remain; the opening mission, purpose and first proof paragraph are visible in the saved frame.

### Rebuild recipe

Use a semantic article with a fixed maximum reading width, consistent paragraph spacing and clearly distinguishable links. Place a responsive illustration above it with intrinsic dimensions. Keep onward actions as a separate navigation group after the essay.

### Asset production

Commission or license an illustration connected to the client's actual work. Write a specific, fact-checked manifesto and supply the evidence destinations. A drawing can be generated from original direction if reviewed for architectural coherence.

### Adaptation decisions

Use only enough prose to explain the real point of view. Turn unsupported scale claims into verified evidence or remove them. Provide a clear route to relevant work or inquiry so a reader has a next step.

### Interaction evidence and gaps

Inline link destinations and final sales/docs/careers routes were inspected in the DOM; they were not opened. This is the currently observed about-page layout, not an assumed historical Stripe design.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores are editorial judgments, with no measured conversion result or complete rebuild validation.

## Humaan — staggered portrait grid with persistent role labels

ID: `humaan-team` · Type: team · Observed: 2026-11-06

Source: [Humaan — staggered portrait grid with persistent role labels](https://www.humaan.com/about)

Status: observed reference; not rebuild-validated.

Borrow: four staggered portrait columns with small name-and-role pills that remain visible over each image

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/humaan-team-desktop.jpg), [view 2](shots/humaan-team-desktop-intro.jpg)

Mobile: [view 1](shots/humaan-team-mobile.jpg)

### Use when

A sizable service team with comparable photos and clear individual roles.

### Avoid when

A tiny founding team, an incomplete directory, or inconsistent headshots that cannot support an aligned visual system.

### Content slots

Team introduction; group image; person portrait; name; role; optional hiring route after the directory.

### Desktop composition

A blue group image and large team headline introduce the people section. Below, four rounded portrait columns are vertically staggered against a pale blue background. Each portrait carries a white capsule with a dark name segment and a readable role segment.

### Observed mobile behavior

The multi-column grid becomes a single column of large rounded portraits. Name and role remain on the image. Floating bottom navigation can overlap nearby labels in the source capture; position such UI clear of content in a rebuild.

### Rebuild recipe

Model people as an ordered list with image, name and role. Use a four-column desktop grid with controlled offsets, retaining a logical DOM order. Collapse to one column at narrow widths. Make labels actual HTML and keep them readable without hover or animation.

### Asset production

Consistent real portraits with comparable background, lighting, pose scale and ample crop room. The source uses varied portrait media; prepare still posters and reserve any motion for optional enhancement.

### Adaptation decisions

Choose a layout density proportional to team size. Keep roles specific enough to explain who does what. Confirm consent, current titles and image rights. Never use generated faces as real staff.

### Interaction evidence and gaps

Static identity/role labels and responsive reflow were inspected. Portrait hover or playback behavior and hiring navigation were not exercised; motion should be treated as an optional proposed enhancement.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores are editorial judgments, with no measured conversion result or complete rebuild validation.

## Team Design — text directory with inline portrait biographies

ID: `teamdesign-team` · Type: team · Observed: 2026-11-06

Source: [Team Design — text directory with inline portrait biographies](https://team.design/about/)

Status: observed reference; not rebuild-validated.

Borrow: a compact name-and-role directory whose selected row expands into a portrait and detailed biography

Editorial scores: conversion clarity 8/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/teamdesign-team-desktop.jpg), [view 2](shots/teamdesign-team-desktop-bio.jpg)

Mobile: [view 1](shots/teamdesign-team-mobile.jpg), [view 2](shots/teamdesign-team-mobile-bio.jpg)

### Use when

A consultancy whose individual backgrounds matter but whose full biographies would overwhelm an always-expanded grid.

### Avoid when

A very small team or a page needing immediate contact with named staff instead of longer biographies.

### Content slots

Directory heading; person; precise role; biography trigger; portrait; supporting biography; close control.

### Desktop composition

A spare white layout aligns names in a narrow left column and muted roles in a wider right column. Selecting a person inserts a large portrait below the name and the full biography beside it, pushing later rows down.

### Observed mobile behavior

Each name sits above its role. An expanded profile places the portrait before the biography in one column. The saved phone states show the compact directory and the expanded first profile; a full long-bio scroll was not captured.

### Rebuild recipe

Use one ordered people dataset and disclosure buttons with aria-expanded/aria-controls. Keep each biography adjacent to its trigger in DOM order. Expand an inline grid for portrait/prose on desktop and stack it on phones. Return focus sensibly on close and ensure content height follows text.

### Asset production

Real headshots, approved biographies and current roles. Portraits can be conventional; the typography and directory structure supply the character.

### Adaptation decisions

Lead biographies with expertise relevant to the client decision. Limit visible summaries and disclose detail on demand. Distinguish leadership from directory order if the business needs that hierarchy.

### Interaction evidence and gaps

Read more about Matt Basford expanded a portrait and biography inline. The visible Close control collapsed it. Keyboard activation, focus return, opening multiple profiles and all other people were not tested.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores are editorial judgments, with no measured conversion result or complete rebuild validation.

## Lime Studio — complementary founders with cinematic portraits

ID: `lime-team` · Type: team · Observed: 2026-11-06

Source: [Lime Studio — complementary founders with cinematic portraits](https://limestud.io/)

Status: observed reference; not rebuild-validated.

Borrow: two equal cinematic portraits followed by separate practice labels and concise experience summaries

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/lime-team-desktop.jpg), [view 2](shots/lime-team-desktop-intro.jpg)

Mobile: [view 1](shots/lime-team-mobile.jpg), [view 2](shots/lime-team-mobile-lower.jpg)

### Use when

A small partnership where customers actually work with both named principals.

### Avoid when

A larger organization whose delivery cannot truthfully promise direct founder involvement.

### Content slots

Working-relationship promise; role split; two portraits; names; disciplines; concise experience; optional professional profiles.

### Desktop composition

A wide serif relationship statement and short explanation precede two equal landscape portraits on dark green. Each portrait has a name, acid-green uppercase discipline, a narrow experience summary and a small social route.

### Observed mobile behavior

The two founder cards stack. Each keeps portrait, name, discipline, experience and profile route together. Complementary phone frames show both founders instead of squeezing them into a narrow pair.

### Rebuild recipe

Use a short intro followed by a two-item list in equal columns. Give portraits a shared aspect ratio and align identity fields. Stack whole person records on phones. Keep biographies short and profile icons properly labeled.

### Asset production

Commission real founders with coordinated lighting, wardrobe and background. Provide enough shadow detail for faces to stay recognizable; plan landscape desktop and portrait phone crops from high-resolution originals.

### Adaptation decisions

Explain how the roles affect delivery. Substitute actual credentials and working arrangements. Increase dark-image visibility if necessary; keep the cinematic treatment subordinate to recognition and identity.

### Interaction evidence and gaps

Portraits, identity text and external profile affordances inspected. Social destinations were not opened. No portrait interaction was needed to read the roles.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores are editorial judgments, with no measured conversion result or complete rebuild validation.

## Linear — restrained four-tier comparison

ID: `linear-pricing` · Type: pricing · Observed: 2026-11-06

Source: [Linear — restrained four-tier comparison](https://linear.app/pricing)

Status: observed reference; not rebuild-validated.

Borrow: equal-width pricing columns with aligned prices, billing rows, benefits and bottom actions

Editorial scores: conversion clarity 9/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/linear-pricing-desktop.jpg)

Mobile: [view 1](shots/linear-pricing-mobile.jpg)

### Use when

A product with meaningful feature and seat limits across three or four plans.

### Avoid when

A single offer or tiers differentiated only by vague adjectives.

### Content slots

Plan; amount and billing unit; billing period; inherited benefits; distinguishing features; signup or sales action.

### Desktop composition

Four columns on black with faint vertical dividers. Headings, prices, billing rows and benefit lists share alignment. Buttons sit along the bottom; the Business signup has stronger contrast.

### Observed mobile behavior

Plans stack as full-width sections. The phone capture shows Basic with a feature list and action, then Business. A single-plan comparison selector appears below in the DOM; it was not exercised.

### Rebuild recipe

Model plans separately from billing state. Use consistent header, benefit and action regions; let benefit lists absorb height differences. Drive every billing checkbox from one shared value. Stack when benefit text becomes cramped.

### Asset production

Typography and check icons suffice. Prepare actual plan limits, inherited features and checkout/sales destinations.

### Adaptation decisions

State per-seat or per-account units explicitly. Explain annual commitment and total billing. Prioritize the distinctions customers actually compare.

### Interaction evidence and gaps

Unchecking one yearly checkbox updated both paid-plan controls and monthly amounts. Corrected desktop evidence shows the default yearly state; phone evidence shows monthly. Signup, sales and the lower comparison selector were not exercised.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Resend — usage-guided plan recommendation

ID: `resend-pricing` · Type: pricing · Observed: 2026-11-06

Source: [Resend — usage-guided plan recommendation](https://resend.com/pricing)

Status: observed reference; not rebuild-validated.

Borrow: usage slider above four plans, with a green recommendation badge on the matching plan

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/resend-pricing-desktop.jpg), [view 2](shots/resend-pricing-desktop-lower.jpg)

Mobile: [view 1](shots/resend-pricing-mobile.jpg)

### Use when

A metered product whose usage bands determine a suitable plan.

### Avoid when

Recommendations requiring qualitative advice or unpredictable usage.

### Content slots

Product tabs; usage prompt; slider and value; tiers; price; quota; overage unit; benefits; recommendation; action.

### Desktop composition

A serif heading contrasts with utilitarian plan text. A centered volume slider precedes four rounded dark cards. The matching card gains a green badge; other cards recede.

### Observed mobile behavior

Cards become a vertical stack. The phone evidence isolates the recommended Pro card, with quota, extra cost, benefits and action readable.

### Rebuild recipe

Keep one usage value and a deterministic recommendation function. Use a keyboard-operable range input with visible output. Render recommendation as text and border treatment. Retain readable contrast and independent selection for every alternative.

### Asset production

Small product icons and true usage/fee data; no large visual asset required.

### Adaptation decisions

Add numeric entry if slider steps are too coarse. Verify boundary bands and overages. Preserve legibility on nonrecommended cards.

### Interaction evidence and gaps

ArrowRight moved the slider one band and visibly recommended Pro. Product tabs, remaining bands and checkout were not exercised.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Lemon Squeezy — parallel billing models in pastel panels

ID: `lemon-pricing` · Type: pricing · Observed: 2026-11-06

Source: [Lemon Squeezy — parallel billing models in pastel panels](https://www.lemonsqueezy.com/pricing)

Status: observed reference; not rebuild-validated.

Borrow: two colored product-family panels, each explaining its own billing unit and inclusions

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/lemon-pricing-desktop.jpg)

Mobile: [view 1](shots/lemon-pricing-mobile.jpg)

### Use when

Complementary products with different billing bases, such as transactions and subscribers.

### Avoid when

Good/better/best tiers requiring direct feature comparison.

### Content slots

Product label; amount and unit; fee explanation; inclusions; exceptions; volume route; second product selector and billing period.

### Desktop composition

Mint and pink panels sit side by side with generous padding. Large amounts lead; hairline dividers separate short benefits. Exceptions and volume-contact links stay with the relevant offer.

### Observed mobile behavior

Panels stack. The captured phone view contains the transaction fee, benefit rows, volume route and extra-fee footnote.

### Rebuild recipe

Create independent offer modules with separate price models and contextual terms. Place them in two columns, then stack in reading order. Derive usage value and corresponding price from one state. Keep footnotes near the fee they qualify.

### Asset production

Optional small brand shapes. Supply current fee schedules and destinations; have the offer owner verify exceptions.

### Adaptation decisions

Use client colors with sufficient contrast. Keep billing scope, additional charges and commitments readable. Shorten benefits to distinctions rather than copying source copy.

### Interaction evidence and gaps

ArrowRight on the subscriber slider changed its displayed band and monthly amount. Annual discount, contact and signup were not exercised. Captures were taken after entry animation settled.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Designjoy — tangible membership beside one subscription

ID: `designjoy-pricing` · Type: pricing · Observed: 2026-11-06

Source: [Designjoy — tangible membership beside one subscription](https://www.designjoy.co/)

Status: observed reference; not rebuild-validated.

Borrow: dark single-offer card paired with a colorful membership-object visual and explicit service limits

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/designjoy-pricing-desktop.jpg)

Mobile: [view 1](shots/designjoy-pricing-mobile.jpg)

### Use when

A recurring service with one primary package and a strong brand asset.

### Avoid when

Complex seat/usage tiers or scope that cannot be stated concisely.

### Content slots

Headline; membership visual; availability; recurring amount; promotion conditions; included scope/capacity; action; pause/refund context.

### Desktop composition

Mixed sans and italic serif headline above a white illustrated panel and a wider black offer card. An inset two-column inclusion list sits between price and join action.

### Observed mobile behavior

The illustration panel precedes the offer card. Inclusions become one list; the phone capture includes the recurring amount, scope and action.

### Rebuild recipe

Separate the illustration and offer into a weighted two-column grid. Keep plan information in HTML. Define capacity, delivery and account limits explicitly. Stack the panels without squeezing the price card.

### Asset production

Create a client-specific membership object or branded 3D still with intentional overlap and a simple mobile crop. Prepare truthful capacity and cancellation terms.

### Adaptation decisions

Reduce the illustration's phone height if it delays the offer. Use strike-through promotions only with genuine conditions. Keep service capacity explicit.

### Interaction evidence and gaps

Pricing anchor navigation was used. Purchase and billing destinations were not opened or submitted.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Linear — asymmetric quotes linked to customer stories

ID: `linear-proof` · Type: social-proof · Observed: 2026-11-06

Source: [Linear — asymmetric quotes linked to customer stories](https://linear.app/)

Status: observed reference; not rebuild-validated.

Borrow: two oversized pastel quote cards with bottom-aligned attribution and links to full customer stories

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/linear-proof-desktop.jpg)

Mobile: [view 1](shots/linear-proof-mobile.jpg)

### Use when

Two strong attributed endorsements with relevant full customer stories.

### Avoid when

Many weak quotes, unattributed praise or audiences unfamiliar with the cited use case.

### Content slots

Short quote; person; role/company; customer mark; case-study destination; supporting customer count and story index.

### Desktop composition

A wide lavender card and narrower acid-yellow card occupy one horizontal row on black. Large quotes anchor the top; company marks and people sit along the bottom. A quieter story-index row follows.

### Observed mobile behavior

The two desktop cards become a horizontal rail with part of the next card visible. Attribution simplifies to person and company; the first quote and the following site CTA remain legible.

### Rebuild recipe

Model each endorsement as quote, attribution and story destination. Use a weighted desktop grid and a phone overflow rail with scroll snap and visible continuation. Use blockquote/cite semantics and clear focus states for story links.

### Asset production

Verified customer quotes, permissioned brand marks and published case studies. Recreate a faint background motif only with client-owned artwork.

### Adaptation decisions

Match card width to quote length; use two similarly strong endorsements. Provide a visible rail cue and keyboard access. Keep meaningful evidence accessible without requiring a story click.

### Interaction evidence and gaps

Story destinations were inspected but not opened. Mobile rail continuation was visible; horizontal scrolling and keyboard navigation were not exercised.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Raycast — profile selector with specific usage endorsements

ID: `raycast-proof` · Type: social-proof · Observed: 2026-11-06

Source: [Raycast — profile selector with specific usage endorsements](https://www.raycast.com/)

Status: observed reference; not rebuild-validated.

Borrow: a highlighted portrait profile above a quote and concrete favorite-feature context

Editorial scores: conversion clarity 7/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/raycast-proof-desktop.jpg)

Mobile: [view 1](shots/raycast-proof-mobile.jpg)

### Use when

Several credible users with distinct use cases and usable portrait permissions.

### Avoid when

A small proof set that would make an elaborate selector feel empty.

### Content slots

Proof heading; portrait; name; role/handle; selected quote; favorite feature; extension or workflow context.

### Desktop composition

A horizontal strip centers the selected portrait/name panel while neighbors fade. Below, feature and extension context sit left of a large quote, separated by a vertical rule.

### Observed mobile behavior

The profile strip remains horizontal. In the corrected saved phone frame, the selected quote comes before compact favorite-feature and extension rows; the richer explanatory descriptions from desktop are omitted.

### Rebuild recipe

Store each profile, quote and usage context together. Implement selection with real buttons or tabs, an accessible selected state and a single associated panel. Keep a static first quote available immediately. Use gentle opacity changes and honor reduced motion.

### Asset production

Permissioned portraits and verified quotes; small actual feature/extension icons where relevant. Avoid fabricated endorsements or generated customer faces.

### Adaptation decisions

Use recognizable roles rather than celebrity status alone. Preserve quote contrast instead of copying very dim inactive content. Supply controls and pause behavior if introducing automatic rotation.

### Interaction evidence and gaps

The first desktop state showed Guillermo Rauch. A click attempt on Marques Brownlee returned a timeout; subsequent mobile inspection showed his selected profile and changed quote. Selection change was observed, but click reliability, automatic cycling and keyboard behavior were not verified. Corrected final captures show Guillermo Rauch on both viewport sizes; the earlier alternate-profile state is described as observation only.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Designjoy — two editorial endorsements without cards

ID: `designjoy-proof` · Type: social-proof · Observed: 2026-11-06

Source: [Designjoy — two editorial endorsements without cards](https://www.designjoy.co/)

Status: observed reference; not rebuild-validated.

Borrow: two short oversized serif endorsements with contrasting company-logo and portrait attribution

Editorial scores: conversion clarity 7/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/designjoy-proof-desktop.jpg)

Mobile: [view 1](shots/designjoy-proof-mobile.jpg)

### Use when

Two concise, legitimately attributed endorsements beside a strong portfolio.

### Avoid when

Long detailed case studies or proof that depends on quantitative context.

### Content slots

Two short quotes; company mark or portrait; person and role; neighboring work evidence.

### Desktop composition

Two equal quote columns on a warm light background. Tall condensed serif text supplies the visual character; a company mark under one quote and a portrait with identity under the other anchor attribution.

### Observed mobile behavior

The quotes stack, each followed by its attribution. The next work visual starts below. A horizontal overflow artifact from adjacent content appears at the top of the captured source viewport; it is not part of the pattern to reproduce.

### Rebuild recipe

Use a two-column semantic quote list with generous spacing and no extra cards. Cap quote width and keep attribution directly after its quote in DOM order. Stack to one column and size typography for comfortable line lengths.

### Asset production

Real short endorsements, a licensed/permissioned logo and portrait. Pair with client-owned portfolio evidence if relevant.

### Adaptation decisions

Prefer specific substantiated endorsements. Treat praise from a recognized person as an endorsement, not proof of a customer relationship or numerical results. Choose a licensed display face with a readable phone size.

### Interaction evidence and gaps

Static quotes and attributions inspected. No source attribution links or supporting interview were verified; the reference documents presentation, not independent validation of the endorsements.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Opendoor — family stories with inline video and location

ID: `opendoor-proof` · Type: social-proof · Observed: 2026-11-06

Source: [Opendoor — family stories with inline video and location](https://www.opendoor.com/)

Status: observed reference; not rebuild-validated.

Borrow: one larger video story beside photo testimonials, with quotes, names and local context

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/opendoor-proof-desktop.jpg), [view 2](shots/opendoor-proof-desktop-playing.jpg)

Mobile: [view 1](shots/opendoor-proof-mobile.jpg)

### Use when

A considered consumer service with permissioned customer stories and video.

### Avoid when

Stock-photo endorsements or video that hides all meaningful proof.

### Content slots

Section promise; poster/video; play/pause; quote; customer identity; location; rail navigation.

### Desktop composition

A large left story video and narrower portrait cards continue offscreen. Rounded media sits above plain text quotes, hairlines, names and locations. Desktop arrows appear near the heading.

### Observed mobile behavior

A swipe-style rail exposes the first story and a portion of the next. The poster, readable excerpt, identity and location remain in one card without opening a modal.

### Rebuild recipe

Make each story a data record with poster, media URL, text, identity and location. Use a horizontal scroll-snap list with desktop controls. Keep video inline with play/pause, captions, mute controls and a readable transcript/excerpt. Lazy-load video after interaction.

### Asset production

Client-owned interviews, high-quality posters and written quote approval. Preserve captions and a static alternative; source families and footage are study evidence.

### Adaptation decisions

Choose stories that cover different customer concerns. Use genuine local context when relevant. Maintain a readable quote and identity even if media fails or motion is reduced.

### Interaction evidence and gaps

Activating the first play affordance returned a locator timeout, but the next inspection confirmed inline playback, captions and a Pause video control. Pause was clicked before leaving. Full playback, caption toggle, audio and rail arrows were not tested.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Designjoy — three illustrated service steps

ID: `designjoy-process` · Type: how-it-works · Observed: 2026-11-06

Source: [Designjoy — three illustrated service steps](https://www.designjoy.co/)

Status: observed reference; not rebuild-validated.

Borrow: three equally sized vivid cards that show subscription, request scope and delivered output

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/designjoy-process-desktop.jpg)

Mobile: [view 1](shots/designjoy-process-mobile.jpg)

### Use when

A simple recurring service where the visitor needs to understand what to request and receive.

### Avoid when

A process with many exceptions or mandatory detailed compliance instructions.

### Content slots

Process heading; three action verbs; one explanation per stage; corresponding visual; delivery expectation.

### Desktop composition

A centered mixed sans/italic-serif heading introduces three tall rounded cards. Each has vivid gradient artwork, an illustrative object in the upper region and concise step text below. A client-logo strip follows.

### Observed mobile behavior

Cards stack vertically. The mobile view captures Subscribe and Request; the latter uses cropped moving labels as scope examples. Text remains HTML and readable.

### Rebuild recipe

Use an ordered three-item grid. Give illustrations consistent height and the same text baseline, with independent visual layers clipped within each card. Stack cards in order on phones. Keep essential instructions visible with motion disabled.

### Asset production

Produce a brand-specific membership mockup, request taxonomy illustration and delivered-work montage. Plan light/dark text contrast per card and a static poster for animated labels.

### Adaptation decisions

Name steps using the customer's actions and show the actual deliverable. Replace broad scope examples with supported requests. Add truthful delivery expectations and revision/capacity context nearby.

### Interaction evidence and gaps

Scroll-triggered card reveals and moving request labels were observed. No request workflow was entered. Capture followed settling of reveal animation; initial blank cards were rejected.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Framer — product demonstration with three stage summaries

ID: `framer-process` · Type: how-it-works · Observed: 2026-11-06

Source: [Framer — product demonstration with three stage summaries](https://www.framer.com/)

Status: observed reference; not rebuild-validated.

Borrow: large product demonstration followed by a restrained three-column start/refine/publish summary

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/framer-process-desktop.jpg)

Mobile: [view 1](shots/framer-process-mobile.jpg)

### Use when

A visual software workflow with a useful demonstration and three meaningful phases.

### Avoid when

Services where a fabricated application demo would be misleading.

### Content slots

Section heading; product demo/poster; three icons; stage verbs; compact explanation of input, refinement and output.

### Desktop composition

A wide dark product demonstration sits above one rounded outlined strip split into three equal columns. Each column contains a small line icon, short stage heading and compact gray explanation.

### Observed mobile behavior

The summary strip becomes three stacked rows with horizontal rules. All three stages fit in the saved phone viewport, followed by the next section.

### Rebuild recipe

Separate demonstration media from an ordered stage list. Use a three-column grid with shared padding and dividers, then a single column. Set an aspect ratio on media to prevent layout shift. Retain text stages outside the video.

### Asset production

Record the client's actual product at a deliberate pace; export optimized video and a legible poster. Use consistent line icons and original project content.

### Adaptation decisions

Show a real beginning, editing decision and finished result. Keep phone text concise; provide a reduced-motion poster and controls for long demonstrations. Avoid mimicking editor UI as if it were an interactive product.

### Interaction evidence and gaps

The product demonstration and text stages were inspected. No editor controls, signups or end-to-end publishing workflow were exercised.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Opendoor — selectable steps with matching service visuals

ID: `opendoor-process` · Type: how-it-works · Observed: 2026-11-06

Source: [Opendoor — selectable steps with matching service visuals](https://www.opendoor.com/)

Status: observed reference; not rebuild-validated.

Borrow: four selectable service steps connected to a large contextual illustration, with one description expanded

Editorial scores: conversion clarity 9/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/opendoor-process-desktop.jpg), [view 2](shots/opendoor-process-desktop-step2.jpg)

Mobile: [view 1](shots/opendoor-process-mobile.jpg)

### Use when

A multi-stage service with distinct artifacts or actions at each step.

### Avoid when

Tiny processes where selection adds more effort than a static list.

### Content slots

Section heading; four step labels; short descriptions; icons; selected state/progress; matching visual or demo.

### Desktop composition

A large rounded media panel occupies the left half. On the right, a strong heading precedes four ruled step buttons with small icon boxes. One description is expanded, with a thin progress treatment.

### Observed mobile behavior

The heading and stage list become one column; the active illustration appears inside the first stage's expanded content. Later step labels remain below. Resizing reset the observed state to step one.

### Rebuild recipe

Keep steps and their media in one data model. Use semantic buttons with aria-expanded and controlled panels. On desktop display active media beside the list; on phones place it with the active step. Preserve readable instructions and stable dimensions while changing state.

### Asset production

Produce one real illustration, photo or short demo per stage. The source pairs a house image/address mockup with an app-guided photo tour; recreate only the client's actual process.

### Adaptation decisions

Keep the customer action distinct from the company's processing. Specify timing and commitments truthfully. If adding timed progression, pause on interaction and support reduced motion; a static ordered list should still explain the journey.

### Interaction evidence and gaps

Selecting Show us your home expanded its explanation and changed the desktop visual to an app-guided photo tour. Step one and step two were captured. Remaining selections, timer behavior and keyboard navigation were not tested. No home address was entered.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Lime Studio — editorial numbered process with proof and next action

ID: `lime-process` · Type: how-it-works · Observed: 2026-11-06

Source: [Lime Studio — editorial numbered process with proof and next action](https://limestud.io/)

Status: observed reference; not rebuild-validated.

Borrow: three spacious numbered editorial rows followed by one supporting quote and a focused booking action

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/lime-process-desktop.jpg), [view 2](shots/lime-process-desktop-lower.jpg)

Mobile: [view 1](shots/lime-process-mobile.jpg), [view 2](shots/lime-process-mobile-lower.jpg)

### Use when

A consultative service with a clear first conversation, delivery stage and client outcome.

### Avoid when

Operational instructions requiring precise individual tasks; the final outcome here is positioning rather than an operational step.

### Content slots

Process heading; number; stage title; short explanation; relevant attributed quote; next action.

### Desktop composition

Dark green background with a centered serif heading. Full-width rows use acid-yellow numbers, white serif titles, short sans explanations and fine separators. The lower section centers an attributed quote above a lime booking button.

### Observed mobile behavior

The same rows remain vertically ordered with narrow padding. Titles and paragraphs wrap naturally; a second phone capture includes the final outcome, quote and action.

### Rebuild recipe

Create a semantic ordered list with three rows and separate proof/action regions. Use typography, spacing and dividers for hierarchy. Keep quote attribution and action next to the sequence they support. Scale headings and row spacing with viewport width.

### Asset production

Licensed serif/sans pairing and one verified relevant customer quote; no large imagery necessary. Link to the client's real booking route.

### Adaptation decisions

Replace generic stages with concrete client decisions and deliverables. Distinguish the outcome from a guaranteed result. Retain the proof only if it supports this exact engagement process.

### Interaction evidence and gaps

Static stages, quote and booking affordance inspected. Booking was not opened and the source quote's claims were not independently verified.

### Verification

Live desktop and mobile inspection; saved viewport evidence reviewed. No complete rebuild or measured conversion test.

## Attio — testimonial-backed sales inquiry

ID: `attio-testimonial-contact` · Type: contact · Observed: 2026-11-06

Source: [Attio — testimonial-backed sales inquiry](https://attio.com/contact/sales)

Status: observed reference; not rebuild-validated.

Borrow: split inquiry section with promise and attributed testimonial beside a six-field qualification form

Editorial scores: conversion clarity 8/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/attio-contact-desktop.jpg)

Mobile: [view 1](shots/attio-contact-mobile.jpg)

### Use when

A consultative sale where team size and region affect the response, and a genuine customer endorsement can reduce uncertainty.

### Avoid when

Low-commitment newsletter signup or urgent support. Qualification questions should earn their added effort.

### Content slots

Sales context label; specific demo promise; short explanation; attributed customer quote; first and last name; work email; region; team size; needs; submit action and disclosure.

### Desktop composition

Two equal-width panels separated by a hairline. The left has a large two-line headline and supporting copy above a lower testimonial. The right uses paired short fields, full-width email and details, and a dark full-width action.

### Observed mobile behavior

The desktop split becomes intro, one-column form, then testimonial. First/last name and the qualification controls stack individually. The saved mobile capture includes the full sequence, with extra space between intro and form.

### Rebuild recipe

Create a section with copy/proof and form regions. Use a two-column field grid for short controls and full spans for email and textarea. Stack the regions and fields at a content-driven breakpoint. Keep real labels, selected values, validation, and submission status in the component contract.

### Asset production

A verified attributed quote and optional customer identity; no decorative hero asset is necessary. Use the client's actual form destination.

### Adaptation decisions

Tailor qualification to the sales process, shorten the empty mobile spacing, and specify the promised response or demo outcome. Move proof earlier on phones if trust is the main obstacle.

### Interaction evidence and gaps

Form labels and controls were inspected; no fields were submitted and error/success states were not exercised. The mobile quote appears after the form.

### Verification

Live desktop/mobile inspection; full-page captures were cropped before the unrelated footer.

## Linear — intent-routing contact cards

ID: `linear-contact-router` · Type: contact · Observed: 2026-11-06

Source: [Linear — intent-routing contact cards](https://linear.app/contact)

Status: observed reference; not rebuild-validated.

Borrow: three contact-routing cards for sales, support, and other inquiries above a quieter self-service resource grid

Editorial scores: conversion clarity 9/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/linear-contact-desktop.jpg)

Mobile: [view 1](shots/linear-contact-mobile.jpg)

### Use when

An organization with different teams or workflows for sales, support, press, partnerships, and product help.

### Avoid when

A small business with one inbox and one main inquiry type; routing should simplify a real distinction.

### Content slots

Short assistance headline; two or three contact purposes; descriptions that distinguish those purposes; route labels; optional docs/community/status resources.

### Desktop composition

A large left-aligned question introduces three equal dark cards. Each card separates a short title, explanatory text, and route. Lower resource links use a lighter visual hierarchy instead of competing for attention.

### Observed mobile behavior

Sales and support become a vertical list with separators. Other inquiries moves into the resource area, rather than preserving three identical large cards. Secondary resources remain below.

### Rebuild recipe

Use a semantic navigation list for primary routes and a separate resource list. Let the whole relevant route area be usable while keeping a clear accessible label. On phones reduce card chrome and preserve purpose before destination.

### Asset production

No large imagery needed. Prepare the actual sales/support destinations and resource taxonomy.

### Adaptation decisions

Route by visitor intention, not internal department jargon. Limit choices to meaningful differences and keep support available without forcing a sales form.

### Interaction evidence and gaps

Destination links and the inquiry email affordance were inspected; messages and forms were not submitted. External support/community journeys were not tested.

### Verification

Desktop/mobile captures inspected; main content retained and the unrelated footer cropped.

## Studio Freight — editorial project brief form

ID: `freight-editorial-contact` · Type: contact · Observed: 2026-11-06

Source: [Studio Freight — editorial project brief form](https://studiofreight.com/contact)

Status: observed reference; not rebuild-validated.

Borrow: a narrow serif inquiry form with underlined fields and budget context, balanced by a capabilities visual and secondary links

Editorial scores: conversion clarity 7/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/freight-contact-desktop.jpg)

Mobile: [view 1](shots/freight-contact-mobile.jpg)

### Use when

A studio or consultancy qualifying substantial projects with meaningful scope and budget requirements.

### Avoid when

Commodity service bookings or urgent mobile inquiries where placeholder-only visual cues and editorial density would add friction.

### Content slots

Inquiry label; contact identity; company; project description; approximate budget; referral source; submit; optional capabilities link and inquiry-specific FAQ.

### Desktop composition

A compact form occupies a narrow column within a much larger black canvas. Thin rules replace boxed inputs. Serif text unifies labels and navigation. A secondary column carries social links and a distinctive black-and-white capabilities preview.

### Observed mobile behavior

The form stretches across the narrow screen, followed by the FAQ, then secondary links and capabilities content. The visual does not precede the task.

### Rebuild recipe

Make the form, inquiry FAQ, and secondary resources separate modules. Use real persistent labels even if the visual treatment resembles inline prompts. Define focus, error, helper-text, and textarea expansion states before implementing underlined controls.

### Asset production

A genuine capabilities deck or work sample can supply the supporting visual. Its source-site artwork is reference material; build a client-specific preview.

### Adaptation decisions

Keep only qualification questions the team uses. Separate careers, press, and collaboration routes from the project form. Use the brand's own type and voice.

### Interaction evidence and gaps

Visible fields and submit control were inspected. The adjoining inquiry FAQ was opened separately. No inquiry was sent; validation and delivery remain untested.

### Verification

Live desktop/mobile inspection; captures show the actual form and surrounding editorial structure.

## Stripe — staged sales-routing form

ID: `stripe-staged-contact` · Type: contact · Observed: 2026-11-06

Source: [Stripe — staged sales-routing form](https://stripe.com/contact/sales)

Status: observed reference; not rebuild-validated.

Borrow: a centered white form card over a flowing branded background, with a three-step progress indicator and a two-field first stage

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/stripe-contact-desktop.jpg)

Mobile: [view 1](shots/stripe-contact-mobile.jpg)

### Use when

A genuine multi-stage inquiry where early answers route the visitor to a relevant next step.

### Avoid when

Short forms split solely to make them look easier. A wizard must preserve progress and explain why later questions are needed.

### Content slots

Brand and optional account route; progress indicator; routing headline; short explanation; work email; region; continue; clear privacy information.

### Desktop composition

A generous abstract ribbon fills the background while a white rectangular card holds the task. Desktop aligns labels beside controls and highlights the current progress segment in purple. The action sits at the lower right.

### Observed mobile behavior

The card becomes near full width; labels move above controls; the continue action becomes full width. The captured mobile design simplifies the progress display. A small horizontal scrollbar was visible and should not be copied.

### Rebuild recipe

Implement a real staged form with current/completed states, back navigation, retained answers, and field validation. Keep the asset independent from the card and use a static background fallback. Announce progress semantically rather than relying on a colored line.

### Asset production

Create a branded abstract still or lightweight motion asset with enough quiet area behind the form. Match the client's own color language.

### Adaptation decisions

Define routing logic before drawing the stages. Keep email and region only if they affect the path; fix mobile overflow and make the next-step expectation specific.

### Interaction evidence and gaps

Only the initial stage was inspected. No email was entered or submitted, and later stages, error handling, and routing were not tested. Consent UI was dismissed before final capture.

### Verification

Desktop/mobile first-stage screenshots inspected. The three-step journey is visible in the design, not verified end to end.

## Unseen Studio — scene-led direct contact

ID: `unseen-scene-contact` · Type: contact · Observed: 2026-11-06

Source: [Unseen Studio — scene-led direct contact](https://unseen.co/contact/)

Status: observed reference; not rebuild-validated.

Borrow: a large italic serif greeting and direct email over a softly lit authored interior scene, with business/general inquiry selectors

Editorial scores: conversion clarity 6/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/unseen-contact-desktop.jpg)

Mobile: [view 1](shots/unseen-contact-mobile.jpg)

### Use when

A creative practice selling distinctive visual judgment and working through direct conversations rather than structured qualification.

### Avoid when

Urgent service inquiries, weak devices without a fallback, or tasks where an entrance screen delays an essential action.

### Content slots

Greeting; short invitation; business/general selector; visible direct contact; optional location details and restrained navigation.

### Desktop composition

A pastel interior with curtains, a sculptural chair, platform, and reflective floor fills the view. Italic serif display type contrasts with plain interface text. The contact cluster occupies a deliberately quiet area of the scene.

### Observed mobile behavior

The greeting, invitation, selector row, and email stack above the recropped interior. The scene retains the chair and platform at a smaller scale. The final mobile capture was taken after the entrance and typography transitions settled.

### Rebuild recipe

Start with a still composition and semantic contact content. Add selector state only if it changes a real destination. Place the scene behind readable HTML and independently art-direct the mobile crop. If adding 3D or motion, preserve a fast static path.

### Asset production

Commission, generate, or build an original brand environment with clear text-safe space. The precise source rendering technique was not verified; a Three.js runtime is not required to reproduce the compositional idea.

### Adaptation decisions

Borrow the relationship of an authored scene and a direct invitation. Use the client's own environment and type. Remove an entrance gate for task-focused client sites and keep email legible during any transition.

### Interaction evidence and gaps

The no-audio entry was exercised and the general inquiry selector was clicked. No email client was launched. Complete selector routing, keyboard access, and reduced-motion behavior were not verified.

### Verification

Settled desktop/mobile viewport captures inspected. The source's entrance and animated transitions are documented as implementation considerations.

## KUBE Saint-Tropez — map and direct contact

ID: `kube-map-contact` · Type: contact · Observed: 2026-11-06

Source: [KUBE Saint-Tropez — map and direct contact](https://www.kubehotel-saint-tropez.com/en/contact)

Status: observed reference; not rebuild-validated.

Borrow: an equal-width map and contact-details split with a serif title and clearly separated address, phone, and email roles

Editorial scores: conversion clarity 8/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/kube-contact-desktop.jpg)

Mobile: [view 1](shots/kube-contact-mobile.jpg)

### Use when

A place-based business where finding the location and contacting staff are the main tasks.

### Avoid when

Remote services without a visitor-facing premises; a decorative map adds cost without helping a real task.

### Content slots

Context label; contact heading; short explanation; address; tap-to-call phone; email; map/directions; optional arrival guidance below.

### Desktop composition

A large map occupies the left half and an off-white information panel the right. A constrained copy column and small uppercase field labels keep the address and channels distinct. The rest of the site supplies the visual identity.

### Observed mobile behavior

Contact information leads and the map follows, reversing the desktop left-to-right visual order. The map has an external open-in-maps affordance. The captured iframe was still resolving map tiles on mobile.

### Rebuild recipe

Use a semantic address/contact region and a separate map region. Set the mobile reading order intentionally; keep essential details outside the iframe. Provide a direct directions link and a static or lazy-loaded map alternative.

### Asset production

Use the actual location and map provider appropriate to the client. Include accurate coordinates, address, phone formatting, and contact destination.

### Adaptation decisions

Add opening hours or parking guidance if they answer common questions. Keep map embeds from consuming the mobile page before the contact channels appear.

### Interaction evidence and gaps

Phone/email link destinations and the map affordance were inspected; no call, email, map navigation, or location permission was triggered.

### Verification

Desktop/mobile viewport captures inspected. Essential details remained readable while map imagery loaded.

## Studio Freight — inquiry-routing FAQ

ID: `freight-inquiry-faq` · Type: faq · Observed: 2026-11-06

Source: [Studio Freight — inquiry-routing FAQ](https://studiofreight.com/contact)

Status: observed reference; not rebuild-validated.

Borrow: a narrow serif FAQ below the project form, routing careers, press, and collaboration requests through expandable answers

Editorial scores: conversion clarity 7/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/freight-faq-desktop.jpg)

Mobile: [view 1](shots/freight-faq-mobile.jpg)

### Use when

A project inquiry page receiving several kinds of non-client correspondence.

### Avoid when

A general product help center or a large corpus of technical questions; the narrow editorial column suits a small set.

### Content slots

FAQ label; inquiry-type questions; short answers; appropriate contact links; optional brand-personality questions.

### Desktop composition

A narrow list of underlined rows shares the form's serif typography. Right-aligned plus controls change to a cross for the expanded answer. The answer stays within the same column.

### Observed mobile behavior

The list expands to the screen's available width below the form. Answers wrap into short lines; secondary links and capabilities content follow. The capture shows the careers answer expanded.

### Rebuild recipe

Use accessible accordion buttons inside headings with controlled answer regions. Keep the inquiry links as actual anchors. Define active icon, row divider, focus, answer spacing, and long-email wrapping.

### Asset production

No imagery is needed inside the FAQ. The adjacent capabilities preview belongs to the surrounding contact page.

### Adaptation decisions

Use real correspondence categories. A small personality question can fit an agency voice, but place operational questions first. Improve heading and button semantics if the source's paragraph-based appearance is reused.

### Interaction evidence and gaps

The careers row was clicked and its answer became visible with a changed indicator. Email links were inspected but not launched; keyboard behavior was not tested.

### Verification

Expanded-state desktop/mobile captures inspected; this is an inquiry FAQ rather than a purchase-objection list.

## KUBE Saint-Tropez — editorial practical FAQ

ID: `kube-editorial-faq` · Type: faq · Observed: 2026-11-06

Source: [KUBE Saint-Tropez — editorial practical FAQ](https://www.kubehotel-saint-tropez.com/en/contact)

Status: observed reference; not rebuild-validated.

Borrow: wide ruled question rows beneath a left-aligned serif heading, with small lime plus/minus controls and one active answer

Editorial scores: conversion clarity 8/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/kube-faq-desktop.jpg)

Mobile: [view 1](shots/kube-faq-mobile.jpg)

### Use when

Practical access, appointment, arrival, and service questions near a contact or booking decision.

### Avoid when

Long policy documents or situations where critical restrictions would be hidden from purchasers.

### Content slots

Context label; FAQ heading; approximately six distinct practical questions; concise answers with relevant links.

### Desktop composition

An off-white canvas, generous row spacing, thin dividers, uppercase question labels, and lime circular toggles. Answers occupy a narrower measure than the full question row.

### Observed mobile behavior

Questions wrap while the toggle stays at the right edge. The answer remains in the same vertical flow. The saved mobile state shows the address answer open.

### Rebuild recipe

Build a single-open accordion with heading/button pairs and explicit expanded states. Reserve space for the toggle; constrain answer measure independently from the question row. Make the full question usable as the control.

### Asset production

No section-specific imagery; use the brand's type and accent roles. Any adjacent photographs should be real client material.

### Adaptation decisions

Use actual visitor questions and retain essential booking terms elsewhere in visible content. Keep desktop rows from becoming unnecessarily tall on phones.

### Interaction evidence and gaps

The address question was clicked; the previous answer collapsed and the selected one opened. Keyboard navigation and every answer were not tested.

### Verification

Live desktop/mobile expanded-state captures inspected. The desktop heading is partly behind the persistent header in the saved view; its full treatment is visible on mobile.

## Raycast Pro — centered dark accordion

ID: `raycast-centered-faq` · Type: faq · Observed: 2026-11-06

Source: [Raycast Pro — centered dark accordion](https://www.raycast.com/pro)

Status: observed reference; not rebuild-validated.

Borrow: a centered section title above a constrained accordion column with bold questions, dimmer answers, and simple chevrons

Editorial scores: conversion clarity 8/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/raycast-faq-desktop.jpg)

Mobile: [view 1](shots/raycast-faq-mobile.jpg)

### Use when

A product or subscription page with a handful of real buying objections and moderate answer lengths.

### Avoid when

Many unrelated support issues or long answers that dominate the narrow mobile screen.

### Content slots

Section title; brief contextual line; question buttons; plain-language answers; relevant detail links.

### Desktop composition

Near-black background, large centered introduction, then a narrower question list. Bold white questions and gray body text separate scanning from reading. Hairline separators and chevrons supply state cues.

### Observed mobile behavior

The constrained column fills the available width. Questions and answers wrap naturally; the long expanded answer occupies much of the captured phone screen.

### Rebuild recipe

Use a shared container and narrower answer column. Implement real buttons, expanded state, answer regions, visible focus, and collapse/open behavior. Choose answer lengths before setting vertical spacing.

### Asset production

Typography and spacing carry the section; no images are required.

### Adaptation decisions

Shorten long answers and link to detail pages. Check the contrast of secondary text rather than blindly reproducing dim gray. Replace all provider, plan, and privacy claims with verified client facts.

### Interaction evidence and gaps

The first privacy question was opened, collapsed, and reopened during desktop/mobile inspection. Expanded state appeared in the accessibility snapshot. No linked workflows were completed.

### Verification

Desktop/mobile screenshots of the expanded accordion were inspected; product claims are source content, not recommendations or reusable copy.

## Framer — always-visible pricing answers

ID: `framer-open-answer-faq` · Type: faq · Observed: 2026-11-06

Source: [Framer — always-visible pricing answers](https://www.framer.com/pricing/)

Status: observed reference; not rebuild-validated.

Borrow: an open question-and-answer list in a narrow centered column, using spacing rather than accordion controls to separate answers

Editorial scores: conversion clarity 8/9; visual impact 6/9. No measured uplift.

Desktop: [view 1](shots/framer-faq-desktop.jpg)

Mobile: [view 1](shots/framer-faq-mobile.jpg)

### Use when

A manageable set of concise pricing explanations that should remain visible together.

### Avoid when

Dozens of lengthy answers or a page already too long to scan.

### Content slots

FAQ heading; question headings; direct answers; useful account, plan, or support links.

### Desktop composition

Black background and centered section heading precede a narrow left-aligned text column. Each question is brighter than its answer; generous vertical separation replaces boxed cards and toggles.

### Observed mobile behavior

The content becomes a padded single column with all answers visible. Lines wrap without introducing extra controls or interaction.

### Rebuild recipe

Use semantic question headings and ordinary answer content. Set a readable maximum width, an explicit question-to-answer gap, and a larger gap between entries. Keep links distinguishable and long pricing terms readable.

### Asset production

No section imagery. The design depends on accurate concise copy and disciplined type sizing.

### Adaptation decisions

Choose this pattern when disclosure is more useful than compression. Group or add a table of contents if the answer count grows; preserve important purchase conditions outside any later accordion redesign.

### Interaction evidence and gaps

The answers were visible without clicks on desktop and mobile. Pricing, billing, and support destinations were not exercised.

### Verification

Desktop/mobile layout inspected. A fading consent panel remains at the edge of the desktop capture and does not cover the answer column.

## Switchyards — topic-linked document FAQ

ID: `switchyards-topic-faq` · Type: faq · Observed: 2026-11-06

Source: [Switchyards — topic-linked document FAQ](https://www.switchyards.com/faq)

Status: observed reference; not rebuild-validated.

Borrow: a large editorial FAQ title with pill-shaped topic jump links above a long, always-visible question-and-answer document

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/switchyards-faq-desktop.jpg)

Mobile: [view 1](shots/switchyards-faq-mobile.jpg)

### Use when

Membership or venue information covering several distinct practical themes.

### Avoid when

A short three-question section where a full topic index adds unnecessary interface.

### Content slots

FAQ title; topic index; category headings; question headings; direct answers; links; return-to-top control.

### Desktop composition

A warm light background and navy editorial type. A centered title sits over a row of thin outlined topic pills. Large category headings and smaller question headings create a document hierarchy.

### Observed mobile behavior

Topic pills wrap across several rows and the document becomes a padded single column. The visual hierarchy stays intact rather than collapsing into an unrelated help-center template.

### Rebuild recipe

Create a linked topic index and semantic sections with stable IDs. Use scroll margins to keep anchored headings clear of sticky navigation. Add a return-to-top route and preserve browser hash navigation.

### Asset production

No major visual assets; a carefully chosen serif and optional small brand marks supply character.

### Adaptation decisions

Organize by visitor questions rather than department names. Reduce excessive heading whitespace if mobile readers must reach answers quickly. Use a more readable body face if long serif answers slow scanning.

### Interaction evidence and gaps

The Phone Booths jump link was exercised and the URL changed to its category anchor. The complete document remained open. All category links and keyboard navigation were not tested.

### Verification

Desktop/mobile captures inspected; a transient viewport-scaling capture was replaced with a settled phone view.

## TypeSafe AI — terminal-inspired technical accordion

ID: `typesafe-terminal-faq` · Type: faq · Observed: 2026-11-06

Source: [TypeSafe AI — terminal-inspired technical accordion](https://typesafe.ai/)

Status: observed reference; not rebuild-validated.

Borrow: monospace question labels and small square arrow controls paired with large sans-serif answers and a thin vertical rule

Editorial scores: conversion clarity 7/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/typesafe-faq-desktop.jpg)

Mobile: [view 1](shots/typesafe-faq-mobile.jpg)

### Use when

A technically fluent audience evaluating mechanism, reliability, or integration questions.

### Avoid when

Brands whose audience would find terminal conventions unfamiliar, or layouts where uppercase monospace labels become difficult to read.

### Content slots

Section title; technical questions; square state controls; plain-language answer paragraphs; appropriate detail links.

### Desktop composition

Dark gray canvas with bracket-like details. Questions occupy a narrower left-side column with a vertical line and sparse square controls. Answers switch to larger sans-serif text with clear paragraph breaks.

### Observed mobile behavior

The same accordion becomes full width with wrapping monospace questions. Large answer text can occupy an entire screen; the saved phone capture shows an expanded second answer.

### Rebuild recipe

Implement accessible question buttons and answer regions first, then add line and bracket decoration. Keep the answer readable at narrow widths, preserve focus visibility, and ensure icon direction consistently conveys expanded state.

### Asset production

Mostly CSS typography and simple vector lines. No generated scene or large image is required.

### Adaptation decisions

Borrow the mixed typography and schematic control grammar. Keep claims specific to the client and shorten answers where a large mobile type size creates excessive scrolling.

### Interaction evidence and gaps

The second question was clicked and its answer opened while the previous answer closed. Expanded button state was present in the loaded snapshot. Full keyboard and reduced-motion behavior were not tested.

### Verification

Desktop/mobile expanded-state captures inspected. A loading overlay in the first mobile attempt was replaced with a settled capture.

## KUBE Saint-Tropez — restrained reservation close

ID: `kube-reservation-close` · Type: cta · Observed: 2026-11-06

Source: [KUBE Saint-Tropez — restrained reservation close](https://www.kubehotel-saint-tropez.com/en/contact)

Status: observed reference; not rebuild-validated.

Borrow: a centered serif invitation and one lime booking button in a quiet band immediately before the footer

Editorial scores: conversion clarity 8/9; visual impact 6/9. No measured uplift.

Desktop: [view 1](shots/kube-cta-desktop.jpg)

Mobile: [view 1](shots/kube-cta-mobile.jpg)

### Use when

A page that has already established the offer and resolved objections, leaving one obvious next step.

### Avoid when

A cold visitor who still needs to understand the product or choose among several different services.

### Content slots

Small context label; concise invitation; booking action; optional expectation or reassurance when required.

### Desktop composition

Warm off-white band, centered serif display line, and a small contrasting lime button. A divider separates the closing invitation from the utility footer.

### Observed mobile behavior

The headline wraps into a compact two-line block. The booking button expands to nearly the available width, preserving its prominence.

### Rebuild recipe

Build a semantic CTA region with one action, consistent section padding, and bounded text width. Make the mobile control comfortably usable and keep any booking integration out of the initial page load when practical.

### Asset production

No new imagery is needed; the surrounding page carries the destination's visual world.

### Adaptation decisions

Make the action describe the actual next step. Add availability or response expectations only when accurate. Preserve this restrained option for pages whose imagery is already rich.

### Interaction evidence and gaps

The booking control was observed. No booking was submitted; the external booking engine and transaction journey were not tested.

### Verification

Desktop/mobile viewport screenshots inspected; this is a visual and clarity reference rather than measured conversion evidence.

## Switchyards — membership offer and oversized join action

ID: `switchyards-membership-offer` · Type: cta · Observed: 2026-11-06

Source: [Switchyards — membership offer and oversized join action](https://www.switchyards.com/)

Status: observed reference; not rebuild-validated.

Borrow: an editorial price promise beside two billing choices inside one panel, anchored by a full-width pill-shaped join button

Editorial scores: conversion clarity 9/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/switchyards-cta-desktop.jpg)

Mobile: [view 1](shots/switchyards-cta-mobile.jpg)

### Use when

One membership with a small number of billing choices and a clear entry path.

### Avoid when

Complex feature-tier comparisons or offers where the displayed periodic price conceals a larger commitment.

### Content slots

Offer headline; actual billing choices; price and period; transparent commitment terms; optional truthful savings cue; join action.

### Desktop composition

A large navy serif promise fills the left column. The right is a pale rounded panel with two price groups, small branded stickers, and an oversized navy action spanning the panel.

### Observed mobile behavior

The promise sits above the offer panel. Prices remain grouped and the large join control stays within the panel. The narrow layout preserves the brand's serif character and navy contrast.

### Rebuild recipe

Use an offer-summary region and an adjacent conversion panel. Represent each billing option semantically and keep period/commitment next to the value. Stack the two regions on small screens and retain a clear dominant action.

### Asset production

Optional small custom badge illustrations; they should reinforce a real offer rather than simulate urgency.

### Adaptation decisions

Use this for the client's actual offer. Show total commitment and savings honestly. If plans differ in substance, introduce a comparison rather than forcing them into this compact format.

### Interaction evidence and gaps

Join and membership destinations were observed; no membership was purchased, no location permission was requested, and checkout was not exercised.

### Verification

Desktop/mobile captures inspected. Source prices and savings are contextual evidence, not reusable client claims.

## Linear — self-service and sales closing CTA

ID: `linear-two-route-close` · Type: cta · Observed: 2026-11-06

Source: [Linear — self-service and sales closing CTA](https://linear.app/)

Status: observed reference; not rebuild-validated.

Borrow: a compact two-line promise above a bright self-service action and quieter sales action, separated from the footer by ample space

Editorial scores: conversion clarity 8/9; visual impact 6/9. No measured uplift.

Desktop: [view 1](shots/linear-cta-desktop.jpg)

Mobile: [view 1](shots/linear-cta-mobile.jpg)

### Use when

A product with genuinely useful self-service and assisted-sales entry points.

### Avoid when

A campaign with one intended destination, where a second action would dilute the decision.

### Content slots

Short closing promise; primary start action; secondary sales action; optional relevant reassurance.

### Desktop composition

Near-black section, narrow centered white headline, and two adjacent pill controls. The bright primary action contrasts with the darker secondary action; the rest of the band stays quiet.

### Observed mobile behavior

The headline wraps more tightly while both actions remain together in the captured phone width. The footer follows after a visible separation.

### Rebuild recipe

Create a CTA group with a clear primary/secondary style relationship. Allow controls to wrap or stack before labels become cramped. Keep spacing between the CTA region and footer independent from button layout.

### Asset production

No section-specific media; typography and action contrast do the work.

### Adaptation decisions

Change the promise and button labels to match the client journey. Keep the secondary route only if it serves a distinct buyer need.

### Interaction evidence and gaps

Signup and contact-sales destinations were inspected. Registration and inquiry submission were not performed.

### Verification

Desktop/mobile captures inspected. The minimalist treatment provides a useful contrast to more asset-heavy options.

## Framer — product-start CTA with a mobile alternative

ID: `framer-inline-start-cta` · Type: cta · Observed: 2026-11-06

Source: [Framer — product-start CTA with a mobile alternative](https://www.framer.com/)

Status: observed reference; not rebuild-validated.

Borrow: an inline prompt composer beneath the closing headline on desktop, replaced by a direct signup button and glowing product visual on mobile

Editorial scores: conversion clarity 8/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/framer-cta-desktop.jpg)

Mobile: [view 1](shots/framer-cta-mobile.jpg)

### Use when

A product whose first meaningful action can be initiated in a small inline interaction.

### Avoid when

A simulated composer with no actual continuation, or an interaction that asks for sensitive project details before explaining handling.

### Content slots

Closing headline; desktop input/composer and submit affordance; helpful starting suggestions; alternative start path; mobile button; product visual.

### Desktop composition

Centered white headline above a dark rectangular composer. Suggested use cases and an alternate route sit below. The desktop interface is itself the central visual.

### Observed mobile behavior

The composer and suggestion chips are replaced by a prominent start button and a glowing cropped canvas UI image. This is an observed change of interaction, not simply a smaller desktop box.

### Rebuild recipe

Build separate responsive presentations of the same intended journey. On desktop, carry the user's input into a real product flow. On mobile, route directly and use a compact accurate visual. Keep accessible labels and loading/error states explicit.

### Asset production

An accurate product-interface crop with a controlled glow treatment for the mobile presentation. Use the client's own UI and keep actual controls as HTML.

### Adaptation decisions

Only embed the task if it can continue without losing input. Decide which devices benefit from it; use a normal CTA elsewhere. Keep an accessible non-composer route available.

### Interaction evidence and gaps

The composer, suggested prompts, mobile replacement, and destinations were inspected. No prompt was submitted and continuation, signup, or generation was not tested.

### Verification

Desktop/mobile captures show a deliberate change of content and interaction at the narrow viewport.

## Front — branded demo panel with people imagery

ID: `front-branded-demo-cta` · Type: cta · Observed: 2026-11-06

Source: [Front — branded demo panel with people imagery](https://front.com/)

Status: observed reference; not rebuild-validated.

Borrow: a large inset deep-purple CTA panel with a left-aligned white promise, lime demo button, and supporting people imagery

Editorial scores: conversion clarity 7/9; visual impact 8/9. No measured uplift.

Desktop: [view 1](shots/front-cta-desktop.jpg)

Mobile: [view 1](shots/front-cta-mobile.jpg)

### Use when

An assisted-sale offer that needs a distinctive final invitation and credible human context.

### Avoid when

Pages where additional chat widgets or competing CTAs obscure the main action.

### Content slots

Specific outcome headline; demo action; optional relevant people or workplace image; clear onward journey.

### Desktop composition

Rounded inset purple panel, large left-aligned white type, and a bright lime action. The settled desktop capture includes workplace imagery at the right and a block-like branded motif below.

### Observed mobile behavior

The message becomes a tall text block and the action remains below it. An automatically opened chat panel overlaps much of the lower section in the observed phone view, though the main button remains visible.

### Rebuild recipe

Use a two-column panel when imagery helps, with separate text and image regions and a consistent inset. Stack or remove imagery on narrow screens. Design chat and floating utilities around a reserved safe area rather than letting them compete with the CTA.

### Asset production

Licensed or client-supplied workplace photography with a focal crop that supports the message. Avoid implying stock subjects are the client's employees.

### Adaptation decisions

Borrow the clear color/action contrast and inset composition. Keep the promise concise and prevent automatic overlays from covering content or controls.

### Interaction evidence and gaps

The demo control and chat overlay were observed. The third-party panel did not expose a usable dismissal control through the available inspection route. No chat message or demo request was submitted.

### Verification

Desktop/mobile captures preserve the actual overlay limitation; the rebuild should improve that behavior. The desktop photo loaded after the initial observation.

## charity: water — illustrated newsletter signup

ID: `charity-illustrated-newsletter` · Type: cta · Observed: 2026-11-06

Source: [charity: water — illustrated newsletter signup](https://www.charitywater.org/)

Status: observed reference; not rebuild-validated.

Borrow: a small envelope illustration and benefit statement beside a signup form, with a wide yellow subscription action

Editorial scores: conversion clarity 7/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/charity-newsletter-desktop.jpg)

Mobile: [view 1](shots/charity-newsletter-mobile.jpg), [view 2](shots/charity-newsletter-mobile-lower.jpg)

### Use when

An organization with a meaningful email program and enough reason for visitors to stay connected.

### Avoid when

A generic newsletter request without a clear benefit, or unnecessary personal questions that add effort without relevance.

### Content slots

Small illustration; useful signup promise; brief description; email and justified identity fields; optional preference; subscription action; clear information-use note.

### Desktop composition

A white signup panel on a warm pale surround. The left combines envelope artwork with a short headline; the right contains paired name fields, email, optional birthday controls, and the yellow action.

### Observed mobile behavior

Illustration and invitation lead, then the fields stack. Name inputs become separate rows and birthday controls rearrange across two rows. The full-width subscription control stays in the form; a second view shows the lower context.

### Rebuild recipe

Use copy/illustration and form regions in a shared panel. Keep labels persistent and required/optional states clear. Handle validation and success without losing entered values. Use a single-column layout before controls become cramped.

### Asset production

An original small illustration matching the client's icon/line/color language; avoid copying the source envelope.

### Adaptation decisions

Begin with email-only unless extra fields have a concrete purpose. Make the email benefit and expected cadence specific. Explain any optional preference and preserve a clear unsubscribe path.

### Interaction evidence and gaps

Fields and the subscription control were inspected; no information was entered and no subscription was sent. Consent UI was dismissed before capture; delivery, validation, and success were not tested.

### Verification

Desktop and complementary mobile captures inspected. The longer form is a design choice to assess, not a universal signup template.

## Framer — large sitemap with a separate utility strip

ID: `framer-footer` · Type: footer · Observed: 2026-11-06

Source: [Framer — large sitemap with a separate utility strip](https://www.framer.com/)

Status: observed reference; not rebuild-validated.

Borrow: six aligned link columns above a quieter utility row for language, social, assurance and service status

Editorial scores: conversion clarity 9/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/framer-footer-desktop.jpg)

Mobile: [view 1](shots/framer-footer-mobile.jpg), [view 2](shots/framer-footer-mobile-lower.jpg)

### Use when

A mature product or platform with many genuinely useful destinations.

### Avoid when

A small service site with fewer than a dozen meaningful pages; copying this density would create filler.

### Content slots

Product/resource/solution/company groups; descriptive links; occasional update badges; home mark; language; social routes; assurance marks; live status; copyright.

### Desktop composition

On black, six evenly spaced text columns use brighter group labels and subdued links. Some columns contain secondary subgroups. A bottom utility strip distributes the mark, locale, social icons, assurance marks, service status and copyright.

### Observed mobile behavior

The sitemap becomes two long columns with different group placement, followed by a stacked utility region. The phone views show both the upper link directory and the lower language/social/status area. No accordion is used in the observed layout.

### Rebuild recipe

Define navigation groups as data and render labeled semantic lists. Use desktop grid areas to organize long and short groups; preserve a sensible reading and keyboard order when reflowing to two phone columns. Put utilities in a separate region with flexible wrapping.

### Asset production

Brand mark, labeled social icons, real assurance permissions and an actual service-status destination. No stock imagery is needed.

### Adaptation decisions

Keep only destinations that earn their place. Match the group taxonomy to visitor tasks and maintain text contrast. Link assurance badges to evidence, and display live service state only when it has a real data source.

### Interaction evidence and gaps

Link destinations and language control were inspected. The status label settled from a checking state to an online state. Language changes, status destination and navigation links were not opened.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores are editorial judgments, with no measured conversion result or complete rebuild validation.

## Mailchimp — warm resource directory and brand-family utility layer

ID: `mailchimp-footer` · Type: footer · Observed: 2026-11-06

Source: [Mailchimp — warm resource directory and brand-family utility layer](https://mailchimp.com/)

Status: observed reference; not rebuild-validated.

Borrow: a warm five-column directory separated from brand-family, app, social and legal utilities by a clear horizontal rule

Editorial scores: conversion clarity 8/9; visual impact 7/9. No measured uplift.

Desktop: [view 1](shots/mailchimp-footer-desktop.jpg), [view 2](shots/mailchimp-footer-desktop-lower.jpg)

Mobile: [view 1](shots/mailchimp-footer-mobile.jpg), [view 2](shots/mailchimp-footer-mobile-lower.jpg)

### Use when

A product with a real resource ecosystem, mobile apps and a broader company family.

### Avoid when

A local service business without that ecosystem, or a brand using unverified trust badges as decoration.

### Content slots

Related resources; five navigation groups; brand-family routes; app stores; social routes; assurance link; language selector; legal/cookie preferences.

### Desktop composition

A mustard field contains related resources above five evenly spaced link groups. A ruled lower band centers the brand family, app store badges, social icons and assurance mark, then places language beside small legal copy.

### Observed mobile behavior

All directory groups become a single vertical list rather than collapsible sections. The lower layer stacks brand-family marks, two app badges, social icons, assurance, a full-width language selector and legal text. A chat launcher remains visible near the lower edge.

### Rebuild recipe

Separate the resource directory from brand, app and policy utilities. Use semantic lists and underlined links. Collapse the five-column grid to one column when labels wrap; let each lower group wrap independently. Keep app badge ratios and legal text readable.

### Asset production

Permissioned company-family marks, official app badges, current social routes and documented assurance links. Provide the actual locale/policy destinations.

### Adaptation decisions

Trim secondary links for smaller inventories. Increase small source text where needed, retain contact/help visibility and keep chat widgets clear of the policy links. Show only relevant company-family and app assets.

### Interaction evidence and gaps

The personalization prompt was dismissed without supplying information; the cookie notice was closed. Footer links, app badges and language options were inspected, but no language change, chat, download or navigation flow was exercised.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores are editorial judgments, with no measured conversion result or complete rebuild validation.

## Locomotive — ruled navigation and a typographic contact signature

ID: `locomotive-footer` · Type: footer · Observed: 2026-11-06

Source: [Locomotive — ruled navigation and a typographic contact signature](https://locomotive.ca/en)

Status: observed reference; not rebuild-validated.

Borrow: ruled navigation groups above an oversized address/phone/email signature built from expressive type and symbols

Editorial scores: conversion clarity 8/9; visual impact 9/9. No measured uplift.

Desktop: [view 1](shots/locomotive-footer-desktop.jpg), [view 2](shots/locomotive-footer-desktop-newsletter.jpg)

Mobile: [view 1](shots/locomotive-footer-mobile.jpg)

### Use when

A design-led studio with a few navigation groups, meaningful location details and room for a custom typographic treatment.

### Avoid when

Large compliance-heavy platforms or audiences who would struggle to decode decorative contact details.

### Content slots

Site routes; social links; related projects; locale; cookie preferences; newsletter trigger; address/map; telephone; email; copyright.

### Desktop composition

White space, thin black rules and large sans links organize menu, social and external groups. The lower address/contact block switches to a large editorial serif mixed with custom symbols and diagram-like details, with copyright at the edge.

### Observed mobile behavior

Social and external links form two compact columns. Primary menu links are omitted from the footer and remain available through the header menu. Locale and preferences sit below, then the large contact signature wraps into several lines with copyright last.

### Rebuild recipe

Use semantic navigation lists above a separate address element with map, tel and mailto links. Build decorative symbols as aria-hidden spans while retaining a clean accessible text label. Let the contact block wrap at intentional phrases. Keep newsletter disclosure independent from footer navigation.

### Asset production

A licensed serif/sans pair, client-specific graphic symbols, real address and contact routes. Use SVG or styled text for decoration rather than baking all contact information into an image.

### Adaptation decisions

Make phone/email unmistakable and selectable. Keep a plain-text fallback and ensure decorative glyphs do not pollute accessible names. Retain primary footer routes on mobile if header-menu dependence would harm task completion.

### Interaction evidence and gaps

Necessary cookies were accepted to clear the notice. Newsletter opened an inline email subscription panel and the visible Close control returned to navigation. No email was entered or submitted; map, phone, email, language and preference destinations were not exercised.

### Verification

Live desktop and phone layouts inspected; saved screenshots reviewed. Scores are editorial judgments, with no measured conversion result or complete rebuild validation.

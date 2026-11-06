# Observed hero and bento references

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

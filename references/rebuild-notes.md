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

# Prompt: Author the revised Americas SAF Study deck content

Paste everything below to a fresh Claude Code (Sonnet) session. It is self-contained — you do
not need any other file from the source project to execute it.

---

## Your mission

You are authoring the content for a revised internal strategy deck: **"Americas' SAF Market
Outlook, Strategic Insights and Opportunities."** The current deck (24 slides, PPTX) has been
audited against a research draft, and every required change has already been decided — your job
is to **execute** that change list, not to re-research or second-guess it. Treat every fact,
figure and instruction below as final and pre-verified except where explicitly marked
"unverified" or "pending" — those must stay flagged, not resolved.

Produce exactly two kinds of deliverable:

1. **`slide-content.md`** — one file containing every slide in final order: title, full body
   content (bullets/tables written out, not summarized), speaker notes, and a `Visual:` line
   naming which visualization treatment it gets (see below).
2. **Standalone HTML files**, one per complex visualization identified below — self-contained,
   openable directly in a browser, designed to be screenshotted and dropped into the
   corresponding PowerPoint slide as an image. Each must work in both light and dark viewing
   (see house style, below) even though it will end up as a static screenshot — screenshot it in
   light mode unless told otherwise.

Do not build a `.pptx` file — there is no source PowerPoint file available to you to edit
programmatically, and the deck's exact template/master slide styling isn't something you can
reproduce blind. The `slide-content.md` + screenshot-ready HTML combination is what a human will
use to rebuild the deck by hand.

Before building any visualization, load your `dataviz` skill (if you have skills available) and
follow its method. If you don't have that skill, use the condensed house style given in the
"Visual style reference" section near the end of this prompt — it's extracted from a
visualization already built for this same deck, so matching it keeps the new visuals consistent
with the one that already exists.

---

## Ground rules

- **Never invent numbers.** Where a figure is explicitly said to be missing below (e.g. no
  Americas-specific biofuels market-sizing exists), say so on the slide or in speaker notes as
  "pending" — do not estimate or backfill it.
- **Keep "pending" items pending.** Two items are explicitly not resolved and must stay flagged
  in the output, not stated as settled fact (see "Items to keep flagged as pending" below).
- **Sourcing caveats belong in speaker notes, not slide body text** (see that section below) —
  don't surface them as headline claims, but don't drop them either.
- **Apply the cross-cutting corrections everywhere the underlying figure appears**, not just in
  the one slide where it's first mentioned (see that section below).
- Where this prompt gives you a specific number, date, or named source, use it verbatim. Where it
  describes a shape of content ("a native comparison table," "a corridor diagram") without every
  exact word, use your judgment on phrasing but keep the facts as given.

---

## Background you need (condensed working context)

**The strategic thesis (Working Hypothesis).** The Americas are likely to be one of the most
important SAF supply regions through 2030, but the opportunity for Singapore is shifting. The
previous route — Asia-origin used cooking oil (UCO) aggregated through Singapore and sold into
the U.S. renewable fuels market — is becoming less attractive as U.S. policy favours North
American feedstock. Singapore should therefore focus less on pass-through UCO trade into the
U.S., and more on building a role in new SAF corridors linking Latin American feedstock,
production projects and offtake demand in Europe and Asia.

Two implications follow from the U.S. feedstock re-nationalisation (see policy section below):

1. Singapore's trading and blending value proposition needs to re-orient toward Europe- and
   Asia-Pacific-bound cargoes rather than U.S.-bound ones, since non-North American UCO no longer
   qualifies for the 45Z tax credit.
2. The same North American-content logic that excludes Asian UCO from U.S. tax credits creates an
   opening for Latin American feedstock (Brazilian soybean oil and macaúba, Argentine soy oil
   already flowing into Canada) to fill the North American gap — a trade Singapore-based
   commodity houses are well placed to help finance and structure, even without touching
   Singapore soil.

**Three judgments underpinning the whole deck:**
1. U.S. SAF growth increasingly depends on North American feedstock (OBBBA/45Z).
2. Brazil is the best-positioned Americas market (Acelen Bahia project + a legislated pathway to
   2037).
3. North America's 45Z-driven feedstock re-nationalisation creates **multiple cross-border
   corridors — not a single Canada-specific one** — that Singapore trading houses can finance and
   structure without touching Singapore soil. Canada's own domestic SAF volume is negligible
   (0.8% of CFR credits in 2024) and bifurcated between BC's 2028 mandate and a federal credit
   market that isn't SAF-specific — which is precisely why Canada's relevance to Singapore is
   corridor-based rather than production-based.

**Three cross-border corridors, in order of how well-documented each is:**
- **Argentina→Canada** soy oil feeding Braya Renewable Fuels — 757,000 tonnes imported in 2024,
  up from 48,000 tonnes in 2023. This is the flagship, best-evidenced example.
- **Mexico/Canada→U.S.** tallow and UCO flowing into 45Z-eligible U.S. supply chains.
- **Brazil→U.S./Europe finished SAF** (Acelen's ~90% pre-contracted volumes) — structurally
  different from the other two since it's a product-export flow rather than a feedstock-import
  corridor, so Singapore's angle there is book-and-claim/certificate trade (SAFc Registry model),
  not physical logistics.

**Watch item on the flagship corridor.** Argentina's own emerging SAF ambitions (the Santa Fe Bio
JV — see the watchlist slide, below) are worth flagging as a factor that could, over time, compete
with rather than purely supply the Argentina→Canada corridor. Today the corridor is a small share
of Argentina's total soy-oil export base (India still takes the majority) — there's room for both
to grow before that tension becomes material — but the corridor shouldn't be presented as a
one-way, permanent flow.

**Cross-cutting corrections — apply wherever the number appears, not just its "home" slide:**
- **Montana Renewables DOE loan:** $782M first-tranche loan guarantee + $150M Calumet equity =
  **$1.67B total** (Title 17 §1706, closed Jan 2025) — not "$1.44 billion."
- **World Energy / Air Products:** Air Products exited the companies' $2B Paramount, CA expansion
  partnership in **Feb 2025**. World Energy's existing 250M gal/yr operations are unaffected, but
  the expansion's financing path is now an open question — don't present the $2B expansion as
  still active.
- **Acelen jobs figures — never conflate these two:** ~3,600 peak **construction** jobs (trade
  press) vs. FGV's ~85,000 direct+indirect jobs over a ten-year **full value chain** horizon (a
  different, larger metric). Present as two distinct numbers whenever either is cited.

**Sourcing caveats — carry these as speaker notes only, not slide body text:**
- Petrobras and Ecopetrol have **no SAF-specific investor disclosures** — lean on ANP/Aerocivil
  filings and trade press, don't imply IR-level confirmation.
- BC-LCFS has **no confirmed public compliance/credit registry** — presumed under gov.bc.ca but
  not directly verified.
- The FGV Acelen economic-impact figures and the Embrapa/University of São Paulo macaúba research
  are **unconfirmed primary sources** — only secondary coverage was located.

**Items to keep flagged as pending, not resolve:**
- The "Singapore strengths" slide (see slide 12 below) genuinely needs Trade-team/internal input
  and cannot be resolved from public sourcing — keep it labeled "pending Trade input," don't
  fabricate content to fill it.
- The CAAS levy flight-departure timing (see slide 14 below): trade reporting suggests a deferral
  from 1 Oct 2026 to 1 Jan 2027, announced March 2026 — this needs direct confirmation against
  caas.gov.sg before it appears in any external-facing version of the deck. Flag on-slide as
  "reported, pending direct CAAS confirmation," not settled fact.

**Known data gap — do not fill it:** there is no Americas-specific biofuels market-sizing figure
available to replace or supplement the deck's existing Global & Europe biofuels market
projection chart (US$59.04B global 2023 → US$207.87B 2030, 11% CAGR; Europe US$28.38B → 
US$99.53B, 11.1% CAGR). Keep the existing global/Europe numbers as-is and add an explicit note
that an Americas-specific figure is not yet available — do not estimate one.

---

## Final slide order

The deck goes from 24 slides to roughly 19–22, depending on layout choices you're free to make
(e.g. whether Brazil needs one slide or two given how much content it carries relative to
US/Canada — use your judgment, favor readability over cramming). Use this as your target
sequence:

| # | Slide | Action |
|---|---|---|
| 1 | Title | KEEP as-is |
| 2 | Background & Key Objectives | TWEAK — add Working Hypothesis |
| 3 | Section frame: Introduction to Biofuels | KEEP |
| 4 | Biofuels market size chart | TWEAK — flag Americas data gap |
| 5 | Growth drivers | TWEAK — lead Americas-first |
| 6 | Section frame: Introduction to SAF | KEEP |
| 7 | SAF regional revenue table | KEEP as-is |
| 8 | HEFA vs PtL vs ATJ | TWEAK — update figures, add ATJ |
| 9 | SAF cost and economics | BUILD (was a blank placeholder) |
| 10 | Value chain / ecosystem stakeholders | TWEAK — name SAFc Registry |
| 11 | Trade flows (SG/SEA ↔ North America ↔ LatAm) | MERGE (was two duplicate placeholders) |
| 12 | Singapore strengths | MERGE, mark "pending Trade input" |
| 13 | Americas policy overview | BUILD — absorbs old OBBBA-restrictions slide |
| 14 | Singapore's target & strategies on SAF | TWEAK |
| 15 | Section frame: SAF Market Deep Dives | KEEP |
| 16 | US deep dive | TWEAK — corridor reframe |
| 17 | Canada deep dive | TWEAK — corridor reframe |
| 18 | Brazil deep dive (full profile) | NEW — split out of old combined LATAM slide |
| 19 | Chile / Colombia / Mexico watchlist | Condensed format |
| 20 | Section: Summary & Recommendations | KEEP |
| 21 | Americas "at a glance" | NEW |
| 22 | Comparative Opportunity Map + house view + industry events + next steps | Unified format |

Two old hidden Europe reference slides and one empty slide are dropped entirely — they don't
appear in the sequence above and need no replacement beyond what's already listed.

---

## Slide-by-slide content

### Slide 1 — Title
No change. "Americas' SAF Market Outlook, Strategic Insights and Opportunities" — 2026.

**Visual:** none needed.

### Slide 2 — Background & Key Objectives
Keep the existing Vision/Mission/agenda bullets:
- Vision: Singapore as Asia's leading Sustainable Aviation Fuel (SAF) hub.
- Mission: Strengthening the ecosystem to grow SAF value-added activities in Singapore.
- This presentation will: (a) provide an overview of the global SAF industry and Singapore's
  strengths/position, (b) deep dive into countries within the Americas with notable SAF
  ecosystems — key developments, policy mandates, key players, opportunities and challenges in
  scaling SAF, (c) seek OCs' and Trade's feedback on strategic considerations for how Singapore
  can capture value from SAF growth in SEA and the Americas.

**Add** the full Working Hypothesis and three judgments from the Background section above as new
content on this slide — this is the deck's actual strategic thesis and is currently missing.

**Visual:** native — text/bullets, no custom build needed.

### Slide 4 — Introduction to Biofuels (market size chart)
Keep the existing chart and 4-generations-of-biofuels content structure. Add an explicit
callout/footnote: **"Americas-specific biofuels market-sizing: not yet available in current
sourcing — global/Europe figures shown are the best available reference."** Do not invent a
number.

**Visual:** native — existing chart unchanged, just add the gap note as an on-slide or
speaker-note caveat.

### Slide 5 — Growth drivers
Trim the current long Europe-focused geopolitical disruption table (Russia-Ukraine, OPEC+, Strait
of Hormuz, Red Sea) sharply — it can stay as a small secondary reference if space allows, but
should **not** lead the slide. Lead instead with three Americas-relevant demand drivers:
- **Policy mandates/tax credits:** Brazil's E30/B15 fuel blend mandates, Canada's Clean Fuel
  Regulations, US 45Z Clean Fuel Production Credit.
- **Energy security:** Brazil's ethanol/biodiesel programme as the clearest Americas example.
- **Decarbonisation:** CORSIA becomes mandatory for all member states from 2027 (voluntary since
  2021); IATA's net-zero-by-2050 commitment, with SAF expected to deliver ~65% of the required
  emissions reduction.

**Visual:** native — a simple 3-column icon/driver layout works well; no custom HTML needed.

### Slide 7 — Introduction to SAF (regional revenue table)
No change needed. Keep the existing table as-is:

| Region | 2024 Revenue (US$B) | 2030 Forecast (US$B) | CAGR (2025–2030) |
|---|---|---|---|
| Asia Pacific | 0.162 | 3.170 | 64.1% |
| Europe | 0.266 | 4.755 | 61.7% |
| North America | 0.482 | 6.657 | 54.9% |
| Latin America | 0.069 | 0.793 | 50.1% |
| Middle East & Africa | 0.058 | 0.476 | 40.3% |

**Visual:** native — this table already exists and needs no rebuild.

### Slide 8 — HEFA vs PtL vs ATJ
Update and expand the existing HEFA/PtL two-column comparison into three columns:

**HEFA** — Process: converts used oils and fats via hydrogenation, cracking and isomerization;
commercially mature, dominates SAF supply today (>95%). Feedstock: UCO, animal fats, vegetable
oils. Usage/emissions: certified for up to 50% blending; ~90% lifecycle GHG reduction. Cost:
EASA 2024 reference price **€2,085/t vs €734/t fossil jet — roughly a 2–5x premium** (unchanged
from before).

**PtL** — Process: synthesizes fuel using green hydrogen and captured CO₂ via Fischer-Tropsch;
early-stage, ~15–20 years to commercial viability. Feedstock: renewable electricity + CO₂ (direct
air or industrial capture), no organic feedstocks. Usage/emissions: limited to pilots (mainly
Europe); near-100% GHG reduction potential. Cost: EASA 2024 reference price **€7,695/t — up to
~10–12x fossil jet, not the previous "5–8x" figure**. This is the one hard correction on this
slide: update the multiple.

**ATJ (Alcohol-to-Jet) — new third column, flag as Brazil-specific.** Converts sugarcane/corn
ethanol into jet fuel. Note on-slide: an estimated ~2 billion litres of ethanol would be needed to
meet Brazil's ProBioQAV 1.2-billion-litre 2037 SAF demand via ATJ alone. This ties the slide
directly forward to the Brazil deep dive later in the deck.

**Drop entirely:** the current slide's "add cellulosic" note. No sourced cellulosic-pathway
content exists to build this out — remove the note rather than trying to populate it.

**Visual:** native — a 3-column comparison table works fine in PowerPoint directly. Optional: if
you want a more polished look, a small HTML "cost multiple" bar strip (HEFA ~3x / PtL ~10–12x)
is a nice-to-have, not required.

### Slide 9 — SAF cost and economics (currently a bare placeholder — BUILD fully)
This is one of the two slides that most needs a custom-built visualization (see below). Content
to include:
- **EASA 2024 reference prices:** HEFA €2,085/t (~3x fossil jet premium), PtL €7,695/t (up to
  ~10–12x). Fossil jet reference: €734/t.
- **IATA:** airlines paid a collective **$2.9B premium** for 1.9Mt of SAF in 2025, of which
  **$1.4B** was the structural price spread over fossil jet.
- **Global SAF production forecast:** only **2.4 million tonnes in 2026** — about **0.8%** of
  total jet fuel consumption.
- **Platts CIF NW Europe SAF price assessment:** ~**4.7x** the volatility of fossil jet fuel
  since its Sept 2023 launch ($444/mt standard deviation vs $95/mt for fossil jet). Carry as a
  speaker-note caveat: Platts moved to a new CIF NW Europe methodology in March 2025 (premium to
  Jet CIF NWE forward curve) — this stat is historical; pull the live series rather than leaning
  on it as current.
- **Note as a to-add item:** Argus Media's *Argus Americas Biofuels* is the missing US-specific
  benchmark (Platts' assessment above is Europe-only) — worth adding once budget/access is
  confirmed. Present this as a forward-looking note, not as data you have.
- **Two-to-three policy models for managing the SAF cost premium:** Europe's "polluter pays"
  model (ReFuelEU — cost passed to airlines/passengers) vs. the U.S. taxpayer-funded production
  credit (45Z) vs. Singapore's own hybrid model — a fixed, centrally-procured passenger/cargo
  levy (this ties forward to slide 14, Singapore's own strategy).

**Visual: BUILD as standalone HTML** — `saf-cost-economics.html`. Suggested layout: a stat-tile
row across the top (IATA $2.9B/$1.4B premium, 2.4Mt/0.8% production forecast, 4.7x volatility)
paired with a small EASA price-comparison bar (fossil €734 / HEFA €2,085 / PtL €7,695, log-scale
or clearly labeled multiples so PtL doesn't visually dwarf the others into illegibility), and a
compact 3-way policy-model comparison strip (Europe / US / Singapore) below. This slide currently
has zero content in the source deck, so the visual is doing real communication work here, not
just decoration.

### Slide 10 — Value chain / ecosystem stakeholders
Keep the existing value chain structure (Feedstock Suppliers → SAF Producers → Fuel
Blenders/Distributors → Airport Fuel Infrastructure → Airlines / Corporate SAF Buyers, plus
Regulators & Certifiers and Integrated Suppliers & Producers as cross-cutting categories). One
addition: in the **Corporate SAF Buyers / Book-and-Claim** box, name the **SAFc Registry**
(docs.safcregistry.org) explicitly — it's the actual mechanism behind the Google/American
Airlines book-and-claim deal (35 million gallons), and is worth citing directly given Singapore's
own book-and-claim ambitions (see slide 18, Brazil).

**Visual:** native — this is an existing value-chain diagram; just add the registry name to the
relevant box, no rebuild needed.

### Slide 11 — Trade flows (merged from two duplicate placeholders)
Build a single trade-flows slide covering SG/SEA ↔ North America ↔ LatAm. Content:
- **The reconciled China UCO picture — present both figures together, not either alone:**
  US-bound Chinese UCO exports **fell 55% y/y** (1.2Mt Jan–Nov 2024 → 540,000t same period 2025)
  while China's **global** UCO exports were **up 36.8% y/y** in Jan–May 2026 (1.37Mt cumulative).
  The story is redirection to Europe, not a volume collapse — make sure both numbers appear
  together so the slide doesn't read as "China UCO trade is shrinking."
- **The Argentina→Canada soy-oil corridor** feeding Braya Renewable Fuels: 757,000 tonnes
  imported in 2024, up from 48,000 tonnes in 2023.
- **HS-code caveat — state this on the slide itself, not buried in speaker notes:** no customs
  code isolates SAF itself. The available codes are feedstock proxies only: 1518 (UCO, not
  cleanly isolated), 1502 (tallow), 1507/1511/1514 (soy/palm/canola oil), 2207 (ethanol), 3826
  (biodiesel/blends), 2710.20 (biodiesel-containing fuel oils). Any trade-data claim on this
  slide is scoped to feedstock flows, not finished SAF volumes — say this explicitly.
- **Best free verification sources to cite:** USITC DataWeb, Comex Stat/MDIC + ABIOVE (Brazil),
  INDEC (Argentina), UN Comtrade/WITS.

**Visual: BUILD as standalone HTML** — `saf-trade-flows.html`. Suggested layout: a corridor
diagram with three labeled nodes (SG/SEA, North America, LatAm), directional arrows sized or
labeled by the tonnages above, with the China UCO redirection and HS-code caveat as supporting
callouts beside the diagram rather than crowding the arrows themselves. Add one small annotation
beside the Argentina→Canada arrow noting Santa Fe Bio as a forward-looking, second Argentina
angle — distinct from the corridor since it's a product-export case, not a feedstock-import one;
keep it to a short label/footnote, not a second diagram. This is a genuine flow/diagram case —
native PowerPoint SmartArt won't handle the specific volumes and multi-source caveat cleanly.

### Slide 12 — Singapore strengths (merged from two duplicate, vague placeholders)
This section genuinely needs Trade-team/internal input and cannot be resolved from public
sourcing. **Do not fabricate content to fill it.** Collapse the two old duplicate placeholder
slides into one, clearly labeled **"Pending Trade input."** Leave a structural placeholder
(e.g. "SG's existing trading/logistics/certification strengths — input needed from Trade") so
whoever picks this up next knows what's expected, but don't write speculative content as if it
were researched.

**Visual:** none — this is intentionally a placeholder slide.

### Slide 13 — Americas policy overview (BUILD)
This absorbs the old standalone "US OBBBA feedstock restrictions" placeholder, plus a compact
side-by-side comparison of all three countries' policy mechanisms:

- **US — 45Z Clean Fuel Production Credit (post-OBBBA):** credit extended to **Dec 31, 2029**;
  maximum SAF credit **cut from $1.75 to $1.00/gallon (a 43% reduction)**; feedstock **restricted
  to material produced/grown in the US, Canada or Mexico from 2026**; ILUC penalties removed for
  post-2025 production; "foreign entity of concern" ownership restrictions added.
- **Canada — federal Clean Fuel Regulations** (credit-trading, not SAF-mandating — SAF was just
  **0.8%** of credit-generating fuel in 2024) **+ British Columbia's BC-LCFS** — the first
  jurisdiction in North America to mandate SAF blending: **1% by 2028, rising to 3% by 2030.**
- **Brazil — "Fuel of the Future" Law (Lei 14.993/2024) and ProBioQAV** — a well-to-wake
  emissions-reduction target (**1% by 2027, rising to 10% by 2037**), structurally distinct from
  the blend-volume mandates used elsewhere.

Keep this as a summary/comparison layer only — full policy detail for each country stays on its
own Section 3 deep-dive slide (slides 16–18) to avoid duplicating content.

**Visual: BUILD as standalone HTML** — `saf-policy-overview.html`. Suggested layout: three
country cards side by side (US / Canada / Brazil), each with the mechanism name, key numeric
terms, and a compact timeline marker (2026 / 2028 / 2029 / 2030 / 2037 as relevant to that
country). This is the same kind of comparison shape as the Comparative Opportunity Map (slide 22)
— keep them visually consistent since they're two views of the same three-country structure.

### Slide 14 — Singapore's target and strategies on SAF
- **Keep:** 1% SAF uplift target for flights departing Singapore from 2026, rising to 3–5% by
  2030 (subject to global SAF availability).
- **Add:** SAFCo (Singapore Sustainable Aviation Fuel Company Ltd.) as the central
  procurement/allocation entity managing the SAF Fund, plus its separate voluntary SAF
  procurement trial for corporate demand.
- **Add:** APSAC (Asia-Pacific Sustainable Aviation Centre), launched July 2025, as Singapore's
  regional engagement platform — note that this becomes a recurring "Singapore opportunity" hook
  in the Brazil deep dive too (slide 18).
- **Correct, with a caveat:** ticket sales for the levy begin 1 April 2026, but trade reporting
  suggests flight-departure applicability was **deferred from 1 October 2026 to 1 January 2027**
  (per a March 2026 announcement). Flag this on-slide as **"reported, pending direct CAAS
  confirmation"** — do not state it as settled fact.
- **Remove:** the current slide's claim that Singapore will host "the world's largest SAF
  production plant." This claim does not appear anywhere in the underlying research and isn't
  corroborated by any figure in the market deep dives — Acelen's Bahia project (the largest
  Americas project in this study) is 1 billion litres/year, not obviously "world's largest," and
  is Brazilian, not Singaporean. Cut this claim unless a separate source is found for it —
  presenting an unverified superlative carries the same risk flagged for the levy-timing item
  above.
- **Keep** the existing sector-strategy bullets (from Trade's "SAF Hub" deck): accelerate
  cellulosic production pathways to boost SAF liquidity; promote feedstock acceptance; help local
  enterprises seize new growth in the SAF value chain; anchor top global biofuels players in
  Singapore.

**Visual:** native — bullets/callout boxes; no custom build needed.

### Slide 15 — Section frame: SAF Market Deep Dives
No change. Section divider only.

### Slide 16 — US deep dive
Use the common deep-dive framework: current state of the SAF industry; policy & regulations
(feedstock sourcing, adoption, export — pull from slide 13's 45Z detail); feedstock source &
availability; state of SAF production capabilities; production innovation/R&D; key players
(mark which are already on GTP or the GTP target list); future outlook; strengths & challenges;
opportunities for Singapore.

**Singapore-opportunity framing for this slide:** name the Mexico/Canada→U.S. tallow-and-UCO
corridor directly here — this is the parallel, on the U.S. side of the border, to the
Argentina→Canada corridor detailed in the Canada slide. The two should read as the same
structural pattern (45Z's North American-content rule creating cross-border feedstock corridors)
applied on either side of the border, not as two unrelated country stories — cross-reference the
Canada slide explicitly.

**Visual:** native — narrative/bulleted deep-dive slide. Optional: a small stat-tile row (e.g.
key production capacity figures) can be done natively in the slide-content doc; no custom HTML
required.

### Slide 17 — Canada deep dive
Same framework as slide 16. Content specifics:
- **Policy:** federal Clean Fuel Regulations (credit-trading, SAF 0.8% of credit-generating fuel
  in 2024) + BC-LCFS (1% by 2028, rising to 3% by 2030) — detail beyond what's on slide 13.
- **Feedstock:** insufficient domestically; import-dependent, principally on Argentine soy oil.
  Note briefly that Argentina has its own emerging SAF ambitions (Santa Fe Bio — full detail on
  the watchlist slide) that are worth watching as a factor which could eventually compete with,
  not just supply, this corridor — don't present the corridor as a one-way, permanent flow.
- **Production/players:** Braya, Tidewater, Imperial Oil — note that most of this capacity is
  renewable diesel, not SAF specifically.

**Singapore-opportunity framing — reword away from presenting the Argentina→Canada corridor as
Canada's singular value proposition.** Lead instead with: **"Canada is one of several
cross-border feedstock corridors 45Z's re-nationalisation has opened up,"** and cross-reference
the parallel Mexico/Canada→U.S. corridor named on the US slide (16) — same structural pattern,
applied on either side of the border. Keep the concrete Braya tonnage figures (757,000t 2024 vs
48,000t 2023) as the flagship evidence, since this is the best-documented of the three corridors
described in the Background section above.

**Visual:** native — same treatment as slide 16.

### Slide 18 — Brazil deep dive (new, full profile — split out of the old combined LATAM slide)
This is the most fully-developed country profile and should get the same full framework as
US/Canada (policy, feedstock, production/players, R&D, outlook, Singapore opportunity). Use your
judgment on whether this needs one slide or two given the content density below — don't cram it
illegibly onto one slide if it doesn't fit.

- **Policy:** "Fuel of the Future" Law (Lei 14.993/2024) and ProBioQAV — well-to-wake target, 1%
  by 2027 rising to 10% by 2037.
- **Feedstock:** unmatched base in the region — soy, sugarcane/ethanol (for ATJ), UCO, macaúba.
- **Flagship project:** Acelen/Mubadala's Bahia biorefinery — ~$3B+ investment, 1 billion
  litres/year capacity, ~90% pre-contracted offtake, 2029 start, with a Finboot blockchain
  traceability partnership.
- **Petrobras:** likely offtake/production role — carry as a speaker-note caveat that there are
  no SAF-specific investor-relations disclosures confirming this; lean on ANP filings and trade
  press only.
- **Jobs figures — keep as two distinct numbers, never conflate:** ~3,600 peak construction jobs
  (trade press) vs. FGV's ~85,000 direct+indirect jobs over a ten-year full value chain horizon.
- **Market outlook:** the clearest structural Americas winner, 2027–2035.
- **Four Singapore-opportunity angles:** trade finance/structuring, certification/traceability,
  book-and-claim (tie back to the SAFc Registry named on slide 10), and the APSAC channel (named
  on slide 14).

**Visual:** native — narrative deep-dive slide, same treatment as US/Canada. A simple stat-tile
row (e.g. $3B+ / 1B litres/yr / ~90% pre-contracted / 2029) is a nice native addition; no custom
HTML build required for this slide.

### Slide 19 — Argentina / Chile / Colombia / Mexico watchlist (condensed)
Match a condensed watchlist format — not the full policy/feedstock/production/R&D/outlook
structure used for US/Canada/Brazil. Just what's changed or newly sourced for each:
- **Argentina:** no SAF-specific blending mandate, but the general biofuels programme (ethanol
  12%, biodiesel 7.5%) was extended by the lower house through 2030. Argentina is the world's
  largest soybean-oil exporter, but the majority of shipments currently go to **India**, not North
  America — a caveat against overreading the Argentina→Canada corridor (Section 3, Canada slide)
  as a large share of Argentina's total export base. Export taxes (retenciones) on soy oil/meal
  are on a legislated step-down path — 24.5% as of March 2025, cutting monthly through 2027 toward
  15% by end-2028 — which could improve domestic crush-sector economics and pull some soybean oil
  toward domestic biodiesel/SAF use rather than export. The clearest project-level development is
  **Santa Fe Bio**, a ~$400M joint venture (announced Aug 2025) between state oil major YPF and
  Essential Energy to build a SAF/HVO facility at YPF's San Lorenzo refinery, planned in two
  phases and financed partly through Argentina's Large Investment Incentive Regime, using UCO and
  crop residues as feedstock and explicitly positioned for export given San Lorenzo's port access.
  Flag capacity, phase timing and the YPF/Essential Energy ownership split as **unconfirmed** in
  public reporting — directional, not yet sized. **Singapore angle:** for now this is a
  watching-brief, not an active opportunity — the near-term angle is the same cross-border
  feedstock-structuring logic already identified for the Argentina→Canada corridor, with Santa Fe
  Bio worth tracking as a second angle: either a future direct engagement, or the signal that
  Argentina's own SAF ambitions could eventually compete with, rather than only supply, the
  corridor.
- **Chile:** relevance is entirely Haru Oni (HIF Global) — e-gasoline/e-methanol, **not** e-SAF;
  HIF capital is migrating elsewhere, including a planned $4B e-fuels plant in Brazil (announced
  Feb 2026); no SAF blending mandate exists.
- **Colombia:** Aerocivil's SAF Roadmap (Jan 2025) targets 100M gallons by 2035 / 450M by 2050;
  an MIT LatAm decarbonisation study finds ~250M litres/yr potential with a 20% palm/sugarcane
  output increase; regional SAF costs run $1.11–2.86/litre vs ~$0.70/litre for conventional fuel.
- **Mexico:** no binding SAF mandate or biofuels law as of mid-2026; a net UCO **exporter** rather
  than a domestic SAF input source; treat as a policy-trigger watch item only, not an active
  opportunity.

**Visual:** native — four short text blocks (Argentina's runs longer given the Santa Fe Bio
detail; keep the other three tight so the slide doesn't skew disproportionately toward Argentina),
no custom build needed.

### Slide 20 — Section: Summary & Recommendations
No change. Section divider only.

### Slide 21 — Americas "at a glance" (new)
This replaces a hidden Europe-only reference slide that existed purely as a format model. Build
new content driven by the Working Hypothesis (see Background section above): summarize the
strategic thesis and the three judgments as a single scannable executive-summary slide — this is
the "headline takeaway" that opens the Summary & Recommendations section, before the detailed
Comparative Opportunity Map on slide 22.

**Visual:** native — text/callout treatment of the Working Hypothesis and three judgments.
Optional: a simplified 3-corridor mini-diagram (Argentina→Canada / Mexico-Canada→US /
Brazil→US-Europe) can echo slide 11's trade-flow diagram at a smaller, less detailed scale, but
this is a nice-to-have, not required — don't duplicate slide 11's full HTML build here.

### Slide 22 — Comparative Opportunity Map + house view + industry events + next steps
Replace the old separate North America / LatAm house-view slides with **one unified comparative
table** across the three deep-dive markets (Brazil, US, Canada), scored on five dimensions:
feedstock scale, policy certainty, project scale/maturity, near-term Singapore relevance, and
realistic volume timeline.

**Scope decision — keep to three markets, not seven.** Argentina, Chile, Colombia and Mexico are
the condensed watchlist (slide 19) and are **not** scored on this table — footnote them explicitly
as "Argentina, Chile, Colombia and Mexico are tracked as a watchlist, not scored here" rather than
force-fitting light-touch scores for markets whose sourcing wasn't built for this kind of
comparison.

**The scored data** (exact cell content — use this verbatim):

| Dimension | United States | Brazil | Canada |
|---|---|---|---|
| Feedstock scale | **Medium** — Large but now North America-restricted under 45Z | **High** — Largest and most diversified in the region (soy, sugarcane/ethanol, UCO, macaúba) | **Low** — Insufficient domestically; import-dependent (Argentina soy oil) |
| Policy certainty | **Medium** — 45Z extended to 2029 but credit value cut 43%; GREET/FD-CIC still finalising | **High** — Legislated ProBioQAV pathway to 2037; ANP SAF-specific rules still pending (2H 2026) | **Low–Medium** — CFR credit market not SAF-specific; BC-LCFS is the only hard SAF mandate (from 2028) |
| Project scale / maturity | **High** — Largest existing capacity base (DGD, World Energy, Montana Renewables) but still import-dependent | **High** — Acelen ~90% pre-contracted, $3bn+, FID'd, 2029 start | **Low** — Braya/Tidewater/Imperial Oil capacity is mostly renewable diesel, not SAF |
| Near-term SG relevance | **Medium** — Reoriented: Canadian/Mexican feedstock structuring, traceability, book-and-claim rather than Asian UCO pass-through | **High** — Trade finance, traceability, book-and-claim, APSAC channel | **Medium** — Corridor structuring, not production (flagged: same score as the US, but for a structurally different reason — see reading paragraph) |
| Realistic volume timeline | Ongoing, but growth pace uncertain post-OBBBA | 2029 onward (Acelen); mandate ramps through 2037 | BC mandate from 2028; national volume remains marginal before then |

**Reading paragraph (use near-verbatim):** Brazil scores well across every dimension that
matters and is the clear near-term priority. The U.S. remains the region's largest existing
capacity base but Singapore's value proposition there has narrowed from feedstock pass-through
to structuring/traceability/book-and-claim. Canada's production case is weak almost everywhere
it's scored — except the one dimension that counts most for Singapore, near-term relevance,
where it lands at Medium, the same score as the U.S. That gap exists entirely because 45Z's
North American-content rule turned Canada into a feedstock corridor, not because Canada is
building SAF capacity.

**Cross-market link — state this explicitly, don't let the two country stories read as
unrelated:** Canada's and the U.S.'s Singapore relevance both flow from the same
corridor-structuring logic — 45Z's North American-content rule pushed Argentine soy oil into
Canada and Mexican/Canadian tallow-UCO into the U.S. This is one structural story with two live
examples, not two independent market narratives.

**Also on this slide:**
- Industry events list: Argus North American Biofuels, LCFS & Carbon Markets Summit — California,
  15–17 Sep.
- "Next Steps — to work with Trade on this." Keep as-is; no further content available for this
  item.

**Visual: BUILD as standalone HTML** — `saf-opportunity-map.html`. This effectively rebuilds a
visualization that already exists for this deck, so match its established design: a 3-column ×
5-row scored grid with ordinal color-coded cells (a single blue accent ramp, four levels: Low /
Low–Medium / Medium / High), the Canada near-term-relevance cell visually flagged/highlighted
since its "Medium" score needs the reading-paragraph explanation to not read as a data error, the
reading paragraph set below the grid, and a footer note that Argentina/Chile/Colombia/Mexico are
tracked as an unscored watchlist. See the "Visual style reference" section below for the exact
color tokens to use.

---

## Output file structure

**`slide-content.md`** — use this heading pattern for each slide so it's easy to scan and hand
off:

```
## Slide N — Title

**Action:** [KEEP / TWEAK / BUILD / MERGE / new]

[body content, written out in full — bullets, tables, whatever the slide needs]

**Speaker notes:** [any caveat that belongs here rather than in the body]

**Visual:** [native | BUILD → filename.html]
```

**HTML files** — exactly four, matching the BUILD visuals identified above:
- `saf-cost-economics.html` (slide 9)
- `saf-trade-flows.html` (slide 11)
- `saf-policy-overview.html` (slide 13)
- `saf-opportunity-map.html` (slide 22)

Each should be a single self-contained file (inline CSS, no external requests) sized reasonably
for a 16:9 slide screenshot (roughly 1280×720 or a similar widescreen aspect ratio).

---

## Visual style reference (use if you don't have the `dataviz` skill available)

This is extracted from a visualization already built for this deck, so matching it keeps new
visuals consistent with existing ones. Warm-neutral background, single blue accent used as a
4-step ordinal ramp (not a rainbow of category colors), light/dark aware:

```css
:root {
  --page:        #f9f9f7;   /* page background, light */
  --surface:     #fcfcfb;   /* card/surface background, light */
  --ink:         #0b0b0b;   /* primary text, light */
  --ink-2:       #52514e;   /* secondary text, light */
  --ink-muted:   #898781;   /* muted/caption text, light */
  --line:        #e1e0d9;   /* borders/dividers, light */
  --accent:      #2a78d6;   /* single brand-blue accent */
  --accent-wash: rgba(42,120,214,0.08);

  /* ordinal ramp, light mode — Low to High */
  --lvl1: #86b6ef;  /* Low */
  --lvl2: #5598e7;  /* Low-Medium */
  --lvl3: #2a78d6;  /* Medium */
  --lvl4: #184f95;  /* High */
}
@media (prefers-color-scheme: dark) {
  :root {
    --page: #0d0d0d; --surface: #1a1a19; --ink: #ffffff; --ink-2: #c3c2b7;
    --ink-muted: #898781; --line: #2c2c2a; --accent: #3987e5;
    --accent-wash: rgba(57,135,229,0.14);
    /* ordinal ramp, dark mode — ramp direction reverses in intensity */
    --lvl1: #184f95; --lvl2: #256abf; --lvl3: #5598e7; --lvl4: #9ec5f4;
  }
}
```

Font: `system-ui, -apple-system, "Segoe UI", sans-serif`. Keep type sizes generous — these are
meant to be screenshotted at a size that reads clearly projected on a screen, not squinted at on
a laptop.

---

## Before you finish — self-check

- [ ] Every one of the 22 slides above has a `slide-content.md` entry.
- [ ] All four HTML visualizations are built and open correctly in a browser with no console
      errors.
- [ ] No number was invented — the Americas biofuels market-sizing gap is stated as a gap, not
      filled with an estimate.
- [ ] Both pending items (slide 12 Singapore strengths, slide 14 CAAS levy timing) are still
      flagged as pending in the output, not stated as resolved.
- [ ] The three cross-cutting corrections (Montana Renewables $1.67B, World Energy/Air Products
      Feb 2025 exit, Acelen's two distinct jobs figures) are correct everywhere they appear, not
      just in their "home" slide.
- [ ] The three sourcing caveats (Petrobras/Ecopetrol, BC-LCFS, FGV/Embrapa) appear in speaker
      notes, not as slide-body claims.
- [ ] The Comparative Opportunity Map (slide 22) scores exactly three markets (US/Brazil/Canada),
      not seven, with Argentina/Chile/Colombia/Mexico footnoted as an unscored watchlist.
- [ ] Argentina's watchlist entry (slide 19) carries its full justification (Santa Fe Bio, biofuels
      law extension to 2030, retenciones step-down) and is not conflated with a full country
      deep-dive — it stays in the condensed watchlist format, not the US/Brazil/Canada framework.

# Prompt: Close the coverage gaps in the Americas SAF Study deck

Paste everything below to a fresh Claude Code (Sonnet) session. It is self-contained for the
*gap-closing* pass — you do not need this conversation's history to execute it. You will,
however, need the current deck content (see "What you're working from," below) and, ideally,
`slide-generation-prompt.md`, `slide-revisions.md`, `Datasources.md` and `FreeSources.md` from
this repo for conventions and source tiers.

---

## Your mission

The Americas SAF deck ("Americas' SAF Market Outlook, Strategic Insights and Opportunities") has
already been through one full revision pass (see `slide-generation-prompt.md` /
`slide-revisions.md` in this repo — that pass is done and is not what you're redoing). A second
audit was then run specifically to find **content that's missing from the deck entirely**, not
errors in what's already there. This prompt is that audit's output, turned into build
instructions.

You are **adding new material to close those gaps** — not rewriting the deck, not re-litigating
decisions already made in the prior revision pass. Every item below is either (a) a new fact/topic
to add to an existing slide, or (b) a new slide to insert. Nothing below asks you to remove or
contradict existing content.

Produce the same two kinds of deliverable as the prior pass:
1. Updated/new slide content — full body text, speaker notes, and a `Visual:` line where relevant
   — added into wherever this project's current slide-content source lives (ask the user if you
   can't find `slide-content.md`; if only the deck text exists as pasted chat content or a PPTX,
   ask for it).
2. Any new standalone screenshot-ready HTML visualization this pass calls for (see the
   competitive-hub-benchmark item below) — self-contained, both light/dark viewing, following this
   repo's existing house style (load the `dataviz` skill first if available; otherwise match
   `saf-comparison-chart.html`'s style as a reference).

## What you're working from

Slide references below use the **current deck's own numbering** — "DECK SLIDE NN (page P)" —
i.e., the deck as it exists *after* the first revision pass, not the original 24-slide source
outline. If you're starting from `currentslideflow.md` or `slide-revisions.md` instead, note those
use the *old* pre-revision numbering (1–24) and will need re-mapping; the renumbering table near
the bottom of `slide-revisions.md` gives that mapping.

## Ground rules (same discipline as the prior pass)

- **Never invent numbers.** Every new figure below (Neste capacity, RIN values, LCFS credit
  prices, Rotterdam/Fujairah throughput, SAF Grand Challenge targets, etc.) must be verified
  against a primary or clearly-attributed secondary source before it goes on a slide. If you
  cannot verify a figure, say so in speaker notes as "pending verification" rather than dropping
  it or guessing at a value.
- **Keep unresolved items flagged as pending, not resolved.** Several items below are genuinely
  open questions for Trade (see the "questions for Trade" slide) — do not resolve these yourself.
- **Sourcing caveats belong in speaker notes, not slide body text**, consistent with how the rest
  of the deck is written.
- Use this repo's existing sourcing tiers (`Datasources.md` for the full map, `FreeSources.md` for
  the free-tier subset) as your first stop for verification. Good candidate sources per item are
  suggested below, but confirm current URLs/figures yourself — don't take the suggestions as
  already-verified.
- Match the deck's existing tone and structure: each market/topic slide states policy, feedstock,
  players, then a "★ possible Singapore angle" callout where relevant — follow that pattern for
  new content rather than inventing a new slide format.

---

## Part 1 — Content/topic gaps (net-new material, nothing like this exists in the deck today)

1. **Neste's Singapore refinery (Tuas).** This is the single largest omission. Neste is the
   world's largest SAF/renewable diesel producer by volume and already operates a production
   facility in Singapore — yet a deck arguing "Singapore as Asia's leading SAF hub" (DECK SLIDE
   02) never names it. Add to the Singapore strengths section, **DECK SLIDE 12 (page 8)**, which
   is currently a pending Trade-input placeholder — this item does not require Trade input, it's
   independently verifiable, so it can be added now rather than left fully blank. Verify current
   Tuas SAF/renewable-fuels capacity and product slate against Neste's own investor
   disclosures/press releases, not secondary trade press alone.
2. **RFS / RIN credit stacking with 45Z.** DECK SLIDE 13 (page 9) covers 45Z as if it's the only
   US federal mechanism at play. In practice, US SAF/biofuel economics are driven by 45Z credits
   *stacked* with Renewable Fuel Standard RIN credits. Omitting this understates/misstates how US
   producer economics actually work, which matters directly for any Singapore trade-finance
   angle into that market. Add a short RIN-stacking explainer to DECK SLIDE 13 and/or the US deep
   dive, **DECK SLIDE 16 (page 11)**. Source: EPA's RFS program pages for RIN mechanics.
3. **California LCFS, defined.** DECK SLIDE 22 (page 17) already lists "LCFS & Carbon Markets
   Summit, California" as an industry event, but the deck never explains what LCFS is, that it's
   distinct from Canada's BC-LCFS (already covered on DECK SLIDE 13), or how SAF/aviation
   interacts with it. Add a one- or two-line definition wherever LCFS is first referenced — likely
   DECK SLIDE 13 or 16. Source: California Air Resources Board (CARB).
4. **DOE/USDA/FAA SAF Grand Challenge target (3B gallons by 2030 / 35B by 2050).** This is the
   headline US federal SAF production target that 45Z exists to support, and it's absent from the
   deck entirely, leaving the US policy section without the top-line goal that gives 45Z's
   mechanics context. Add to DECK SLIDE 13 or 16. Source: the original interagency SAF Grand
   Challenge announcement/roadmap (DOE/USDA/FAA/EPA) — verify current status, since this was a
   prior-administration initiative and its standing may have changed; state current status
   accurately rather than assuming it's unchanged.
5. **GREET model / carbon-intensity (CI) scoring, explained in plain terms.** DECK SLIDE 22
   (page 17) flags "GREET/FD-CIC still finalising" under policy certainty but never explains what
   GREET does. CI scoring is the mechanism that actually determines 45Z credit value per
   feedstock/corridor — it's the variable that decides whether a given corridor is economic at
   all, not a minor caveat. Add a short explainer to DECK SLIDE 13 or 16. Source: EPA/Treasury
   GREET-related guidance, Federal Register 45Z rulemaking.
6. **Foreign Entity of Concern (FEOC) restriction, spelled out.** DECK SLIDE 13 (page 9) lists
   "'Foreign entity of concern' ownership restrictions added" as a bare bullet. Given Singapore
   trading houses' exposure to Chinese-origin UCO (see DECK SLIDE 11's China UCO redirection data)
   and Chinese-backed refining capital, what FEOC actually restricts is directly relevant to
   whether a Singapore-structured deal stays 45Z-eligible. Expand the bullet into 1–2 sentences of
   actual restriction detail. Source: Federal Register, the OBBBA/45Z FEOC provisions themselves.
7. **Certification schemes, named specifically (ISCC EU / ISCC CORSIA / RSB).** The value-chain
   slide, **DECK SLIDE 10 (page 6)**, has a generic "Regulators & Certifiers" cross-cutting box
   but never names which certification scheme governs eligibility into which destination market.
   For a hub built on trade/structuring, the certification scheme is often the actual constraint
   on which corridor a given cargo can legally flow through. Add specificity to DECK SLIDE 10 —
   which scheme(s) apply to EU-bound vs. US-bound vs. Asia-bound cargo. Source: ISCC System GmbH,
   RSB (Roundtable on Sustainable Biomaterials).
8. **Asia-side demand proof points, incl. Singapore Airlines.** The whole deck is
   feedstock/production-side. There's no mention of Singapore Airlines' own SAF pilot
   flights/procurement or Changi Airport blending activity — the demand-side proof point sitting
   in Singapore's own backyard, and a natural complement to DECK SLIDE 14's coverage of CAAS's SAF
   uplift target. Add to **DECK SLIDE 14 (page 10)**. Source: Singapore Airlines' own
   sustainability disclosures/press releases, CAAS.
9. **India as an Asian demand market.** **DECK SLIDE 19 (page 15)**, Argentina entry, notes
   Argentine soy oil goes "mostly to India, not North America" as a caveat against reading the
   Argentina→Canada corridor as large relative to Argentina's total exports — but never asks the
   inverse question: is India itself a growing SAF demand market Singapore could serve? Add a
   watchlist flag to DECK SLIDE 19 (or DECK SLIDE 22's summary table as a forward-looking note).
   Treat as genuinely open/unsized — do not manufacture a market-sizing figure for this.

## Part 2 — Sourcing/rigor gaps (structural, not a missing fact)

10. **No confidence/verification rollup slide.** Caveats are currently scattered per-slide (FGV
    Acelen figures on DECK SLIDE 18a/18b, Embrapa/USP macaúba research, Petrobras/Ecopetrol roles,
    Santa Fe Bio sizing on DECK SLIDE 19, BC-LCFS registry data on DECK SLIDE 13/17). Before this
    deck goes beyond internal Trade review, build **one new appendix slide** that aggregates every
    "not yet independently verified" item across the deck into a single list, so a reader doesn't
    have to reconstruct it from individual speaker notes. This is a compilation task, not new
    research — pull the existing caveats forward rather than re-deriving them.
11. **No confidence-tag legend.** The deck currently uses inconsistent ad hoc phrasing ("as
    supplied, not independently re-verified," "unconfirmed primary source," "directionally
    corroborated") without a shared convention. Add a short legend — either as a slide-master
    footer convention or a line on the new appendix slide from item 10 — so severity is
    comparable at a glance.

## Part 3 — Strategic/Singapore-angle gaps

12. **Compiled "questions for Trade" slide.** Nearly every deep-dive slide ends with some version
    of "untested with Trade" or "open question for Trade" — DECK SLIDE 11, 16, 17, 18b, and the
    scoring table on DECK SLIDE 22 all raise this but never convert it into an actual discussion
    agenda. Build **one new slide** that lists the concrete questions to put to Trade in the
    meeting (e.g.: "Can Singapore trading houses structure/finance the Mexico–Canada→U.S. tallow
    corridor?", "Is APSAC (DECK SLIDE 14) a usable channel for Americas engagement?", "Does
    Singapore want a trade-finance, certification/traceability, or book-and-claim role in Brazil,
    or some combination?"). This should replace or extend the current bare "Next steps: To work
    with Trade on this" line on **DECK SLIDE 22 (page 17)**.
13. **Urgency/timeline framing.** 45Z's North-American-content feedstock restriction is already in
    effect (2026) and the credit sunsets in 2029 (DECK SLIDE 13). The deck states these dates but
    never frames the decision window this creates for Singapore — i.e., roughly how much runway
    exists before a corridor-structuring opportunity is moot. Add a line to **DECK SLIDE 21
    (page 16)** or 22 making this explicit as a "why now" framing, not a new fact.
14. **Downside/inaction case.** The deck frames this entirely as upside-if-Singapore-acts. Add an
    explicit "what's the cost of not moving" framing — e.g., another hub (see Part 4) capturing
    the corridor-structuring role first — to DECK SLIDE 21 or the new "questions for Trade" slide
    from item 12. Keep this qualitative; do not invent a probability or dollar figure for what's
    lost.

## Part 4 — Competitive/benchmarking gaps (largest structural gap — nothing like this exists today)

15. **New slide: competitive hub benchmark.** The deck asserts a vision of "Singapore as Asia's
    leading SAF hub" (DECK SLIDE 02) but never once benchmarks Singapore against the hubs it would
    actually compete with for the corridor-structuring role described throughout Section 04. Build
    one new slide comparing Singapore against:
    - **Rotterdam/ARA** — Europe's dominant renewable diesel/SAF hub, anchored by Neste's
      Rotterdam refinery (the same company flagged in item 1 — note that connection explicitly:
      Neste operates in both Rotterdam and Singapore, which sharpens rather than dilutes the
      comparison).
    - **Fujairah/UAE** — an emerging Middle East bunkering/biofuels hub, geographically relevant
      to some of the same East-West trade lanes discussed in Section 04.
    - **Other Asian contenders** — Malaysia (Petronas), South Korea, Japan — as potential
      competitors for the same Southeast Asia hub role.
    Use the same qualitative, unweighted scoring convention already established on DECK SLIDE 22
    (feedstock scale / policy certainty / project maturity / near-term relevance) so the new slide
    reads as part of the same analytical framework, not a bolt-on. This is likely the one item in
    this whole prompt that also justifies a new HTML visual (a hub-comparison table or map,
    matching `saf-comparison-chart.html`'s existing house style) — build it if the comparison
    has enough sourced substance to justify a visual; if sourcing comes back thin, a plain table
    on the slide is fine and preferable to a sparse chart.
    Sourcing starting points: Neste's own facility disclosures (Rotterdam vs. Singapore capacity),
    Fujairah Port / ADNOC-linked announcements for UAE biofuels activity, Petronas/Malaysia
    government SAF policy announcements. Flag anything that comes back thin as a watchlist-style
    item rather than forcing a fully scored row.
16. **Hub-funding-model comparison.** DECK SLIDE 09 (page 5) already compares Europe/US/Singapore
    on *national demand-side* policy (polluter-pays / tax credit / hybrid levy) — that is not the
    same axis as hub-vs-hub competitive positioning. If sourcing supports it, add a short note to
    the new competitive-hub-benchmark slide (item 15) on how Rotterdam/Fujairah fund or attract SAF
    activity, distinct from DECK SLIDE 09's existing comparison. Do not duplicate DECK SLIDE 09 —
    cross-reference it instead.

---

## Net-new slides this prompt calls for

- **Competitive hub benchmark** (item 15, folds in item 16) — insert in Section 04 or as a lead-in
  to Section 05, since it's most useful right before the existing house-view synthesis on DECK
  SLIDE 21/22.
- **Confidence/sourcing rollup + legend** (items 10–11) — appendix slide, likely placed right
  before or after DECK SLIDE 22.
- **Questions for Trade** (item 12, folds in items 13–14) — replaces/extends the "Next steps" line
  on DECK SLIDE 22, or sits as its own slide immediately after it.

Everything else (items 1–9) is an addition to an existing slide, not a new one — see each item's
placement note above.

## Deliverable checklist

- [ ] Items 1–9 added to their named existing DECK SLIDE, in the deck's existing voice/format.
- [ ] Three new slides built (competitive benchmark, confidence rollup, questions for Trade).
- [ ] Any new figure sourced and cited; anything unverifiable explicitly marked pending in speaker
      notes, not silently dropped or estimated.
- [ ] New HTML visual only built if the competitive-hub-benchmark sourcing supports it (see item
      15) — otherwise a plain in-slide table is the right call.
- [ ] If a figure from this pass turns out to be dashboard-worthy (e.g., Neste Tuas capacity,
      Rotterdam/Fujairah throughput, a RIN or LCFS credit price), add it to `stats_data.py` /
      `data_sources.py` following those files' existing row format and citation convention — this
      is optional polish, not required for the deck itself.

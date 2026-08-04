· /plan to edit
Plan: Americas SAF Research Scan

Context

The user is building an Americas SAF study for Enterprise Singapore, following on from an earlier Europe SAF deck. The project folder (/Users/wooz/Documents/GitHub/saf study) currently contains only one substantive file: workingdraft.md, an untracked, ~5,750-word prose draft covering six markets (US, Canada, Brazil, Chile, Colombia, Mexico) with a working hypothesis, market context section, and per-market deep dives. It has almost no sourcing (one inline citation in 212 lines), several unfinished "Singapore Opportunity" subsections (Brazil's is literally "To append"), a promised-but-missing Section 4 opportunity map, and no HS-code/trade-flow content. No Europe SAF deck exists anywhere in this repo.

The user now wants a distinct deliverable: a research scan (not a deck, not an edit to workingdraft.md) that is tightly source-grounded, separates confirmed facts from hypotheses, and follows an 11-section structure the user specified, refocused on a narrower priority set (US + Brazil deep dive, Canada baseline, Chile/Argentina watchlist). This scan will be used to brief Xiaowen and to decide what goes into the actual deck later.

Per the user's answers to clarifying questions:
- Europe deck: not available in this session — proceed without it. Section 10 (deck outline) will use workingdraft.md's existing structure plus standard SAF-deck conventions as a proxy, and will be explicitly flagged as needing review once the user shares the real Europe deck.
- Colombia/Mexico: out of scope for new research, but keep a short appendix note referencing what workingdraft.md already has on them, so that work isn't lost.
- workingdraft.md's existing claims (OBBBA details, Acelen/Mubadala financing, Singapore SAF Levy mechanics, etc.): treat as leads, not facts — independently verify each against primary/reputable sources during research; cite properly if confirmed, flag explicitly if unconfirmed or contradicted.

Output

A new markdown file, Americas_SAF_Research_Scan.md, created at the project root (/Users/wooz/Documents/GitHub/saf study/). workingdraft.md is left untouched — it's a source of leads, not something being edited. Nothing is committed to git unless the user asks afterward.

Approach

1. Parallel research (background agents, general-purpose, WebSearch/WebFetch-equipped)

Given the breadth (US policy, Brazil policy, Canada/Chile/Argentina, HS codes, Singapore angle — each needing multiple live searches since today is 2026-07-13, well past training cutoff), split research into 4 parallel background agents to keep raw search output out of the main context window. Each agent returns a structured brief: claim → source name/link → publication date → confirmed/hypothesis flag, and explicitly notes where it corroborates, updates, or contradicts a specific claim from workingdraft.md.

- Agent A — US deep dive: 45Z (post-OBBBA terms, effective dates, credit values), OBBBA text/implications, tariffs/trade measures touching SAF or feedstocks, domestic-content/localisation rules, feedstock sourcing split (UCO, tallow, soybean oil, corn oil, ethanol), major producers/projects/offtakes (verify Diamond Green Diesel, World Energy, Montana Renewables, Phillips 66, Neste claims from workingdraft.md; find others), FAST grant status, implications for global feedstock flows (e.g. the claimed Chinese UCO export drop to the US). Sources to prioritize: Federal Register, IRS/Treasury, EPA, DOE, EIA, USDA, Argus, S&P Global, BNEF, company press releases cross-checked against independent coverage.
- Agent B — Brazil deep dive: SAF mandate (ProBioQAV / RenovaBio-linked framework) and 2027+ timeline, alcohol-to-jet and cellulosic/ethanol SAF potential, feedstocks and industrial base (sugarcane ethanol especially), major producers/projects/offtakes (verify Acelen/Mubadala Bahia biorefinery figures — $3bn, 1bn L/yr, legislated pathway to 2037 — plus find others), export/regional hub ambitions. Sources: ANP, MME, EPE, Reuters/local Brazilian trade press, IEA, ICAO.
- Agent C — Canada / Chile / Argentina / HS codes: Canada SAF policy (Clean Fuel Regulations), major projects (verify Braya Newfoundland claim), producers, offtake/airline demand signals. Chile and Argentina — search for material SAF-specific developments (mandates, projects, feedstock advantages, offtakes); if genuinely thin, say so rather than padding. HS code research: relevance/limits of HS 3826 (biodiesel blends) and HS 2710 (petroleum/mineral oils, likely too broad), plus any more precise codes for UCO, tallow, ethanol, renewable diesel, SAF specifically, and caveats on using trade data to infer SAF flows (blending, re-export, code granularity issues).
- Agent D — Singapore angle, value chain/pathways, cross-cutting offtakes: Singapore SAF Levy mechanics and dates, CAAS Sustainable Air Hub Blueprint, SAFCo, APSAC (verify workingdraft.md's Oct 1 2026 levy start, Apr 1 2026 ticket-sale trigger, 1%→3-5% uplift targets, APSAC July 2025 launch); SAF pathway fundamentals (HEFA, alcohol-to-jet, cellulosic/waste-based) with 2024-2026 sourcing; recent (2024-2026) notable Americas SAF offtake examples spanning airlines/producers/airports/fuel buyers not already covered by Agents A/B.

2. Synthesis

Compile all four briefs into Americas_SAF_Research_Scan.md following the user's exact 11-section structure (Executive Summary through Open Questions and Follow-ups), plus a short closing appendix note on Colombia/Mexico (out-of-scope, pointing back to workingdraft.md's existing sections). Requirements carried through from the brief:
- Every factual point gets an inline source link and date where available.
- Confirmed facts vs. hypotheses/implications/open questions kept visibly separate (not blended into flowing prose).
- 2024-2026 sources prioritized; older sources only where foundational, and labeled as such.
- Conflicting sources flagged explicitly rather than silently reconciled.
- Section 10 (deck outline) marked as provisional/needs-review-against-real-Europe-deck.
- Section 11 open questions grouped exactly as specified: Trade/Andrew, Brazil/São Paulo OC, US OC, Canada OC, internal SAF/aviation colleagues, Julien/São Paulo attachment.
- Plain, working-level tone — no inflated claims, no filler.

3. Self-check pass

Before finishing, re-scan the draft for: (a) any factual sentence lacking a source, (b) any place a hypothesis reads like a stated fact, (c) whether Chile/Argentina section honestly reflects thin vs. strong findings, (d) whether HS code caveats are clear enough to prevent over-reading trade data.

Verification

This is a research/writing deliverable, not code — verification means confirming the output actually meets the brief before handing it over:
- Read through the finished Americas_SAF_Research_Scan.md end-to-end and confirm all 11 requested sections are present with the right sub-content.
- Spot-check a handful of the most load-bearing citations (e.g. 45Z credit value, OBBBA signing date, Brazil mandate timeline, SG SAF Levy dates) by re-checking the source link resolves to what's claimed.
- Confirm every claim carried over from workingdraft.md is either sourced-and-confirmed, sourced-with-an-update/correction, or explicitly flagged unconfirmed — none should appear unlabeled.
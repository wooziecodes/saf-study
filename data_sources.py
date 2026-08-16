"""Structured catalog of data sources for the Americas SAF study.

Extracted from Datasources.md. Kept as plain Python so the Streamlit app
can import it directly with no parsing step.
"""

# Fixed categorical color order (validated palette, dataviz skill default).
# Reused everywhere a category needs a color so identity stays consistent.
CATEGORY_COLORS = {
    "Government & Regulatory": "#2a78d6",       # blue
    "Trade & Feedstock Flow": "#eb6834",        # orange
    "Market Intelligence & Industry": "#1baf7a",  # aqua
    "Company & Project": "#eda100",             # yellow
    "Academic & Research": "#e87ba4",           # magenta
    "Certification & Traceability": "#008300",  # green
    "Trade Press": "#4a3aa7",                   # violet
}

CATEGORY_COLORS_DARK = {
    "Government & Regulatory": "#3987e5",
    "Trade & Feedstock Flow": "#d95926",
    "Market Intelligence & Industry": "#199e70",
    "Company & Project": "#c98500",
    "Academic & Research": "#d55181",
    "Certification & Traceability": "#008300",
    "Trade Press": "#9085e9",
}

# Curated per-market shortlist (refreshed 2026-08-16). Pruned from an earlier 89-entry research
# log down to the best free/open-access primary portal(s) per market, so an officer doing
# follow-up research beyond the deck has one clean list to click through rather than a raw
# research dump. The fuller research archive (incl. paid/unconfirmed sources) still lives in
# Datasources.md / FreeSources.md for anyone who needs to go deeper.
# cost values are normalized to: Free, Freemium, Paid, Restricted, Unknown
SOURCES = [
    # --- United States ---
    dict(category="Government & Regulatory", region="United States", name="EIA Petroleum & Other Liquids Data",
         url="https://www.eia.gov/petroleum/data.php", cost="Free", frequency="Monthly",
         description="Production/capacity/feedstock-consumed/imports-exports for biodiesel, renewable diesel, SAF."),
    dict(category="Government & Regulatory", region="United States", name="EPA RIN Generation Data / EMTS",
         url="https://www.epa.gov/fuels-registration-reporting-and-compliance-help", cost="Free", frequency="Monthly",
         description="RIN generation/retirement by D-code, incl. SAF-eligible categories. Best free proxy for actual RFS-compliant volumes."),
    dict(category="Government & Regulatory", region="United States", name="CARB LCFS Data Dashboard",
         url="https://ww2.arb.ca.gov/applications/lcfs-data-dashboard", cost="Free", frequency="Monthly",
         description="Credit/deficit generation by pathway and credit prices — best proxy for real transacted SAF/renewable-diesel volumes and pricing."),
    dict(category="Trade & Feedstock Flow", region="United States", name="USITC DataWeb",
         url="https://dataweb.usitc.gov/", cost="Free", frequency="Monthly",
         description="US Census-sourced import/export data, 1989–present, HTS 10-digit. Best free source for US-side UCO/tallow imports by origin — exportable to CSV."),

    # --- Brazil ---
    dict(category="Government & Regulatory", region="Brazil", name="ANP RenovaBio CBIO Dynamic Panel",
         url="https://www.gov.br/anp/", cost="Free", frequency="Fortnightly",
         description="CBIO issuance/registration/retirement plus B3 exchange price data. Central Brazil source for this study."),
    dict(category="Government & Regulatory", region="Brazil", name="Comex Stat / MDIC",
         url="https://comexstat.mdic.gov.br/", cost="Free", frequency="Monthly",
         description="Official Brazilian customs data (SISCOMEX) at HS-code level — exportable trade-flow data."),

    # --- Canada ---
    dict(category="Government & Regulatory", region="Canada", name="ECCC Clean Fuel Regulations Credit Market Reports",
         url="https://www.canada.ca/en/environment-climate-change.html", cost="Free", frequency="Quarterly",
         description="Credit generation by category (CC1/CC2/CC3), prices, trading activity. Confirms SAF's negligible CFR credit share."),

    # --- Mexico ---
    dict(category="Government & Regulatory", region="Mexico", name="Mexico SIE (SENER)",
         url="https://sie.energia.gob.mx/", cost="Freemium", frequency="Ongoing",
         description="Official national energy statistics portal; public and institutional tiers."),

    # --- Colombia ---
    dict(category="Market Intelligence & Industry", region="Colombia", name="Fedebiocombustibles",
         url="https://www.fedebiocombustibles.com/", cost="Free", frequency="Periodic",
         description="Colombian biodiesel/ethanol sales volumes; industry-association data treated as sector record."),

    # --- Argentina ---
    dict(category="Trade & Feedstock Flow", region="Argentina", name="INDEC",
         url="https://www.indec.gob.ar/", cost="Free", frequency="Monthly",
         description="Official Argentine trade statistics by HS code — tracks the Argentina soy-oil-to-Canada corridor."),

    # --- Singapore ---
    dict(category="Government & Regulatory", region="Singapore", name="CAAS Newsroom / Policy Documents",
         url="https://www.caas.gov.sg/", cost="Free", frequency="Ad hoc",
         description="SAF Levy mechanics, rate bands, SAFCo mandate. Check for the March 2026 levy-timing deferral before citing dates."),
    dict(category="Company & Project", region="Singapore", name="Neste Singapore Refinery (Tuas)",
         url="https://www.neste.com/en-sg/about-neste/how-we-operate/production/singapore-refinery", cost="Free", frequency="Static",
         description="Official facility page for Neste's Tuas refinery — world's largest renewable diesel/SAF facility (~1Mt/yr SAF capability)."),

    # --- Global / International ---
    dict(category="Government & Regulatory", region="International", name="ICAO SAF Production Facilities Tracker",
         url="https://www.icao.int/SAF/SAF-production-facilities", cost="Free", frequency="Ongoing",
         description="Official list of existing and announced SAF production facilities."),
    dict(category="Government & Regulatory", region="International", name="IATA SAF Facilities Map & Fact Sheet",
         url="https://www.iata.org/en/programs/sustainability/sustainable-aviation-fuel-saf/", cost="Free", frequency="Semi-annual",
         description="Location/technology/capacity/status by facility; source of the industry's 2.4Mt / 0.8%-of-jet-fuel 2026 figures."),

    # --- Asia-Pacific hub competitors (for benchmarking Singapore's hub positioning) ---
    dict(category="Government & Regulatory", region="Malaysia", name="Malaysia SAF Market Intelligence (US ITA)",
         url="https://www.trade.gov/market-intelligence/malaysia-energy-sustainable-aviation-fuel", cost="Free", frequency="Periodic",
         description="US Dept. of Commerce brief on Petronas/Malaysia's SAF build-out (targeting ~1Mt/yr by 2028) — Southeast Asia hub-benchmark comparator to Singapore."),
    dict(category="Government & Regulatory", region="South Korea", name="MOLIT/MOTIE SAF Mandate Press Releases",
         url="https://www.molit.go.kr/USR/NEWS/m_71/lst.jsp", cost="Free", frequency="Ad hoc",
         description="Official Korean government press releases on the SAF blending mandate (1% from 2027, ramping to 7-10% by 2035). Korean-language primary source."),
    dict(category="Government & Regulatory", region="Japan", name="METI/MLIT SAF Public-Private Council",
         url="https://www.meti.go.jp/shingikai/energy_environment/saf/index.html", cost="Free", frequency="Periodic",
         description="Official proceedings of Japan's joint METI/MLIT council on SAF introduction (targets, supply-side mandate, subsidy design). Japanese-language primary source."),
    dict(category="Company & Project", region="Netherlands", name="Neste Rotterdam Refinery Expansion",
         url="https://www.neste.com/news/neste-invests-in-its-world-scale-renewable-products-refinery-in-rotterdam", cost="Free", frequency="Static",
         description="Neste's own investment announcement for its Rotterdam (ARA) refinery — the sharpest hub-benchmark comparator to Singapore, since Neste operates both sites."),
]

CORRECTIONS = [
    dict(title="Singapore SAF Levy date",
         detail="CAAS reportedly deferred the levy in March 2026: ticket sales still start Oct 2026, but actual "
                "flight-departure applicability was pushed to Jan 2027, not Oct 2026 as workingdraft.md states. "
                "Verify against caas.gov.sg before the next draft pass."),
    dict(title="World Energy / Air Products",
         detail="Air Products exited the $2B Paramount, CA expansion partnership in Feb 2025. Existing 250M gal/yr "
                "operations are unaffected, but this live project-risk fact is missing from the US section."),
    dict(title="Montana Renewables DOE loan structure",
         detail="Actual structure is $782M first tranche + $150M Calumet equity under Title 17 Section 1706, "
                "$1.67B total including capitalized interest — more precise than the draft's flat '$1.44 billion'."),
    dict(title="China UCO export figures need reconciling",
         detail="The draft cites a 55% YoY drop in China-to-US UCO (Jan-Nov 2024 vs 2025). Separately, China's "
                "global UCO exports were up 36.8% YoY in Jan-May 2026 (1.37Mt). Not necessarily contradictory "
                "(US-bound down, global/Europe-bound up), but currently presented as two disconnected stats."),
    dict(title="HS codes can't isolate SAF",
         detail="No customs code isolates SAF itself — it clears customs blended under jet-fuel codes or isn't "
                "separately declared. Any trade-data-based claims in the study should be scoped to feedstock "
                "flows, not finished SAF volumes."),
    dict(title="Acelen jobs figures are two different metrics",
         detail="Trade press cites ~3,600 peak construction jobs; FGV's 85,000 figure is a full-value-chain, "
                "ten-year estimate. These shouldn't be presented as interchangeable."),
    dict(title="Petrobras / Ecopetrol have no SAF-specific IR disclosures",
         detail="Neither company has formalized SAF reporting in investor-facing disclosures yet. The study "
                "should lean on ANP/Aerocivil regulatory filings and trade press for these two, and say so "
                "explicitly rather than imply IR-level confirmation."),

    # --- Added 2026-08-04: findings from live extraction against the top-10 free sources ---
    dict(title="China UCO export-decline magnitude still disputed between sources",
         detail="The draft's ~55% YoY decline (1.2Mt to 540,000t, Jan-Nov 2024 vs 2025) is directionally "
                "confirmed but a July 2026 Fastmarkets figure instead shows 1,124,000t to 368,000t, a 67% "
                "decline, over an unstated comparison window. USITC DataWeb (the authoritative free source) "
                "is a session-gated interactive query tool with no scrapable URL API, so neither figure could "
                "be independently verified against Census/USITC data directly. Re-pull DataWeb HTS 1518.00.4000 "
                "by-country data directly for a precise figure before citing an exact percentage."),
    dict(title="45Z North American feedstock restriction is a proposed rule, not yet final",
         detail="Treasury/IRS proposed regulations (Federal Register docket 2026-02246, issued Feb 3, 2026) "
                "specify the US/Canada/Mexico feedstock-origin restriction, but the 2026 Unified Regulatory "
                "Agenda targets the final rule for November 2026. The restriction is operative in guidance and "
                "industry practice, but the study should describe it as proposed/pending finalization, not law."),
    dict(title="EIA and EPA do not report SAF as a standalone line item",
         detail="EIA's capacity tables group SAF into 'renewable heating oil, renewable jet fuel, renewable "
                "naphtha, renewable gasoline and other biofuels/biointermediates' with no SAF-only breakout. "
                "EPA's RIN generation CSV commingles SAF RINs into the D4 (biomass-based diesel) and D5 "
                "(advanced biofuel) categories alongside conventional biodiesel/renewable diesel. Any capacity "
                "or RIN-volume figure sourced from EIA/EPA should be labeled as a biofuels-inclusive proxy, "
                "not an isolated SAF number."),
    dict(title="Three of the ten prioritized free sources are not directly scrapable",
         detail="ANP's RenovaBio CBIO panel (Power BI embed), CARB's LCFS dashboard (Tableau, returns HTTP 403 "
                "to both direct fetch and proxy), and USITC DataWeb (login/session-gated query tool) could not "
                "be extracted directly during the 2026-08-04 pull. Data for these was substituted from CARB's "
                "own quarterly PDF summary (also 403-blocked directly, retrievable only via a reader proxy) and "
                "from trade press/analyst notes citing the underlying ANP and USITC data. Flag any figure from "
                "these three sources as secondary until a browser-automation-capable fetch can hit them directly."),
    dict(title="ICAO's own site (SAF facilities tracker, CORSIA Docs 05/06) blocks automated fetches",
         detail="icao.int returns a Cloudflare bot-challenge (HTTP 403) to both direct WebFetch and curl with "
                "browser headers. The 2026-08-04 pull retrieved CORSIA Doc 05/06 content via a reader-proxy "
                "fetch of the same ICAO URLs (so content is primary-document text), but the facilities tracker "
                "itself (a JS map/dashboard) could not be retrieved even via proxy — its 108-facility count was "
                "sourced instead from ICAO's own 'Short-Term Projections' PDF, a different but related document."),

    # --- Added 2026-08-04, round 2: DOE/USDA/ICCT/SEC/Colombia/Chile/Mexico extraction ---
    dict(title="Mexico enacted a national Biofuels Law in March 2025 — the draft's framing is outdated",
         detail="workingdraft.md frames a Mexican biofuels law as ~50% likely (a 2024 assessment). A "
                "'Ley de Biocombustibles' was actually published in the Diario Oficial de la Federación on "
                "March 18, 2025, with implementing regulations published October 2025 (permit holders must "
                "file notice of operations by Oct 6, 2026). This is NOT SAF-specific — it covers ethanol/"
                "biodiesel distribution and import/export permitting broadly, with no SAF mandate or blending "
                "percentage — but the Mexico section's 'no binding law as of mid-2026' framing needs updating "
                "to reflect that a law now exists, just not a SAF-specific one."),
    dict(title="DOE's SAF Grand Challenge Tracking Metrics Dashboard has not been updated since early 2025",
         detail="The most recent dashboard/progress report found is dated September 2024 (fact sheet) and "
                "January 2025 (progress report). No 2025 or 2026 edition could be located despite targeted "
                "searching — the tracking-metrics program appears to have gone stale under the current "
                "administration. Any DOE Grand Challenge figure in the study should be dated accordingly "
                "(~18-20 months old as of Aug 2026), not presented as current."),
    dict(title="No USDA 'United States: Biofuels Annual' GAIN report exists",
         detail="USDA FAS GAIN Biofuels Annual reports are written by attachés about foreign countries for "
                "US exporters' benefit — there is no domestic-US edition. US biofuel figures should be sourced "
                "from EIA/USDA-ERS instead; don't cite a nonexistent 'US Biofuels Annual GAIN report.'"),
    dict(title="Chile's CNE Anuario Estadístico does not track SAF/e-fuels volumes",
         detail="Checked the current (2024) edition and prior editions (2020-2023) via press coverage — the "
                "Anuario's scope is electricity, hydrocarbons and environmental permitting, with green "
                "hydrogen/electromobility added narratively since ~2022, but no dedicated biofuels/e-fuels/SAF "
                "production series. The 2024 edition's actual PDF is also behind an unauthenticated CNE "
                "SharePoint link (HTTP 401) — a genuine access barrier. Haru Oni/HIF output data should come "
                "from HIF Global and independent trackers instead, not CNE."),
    dict(title="Haru Oni has missed its own published scale-up targets",
         detail="HIF Global's originally announced targets were ~55 million liters/yr by 2025 and 550+ "
                "million liters/yr by a subsequent phase. Independent tracking (mid-2025) instead shows "
                "output essentially flat at pilot scale (~130,000 L/yr e-gasoline, ~750,000 L/yr e-methanol) "
                "since the 2022 opening — both scale-up targets have been missed. HIF's own public materials "
                "don't disclose current throughput; treat any Haru Oni volume figure as a third-party estimate."),
    dict(title="Boeing's SAF Dashboard and Insper's HEFA-vs-ATJ comparison could not be data-extracted",
         detail="Boeing's dashboard (BloombergNEF-sourced, quarterly-updated) is a JS-rendered interactive "
                "tool with no static/scrapable data — only background facts (launch date, data source, update "
                "cadence) could be confirmed. Separately, Insper's Agro in Data SAF article was fetched "
                "directly but contains no quantitative HEFA-vs-ATJ cost/production comparison for Brazil "
                "despite the series' stated framing — either that comparison lives in a different, "
                "unsurfaced article, or the framing in Datasources.md overstates what this source provides."),
    dict(title="SEC EDGAR and theicct.org block WebFetch's default request path",
         detail="Both domains returned HTTP 403 to a plain WebFetch call during the round-2 pull; content was "
                "still retrieved successfully via curl with a browser user-agent. Note this if a future pull "
                "reports these sources as inaccessible — the workaround exists, it just isn't WebFetch's "
                "default behavior."),
]

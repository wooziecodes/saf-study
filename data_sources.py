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

# cost values are normalized to: Free, Freemium, Paid, Restricted, Unknown
SOURCES = [
    # --- Government & Regulatory : United States ---
    dict(category="Government & Regulatory", region="United States", name="EIA Petroleum & Other Liquids Data",
         url="https://www.eia.gov/petroleum/data.php", cost="Free", frequency="Monthly",
         description="Production/capacity/feedstock-consumed/imports-exports for biodiesel, renewable diesel, SAF."),
    dict(category="Government & Regulatory", region="United States", name="EPA RIN Generation Data / EMTS",
         url="https://www.epa.gov/fuels-registration-reporting-and-compliance-help", cost="Free", frequency="Monthly",
         description="RIN generation/retirement by D-code, incl. SAF-eligible categories. Best free proxy for actual RFS-compliant volumes."),
    dict(category="Government & Regulatory", region="United States", name="USDA ERS Oil Crops Outlook",
         url="https://www.ers.usda.gov/", cost="Free", frequency="Monthly",
         description="Feedstock supply/demand narrative and data for oilseeds feeding biofuel production."),
    dict(category="Government & Regulatory", region="United States", name="USDA FAS GAIN Reports",
         url="https://fas.usda.gov/data/gain-report", cost="Free", frequency="Annual (rolling updates)",
         description="Biofuels Annual and Oilseeds Annual/Update country reports (Canada, Argentina, Malaysia, etc.)."),
    dict(category="Government & Regulatory", region="United States", name="DOE Alternative Fuels Data Center",
         url="https://afdc.energy.gov/fuels/sustainable-aviation-fuel", cost="Free", frequency="Ongoing",
         description="Production/capacity maps and SAF program tracker."),
    dict(category="Government & Regulatory", region="United States", name="SAF Grand Challenge Tracking Metrics Dashboard",
         url="https://www.energy.gov/", cost="Free", frequency="Annual",
         description="Interagency (DOE/FAA/USDA) dashboard: production, lifecycle CO2e reduction, planned capacity."),
    dict(category="Government & Regulatory", region="United States", name="CARB LCFS Data Dashboard",
         url="https://ww2.arb.ca.gov/applications/lcfs-data-dashboard", cost="Free", frequency="Monthly",
         description="Credit/deficit generation by pathway and credit prices — best proxy for real transacted SAF/renewable-diesel volumes and pricing."),
    dict(category="Government & Regulatory", region="United States", name="Washington Dept. of Ecology Clean Fuel Standard Data",
         url="https://ecology.wa.gov/", cost="Free", frequency="Quarterly",
         description="Credit/deficit volumes and prices for Washington's clean fuel program."),

    # --- Government & Regulatory : Brazil ---
    dict(category="Government & Regulatory", region="Brazil", name="ANP RenovaBio CBIO Dynamic Panel",
         url="https://www.gov.br/anp/", cost="Free", frequency="Fortnightly",
         description="CBIO issuance/registration/retirement plus B3 exchange price data. Central Brazil source for this study."),
    dict(category="Government & Regulatory", region="Brazil", name="EPE Balanço Energético Nacional (Open Data)",
         url="https://www.epe.gov.br/pt/publicacoes-dados-abertos", cost="Free", frequency="Annual",
         description="National energy balance including biodiesel/ethanol consumption since 1970."),
    dict(category="Government & Regulatory", region="Brazil", name="ANP General Statistics Portal",
         url="https://www.gov.br/anp/", cost="Free", frequency="Ongoing",
         description="Biodiesel blend-mandate compliance and refining data."),
    dict(category="Government & Regulatory", region="Brazil", name="CONAB",
         url="https://www.conab.gov.br/", cost="Free", frequency="Periodic",
         description="Soybean/sugarcane crop data underlying feedstock-availability estimates (re-verify before citing)."),
    dict(category="Government & Regulatory", region="Brazil", name="Comex Stat / MDIC",
         url="https://comexstat.mdic.gov.br/", cost="Free", frequency="Monthly",
         description="Official Brazilian customs data (SISCOMEX) at HS-code level."),
    dict(category="Government & Regulatory", region="Brazil", name="ABIOVE Statistics",
         url="https://abiove.org.br/en/statistics/", cost="Free", frequency="Monthly",
         description="Brazilian vegetable-oil industry association's soybean-complex export reports, aggregated from Comex Stat."),

    # --- Government & Regulatory : Canada ---
    dict(category="Government & Regulatory", region="Canada", name="ECCC Clean Fuel Regulations Credit Market Reports",
         url="https://www.canada.ca/en/environment-climate-change.html", cost="Free", frequency="Quarterly",
         description="Credit generation by category (CC1/CC2/CC3), prices, trading activity. Confirms SAF's negligible CFR credit share."),
    dict(category="Government & Regulatory", region="Canada", name="NRCan Clean Fuels Fund",
         url="https://natural-resources.canada.ca/energy-sources/clean-fuels", cost="Free", frequency="Ongoing",
         description="Funds projects (Imperial Oil, Tidewater Renewables) but has no single consolidated public project table — fragmented."),
    dict(category="Government & Regulatory", region="Canada", name="BC-LCFS Registry",
         url="https://www2.gov.bc.ca/", cost="Unknown", frequency="Unknown",
         description="BC low-carbon fuel compliance data — dedicated public dashboard not confirmed; needs direct follow-up."),
    dict(category="Government & Regulatory", region="Canada", name="Statistics Canada",
         url="https://www.statcan.gc.ca/", cost="Free", frequency="Ongoing",
         description="General trade/energy tables, not SAF-specific."),

    # --- Government & Regulatory : Colombia / Chile / Mexico ---
    dict(category="Government & Regulatory", region="Colombia", name="Fedebiocombustibles",
         url="https://www.fedebiocombustibles.com/", cost="Free", frequency="Periodic",
         description="Colombian biodiesel/ethanol sales volumes; industry-association data treated as sector record."),
    dict(category="Government & Regulatory", region="Colombia", name="Aerocivil SAF Roadmap (Resolution 00090)",
         url="https://www.aerocivil.gov.co/", cost="Free", frequency="Static",
         description="Colombia's national SAF targets document (100M gal by 2035, 450M gal by 2050)."),
    dict(category="Government & Regulatory", region="Chile", name="Chile CNE Anuario Estadístico",
         url="https://www.energia.gob.cl/", cost="Free", frequency="Annual",
         description="Annual national energy sector statistical yearbook."),
    dict(category="Government & Regulatory", region="Mexico", name="Mexico SIE (SENER)",
         url="https://sie.energia.gob.mx/", cost="Freemium", frequency="Ongoing",
         description="Official national energy statistics portal; public and institutional tiers."),
    dict(category="Government & Regulatory", region="Mexico", name="PEMEX Base de Datos Institucional",
         url="https://ebdi.pemex.com/", cost="Free", frequency="Ongoing",
         description="Pemex operating statistics; not SAF-specific given no domestic mandate exists yet."),

    # --- Government & Regulatory : Singapore ---
    dict(category="Government & Regulatory", region="Singapore", name="CAAS Newsroom / Policy Documents",
         url="https://www.caas.gov.sg/", cost="Free", frequency="Ad hoc",
         description="SAF Levy mechanics, rate bands, SAFCo mandate. Check for the March 2026 levy-timing deferral before citing dates."),
    dict(category="Government & Regulatory", region="Singapore", name="Enterprise Singapore StatLink",
         url="https://statlink.enterprisesg.gov.sg/", cost="Freemium", frequency="Monthly",
         description="Official Singapore bilateral trade by HS/SITC; free basic tier, paid for detailed bilateral extracts."),
    dict(category="Government & Regulatory", region="Singapore", name="data.gov.sg / SingStat Table Builder",
         url="https://data.gov.sg/", cost="Free", frequency="Monthly",
         description="Open Singapore government datasets and API."),
    dict(category="Government & Regulatory", region="Singapore", name="MPA Bunkering Statistics",
         url="https://www.mpa.gov.sg/", cost="Free", frequency="Monthly",
         description="Marine biofuel bunkering volumes — adjacent trading-house infrastructure, not SAF-specific."),

    # --- Government & Regulatory : International ---
    dict(category="Government & Regulatory", region="International", name="ICAO SAF Production Facilities Tracker",
         url="https://www.icao.int/SAF/SAF-production-facilities", cost="Free", frequency="Ongoing",
         description="Official list of existing and announced SAF production facilities."),
    dict(category="Government & Regulatory", region="International", name="ICAO CORSIA Eligible Fuels Registry (Docs 05/06)",
         url="https://www.icao.int/CORSIA", cost="Free", frequency="Periodic",
         description="Approved feedstocks and default lifecycle emissions values — a rules registry, not a volumes database."),
    dict(category="Government & Regulatory", region="International", name="IATA SAF Facilities Map & Fact Sheet",
         url="https://www.iata.org/en/programs/sustainability/sustainable-aviation-fuel-saf/", cost="Free", frequency="Semi-annual",
         description="Location/technology/capacity/status by facility; source of the industry's 2.4Mt / 0.8%-of-jet-fuel 2026 figures."),
    dict(category="Government & Regulatory", region="International", name="IATA / CADO SAF Registry",
         url="https://www.iata.org/", cost="Restricted", frequency="Ongoing",
         description="SAF transaction registry — likely restricted to CORSIA-participant airlines/states."),
    dict(category="Government & Regulatory", region="International", name="IEA Bioenergy Task 39",
         url="https://www.ieabioenergy.com/", cost="Free", frequency="Periodic",
         description="Global SAF commercialization progress reports (PDF), not a live database."),
    dict(category="Government & Regulatory", region="International", name="UN Comtrade",
         url="https://comtrade.un.org/", cost="Freemium", frequency="Monthly/Annual",
         description="Baseline cross-country trade data, ~200 reporters, HS 6-digit granularity."),

    # --- Trade & Feedstock Flow ---
    dict(category="Trade & Feedstock Flow", region="Global", name="ITC Trade Map",
         url="https://www.trademap.org/", cost="Freemium", frequency="Monthly",
         description="220 countries/territories, HS 2/4/6-digit since 2001; adds market-share/unit-value analytics beyond Comtrade."),
    dict(category="Trade & Feedstock Flow", region="Global", name="WITS (World Bank)",
         url="https://wits.worldbank.org/", cost="Free", frequency="Periodic",
         description="Layers UNCTAD TRAINS tariff data onto Comtrade — useful for tariff-driven diversion analysis (e.g. the 125% US tariff on Chinese UCO)."),
    dict(category="Trade & Feedstock Flow", region="Global", name="Trade Data Monitor / S&P Global GTA",
         url="https://www.spglobal.com/", cost="Paid", frequency="Monthly",
         description="Most granular bilateral HS-level data; industry-standard commodity trade desk tool."),
    dict(category="Trade & Feedstock Flow", region="United States", name="USITC DataWeb",
         url="https://dataweb.usitc.gov/", cost="Free", frequency="Monthly",
         description="US Census-sourced import/export data, 1989–present, HTS 10-digit. Best free source for US-side UCO/tallow imports by origin."),
    dict(category="Trade & Feedstock Flow", region="United States", name="US Census Bureau Trade Data",
         url="https://www.census.gov/foreign-trade/", cost="Free", frequency="Monthly",
         description="Underlies USITC DataWeb."),
    dict(category="Trade & Feedstock Flow", region="China", name="GACC (China Customs)",
         url="http://english.customs.gov.cn/", cost="Restricted", frequency="Monthly",
         description="Underlying Chinese export data source; not easily queryable without Chinese-language access."),
    dict(category="Trade & Feedstock Flow", region="China", name="Fastmarkets China UCO Reports",
         url="https://www.fastmarkets.com/insights/", cost="Paid", frequency="Monthly",
         description="Monthly China UCO/biodiesel export volume reports (confirmed live 2026 data); insight articles often free."),
    dict(category="Trade & Feedstock Flow", region="Argentina", name="INDEC",
         url="https://www.indec.gob.ar/", cost="Free", frequency="Monthly",
         description="Official Argentine trade statistics by HS code — needed to track the Argentina soy-oil-to-Canada corridor feeding Braya."),
    dict(category="Trade & Feedstock Flow", region="Global", name="Argus Media Feedstock Pricing",
         url="https://www.argusmedia.com/", cost="Paid", frequency="Daily",
         description="Separate US UCO, Asian UCO, European UCOME price assessments used for supply-contract settlement."),
    dict(category="Trade & Feedstock Flow", region="Global", name="S&P Global Platts Feedstock Pricing",
         url="https://www.spglobal.com/commodity-insights/", cost="Paid", frequency="Daily",
         description="Parallel UCO/feedstock pricing service to Argus."),

    # --- Market Intelligence & Industry ---
    dict(category="Market Intelligence & Industry", region="Global", name="S&P Global Platts SAF Price Assessment",
         url="https://www.spglobal.com/commodity-insights/", cost="Paid", frequency="Daily",
         description="Daily SAF (HEFA-SPK) CIF NW Europe price, priced as a premium to the Jet CIF NWE forward curve."),
    dict(category="Market Intelligence & Industry", region="Global", name="Argus Media SAF Benchmarks",
         url="https://www.argusmedia.com/", cost="Paid", frequency="Daily",
         description="Global, Americas and European SAF benchmarks plus new e-SAF indexes — fills the gap left by Platts' Europe-only coverage."),
    dict(category="Market Intelligence & Industry", region="Global", name="BloombergNEF",
         url="https://about.bnef.com/", cost="Paid", frequency="Periodic",
         description="SAF price-outlook research; no standalone public facility database confirmed."),
    dict(category="Market Intelligence & Industry", region="Global", name="Rystad Energy BioEnergy Solution",
         url="https://www.rystadenergy.com/", cost="Paid", frequency="Periodic",
         description="Americas biofuel project/output forecasts, e.g. US biofuel output growth to 2035."),
    dict(category="Market Intelligence & Industry", region="Global", name="Wood Mackenzie / Stratas Advisors",
         url="https://www.woodmac.com/", cost="Paid", frequency="Periodic",
         description="General energy research firms; dedicated SAF product not confirmed — verify directly before citing."),
    dict(category="Market Intelligence & Industry", region="Global", name="IATA Jet Fuel Price Monitor",
         url="https://www.iata.org/en/publications/economics/fuel-monitor/", cost="Free", frequency="Weekly",
         description="Jet fuel price monitor, joint with Platts."),
    dict(category="Market Intelligence & Industry", region="Global", name="ICCT SAF Series",
         url="https://theicct.org/series/saf/", cost="Free", frequency="Periodic",
         description="SAF cost/policy reports; source of the draft's 2-5x HEFA cost-multiple citation."),
    dict(category="Market Intelligence & Industry", region="Brazil", name="RBQAV",
         url="https://rbqav.com.br/", cost="Free", frequency="Ad hoc",
         description="Brazilian Network for Bio-kerosene and Sustainable Hydrocarbons for Aviation — direct primary source for the Brazil deep dive."),
    dict(category="Market Intelligence & Industry", region="Global", name="IJGlobal",
         url="https://www.ijglobal.com/data", cost="Paid", frequency="Ongoing",
         description="Project-finance database (45,000+ assets); already has the Acelen $1.5B Bahia financing indexed."),
    dict(category="Market Intelligence & Industry", region="Global", name="SAF Investor",
         url="https://www.safinvestor.com/existing-and-planned-saf-projects/", cost="Freemium", frequency="Ongoing",
         description="Dedicated project/producer tracker; 100+ tracked projects, reports 37 US projects under development."),
    dict(category="Market Intelligence & Industry", region="Global", name="SustainableAF",
         url="https://www.sustainableaf.info/", cost="Free", frequency="Ongoing",
         description="Continuously updated global SAF production/company/offtake database sourced from public announcements."),
    dict(category="Market Intelligence & Industry", region="Global", name="Boeing SAF Dashboard",
         url="https://www.boeing.com/", cost="Free", frequency="Periodic",
         description="Aggregates supplier SAF capacity announcements by pathway and location."),
    dict(category="Market Intelligence & Industry", region="Global", name="ADI Analytics SAF Tracker",
         url="https://adi-analytics.com/saf-tracker/", cost="Paid", frequency="Biweekly",
         description="Newsletter tracking airline commitments, plant announcements, supply deals and policy."),
    dict(category="Market Intelligence & Industry", region="Global", name="Sustainable Aviation Futures",
         url="https://www.sustainableaviationfutures.com/", cost="Free", frequency="Monthly",
         description="Monthly SAF Spotlight newsletter and SAF Market Movers Guide."),
    dict(category="Market Intelligence & Industry", region="Global", name="RMI SAF Outlook",
         url="https://saf.rmi.org/", cost="Free", frequency="Unknown",
         description="RMI's SAF outlook tool — surfaced but not verified in depth; follow up if used."),

    # --- Company & Project ---
    dict(category="Company & Project", region="United States", name="Darling Ingredients / Diamond Green Diesel IR",
         url="https://ir.darlingii.com/", cost="Free", frequency="Quarterly",
         description="Quarterly DGD JV earnings and SAF offtake announcements; verifies DGD's 235M gal/yr SAF nameplate."),
    dict(category="Company & Project", region="United States", name="World Energy Press Releases",
         url="https://www.worldenergy.net/press-release", cost="Free", frequency="Ad hoc",
         description="Project updates — including Air Products' Feb 2025 exit from the $2B Paramount, CA expansion partnership."),
    dict(category="Company & Project", region="United States", name="Calumet / Montana Renewables",
         url="https://www.calumet.com/", cost="Free", frequency="Ad hoc",
         description="DOE loan drawdown detail and MaxSAF expansion timeline (phased ramp to 300M gal/yr by 2028)."),
    dict(category="Company & Project", region="Brazil", name="Acelen Renewables Coverage",
         url="https://www.acelen.com/", cost="Free", frequency="Ad hoc",
         description="No dedicated English IR page found; financing consortium and contracted-volume detail comes via trade press."),
    dict(category="Company & Project", region="Canada", name="NRCan Clean Fuels Fund Recipients (via CER)",
         url="https://www.cer-rec.gc.ca/", cost="Free", frequency="Periodic",
         description="CER market snapshots confirm Imperial Oil and Tidewater Renewables as Clean Fuels Fund recipients."),
    dict(category="Company & Project", region="Canada", name="Braya Renewable Fuels (via Fluor)",
         url="https://www.fluor.com/projects/braya-renewable-fuels", cost="Free", frequency="Ad hoc",
         description="Operational status (up to 18,000 bbl/day) and SAF expansion plans."),
    dict(category="Company & Project", region="Global", name="SEC EDGAR",
         url="https://www.sec.gov/edgar/search/", cost="Free", frequency="Quarterly/Annual",
         description="10-K/10-Q/8-K/6-K filings for Valero, Darling Ingredients, Calumet, Ecopetrol and other public players."),
    dict(category="Company & Project", region="United States", name="DOE Loan Programs Office — Montana Renewables",
         url="https://www.energy.gov/lpo", cost="Free", frequency="Ad hoc",
         description="Confirms actual loan structure: $782M first tranche + $150M Calumet equity, $1.67B incl. capitalized interest."),
    dict(category="Company & Project", region="United States", name="FAA FAST Grants Page",
         url="https://www.faa.gov/", cost="Free", frequency="Static",
         description="Confirms the FAST grant program closed at $291M across 22 projects with no further rounds."),

    # --- Academic & Research ---
    dict(category="Academic & Research", region="Brazil", name="Insper Agro in Data",
         url="https://agro.insper.edu.br/en/agro-in-data", cost="Free", frequency="Periodic",
         description="Dedicated SAF/Brazil article series comparing HEFA vs. ATJ pathway competitiveness."),
    dict(category="Academic & Research", region="Brazil", name="FGV Acelen Economic-Impact Study",
         url="https://portal.fgv.br/", cost="Free", frequency="Static",
         description="Source of the $40B/85,000-jobs full-value-chain estimate; underlying PDF not yet located — currently confirmed only via press coverage."),
    dict(category="Academic & Research", region="Colombia", name="MIT Aviation Decarbonization in Latin America Study",
         url="https://news.mit.edu/2025/toward-sustainable-decarbonization-aviation-latin-america", cost="Free", frequency="Static",
         description="Primary source behind the draft's Colombia SAF-potential claim; regional SAF cost estimates across 6 LatAm countries."),
    dict(category="Academic & Research", region="Mexico", name="Columbia SIPA Capstone Directory",
         url="https://www.sipa.columbia.edu/academics/capstone-projects", cost="Free", frequency="Static",
         description="Likely location of the Mexico UCO/SAF capstone report tied to SENER/Pemex; needs a direct by-year search."),
    dict(category="Academic & Research", region="Brazil", name="Embrapa / University of São Paulo Repositories",
         url="https://www.embrapa.br/", cost="Free", frequency="Static",
         description="Claimed macaúba/soy-residue agronomic research — unconfirmed for SAF-specific publications; verify before citing further."),
    dict(category="Academic & Research", region="United States", name="DOE Bioenergy Technologies Office / 45ZCF-GREET",
         url="https://www.energy.gov/eere/bioenergy/bioenergy-technologies-office", cost="Free", frequency="Ongoing",
         description="Lifecycle-emissions model documentation underlying 45Z eligibility determinations."),

    # --- Certification & Traceability ---
    dict(category="Certification & Traceability", region="Global", name="RSB Document Library",
         url="https://rsb.org/library/", cost="Free", frequency="Periodic",
         description="Standards and reports incl. the Sept 2024 Sustainable Feedstock Assessment for SAF."),
    dict(category="Certification & Traceability", region="Global", name="ISCC System",
         url="https://www.iscc-system.org/", cost="Free", frequency="Ongoing",
         description="Searchable certificate registry and credit-transfer mechanics; one of two ICAO-recognized SAF certification schemes."),
    dict(category="Certification & Traceability", region="Global", name="SAFc Registry",
         url="https://docs.safcregistry.org/", cost="Free", frequency="Ongoing",
         description="Book-and-claim registry (founded by RMI + EDF) behind the American Airlines/Google SAF certificate deal."),
    dict(category="Certification & Traceability", region="Brazil", name="Finboot / MARCO Track & Trace",
         url="https://www.finboot.com/acelen-use-case", cost="Free", frequency="Static",
         description="Finboot's own case study confirming the scope of the Acelen blockchain traceability partnership."),

    # --- Trade Press ---
    dict(category="Trade Press", region="Global", name="GreenAir News",
         url="https://www.greenairnews.com/", cost="Free", frequency="Ongoing",
         description="Broke the Acelen-Finboot story; regular monthly roundups."),
    dict(category="Trade Press", region="Global", name="Biofuels Digest",
         url="https://www.biofuelsdigest.com/", cost="Free", frequency="Ongoing",
         description="Annual 'Biofuels Mandates Around the World' (65 countries) and SAF regulatory-change guides."),
    dict(category="Trade Press", region="Brazil", name="epbr / Valor Econômico",
         url="https://epbr.com.br/", cost="Freemium", frequency="Ongoing",
         description="Active Brazilian SAF coverage, Portuguese-language, not deeply indexed in English search."),
    dict(category="Trade Press", region="Global", name="e-fuels.com Investor Tracker",
         url="https://www.e-fuels.com/investor.html", cost="Free", frequency="Ongoing",
         description="Supplementary e-fuels/SAF project tracker, not in the original research brief."),
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

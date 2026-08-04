"""Structured catalog of statistics extracted from workingdraft.md.

Every entry traces back to a specific figure already researched in the
Americas SAF draft. Where Datasources.md's CORRECTIONS list flagged a figure
as imprecise or needing reconciliation, confirmed=False and note= carries
the correction forward so the dashboard surfaces it rather than repeating
the draft's original number silently.
"""

from data_sources import CORRECTIONS  # reused as-is in the Flags tab

# Categorical palette, adjacent-pairlist validated (dataviz skill default
# order: blue, orange, aqua, yellow, magenta, violet) — same hue family as
# data_sources.py's CATEGORY_COLORS, applied to this file's category set.
CATEGORY_COLORS = {
    "Policy & Regulation": "#2a78d6",        # blue
    "Feedstock & Trade Flows": "#eb6834",    # orange
    "Production Capacity": "#1baf7a",        # aqua
    "Financing & Investment": "#eda100",     # yellow
    "Pricing & Economics": "#e87ba4",        # magenta
    "Market Outlook & Targets": "#4a3aa7",   # violet
}

CATEGORY_COLORS_DARK = {
    "Policy & Regulation": "#3987e5",
    "Feedstock & Trade Flows": "#d95926",
    "Production Capacity": "#199e70",
    "Financing & Investment": "#c98500",
    "Pricing & Economics": "#d55181",
    "Market Outlook & Targets": "#9085e9",
}

# Country color map for the production-capacity chart (first 5 slots of the
# same default order — validated on the adjacent-pairlist, the correct check
# for a sorted bar chart where country is a secondary/supporting encoding;
# country name is always shown directly in the bar label, so identity is
# never carried by color alone).
COUNTRY_COLORS = {
    "United States": "#2a78d6",
    "Canada": "#eb6834",
    "Brazil": "#1baf7a",
    "Chile": "#eda100",
    "Colombia": "#e87ba4",
}
COUNTRY_COLORS_DARK = {
    "United States": "#3987e5",
    "Canada": "#d95926",
    "Brazil": "#199e70",
    "Chile": "#c98500",
    "Colombia": "#d55181",
}

# cost/confirmed semantics: confirmed=True means the figure as stated in
# workingdraft.md is taken at face value (not independently re-verified in
# this pass, but not flagged either); confirmed=False means Datasources.md's
# research surfaced a specific correction or open discrepancy, carried in note=.
#
# source_url / as_of (added 2026-08-04): populated only on entries that were
# independently pulled from a live primary (or best-available secondary)
# source during the top-10-free-sources extraction pass, as opposed to the
# entries above which are lifted from workingdraft.md's prose. as_of is the
# date the underlying data itself reflects (not the fetch date, 2026-08-04,
# which is noted in each entry's note= where relevant). Entries without these
# two fields are draft-derived only — stats_app.py's "Primary-sourced only"
# filter uses source_url's presence to distinguish the two populations.
STATS = [
    # ---------------- International / Global ----------------
    dict(country="International", category="Pricing & Economics",
         metric="SAF lifecycle emissions reduction vs. fossil jet fuel",
         value_display="Roughly 60-80%, depending on feedstock/pathway",
         value_num=70.0, unit="% (midpoint of range)", year=None, confirmed=True),
    dict(country="International", category="Policy & Regulation",
         metric="ICAO CORSIA mandatory phase start",
         value_display="2027 (voluntary phase ran 2021-2026)",
         value_num=2027, unit="year", year=2027, confirmed=True),
    dict(country="International", category="Market Outlook & Targets",
         metric="IATA net-zero aviation target / SAF's expected share of reduction",
         value_display="Net-zero by 2050; SAF expected to deliver ~65% of required emissions reduction",
         value_num=65.0, unit="% of required reduction", year=2050, confirmed=True),
    dict(country="International", category="Pricing & Economics",
         metric="EASA 2024 HEFA SAF reference price",
         value_display="€2,085/tonne (vs €734/tonne fossil jet, ~3x)",
         value_num=2085, unit="EUR/tonne", year=2024, confirmed=True),
    dict(country="International", category="Pricing & Economics",
         metric="EASA 2024 fossil jet reference price",
         value_display="€734/tonne",
         value_num=734, unit="EUR/tonne", year=2024, confirmed=True),
    dict(country="International", category="Pricing & Economics",
         metric="EASA 2024 e-SAF / Power-to-Liquid reference price",
         value_display="€7,695/tonne (~10-12x fossil jet)",
         value_num=7695, unit="EUR/tonne", year=2024, confirmed=True),
    dict(country="International", category="Pricing & Economics",
         metric="IATA collective SAF price premium paid by airlines, 2025",
         value_display="$2.9 billion total ($1.4B structural price spread) for 1.9 million tonnes of SAF",
         value_num=2.9, unit="USD billion", year=2025, confirmed=True),
    dict(country="International", category="Market Outlook & Targets",
         metric="Global SAF production forecast, 2026",
         value_display="2.4 million tonnes (~0.8% of total jet fuel consumption)",
         value_num=2.4, unit="Mt", year=2026, confirmed=True,
         source_url="https://www.iata.org/en/iata-repository/pressroom/fact-sheets/fact-sheet-sustainable-aviation-fuels/",
         as_of="2026-06", note="Corroborated directly against IATA's June 2026 SAF Fact Sheet production "
               "tracker, which also gives 2024 actual (1.0Mt, ~0.3%) and 2025 estimate (1.9Mt, ~0.6%)."),
    dict(country="International", category="Market Outlook & Targets",
         metric="EU / UK e-SAF sub-mandate start dates",
         value_display="UK 2028; EU 2030",
         value_num=2030, unit="year (EU)", year=2030, confirmed=True),
    dict(country="International", category="Pricing & Economics",
         metric="Platts SAF price volatility vs. fossil jet (since Sept 2023 launch)",
         value_display="~4.7x ($444/mt stdev vs $95/mt fossil jet)",
         value_num=4.7, unit="x fossil jet volatility", year=None, confirmed=True),
    dict(country="International", category="Feedstock & Trade Flows",
         metric="Google / American Airlines book-and-claim SAF certificate purchase",
         value_display="35 million gallons, June 2026",
         value_num=35, unit="million gallons", year=2026, confirmed=True),
    dict(country="International", category="Production Capacity",
         metric="HEFA share of global SAF supply today",
         value_display=">80% of global SAF supply",
         value_num=80, unit="%", year=None, confirmed=True),

    # ---------------- United States ----------------
    dict(country="United States", category="Policy & Regulation",
         metric="OBBBA signing date",
         value_display="July 4, 2025",
         value_num=None, unit=None, year=2025, confirmed=True),
    dict(country="United States", category="Policy & Regulation",
         metric="45Z Clean Fuel Production Credit — extension",
         value_display="Extended through Dec 31, 2029 (from an original 2027 sunset)",
         value_num=2029, unit="year", year=2029, confirmed=True),
    dict(country="United States", category="Policy & Regulation",
         metric="45Z maximum SAF credit value",
         value_display="Cut from $1.75/gal to $1.00/gal (43% reduction)",
         value_num=1.00, unit="USD/gallon (new max)", year=2026,
         confirmed=True, note="Prior/baseline value under the credit was $1.75/gal."),
    dict(country="United States", category="Policy & Regulation",
         metric="45Z base statutory rate — SAF",
         value_display="~$0.35/gal, scaling up to 5x with prevailing-wage-and-apprenticeship (PWA) compliance",
         value_num=0.35, unit="USD/gallon", year=None, confirmed=True),
    dict(country="United States", category="Policy & Regulation",
         metric="45Z base statutory rate — non-aviation clean fuel",
         value_display="~$0.20/gal",
         value_num=0.20, unit="USD/gallon", year=None, confirmed=True),
    dict(country="United States", category="Policy & Regulation",
         metric="45Z feedstock eligibility restriction",
         value_display="Limited to feedstock produced/grown in the US, Canada or Mexico, from 2026",
         value_num=None, unit=None, year=2026, confirmed=True),
    dict(country="United States", category="Policy & Regulation",
         metric="45Z ILUC penalty removal — effective date",
         value_display="Applies to fuel produced after Dec 31, 2025",
         value_num=None, unit=None, year=2025, confirmed=True),
    dict(country="United States", category="Policy & Regulation",
         metric="Treasury proposed 45Z implementing regulations",
         value_display="170 pages, issued Feb 3, 2026; comment period closed April 2026",
         value_num=170, unit="pages", year=2026, confirmed=True),
    dict(country="United States", category="Financing & Investment",
         metric="FAA FAST grant program (total awarded before OBBBA rescission)",
         value_display="$291 million across 22 projects, Aug 2024; unobligated balances rescinded under OBBBA",
         value_num=291, unit="USD million", year=2024, confirmed=True),
    dict(country="United States", category="Market Outlook & Targets",
         metric="SAF Grand Challenge production target",
         value_display="3 billion gallons of domestic SAF production by 2030 (Biden-era target, harder to reach post-OBBBA)",
         value_num=3.0, unit="billion gallons", year=2030, confirmed=True,
         source_url="https://www.energy.gov/eere/bioenergy/articles/federal-agencies-publish-saf-grand-challenge-progress-report-highlighting",
         as_of="2025-01", note="2026-08-04 extraction: DOE's own tracker shows cumulative US SAF production "
               "of 93 million gallons through Sept 2024 (up from 5M in 2021, 26M in 2023) and >750,000 metric "
               "tons of cumulative lifecycle CO2e reduction (a GREET2-model estimate, not producer-reported). "
               "The Jan 2025 progress report cites 2.6-4.9 billion gal/yr of potential production based on the "
               "announced project pipeline vs. the 3B target, and >$44B in announced funding. No DOE dashboard "
               "update has been found since Jan 2025 — treat these figures as ~18-20 months stale, not current."),
    dict(country="United States", category="Feedstock & Trade Flows",
         metric="US imported UCO volume (pre-2026 baseline)",
         value_display=">3 billion lbs/year by 2023, more than half sourced from China",
         value_num=3.0, unit="billion lbs/year", year=2023, confirmed=True),
    dict(country="United States", category="Feedstock & Trade Flows",
         metric="Chinese UCO exports to the United States",
         value_display="Fell 55% YoY: 1.2 million tonnes (Jan-Nov 2024) to 540,000 tonnes (Jan-Nov 2025)",
         value_num=55, unit="% YoY decline (US-bound)", year=2025, confirmed=False,
         source_url="https://www.fastmarkets.com/insights/waste-feedstock-trade-reroutes-as-us-soybean-oil-biofuel-demand-keeps-climbing/",
         as_of="2026-07-28",
         note="Datasources.md flag: China's *global* UCO exports were up 36.8% YoY over a similar window "
              "(Jan-May 2026, 1.37Mt) — not necessarily contradictory (US-bound down, Europe/global-bound up), "
              "but the draft presents these as two disconnected stats rather than reconciling them explicitly. "
              "2026-08-04 extraction update: direction confirmed, but magnitude is disputed — Fastmarkets "
              "(Jul 28, 2026) instead reports 1,124,000t to 368,000t, a steeper 67% decline, over an unstated "
              "comparison window. USITC DataWeb (the authoritative free source) is session-gated and couldn't "
              "be queried directly to resolve which figure is correct — treat both as approximate pending a "
              "direct DataWeb/Census pull."),
    dict(country="International", category="Feedstock & Trade Flows",
         metric="HS-code limitation for SAF trade-flow analysis",
         value_display="No customs HS code isolates SAF itself — it clears customs blended under jet-fuel codes "
                        "or isn't separately declared",
         value_num=None, unit=None, year=None, confirmed=False,
         note="Datasources.md flag: any trade-data-based claim in this study (including the China UCO figure "
              "above) should be scoped to feedstock flows, not finished SAF volumes."),
    dict(country="United States", category="Production Capacity",
         metric="US SAF production capacity growth, early 2024 through 2025",
         value_display="~1,400% growth (from a very low base)",
         value_num=1400, unit="% growth", year=2025, confirmed=True),
    dict(country="United States", category="Production Capacity",
         metric="Diamond Green Diesel — total renewable diesel capacity",
         value_display="1.2 billion gal/yr across Port Arthur, TX and Norco, LA",
         value_num=1.2, unit="billion gal/yr", year=None, confirmed=True,
         source_url="https://www.sec.gov/Archives/edgar/data/0000916540/000091654026000013/dar-20260404.htm",
         as_of="2026-04-04", note="Confirmed 2026-08-04 direct from Darling Ingredients' Q1 2026 10-Q "
               "(period ended April 4, 2026)."),
    dict(country="United States", category="Production Capacity",
         metric="Diamond Green Diesel — SAF nameplate capacity",
         value_display="235 million gal/yr (up to 50% of Port Arthur's 470M gal/yr RD capacity), completed Q4 2024",
         value_num=235, unit="million gal/yr", year=2024, confirmed=True,
         source_url="https://www.sec.gov/Archives/edgar/data/0000916540/000091654026000013/dar-20260404.htm",
         as_of="2026-04-04"),
    dict(country="United States", category="Financing & Investment",
         metric="Diamond Green Diesel — 45Z production tax credits recognized (Darling's 50% share)",
         value_display="$177.7 million (Q1 2026) vs. $50.9 million (Q1 2025)",
         value_num=177.7, unit="USD million (Q1 2026)", year=2026, confirmed=True,
         source_url="https://www.sec.gov/Archives/edgar/data/0000916540/000091654026000013/dar-20260404.htm",
         as_of="2026-04-04", note="From Darling's 10-Q. Also confirms the 2025 SAF base credit was "
               "inflation-adjusted to $1.86/gallon (IRS Notice 2025-37) before OBBBA's flat $1.00/gallon cap "
               "applies to gallons produced after Dec 31, 2025 — a concrete before/after data point for the "
               "45Z cut."),
    dict(country="United States", category="Production Capacity",
         metric="Valero Renewable Diesel segment sales volumes (DGD: RD + naphtha + neat SAF, combined)",
         value_display="3,833 thousand gal/day (Q2 2026) vs. 2,732 thousand gal/day (Q2 2025); "
                        "3,432 thousand gal/day (H1 2026) vs. 2,584 thousand gal/day (H1 2025)",
         value_num=3833, unit="thousand gal/day (Q2 2026)", year=2026, confirmed=False,
         source_url="https://www.sec.gov/Archives/edgar/data/0001035002/000162828026050937/vlo-20260630.htm",
         as_of="2026-06-30", note="From Valero's Q2 2026 10-Q. Figure is combined RD+naphtha+SAF — Valero "
               "does not break out SAF-only volumes separately, so this is a proxy, not a SAF-isolated number."),
    dict(country="United States", category="Production Capacity",
         metric="World Energy (Paramount, CA) — SAF target",
         value_display="~250 million gal/yr, producing since 2016",
         value_num=250, unit="million gal/yr", year=None, confirmed=True),
    dict(country="United States", category="Financing & Investment",
         metric="World Energy (Paramount, CA) — Air Products expansion partnership",
         value_display="Air Products exited the $2B Paramount expansion partnership in Feb 2025 "
                        "(existing 250M gal/yr operations unaffected) — not mentioned in workingdraft.md",
         value_num=2.0, unit="USD billion (exited partnership)", year=2025, confirmed=False,
         note="Datasources.md flag: a live project-risk fact missing from the draft's US section."),
    dict(country="United States", category="Production Capacity",
         metric="Montana Renewables (Calumet) — SAF capacity ramp",
         value_display="~30M gal/yr today → 150M gal/yr (2026 target) → 300M gal/yr (2028 target)",
         value_num=300, unit="million gal/yr (2028 target)", year=2028, confirmed=True,
         source_url="https://biomassmagazine.com/articles/montana-renewables-will-boost-saf-capacity-to-up-to-150-mmgy-in-q2",
         as_of="2026-05", note="Corroborated 2026-08-04: the 'MaxSAF 150' turnaround/expansion (confirmed in "
               "Calumet's Q1 2026 10-Q) completed in ~48 days with production resuming Q2 2026, on schedule "
               "for the 150M gal/yr milestone. Full 300M gal/yr SAF (330M combined SAF+RD) by 2028 remains "
               "backed by the DOE loan below. Q1 2026 Montana Renewables segment output was 7,853 bpd "
               "(vs. 9,932 bpd Q1 2025, down due to the planned turnaround) per Calumet's earnings release."),
    dict(country="United States", category="Financing & Investment",
         metric="Montana Renewables DOE loan guarantee",
         value_display="Draft states $1.44 billion flat",
         value_num=1.44, unit="USD billion", year=None, confirmed=False,
         note="Datasources.md correction: actual structure is $782M first tranche + $150M Calumet "
              "equity under Title 17 Section 1706, $1.67B total including capitalized interest, closed Jan 2025."),
    dict(country="United States", category="Production Capacity",
         metric="Phillips 66 (Rodeo Renewed, CA) — SAF capacity",
         value_display="~10,000 bbl/day online Q3 2024; production temporarily halted Q4 2024",
         value_num=10000, unit="bbl/day", year=2024, confirmed=True),
    dict(country="United States", category="Production Capacity",
         metric="Neste Galena Park terminal — blending/storage capacity",
         value_display="33.5 million gallons",
         value_num=33.5, unit="million gallons", year=None, confirmed=True),
    dict(country="United States", category="Production Capacity",
         metric="US neat SAF supplied, most recent full year cited",
         value_display="~110 million gallons, of which ~70 million gallons imported",
         value_num=110, unit="million gallons", year=None, confirmed=True),

    # ---------------- Canada ----------------
    dict(country="Canada", category="Policy & Regulation",
         metric="Clean Fuel Regulations (CFR) — in force since",
         value_display="2023",
         value_num=2023, unit="year", year=2023, confirmed=True),
    dict(country="Canada", category="Policy & Regulation",
         metric="2024 CFR credit-generating fuel mix — ethanol share",
         value_display="61.3%",
         value_num=61.3, unit="%", year=2024, confirmed=True),
    dict(country="Canada", category="Policy & Regulation",
         metric="2024 CFR credit-generating fuel mix — renewable diesel share",
         value_display="27.9%",
         value_num=27.9, unit="%", year=2024, confirmed=True),
    dict(country="Canada", category="Policy & Regulation",
         metric="2024 CFR credit-generating fuel mix — SAF share",
         value_display="0.8% — evidence the CFR alone isn't yet moving material SAF volume",
         value_num=0.8, unit="%", year=2024, confirmed=True,
         source_url="https://www.rngcoalition.com/news/2025/7/21/canadas-clean-fuel-credit-market-in-2024-expansion-in-credits-with-flat-volume-growth",
         as_of="2024", note="Corroborated 2026-08-04 against a trade-association summary of ECCC's official "
               "2024 Quarterly Credit Market Report (canada.ca itself returned HTTP 403 to direct fetch)."),
    dict(country="Canada", category="Policy & Regulation",
         metric="BC-LCFS SAF blending mandate trajectory",
         value_display="1% (2028) → 2% (2029) → 3% (2030) — first jurisdiction in North America to mandate SAF blending",
         value_num=3, unit="% by 2030", year=2030, confirmed=True),
    dict(country="Canada", category="Policy & Regulation",
         metric="BC-LCFS jet fuel carbon-intensity reduction target",
         value_display="2% (2026) → 10% (2030)",
         value_num=10, unit="% by 2030", year=2030, confirmed=True),
    dict(country="Canada", category="Financing & Investment",
         metric="Vancouver International Airport low-carbon jet fuel incentive",
         value_display="CA$0.75-1.20 per litre",
         value_num=1.20, unit="CAD/litre (upper bound)", year=None, confirmed=True),
    dict(country="Canada", category="Financing & Investment",
         metric="Federal Biofuels Production Incentive",
         value_display=">CA$370 million over two years, from January 2026",
         value_num=370, unit="CAD million", year=2026, confirmed=True),
    dict(country="Canada", category="Financing & Investment",
         metric="Federal Clean Fuels Fund",
         value_display="CA$1.5 billion",
         value_num=1.5, unit="CAD billion", year=None, confirmed=True),
    dict(country="Canada", category="Policy & Regulation",
         metric="BC Canadian-content requirement — effective date",
         value_display="Jan 1, 2026 (province's 5% renewable-fuel minimum must be met with Canadian-produced material)",
         value_num=5, unit="% renewable-fuel minimum", year=2026, confirmed=True),
    dict(country="Canada", category="Feedstock & Trade Flows",
         metric="Braya Renewable Fuels — Argentina soy oil imports",
         value_display="757,000 tonnes in 2024, up sharply from 48,000 tonnes in 2023",
         value_num=757000, unit="tonnes (2024)", year=2024, confirmed=True),
    dict(country="Canada", category="Production Capacity",
         metric="Braya Renewable Fuels (Newfoundland) — capacity",
         value_display="824 million litres/yr nameplate (began Feb 2024); ~18,000 bbl/day operational per Fluor; 100% exported to the US",
         value_num=824, unit="million litres/yr", year=2024, confirmed=True),
    dict(country="Canada", category="Production Capacity",
         metric="Tidewater Renewables (Prince George, BC) — capacity",
         value_display="170 million litres/yr, commercial since November 2023",
         value_num=170, unit="million litres/yr", year=2023, confirmed=True),
    dict(country="Canada", category="Production Capacity",
         metric="Imperial Oil Strathcona renewable diesel facility",
         value_display="~1 billion litres/yr (Edmonton, Alberta), advanced stages",
         value_num=1.0, unit="billion litres/yr", year=None, confirmed=True),
    dict(country="Canada", category="Financing & Investment",
         metric="NRCan Clean Fuels Fund — Imperial Oil award",
         value_display="~$720 million",
         value_num=720, unit="CAD million", year=None, confirmed=True),
    dict(country="Canada", category="Financing & Investment",
         metric="NRCan Clean Fuels Fund — Tidewater Renewables award",
         value_display="~$342 million",
         value_num=342, unit="CAD million", year=None, confirmed=True),
    dict(country="Canada", category="Production Capacity",
         metric="Parkland Corp. co-processing feedstock limit (ASTM D1655)",
         value_display="Currently 5%; industry pushing toward 30%",
         value_num=30, unit="% (target ceiling)", year=None, confirmed=True),

    # ---------------- Brazil ----------------
    dict(country="Brazil", category="Policy & Regulation",
         metric="'Fuel of the Future' Law enactment",
         value_display="Lei No. 14.993/2024, enacted Oct 9, 2024",
         value_num=None, unit=None, year=2024, confirmed=True),
    dict(country="Brazil", category="Policy & Regulation",
         metric="ProBioQAV well-to-wake emissions-reduction target trajectory",
         value_display="1% by 2027, rising 1 percentage point/yr to 10% by 2037",
         value_num=10, unit="% by 2037", year=2037, confirmed=True),
    dict(country="Brazil", category="Policy & Regulation",
         metric="PNDV mandatory biodiesel blend trajectory",
         value_display="B14 (2025) → B15 (2026) → B20 (2030)",
         value_num=20, unit="% by 2030", year=2030, confirmed=True),
    dict(country="Brazil", category="Policy & Regulation",
         metric="Ethanol-gasoline blending ceiling",
         value_display="Raised to E30 (from E27); CNPE sets the actual annual rate within that range",
         value_num=30, unit="% ceiling", year=None, confirmed=True),
    dict(country="Brazil", category="Policy & Regulation",
         metric="RenovaBio CBIO decarbonisation target",
         value_display="48.09 Mt CO2 (2026) rising to 72.54 Mt CO2e (2034), vs a 2018 baseline",
         value_num=72.54, unit="Mt CO2e (2034 target)", year=2034, confirmed=True,
         source_url="https://www.canaonline.com.br/conteudo/anp-atribui-metas-de-cbios-de-2026-a-distribuidoras-contratos-de-longo-prazo-abatem-5-das-metas.html",
         as_of="2026", note="2026 target of 48.09M CBIOs corroborated 2026-08-04 via Brazilian trade press "
               "(ANP's own Power BI panel has no scrapable HTML data)."),
    dict(country="Brazil", category="Policy & Regulation",
         metric="ANP SAF-specific production/marketing regulations — expected",
         value_display="Second half of 2026",
         value_num=None, unit=None, year=2026, confirmed=True),
    dict(country="Brazil", category="Feedstock & Trade Flows",
         metric="Ethanol needed to meet ProBioQAV's 2037 SAF demand via Alcohol-to-Jet alone",
         value_display="~2 billion litres of ethanol for 1.2 billion litres of SAF",
         value_num=2.0, unit="billion litres ethanol", year=2037, confirmed=True),
    dict(country="Brazil", category="Financing & Investment",
         metric="Acelen Renewables (Mubadala) — Bahia biorefinery financing",
         value_display="$1.5 billion secured May 2026, part of total investment exceeding $3 billion",
         value_num=1.5, unit="USD billion (secured tranche)", year=2026, confirmed=True,
         source_url="https://www.hydrocarbonprocessing.com/news/2026/05/mubadalas-acelen-secures-15-b-to-launch-brazil-saf-biorefinery-project/",
         as_of="2026-05-21", note="Corroborated 2026-08-04 (S&P Global's own coverage of the same deal "
               "blocked direct fetch, HTTP 403). Led by HSBC and IFC, 10 institutions total."),
    dict(country="Brazil", category="Production Capacity",
         metric="Acelen Renewables — Bahia biorefinery target capacity",
         value_display="1 billion litres/yr combined SAF + renewable diesel via HEFA, from 2029",
         value_num=1.0, unit="billion litres/yr", year=2029, confirmed=True),
    dict(country="Brazil", category="Feedstock & Trade Flows",
         metric="Acelen Bahia project — land footprint",
         value_display="144,000 hectares of degraded land (20% earmarked for family-farmer partnerships)",
         value_num=144000, unit="hectares", year=None, confirmed=True),
    dict(country="Brazil", category="Market Outlook & Targets",
         metric="Acelen — contracted commercialisation volumes",
         value_display="~90% of volumes already contracted (Trafigura, Moeve, Bunge, BGN among named partners)",
         value_num=90, unit="%", year=None, confirmed=True),
    dict(country="Brazil", category="Financing & Investment",
         metric="FGV Acelen full value-chain economic-impact estimate",
         value_display="Up to $40 billion and ~85,000 direct + indirect jobs over a decade",
         value_num=40, unit="USD billion", year=None, confirmed=False,
         note="Datasources.md correction: this is a full-value-chain, ten-year estimate — distinct from the "
              "~3,600 peak construction jobs cited separately in trade press. The two figures should not be "
              "presented as interchangeable."),
    dict(country="Brazil", category="Financing & Investment",
         metric="Acelen — peak construction jobs (trade press)",
         value_display="~3,600 peak construction jobs",
         value_num=3600, unit="jobs", year=None, confirmed=True,
         note="Distinct metric from FGV's 85,000 full-value-chain estimate above — see that entry's note."),
    dict(country="Brazil", category="Feedstock & Trade Flows",
         metric="Acelen / Finboot blockchain traceability partnership",
         value_display="12-month term, signed March 2026 ('Marco Track & Trace')",
         value_num=12, unit="months", year=2026, confirmed=True),
    dict(country="Brazil", category="Production Capacity",
         metric="Petrobras — SAF-specific investor disclosure status",
         value_display="No SAF-specific IR disclosures yet, despite an expected central role as ANP's 2026 "
                        "regulations clarify the domestic market",
         value_num=None, unit=None, year=None, confirmed=False,
         note="Datasources.md flag: lean on ANP regulatory filings and trade press for Petrobras SAF claims, "
              "and say so explicitly rather than imply IR-level confirmation."),

    # ---------------- Chile ----------------
    dict(country="Chile", category="Production Capacity",
         metric="Haru Oni (HIF Global, Punta Arenas) — initial e-gasoline capacity",
         value_display="~130,000 litres/yr (initial demonstration phase)",
         value_num=130000, unit="litres/yr", year=None, confirmed=True,
         source_url="https://industrydecarbonization.com/news/whats-up-with-the-production-of-e-fuels-in-chile.html",
         as_of="2025-06",
         note="2026-08-04 extraction: confirmed still essentially flat at this pilot-scale level as of mid-2025 "
              "(independent estimate, not an HIF disclosure — HIF's own materials publish no throughput "
              "figures). Also produces ~750,000 L/yr e-methanol per the same source."),
    dict(country="Chile", category="Production Capacity",
         metric="Haru Oni — FID / first production",
         value_display="FID reached 2021; first litres of synthetic e-gasoline produced Dec 2022",
         value_num=2021, unit="year (FID)", year=2021, confirmed=True),
    dict(country="Chile", category="Production Capacity",
         metric="Haru Oni — planned scale-up targets",
         value_display="~55 million litres/yr (mid-2020s target) → 550 million litres/yr (later-phase "
                        "target) — BOTH MISSED, see note",
         value_num=550, unit="million litres/yr (later-phase target)", year=None, confirmed=False,
         source_url="https://industrydecarbonization.com/news/whats-up-with-the-production-of-e-fuels-in-chile.html",
         as_of="2025-06",
         note="2026-08-04 extraction: both targets confirmed missed — actual output remains at the ~130,000 "
              "L/yr pilot-scale level (see the initial-capacity entry above). HIF's growth capital has instead "
              "moved to a planned Cabo Negro commercial facility (175,000 t/yr e-methanol, ~$830M capex, "
              "environmental approval late 2025, no FID yet) and the Brazil plant below."),
    dict(country="Chile", category="Production Capacity",
         metric="Haru Oni — demonstration-plant equipment",
         value_display="3.4 MW wind turbine + 1.2 MW electrolyser",
         value_num=3.4, unit="MW wind turbine", year=None, confirmed=True),
    dict(country="Chile", category="Financing & Investment",
         metric="HIF Global — planned Brazil e-fuels plant",
         value_display="$4 billion, announced February 2026 — capex guidance later revised down (see note)",
         value_num=4.0, unit="USD billion", year=2026, confirmed=False,
         source_url="https://hydrogen-central.com/hif-global-eyes-significant-capex-savings-on-4-billion-brazil-hydrogen-plant/",
         as_of="2026-02",
         note="2026-08-04 extraction: HIF's Latin America CEO subsequently guided capex to 'below $1B per "
              "module' across 4 planned 220,000 t/yr e-methanol modules (800,000 t/yr total) at Port of Açu, "
              "Rio de Janeiro — a significant reduction from the original $4B headline. First-module financing "
              "close targeted mid-2027; methanol environmental license approved, e-kerosene/eSAF license "
              "still in progress. Secondary source (trade press citing a Reuters interview); Reuters original "
              "and fuelcellsworks.com mirror both blocked direct fetch."),
    dict(country="Chile", category="Pricing & Economics",
         metric="Power-to-Liquid / e-SAF cost multiple vs. fossil jet fuel",
         value_display="Up to ~12x fossil jet fuel cost (IATA)",
         value_num=12, unit="x fossil jet", year=None, confirmed=True),

    # ---------------- Colombia ----------------
    dict(country="Colombia", category="Policy & Regulation",
         metric="Colombia SAF Roadmap (Aerocivil Resolution 00090)",
         value_display="Issued January 2025",
         value_num=None, unit=None, year=2025, confirmed=True),
    dict(country="Colombia", category="Market Outlook & Targets",
         metric="Colombia SAF Roadmap — 2035 production target",
         value_display="100 million gallons (378.5 million litres) by 2035",
         value_num=100, unit="million gallons", year=2035, confirmed=True,
         source_url="https://www.aerocivil.gov.co/publicaciones/4056/desde-ahora-colombia-cuenta-con-una-hoja-de-ruta-para-la-implementacion-de-combustibles-sostenibles-de-aviacion-saf/",
         as_of="2025-01-21", note="Confirmed 2026-08-04 direct from Aerocivil (the issuing regulator); "
               "unrevised across all 2025-2026 coverage found."),
    dict(country="Colombia", category="Market Outlook & Targets",
         metric="Colombia SAF Roadmap — 2050 production target",
         value_display="450 million gallons (1.7 billion litres) by 2050",
         value_num=450, unit="million gallons", year=2050, confirmed=True,
         source_url="https://www.aerocivil.gov.co/publicaciones/4056/desde-ahora-colombia-cuenta-con-una-hoja-de-ruta-para-la-implementacion-de-combustibles-sostenibles-de-aviacion-saf/",
         as_of="2025-01-21"),
    dict(country="Colombia", category="Production Capacity",
         metric="Ecopetrol Reficar (Cartagena) — test-production batch",
         value_display="20,000-32,000 barrels, late 2024, co-processed with up to 5% palm oil/UCO",
         value_num=32000, unit="barrels (batch, upper bound)", year=2024, confirmed=True,
         source_url="https://www.ecopetrol.com.co/wps/portal/Home/es/noticias/detalle/finalizo-prueba-combustible-aviacion",
         as_of="2024-11-05", note="Direct from Ecopetrol's own press release. The company's target for "
               "sustained industrial-scale production is 2028."),
    dict(country="Colombia", category="Market Outlook & Targets",
         metric="Ecopetrol / LATAM co-processed commercial flights",
         value_display="700+ flights, April 2025, using Jet A-1 with 1% renewable feedstock blend",
         value_num=700, unit="flights", year=2025, confirmed=True),
    dict(country="Colombia", category="Production Capacity",
         metric="Ecopetrol e-SAF pilot target (Cartagena, with GIZ)",
         value_display="Up to 800 tonnes/yr, alongside an existing 800-tonne/yr green hydrogen 'Coral Project' electrolyser",
         value_num=800, unit="tonnes/yr", year=None, confirmed=True,
         source_url="https://www.ecopetrol.com.co/wps/portal/Home/es/noticias/detalle/alianza-con-giz-de-alemania-para-producir-combustibles-sostenibles-de-aviacion-a-partir-de-hidrogeno-verde",
         as_of="2026-06-19", note="Confirmed direct from Ecopetrol's own press release — still a "
               "feasibility/engineering study (24-month phase), not a production commitment; no investment "
               "figure disclosed yet."),
    dict(country="Colombia", category="Financing & Investment",
         metric="Ecopetrol planned dedicated SAF production plant",
         value_display="$500-700 million, targeting operations by 2030 (contingent on the Roadmap's regulatory framework)",
         value_num=700, unit="USD million (upper bound)", year=2030, confirmed=True),
    dict(country="Colombia", category="Production Capacity",
         metric="Ecopetrol — SAF-specific investor disclosure status",
         value_display="No SAF-specific IR disclosures yet",
         value_num=None, unit=None, year=None, confirmed=False,
         note="Datasources.md flag: lean on Aerocivil regulatory filings and trade press for Ecopetrol SAF "
              "claims, and say so explicitly rather than imply IR-level confirmation."),
    dict(country="Colombia", category="Market Outlook & Targets",
         metric="MIT study — Colombia SAF potential with a 20% palm/sugarcane output increase",
         value_display="~250 million litres/yr",
         value_num=250, unit="million litres/yr", year=None, confirmed=True),
    dict(country="Colombia", category="Pricing & Economics",
         metric="MIT study — regional SAF cost vs. conventional jet fuel (6 LatAm countries)",
         value_display="$1.11-2.86/litre vs ~$0.70/litre conventional",
         value_num=2.86, unit="USD/litre (upper bound)", year=None, confirmed=True),

    # ---------------- Mexico ----------------
    dict(country="Mexico", category="Market Outlook & Targets",
         metric="Probability of a biofuels law/mandate emerging under President Sheinbaum",
         value_display="~50% (Americas Market Intelligence, 2024 assessment) — SUPERSEDED, see note",
         value_num=50, unit="%", year=2024, confirmed=False,
         source_url="https://www.diputados.gob.mx/LeyesBiblio/pdf/LBio.pdf", as_of="2025-03-18",
         note="2026-08-04 extraction: superseded. A national 'Ley de Biocombustibles' was enacted "
              "March 18, 2025 (official DOF text), with implementing regulations published Oct 2025. Not "
              "SAF-specific — covers ethanol/biodiesel permitting broadly, no SAF mandate or blend % — but "
              "the premise of this 50% probability estimate (a law might emerge) has been overtaken by events."),
    dict(country="Mexico", category="Pricing & Economics",
         metric="SAF cost vs. conventional jet fuel in Mexico",
         value_display="2-3x conventional jet fuel cost",
         value_num=3, unit="x conventional (upper bound)", year=None, confirmed=True),

    # ---------------- Singapore ----------------
    dict(country="Singapore", category="Policy & Regulation",
         metric="CAAS Sustainable Air Hub Blueprint — launch",
         value_display="2024",
         value_num=2024, unit="year", year=2024, confirmed=True),
    dict(country="Singapore", category="Market Outlook & Targets",
         metric="Singapore national SAF uplift target trajectory",
         value_display="1% for flights departing Singapore from 2026, rising to 3-5% by 2030 (subject to global SAF availability)",
         value_num=5, unit="% by 2030 (upper bound)", year=2030, confirmed=True),
    dict(country="Singapore", category="Policy & Regulation",
         metric="Singapore SAF Levy — start date",
         value_display="Draft states flight-departure applicability from Oct 1, 2026 (tickets sold from Apr 1, 2026)",
         value_num=None, unit=None, year=2026, confirmed=False,
         note="Datasources.md correction: CAAS reportedly deferred the levy in March 2026 — ticket sales still "
              "start Oct 2026, but actual flight-departure applicability was pushed to Jan 2027. Verify against "
              "caas.gov.sg before citing."),
    dict(country="Singapore", category="Pricing & Economics",
         metric="Singapore SAF Levy — estimated per-ticket cost impact",
         value_display="S$1-3 for short-haul economy (e.g. Bangkok) to S$6.40-16 for long-haul (e.g. London)",
         value_num=16, unit="SGD (long-haul upper bound)", year=None, confirmed=True),
    dict(country="Singapore", category="Pricing & Economics",
         metric="SAF cost vs. conventional jet fuel (Singapore government estimate)",
         value_display="3-4x conventional jet fuel",
         value_num=4, unit="x conventional (upper bound)", year=None, confirmed=True),
    dict(country="Singapore", category="Policy & Regulation",
         metric="Asia-Pacific Sustainable Aviation Centre (APSAC) — launch",
         value_display="July 2025",
         value_num=None, unit=None, year=2025, confirmed=True),

    # ---------------- Primary-sourced extraction, 2026-08-04 ----------------
    # Everything below was independently pulled from the top-10 free-source list
    # (see FreeSources.md) rather than lifted from workingdraft.md's prose. All
    # entries carry source_url + as_of; confirmed=False marks entries with a
    # meaningful extraction caveat (blocked dashboard, secondary fallback,
    # disputed figure) — read the note before citing.

    # --- International / global ---
    dict(country="International", category="Production Capacity",
         metric="SAF production facilities/announcements tracked (ICAO)",
         value_display="108 facilities (existing + announced, 2024-2027 outlook): 25 rated maturity A, "
                        "19 B, 27 C, 34 D",
         value_num=108, unit="facilities", year=2025, confirmed=False,
         source_url="https://www.icao.int/sites/default/files/environmental-protection/Documents/ICAO-SAF-short-term-projections-methodology-and-results.pdf",
         as_of="2025-06-23",
         note="ICAO's own facilities-tracker dashboard (icao.int/SAF/SAF-production-facilities) returned HTTP "
              "403 (Cloudflare bot-challenge) to direct and proxy fetch alike. This figure is from ICAO's "
              "related 'Short-Term Projections on SAF Production' PDF, not the tracker itself."),
    dict(country="International", category="Market Outlook & Targets",
         metric="Projected regional share of global SAF production capacity by 2030 (ICAO)",
         value_display="North America >58% of global capacity across all scenarios; Europe 16-27%; Asia 2-4%; "
                        "South America/Oceania/Africa combined minimal",
         value_num=58, unit="% (North America, lower bound)", year=2030, confirmed=True,
         source_url="https://www.icao.int/sites/default/files/environmental-protection/Documents/ICAO-SAF-short-term-projections-methodology-and-results.pdf",
         as_of="2025-06-23",
         note="Does not break out US vs. Canada, nor isolate a discrete Latin America figure."),
    dict(country="International", category="Market Outlook & Targets",
         metric="Global SAF production, actual/estimated by year (IATA SAF Fact Sheet, June 2026 edition)",
         value_display="2024 actual: 1.0Mt (~0.3% of jet fuel); 2025 estimate: 1.9Mt (~0.6%); "
                        "2026 projection: 2.4Mt (~0.8%)",
         value_num=1.0, unit="Mt (2024 actual)", year=2024, confirmed=True,
         source_url="https://www.iata.org/en/iata-repository/pressroom/fact-sheets/fact-sheet-sustainable-aviation-fuels/",
         as_of="2026-06",
         note="Direct PDF fetch succeeded — highest-confidence source in this extraction pass. 11 SAF "
              "pathways were ASTM-certified as of 2024 per the same document's milestones list."),
    dict(country="International", category="Production Capacity",
         metric="HEFA pathway lifecycle emissions reduction (IATA, June 2026)",
         value_display="~80% (up to >90% for emerging feedstocks/technology) vs. conventional jet fuel",
         value_num=80, unit="%", year=None, confirmed=True,
         source_url="https://www.iata.org/en/iata-repository/pressroom/fact-sheets/fact-sheet-sustainable-aviation-fuels/",
         as_of="2026-06", note="Corroborates the existing 60-80% range cited from other sources."),
    dict(country="International", category="Policy & Regulation",
         metric="CORSIA Default Life Cycle Emissions Values (Doc 06, 8th Edition) — HEFA core LCA values",
         value_display="UCO 13.9 gCO2e/MJ; soybean oil 40.4 gCO2e/MJ; beef tallow 22.5-29.7 gCO2e/MJ "
                        "(two applicability tiers found, not fully disambiguated)",
         value_num=13.9, unit="gCO2e/MJ (UCO)", year=2025, confirmed=False,
         source_url="https://www.icao.int/sites/default/files/environmental-protection/CORSIA/Documents/CORSIA%20Eligible%20Fuels/ICAO-document-06-Default-Life-Cycle-Emissions-November-2025.pdf",
         as_of="2025-11-19",
         note="icao.int blocks direct fetch (HTTP 403); retrieved via proxy re-fetch of the same URL, so "
              "content is primary-document text. Beef-tallow figure needs visual table verification before "
              "citing a single number — two tiers were found in the extracted text."),
    dict(country="International", category="Policy & Regulation",
         metric="CORSIA-eligible feedstocks (Doc 05/registry)",
         value_display="47 distinct feedstocks currently listed (primary/co-product, by-product, waste and "
                        "residue categories)",
         value_num=47, unit="feedstocks", year=None, confirmed=True,
         source_url="https://www.icao.int/CORSIA/feedstocks", as_of="2026-08-04",
         note="A feedstock count, not a technology-pathway count — distinct from IATA's separately-cited "
              "'11 SAF pathways certified' figure above."),
    dict(country="International", category="Production Capacity",
         metric="SustainableAF tracked global facilities/companies/offtake agreements",
         value_display="300+ facilities; 100+ companies; 90+ airline offtake agreements",
         value_num=300, unit="facilities (rounded)", year=None, confirmed=False,
         source_url="https://www.sustainableaf.info/", as_of="2026-08-04",
         note="Homepage marketing headline figures, not a precise count. Country-level Americas breakdown "
              "(US/Brazil/Canada) is paywalled — not available on the free tier."),

    # --- United States ---
    dict(country="United States", category="Production Capacity",
         metric="Commercial SAF production facilities, named (DOE AFDC)",
         value_display="World Energy (Paramount, CA, since 2016); Neste (supplying US since 2020); "
                        "Montana Renewables/Shell (since 2023)",
         value_num=3, unit="facilities", year=2023, confirmed=True,
         source_url="https://afdc.energy.gov/fuels/sustainable-aviation-fuel", as_of="2023",
         note="Fallback source — ICAO's own tracker was inaccessible (see International entries above). "
              "No 2025/2026-dated US facility count could be located."),
    dict(country="United States", category="Production Capacity",
         metric="US SAF consumption (EPA data cited by DOE AFDC)",
         value_display="2021: ~5M gal; 2022: 15.84M gal; 2023: 24.5M gal",
         value_num=24.5, unit="million gallons (2023)", year=2023, confirmed=True,
         source_url="https://afdc.energy.gov/fuels/sustainable-aviation-fuel", as_of="2023"),
    dict(country="United States", category="Production Capacity",
         metric="Renewable diesel & other biofuels (incl. SAF) operable production capacity (EIA)",
         value_display="4,969 million gal/yr — combined category, not SAF-isolated",
         value_num=4969, unit="million gal/yr", year=2026, confirmed=False,
         source_url="https://www.eia.gov/dnav/pet/pet_pnp_capbio_dcu_nus_m.htm", as_of="2026-05",
         note="EIA's dedicated 'Monthly Biofuels Capacity and Feedstocks Update' report was discontinued "
              "(last standalone edition Sept 2025); this is from EIA's dnav data-browser tables instead. "
              "EIA does not break SAF out from renewable heating oil/naphtha/gasoline in this category — "
              "treat as a biofuels-inclusive proxy, not a SAF-specific figure."),
    dict(country="United States", category="Feedstock & Trade Flows",
         metric="US biofuel feedstock consumed, by type (EIA)",
         value_display="Soybean oil 1,434M lbs; tallow/animal fat 796M lbs; yellow grease (UCO proxy) 605M "
                        "lbs; corn oil 457M lbs; canola oil 293M lbs",
         value_num=1434, unit="million lbs (soybean oil, largest feedstock)", year=2026, confirmed=True,
         source_url="https://www.eia.gov/dnav/pet/pet_pnp_feedbiofuel_dcu_nus_m.htm", as_of="2026-05",
         note="EIA reports on a ~2-month lag; some sub-category splits (e.g. distillers corn oil) are "
              "withheld ('W') for confidentiality."),
    dict(country="United States", category="Production Capacity",
         metric="EPA RIN generation by D-code, H1 2026 (EMTS)",
         value_display="D4 (biomass-based diesel, primary SAF-eligible code) 3,858.5M RINs; D6 (conventional, "
                        "mostly corn ethanol) 7,361.4M; D3 (cellulosic) 592.6M; D5 (advanced) 126.4M; "
                        "D7 (cellulosic diesel) 9,226",
         value_num=3858.5, unit="million RINs (D4, Jan-Jun 2026)", year=2026, confirmed=False,
         source_url="https://www.epa.gov/system/files/other-files/2026-07/generationbreakout_jun2026.csv",
         as_of="2026-01/2026-06",
         note="Directly fetched live CSV, total corroborated independently by Biomass Magazine's H1-2026 "
              "report. EPA does not isolate SAF RINs — they're commingled into D4 (mainly) and D5 alongside "
              "conventional biodiesel/renewable diesel, so this is a proxy, not a SAF-specific volume."),
    dict(country="United States", category="Policy & Regulation",
         metric="CARB LCFS credit/deficit generation and net bank",
         value_display="Q4 2025: 8.20M MT CO2e credits generated, 9.64M MT CO2e deficits generated; "
                        "cumulative net bank 40.11M MT CO2e since 2011",
         value_num=8.20, unit="million MT CO2e (Q4 2025 credits)", year=2025, confirmed=False,
         source_url="https://ww2.arb.ca.gov/sites/default/files/classic/fuels/lcfs/dashboard/quarterlysummary/Q4%202025%20Data%20Summary.pdf",
         as_of="2025-Q4",
         note="CARB's interactive Tableau dashboard is entirely unscrapable (HTTP 403 direct and via proxy); "
              "this is from CARB's own quarterly PDF, also 403-blocked directly and retrieved only via a "
              "reader-proxy fetch of the same official URL. The PDF has no SAF-specific line item and no "
              "machine-readable renewable-diesel breakout — only a % rolling-average chart."),
    dict(country="United States", category="Pricing & Economics",
         metric="CARB LCFS credit price",
         value_display="~$63/MT quarterly average (Q1 2026); spot as high as $66.50/MT, Dec-2026 ICE futures "
                        "as high as $72/MT (Feb 2026); regulatory price ceiling $268.90/MT (Jun 2025-May 2026)",
         value_num=63, unit="USD/metric ton", year=2026, confirmed=False,
         source_url="https://www.argusmedia.com/en/news-and-insights/latest-market-news/2783116-california-lcfs-credit-shrink-lifts-prices-update",
         as_of="2026-Q1",
         note="Secondary source only (Argus Media, paywalled — read via search snippet, not directly "
              "fetched). CARB's own dashboard/PDF publishes no scrapable price series, so this could not be "
              "confirmed against a primary CARB feed."),
    dict(country="United States", category="Feedstock & Trade Flows",
         metric="US feedstock import shifts by origin, YoY (trade press, post-45Z)",
         value_display="Total US UCO imports -38% YoY; from China 1,124,000t to 368,000t (-67%); tallow "
                        "from Brazil 350,000t to 269,000t (-23%); tallow from Australia +24%; UCO from "
                        "Malaysia +38%; UCO from Vietnam +186%",
         value_num=-67, unit="% YoY (China UCO, steepest move)", year=2026, confirmed=False,
         source_url="https://www.fastmarkets.com/insights/waste-feedstock-trade-reroutes-as-us-soybean-oil-biofuel-demand-keeps-climbing/",
         as_of="2026-07-28",
         note="USITC DataWeb (the authoritative free source) is a session-gated interactive tool with no "
              "scrapable URL API — could not be queried directly, so this trade-press figure is a fallback. "
              "Comparison window is unstated (unclear if trailing-12-month or calendar-year). Illustrates "
              "diversification away from China toward Malaysia/Vietnam, consistent with the 45Z North "
              "American-content rule."),

    # --- Brazil ---
    dict(country="Brazil", category="Policy & Regulation",
         metric="CBIO issuance/retirement, Jan-Mar 2026 (Itaú BBA RenovaBio monitoring note)",
         value_display="7.2M CBIOs issued, 3.7M retired; stock opened at 19.5M, closed at 22.5M",
         value_num=7.2, unit="million CBIOs issued", year=2026, confirmed=False,
         source_url="https://minutomt.com.br/agro/renovabio-inicia-2026-com-metas-menores-e-precos-de-cbios-em-queda-aponta-relatorio-do-itau-bba/",
         as_of="2026-01/2026-03",
         note="ANP's own CBIO panel is a Power BI embed with no scrapable data. This figure is corroborated "
              "across multiple search snippets citing the same Itaú BBA report, but the primary article "
              "itself returned HTTP 403 and could not be opened directly to verify verbatim."),
    dict(country="Brazil", category="Pricing & Economics",
         metric="CBIO price trend, late 2025 to mid-2026",
         value_display="~R$35 (Nov 2025) → ~R$32 (Feb 2026) → ~R$29 (Apr 2026); Jan-Feb 2026 average "
                        "R$31.40, down 43% vs. the 2025 average of R$54.70 — market described as in "
                        "'structural excess supply,' lowest since 2020",
         value_num=29, unit="BRL/CBIO (Apr 2026)", year=2026, confirmed=True,
         source_url="https://revistarpanews.com.br/cbios-atingem-nova-minima-historica-e-mercado-passa-a-ser-guiado-por-fundamentos-aponta-analise/",
         as_of="2026-04",
         note="Directly fetched and date-verified — the most current, directly-confirmed CBIO price data "
              "point found in this pass. B3's own live CBIO trading page is JS-rendered and returned no "
              "data to direct fetch."),

    # --- Canada ---
    dict(country="Canada", category="Policy & Regulation",
         metric="CFR credit generation, Q1 2025",
         value_display="1,763,358 CC2/CC3 credits; mix ~65% ethanol, ~19.6% renewable diesel, ~3.4% "
                        "biodiesel, ~2% RNG/biogas, ~0.55% SAF (10,261 credits); down 27% from the Q2 2024 "
                        "peak",
         value_num=10261, unit="SAF credits (Q1 2025)", year=2025, confirmed=False,
         source_url="https://www.clearbluemarkets.com/knowledge-base/canada-cfr-q1-2025-compliance-credit-market-report-review",
         as_of="2025-Q1",
         note="canada.ca returned HTTP 403 to every fetch attempt on ECCC's own compliance-report pages; "
              "this is a secondary analyst note (Clear Blue Markets) citing the ECCC Q1 2025 report."),
    dict(country="Canada", category="Feedstock & Trade Flows",
         metric="CFR credit generation, Q2 2025",
         value_display="2.38MT total compliance credits (+37% QoQ, +9% YoY); SAF volume 30.1K m³ (+301% "
                        "YoY, highest level recorded, entirely import-driven); SAF credits +23% YoY (limited "
                        "by CI rising from 29.7 to 70 gCO2/MJ)",
         value_num=30.1, unit="thousand m³ SAF volume (Q2 2025)", year=2025, confirmed=False,
         source_url="https://www.ccarbon.info/article/canada-cfr-q2-2025-rise-in-domestic-flow-and-total-credits-generation-by-low-ci-fuel-types/",
         as_of="2025-Q2",
         note="Secondary source (cCarbon analyst note); no official ECCC report newer than Q2/Q3 2025 could "
              "be located despite multiple searches — canada.ca's report index also returned HTTP 403."),
    dict(country="Canada", category="Pricing & Economics",
         metric="CFR credit price trend, 2025",
         value_display="Q1 2025 CAD $93.08 (down 41% YoY from CAD $157.23 in 2024) → Q2 2025 CAD $159.20 → "
                        "Q3 2025 CAD $216.65",
         value_num=216.65, unit="CAD/credit (Q3 2025)", year=2025, confirmed=False,
         source_url="https://www.clearbluemarkets.com/knowledge-base/canada-cfr-q1-2025-compliance-credit-market-report-review",
         as_of="2025-Q3",
         note="Secondary analyst source; Q3 figure appears as a forward reference within the Q1 2025 review "
              "article and wasn't independently verified against a Q3-specific report."),

    # ---------------- Primary-sourced extraction, round 2, 2026-08-04 ----------------
    # DOE/USDA/ICCT/SEC EDGAR (United States) and Colombia/Chile/Mexico watchlist coverage.

    # --- International ---
    dict(country="International", category="Pricing & Economics",
         metric="SAF cost premium vs. fossil jet fuel (ICCT)",
         value_display="2-5x generally cited; 2.1-10.6x when derived from EASA's 2024 production-cost range "
                        "(€1,461/tonne biofuels to €7,695/tonne e-fuels) against IEA fossil jet costs",
         value_num=5, unit="x fossil jet (commonly-cited upper bound)", year=2025, confirmed=True,
         source_url="https://theicct.org/why-and-how-to-bring-down-the-cost-of-saf-sept25/", as_of="2025-10-06",
         note="Corroborates the existing 2-5x range cited elsewhere in the study; theicct.org blocked plain "
              "WebFetch (403), retrieved via curl with a browser user-agent."),
    dict(country="United States", category="Policy & Regulation",
         metric="OBBBA 45Z changes — ICCT summary, cross-validated against Darling Ingredients' 10-Q",
         value_display="SAF multiplier removed, credit capped at $1.00/gal (down from $1.75 statutory base); "
                        "ILUC-emissions accounting zeroed out; feedstock restricted to North American origin",
         value_num=1.00, unit="USD/gallon (new cap)", year=2026, confirmed=True,
         source_url="https://theicct.org/the-curious-case-of-the-iras-sustainable-aviation-fuel-tax-credits-mar26/",
         as_of="2026-03-25", note="Independently corroborates the existing 45Z entries above; agrees with "
               "Darling Ingredients' 10-Q language on the same changes."),
    dict(country="International", category="Market Outlook & Targets",
         metric="MIT LatAm study — total cumulative capital investment & emissions outcome, 6-country region",
         value_display="$204 billion cumulative investment (2025-2050) across Brazil/Chile/Colombia/Ecuador/"
                        "Mexico/Peru; high-SAF scenario reaches ~60% reduction in 2050 aviation emissions vs. "
                        "baseline, with SAF at ~65% of fuel deployment by 2050",
         value_num=204, unit="USD billion", year=2050, confirmed=True,
         source_url="https://news.mit.edu/2025/toward-sustainable-decarbonization-aviation-latin-america-0121",
         as_of="2025-01-21", note="Same MIT study already cited for the Colombia-specific figures below; "
               "this is the region-wide total. Cross-verified against sustainability.mit.edu and the full "
               "cs3.mit.edu/publication/118414 report page, which has the per-country breakdown."),

    # --- Argentina (new coverage — Chile/Argentina watchlist) ---
    dict(country="Argentina", category="Production Capacity",
         metric="Argentina biodiesel production and exports (feedstock: soybean oil) — USDA FAS GAIN",
         value_display="Production 1.2 billion litres (2025, near record low); exports 340 million litres "
                        "(near 20-year low); capacity utilization <30%; domestic blend rate 6.6% vs. a 7.5% "
                        "mandate",
         value_num=1.2, unit="billion litres (2025 production)", year=2025, confirmed=True,
         source_url="https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Biofuels+Annual_Buenos+Aires_Argentina_AR2025-0013.pdf",
         as_of="2025-09-02", note="Direct from the live USDA FAS GAIN PDF (Report #AR2025-0013). Underscores "
               "the constrained state of the Argentina soy-oil complex that Braya's Newfoundland imports draw "
               "from — see the Canada entry on Braya's Argentina soy-oil sourcing."),

    # --- Canada ---
    dict(country="Canada", category="Production Capacity",
         metric="Canada renewable diesel production capacity growth — USDA FAS GAIN",
         value_display="994 million litres → 2,380 million litres (new plant came online July 2025)",
         value_num=2380, unit="million litres", year=2025, confirmed=True,
         source_url="https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Biofuels+Annual_Ottawa_Canada_CA2025-0045.pdf",
         as_of="2026-02-25", note="Direct from the live USDA FAS GAIN PDF (Report #CA2025-0045, the "
               "www.fas.usda.gov landing page 403'd but the underlying PDF was reachable). Same report notes "
               "the US BTC-to-45Z transition is disrupting Canadian biodiesel/renewable-diesel exports to the "
               "US — a direct spillover of the 45Z North American-content rule discussed in the US section."),
    dict(country="Canada", category="Market Outlook & Targets",
         metric="Canada biofuel consumption growth, 2025 vs. 2021 (pre-Clean Fuel Regulations baseline)",
         value_display="Ethanol +52%; biodiesel +20%; renewable diesel +275%",
         value_num=275, unit="% growth (renewable diesel)", year=2025, confirmed=True,
         source_url="https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Biofuels+Annual_Ottawa_Canada_CA2025-0045.pdf",
         as_of="2026-02-25"),
    dict(country="Canada", category="Market Outlook & Targets",
         metric="BC-LCFS SAF blending mandate — concrete volumes (USDA FAS GAIN)",
         value_display="22 million litres (2028) → 44 million litres (2029) → 66 million litres (2030), "
                        "implementing the 1%/2%/3% blend trajectory",
         value_num=66, unit="million litres (2030)", year=2030, confirmed=True,
         source_url="https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Biofuels+Annual_Ottawa_Canada_CA2025-0045.pdf",
         as_of="2026-02-25", note="Gives the existing BC-LCFS % trajectory entry a concrete volume figure."),
    dict(country="Canada", category="Financing & Investment",
         metric="Air Canada / Airbus Sustainability Co-Investment Platform — domestic SAF funding",
         value_display="CAD $13.7 million (~$10M USD) joint funding; Airbus committed to a 5-year purchase of "
                        "SAF environmental attributes for 60,000+ litres",
         value_num=13.7, unit="CAD million", year=2026, confirmed=True,
         source_url="https://www.greenairnews.com/?p=9296", as_of="2026-07",
         note="From GreenAir News' July 2026 roundup — new domestic Canadian SAF funding not previously in "
              "the study."),

    # --- Brazil ---
    dict(country="Brazil", category="Financing & Investment",
         metric="MIT LatAm study — Brazil SAF cost range and cumulative capital investment",
         value_display="$1.11-1.77/litre SAF cost; $84 billion cumulative capital investment (2025-2050) — "
                        "the largest of the six countries studied",
         value_num=84, unit="USD billion (cumulative investment)", year=2050, confirmed=True,
         source_url="https://cs3.mit.edu/publication/118414", as_of="2025-01",
         note="Direct from the full MIT CS3 report page (the news.mit.edu/sustainability.mit.edu summary "
              "articles only surface the region-wide total and Ecuador/Brazil headline figures, not all six "
              "countries — this CS3 page has the complete per-country breakdown)."),
    dict(country="Brazil", category="Production Capacity",
         metric="Acelen-Honeywell Ecofining technology partnership (Bahia biorefinery)",
         value_display="Honeywell to deploy modular Ecofining process technology for up to 1 billion litres/"
                        "yr combined SAF + renewable diesel — potentially one of the largest such facilities "
                        "globally",
         value_num=1.0, unit="billion litres/yr", year=2026, confirmed=True,
         source_url="https://www.greenairnews.com/?p=9278", as_of="2026-06",
         note="Same Bahia project as the Acelen financing entry above; this is the technology-partner "
              "announcement specifically."),
    dict(country="Brazil", category="Production Capacity",
         metric="Petrobras — first coprocessed SAF volumes delivered (Presidente Bernardes Refinery)",
         value_display="$1.2 billion project; first coprocessed SAF volumes delivered; Paulínia and Gabriel "
                        "Passos refineries expected to begin SAF production/marketing in 2026",
         value_num=1.2, unit="USD billion (project)", year=2026, confirmed=False,
         source_url="https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/120825-petrobras-delivers-first-coprocessed-saf-volumes-advances-2026-30-clean-fuels-strategy",
         as_of="2026", note="Lower-confidence: S&P Global blocked direct fetch (403), so this is from a "
               "WebSearch snippet only, not a verified live-page read — exact day-level dates unconfirmed. "
               "Directly updates the existing 'Petrobras has no SAF-specific IR disclosures' flag elsewhere "
               "in this dataset; worth a direct follow-up (Biodiesel Magazine also covered the same project) "
               "before citing precisely."),

    # --- Chile ---
    dict(country="Chile", category="Financing & Investment",
         metric="MIT LatAm study — Chile SAF cost range and cumulative capital investment",
         value_display="$1.68-2.53/litre SAF cost; $27 billion cumulative capital investment (2025-2050)",
         value_num=27, unit="USD billion (cumulative investment)", year=2050, confirmed=True,
         source_url="https://cs3.mit.edu/publication/118414", as_of="2025-01"),
    dict(country="Chile", category="Production Capacity",
         metric="Cabo Negro commercial-scale e-methanol facility (HIF Global)",
         value_display="175,000 tonnes e-methanol/yr planned; ~$830 million capex; environmental approval "
                        "received late 2025; no FID or construction start yet",
         value_num=175000, unit="tonnes/yr", year=2025, confirmed=False,
         source_url="https://industrydecarbonization.com/news/whats-up-with-the-production-of-e-fuels-in-chile.html",
         as_of="2025-Q4", note="Secondary source; no primary HIF confirmation of the $830M capex figure "
               "found independently."),
    dict(country="Chile", category="Policy & Regulation",
         metric="Haru Oni — ISCC-EU RFNBO certification",
         value_display="Renewed for the 2025/26 cycle; first non-EU facility to hold this certification "
                        "(originally awarded Oct 1, 2025)",
         value_num=None, unit=None, year=2026, confirmed=True,
         source_url="https://hifglobal.com/media/news-description/2025/10/01/hif-global-awarded-iscc-eu-rfnbo-certification--marking-a-global-milestone-in-the-e-fuels-market",
         as_of="2025-10-01", note="Direct from a live HIF Global primary press release — but it contains no "
               "quantitative production figures, only certification/qualitative language. HIF discloses no "
               "production numbers anywhere found in this extraction."),

    # --- Colombia ---
    dict(country="Colombia", category="Financing & Investment",
         metric="MIT LatAm study — Colombia SAF cost range and cumulative capital investment",
         value_display="$1.51-2.54/litre SAF cost; $23 billion cumulative capital investment (2025-2050)",
         value_num=23, unit="USD billion (cumulative investment)", year=2050, confirmed=True,
         source_url="https://cs3.mit.edu/publication/118414", as_of="2025-01"),
    dict(country="Colombia", category="Policy & Regulation",
         metric="Ecopetrol-Aerocivil 'SAF Vuela' cooperation MOU",
         value_display="Signed July 10, 2025; references a first dedicated SAF biorefinery (BioD-led) "
                        "targeting 50 million gal/yr, timeline reported inconsistently across sources "
                        "(2028-2030)",
         value_num=50, unit="million gal/yr (referenced plant target)", year=2025, confirmed=False,
         source_url="https://www.infobae.com/colombia/2025/07/10/ecopetrol-y-la-aeronautica-civil-acuerdan-impulsar-combustible-sostenible-de-aviacion-buscan-producir-450-millones-de-galones-saf-para-2050/",
         as_of="2025-07-10", note="Secondary news + Fedebiocombustibles corroboration, but the specific "
               "plant's timeline is inconsistent across sources (2028 vs. 2029 vs. a 2030 headline on the "
               "Fedebiocombustibles piece) — treat as unconfirmed pending a primary Aerocivil/BioD statement. "
               "No tax incentives are currently included in the MOU per Infobae."),
    dict(country="Colombia", category="Market Outlook & Targets",
         metric="Regional SAF corridor letters of intent",
         value_display="7 countries reported (Chile, Peru, Bolivia, Panama, Costa Rica, Aruba, Curaçao)",
         value_num=7, unit="countries", year=2026, confirmed=False,
         source_url="https://colombia.reportnews.la/blog/2026/07/17/saf-la-nueva-apuesta-de-colombia-para-atraer-inversion/",
         as_of="2026-04", note="Secondary news-aggregator source, not yet corroborated on Aerocivil's own "
               "site. Same article notes Colombia's pending SAF-incentive Bill 439 of 2024 remains unpassed."),

    # --- Mexico ---
    dict(country="Mexico", category="Financing & Investment",
         metric="MIT LatAm study — Mexico SAF cost range and cumulative capital investment",
         value_display="$1.41-2.40/litre SAF cost; $49 billion cumulative capital investment (2025-2050)",
         value_num=49, unit="USD billion (cumulative investment)", year=2050, confirmed=True,
         source_url="https://cs3.mit.edu/publication/118414", as_of="2025-01"),
    dict(country="Mexico", category="Policy & Regulation",
         metric="Ley de Biocombustibles — implementing regulation",
         value_display="Published Oct 2025; permit holders must file notice of operations start by Oct 6, "
                        "2026; SENER required to issue binding planning provisions by Dec 30, 2025",
         value_num=None, unit=None, year=2025, confirmed=True,
         source_url="https://sidof.segob.gob.mx/notas/docFuente/5769156", as_of="2025-10-03",
         note="Direct from the official DOF/SEGOB decree. Governs biofuels distribution/import-export "
              "permitting broadly — not SAF-specific, no SAF mandate or blend %."),
    dict(country="Mexico", category="Policy & Regulation",
         metric="SENER 'Mesa Técnica de SAF' technical roundtable process",
         value_display="5th roundtable held; 11 ordinary + 70+ extraordinary working sessions between Nov "
                        "2024 and Apr 2026; still no SAF mandate percentage or production target disclosed",
         value_num=5, unit="roundtables held", year=2026, confirmed=False,
         source_url="https://elvalle.com.mx/2026/04/30/gobierno-industria-y-academia-consolidan-hoja-de-ruta-del-saf-en-mexico/",
         as_of="2026-04-30", note="Both source URLs found returned HTTP 403 on direct fetch — relayed via "
               "WebSearch snippets only, not a verified full-text read. Confirms Mexico remains in a "
               "pre-mandate, consultative phase specifically for SAF (distinct from the broader biofuels law "
               "above, which is not SAF-specific)."),
    dict(country="Mexico", category="Production Capacity",
         metric="PEMEX SAF biorefinery proposal (AtJ + HEFA routes)",
         value_display="Proposed, no capacity/investment/timeline disclosed; >5 million hectares of "
                        "bioenergy-feedstock land identified nationally",
         value_num=5, unit="million hectares (feedstock land identified)", year=2026, confirmed=False,
         source_url="https://www.tamaulipasenlared.com.mx/2026/07/pemex-hara-biorrefineria-para-gasolina.html",
         as_of="2026-07-05", note="Secondary regional news outlet, not a PEMEX primary release — no matching "
               "release found on pemex.com or ebdi.pemex.com directly. Early-stage/announcement only."),
]

# Multi-year phased SAF mandate/target trajectories — the countries/regions
# with a genuine year-over-year percentage pathway in workingdraft.md. Powers
# the cross-country trajectory chart. (Colombia and the US Grand Challenge
# targets are volume-based, not percentage-based, so they aren't charted
# here — they're still in STATS as Market Outlook & Targets entries.)
MANDATE_TRAJECTORIES = {
    "Brazil (ProBioQAV, well-to-wake emissions reduction)": [
        (2027, 1), (2037, 10),
    ],
    "Canada — BC-LCFS (SAF blend mandate)": [
        (2028, 1), (2029, 2), (2030, 3),
    ],
    "Singapore (SAF uplift target, upper bound)": [
        (2026, 1), (2030, 5),
    ],
}

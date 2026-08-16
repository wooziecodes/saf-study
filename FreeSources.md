# Free Data Sources — Extracted from Datasources.md

Compiled 2026-07-29, refreshed 2026-08-16 with 8 sources closing gaps flagged in `gap-coverage-prompt.md` (Neste's Singapore/Rotterdam refineries, Singapore Airlines demand-side data, the 45Z FEOC rulemaking, and Malaysia/South Korea/Japan as competitive-hub-benchmark comparators). All sources below are free (or have a usable free tier, noted). Paid/subscription-only sources (S&P Global Platts, Argus Media, BloombergNEF, Rystad, Trade Data Monitor/S&P GTA, IJGlobal, ADI Analytics SAF Tracker) are excluded — see Datasources.md for those.

---

## Government / Regulatory — Primary Data

### United States
- **EIA Petroleum & Other Liquids data + Monthly Biofuels Capacity & Feedstocks Update** — eia.gov/petroleum/data.php — production/capacity/feedstock-consumed/imports-exports for biodiesel, renewable diesel, SAF. Monthly.
- **EPA RIN Generation Data / EMTS** — epa.gov/fuels-registration-reporting-and-compliance-help — RIN generation/retirement by D-code. Monthly CSV. Best free proxy for RFS-compliant volumes.
- **USDA ERS Oil Crops Outlook + USDA FAS GAIN reports** — ers.usda.gov, fas.usda.gov/data/gain-report — feedstock supply/demand. Annual with periodic updates.
- **DOE Alternative Fuels Data Center** — afdc.energy.gov/fuels/sustainable-aviation-fuel — production/capacity maps, program tracker.
- **SAF Grand Challenge Tracking Metrics Dashboard** (DOE/FAA/USDA) — energy.gov — production, lifecycle CO2e, planned capacity. ~Annual.
- **CARB LCFS Data Dashboard** — ww2.arb.ca.gov/applications/lcfs-data-dashboard — credit/deficit generation, prices, transacted volumes. Monthly/quarterly.
- **Washington Dept. of Ecology Clean Fuel Standard data** — ecology.wa.gov — credit/deficit volumes, prices. Quarterly.
- **Federal Register — Section 45Z Clean Fuel Production Credit** — federalregister.gov/documents/2026/02/04/2026-02246/section-45z-clean-fuel-production-credit — primary rulemaking text for the 45Z FEOC restriction (China/Russia/Iran/North Korea ownership ties), effective for tax years after July 4, 2025 / 2027.

### Brazil
- **ANP RenovaBio "Painel Dinâmico da Plataforma CBIO"** — gov.br/anp — CBIO issuance/registration/retirement + B3 exchange price data. Fortnightly.
- **EPE Balanço Energético Nacional — Dados Abertos** — epe.gov.br/pt/publicacoes-dados-abertos — national energy balance since 1970. Annual.
- **ANP general statistics portal** — biodiesel blend-mandate compliance, refining data.
- **CONAB** — conab.gov.br — soybean/sugarcane crop data. (Not independently re-verified — confirm before citing.)
- **Comex Stat / MDIC** — comexstat.mdic.gov.br — Brazilian customs data (SISCOMEX), HS-code level. Monthly.
- **ABIOVE** — abiove.org.br/statistics — vegetable-oil industry association's monthly soybean-complex export reports.

### Canada
- **ECCC Clean Fuel Regulations credit market reports** — canada.ca — quarterly credit generation by category, prices, trading activity.
- **NRCan Clean Fuels Fund** — natural-resources.canada.ca/energy-sources/clean-fuels — funding info; no consolidated project table (fragmented).
- **BC-LCFS registry** — presumed under gov.bc.ca low-carbon-fuels program — **unverified, flag for follow-up.**
- **Statistics Canada** — general trade/energy tables, not SAF-specific.

### Colombia / Chile / Mexico
- **Fedebiocombustibles** — fedebiocombustibles.com — Colombian biodiesel/ethanol sales volumes. Periodic.
- **Aerocivil / Resolution 00090 (SAF Roadmap)** — targets document, not a live feed.
- **Chile CNE Anuario Estadístico** — energia.gob.cl — annual sector statistical yearbook.
- **Mexico SIE (SENER)** — sie.energia.gob.mx — national energy statistics (free/institutional tiers).
- **PEMEX Base de Datos Institucional** — ebdi.pemex.com — operating statistics.

### Singapore
- **CAAS newsroom/policy documents** — caas.gov.sg — SAF Levy mechanics, SAFCo mandate (primary source, not a dataset). **Verify March 2026 levy-deferral date before citing.**
- **Enterprise Singapore StatLink** — statlink.enterprisesg.gov.sg — official bilateral trade by HS/SITC. Free basic tier, monthly (paid for detailed extracts).
- **data.gov.sg / SingStat Table Builder** — free open datasets/API, monthly.
- **MPA bunkering statistics** — adjacent to SAF (marine biofuel). Monthly.

### International
- **ICAO SAF Production Facilities tracker** — icao.int/SAF/SAF-production-facilities — official list of existing + announced facilities.
- **ICAO CORSIA Eligible Fuels registry / Docs 05 & 06** — icao.int/CORSIA — approved feedstocks, default lifecycle emissions values.
- **IATA SAF facilities map + SAF Fact Sheet** — iata.org — location/technology/capacity/status. ~Semi-annual.
- **IEA Bioenergy Task 39** — ieabioenergy.com — global SAF commercialization progress reports (PDFs, not live database).
- **UN Comtrade** — comtrade.un.org — free tier (paid API also available). ~200 reporters, HS 6-digit, monthly/annual.

### Asia-Pacific hub comparators (Malaysia / South Korea / Japan)
*For the competitive hub-benchmark gap — Singapore's "leading SAF hub" claim has never been benchmarked against these three.*
- **Malaysia SAF Market Intelligence (US ITA)** — trade.gov/market-intelligence/malaysia-energy-sustainable-aviation-fuel — Petronas/Malaysia's SAF build-out, targeting ~1Mt/yr by 2028.
- **MOLIT/MOTIE SAF Mandate press releases** — molit.go.kr/USR/NEWS/m_71/lst.jsp — Korea's SAF blending mandate (1% from 2027 → 7–10% by 2035). Korean-language.
- **METI/MLIT SAF Public-Private Council** — meti.go.jp/shingikai/energy_environment/saf/index.html — Japan's joint SAF council proceedings (targets, mandate, subsidies). Japanese-language.

---

## Trade & Feedstock-Flow Data

*Reminder: no HS code isolates "SAF" itself — these are feedstock-flow proxies (UCO 1518, tallow 1502, soy/palm/canola 1507/1511/1514, ethanol 2207, biodiesel/blends 3826, 2710.20), not SAF-volume data.*

- **UN Comtrade** — free tier.
- **ITC Trade Map** — trademap.org — free with registration (paid premium tier for extras). 220 countries, HS 2/4/6-digit since 2001.
- **WITS** (World Bank) — wits.worldbank.org — layers UNCTAD TRAINS tariff data onto Comtrade.
- **USITC DataWeb** — dataweb.usitc.gov — US Census-sourced, 1989–present, HTS 10-digit. Best free source for US-side UCO/tallow imports by origin.
- **US Census Bureau trade data** — census.gov/foreign-trade — underlies DataWeb.
- **GACC (China customs)** — underlying source, but not easily queryable without Chinese-language access.
- **INDEC** (Argentina) — indec.gob.ar — monthly "Comercio Exterior" bulletins; tracks the Argentina soy-oil→Canada corridor feeding Braya.
- **Fastmarkets** — fastmarkets.com/insights — platform is paid, but insight articles are often free.

---

## Market Intelligence, Pricing & Industry Associations

- **IATA** — Jet Fuel Price Monitor (joint w/ Platts), SAF Fact Sheet (updated June 2026).
- **ICCT** — theicct.org/series/saf — SAF cost/policy reports; source of the 2–5x cost-multiple citation.
- **RSB & ISCC** — standards/documentation free (certification itself is fee-based). Note: the two don't mutually recognize each other's voluntary-market certs.
- **RBQAV** (rbqav.com.br) — Brazilian SAF/bio-kerosene network; primary source for the Brazil deep dive.
- **Fedebiocombustibles / Fedepalma** (Colombia) — institutional landscape confirmation.
- **SEC EDGAR** — Valero, Darling Ingredients, Calumet filings.
- **SAF Investor** (safinvestor.com) — 100+ tracked projects, 37 US projects under development (some content gated).
- **SustainableAF** (sustainableaf.info) — continuously updated global production/company/offtake database.
- **Boeing SAF Dashboard**
- **Sustainable Aviation Futures** (sustainableaviationfutures.com) — monthly SAF Spotlight, free.
- **RMI SAF Outlook** (saf.rmi.org) — unverified in depth, follow up.

---

## Company/Project-Level Primary Sources

| Company/Project | Source |
|---|---|
| Darling Ingredients / Diamond Green Diesel | ir.darlingii.com; SEC 8-K/10-Q |
| World Energy (Paramount, CA) | worldenergy.net/press-release |
| Calumet / Montana Renewables | calumet.com; energy.gov/edf/montana-renewables |
| Acelen Renewables (Mubadala) | trade press (S&P Global, ESG Today, bioenergyinternational.com) |
| Imperial Oil / Tidewater Renewables | CER market snapshots; sustainablebiz.ca |
| Braya Renewable Fuels | fluor.com/projects/braya-renewable-fuels |
| Petrobras / Ecopetrol | SEC EDGAR (Ecopetrol 6-K); Petrobras IR — no SAF-specific disclosures yet |
| HIF Global | no company IR page found — trade press only |
| Neste — Singapore refinery (Tuas) | neste.com/en-sg/about-neste/how-we-operate/production/singapore-refinery — world's largest renewable diesel/SAF facility (~1Mt/yr SAF) |
| Neste — Rotterdam refinery | neste.com/news/neste-invests-in-its-world-scale-renewable-products-refinery-in-rotterdam — direct hub-benchmark comparator to Singapore |
| Singapore Airlines | singaporeair.com newsroom (press-release section) — SIA/Scoot SAF offtake deals, 5%-by-2030 target |

**Government loan/grant trackers:**
- **DOE Loan Programs Office — Montana Renewables page** — energy.gov/lpo
- **FAA FAST Grants page** — confirms program closed at $291M/22 projects, no further rounds.
- **NRCan Clean Fuels Fund** — fragmented, no consolidated project table.

---

## Academic / Research Institutions

- **Insper Agro in Data** — agro.insper.edu.br/en/agro-in-data — SAF/Brazil HEFA-vs-ATJ comparison series, English-language.
- **MIT "Toward Sustainable Decarbonization of Aviation in Latin America"** — news.mit.edu/2025; sustainability.mit.edu — primary source behind the Colombia claim (Colombia ~250M L/yr SAF potential; regional SAF cost $1.11–2.86/L vs ~$0.70/L conventional across 6 LatAm countries). Cite this directly.
- **FGV Acelen economic-impact study** — only confirmed via press coverage so far; underlying FGV PDF not yet located.
- **Columbia SIPA capstone (Mexico UCO/SAF)** — likely in sipa.columbia.edu/epd-capstone-directory, needs direct search.

---

## Certification & Traceability

- **RSB Document Library** — rsb.org/library — incl. Sept 2024 "Sustainable Feedstock Assessment for SAF."
- **ISCC System** — iscc-system.org — searchable certificate registry, credit-transfer mechanics.
- **SAFc Registry** — docs.safcregistry.org (RMI + EDF) — book-and-claim registry behind the American Airlines/Google deal.
- **Finboot / MARCO Track & Trace** — finboot.com/acelen-use-case — Acelen partnership case study.

---

## Trade Press for Ongoing Monitoring

- **GreenAir News** — greenairnews.com — broke the Acelen-Finboot story first; monthly roundups.
- **Biofuels Digest** — biofuelsdigest.com — annual "Biofuels Mandates Around the World" (65 countries), 2026 SAF regulatory guide. High signal.
- **Sustainable Aviation Futures** — sustainableaviationfutures.com — monthly SAF Spotlight, SAF Market Movers Guide.
- **SAF Investor** — safinvestor.com — dedicated tracker, some content gated.
- **epbr / Valor Econômico** — active Brazilian SAF coverage, Portuguese-language.
- **e-fuels.com/investor.html**, **RMI's saf.rmi.org** — supplementary trackers, not deeply vetted yet.
- **Ship & Bunker** (shipandbunker.com) — best available tracker for Fujairah's emerging biofuel bunkering activity (e.g. OMTI's first B30 delivery). Thin/watchlist-tier — no official Fujairah Port Authority SAF portal exists yet.

---

## Notes on borderline cases
- **Enterprise Singapore StatLink, ITC Trade Map, Fastmarkets, RSB/ISCC, Mexico SIE** — genuinely free at a basic/registration tier, but have a paid tier for deeper access. Included above but worth flagging if the study needs the paid depth.
- **IATA/CADO SAF Registry** — excluded; flagged in Datasources.md as possibly access-gated to CORSIA-participant airlines/states.

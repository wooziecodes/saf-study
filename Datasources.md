# Americas SAF Study — Data Source Map

Compiled 2026-07-29. Companion to `workingdraft.md` / `workingplan.md`. Organized by category; each entry gives what it provides, access cost, and update cadence where known. A short "Corrections/flags for workingdraft.md" section is at the bottom — worth acting on before the next draft pass.

---

## 1. Government / Regulatory — Primary Data

### United States
- **EIA Petroleum & Other Liquids data + Monthly Biofuels Capacity & Feedstocks Update** — eia.gov/petroleum/data.php — production/capacity/feedstock-consumed/imports-exports for biodiesel, renewable diesel, SAF. Free, monthly.
- **EPA RIN Generation Data / EMTS** — epa.gov/fuels-registration-reporting-and-compliance-help — RIN generation/retirement by D-code (incl. SAF-eligible categories). Free, monthly CSV. Best free proxy for actual RFS-compliant volumes moving through the market.
- **USDA ERS Oil Crops Outlook** + **USDA FAS GAIN reports** (Biofuels Annual, Oilseeds Annual/Update, incl. Canada/Argentina/Malaysia editions) — ers.usda.gov, fas.usda.gov/data/gain-report — feedstock supply/demand narrative + numbers. Free, annual with periodic updates.
- **DOE Alternative Fuels Data Center** — afdc.energy.gov/fuels/sustainable-aviation-fuel — production/capacity maps, program tracker. Free.
- **SAF Grand Challenge Tracking Metrics Dashboard** (DOE/FAA/USDA interagency) — energy.gov — annual dashboard on production, lifecycle CO2e, planned capacity. Free, ~annual (check for 2026 edition).
- **CARB LCFS Data Dashboard** — ww2.arb.ca.gov/applications/lcfs-data-dashboard — credit/deficit generation by pathway, credit prices, transacted volumes. Free, monthly/quarterly. Best available proxy for real transacted SAF/renewable-diesel volumes and pricing in the largest single state program.
- **Washington Dept. of Ecology Clean Fuel Standard data** — ecology.wa.gov — credit/deficit volumes, prices. Free, quarterly.

### Brazil
- **ANP RenovaBio "Painel Dinâmico da Plataforma CBIO"** — gov.br/anp — CBIO issuance/registration/retirement + B3 exchange price data. Free, updated fortnightly. Central Brazil source for this study.
- **EPE Balanço Energético Nacional — Dados Abertos** — epe.gov.br/pt/publicacoes-dados-abertos — national energy balance incl. biodiesel/ethanol consumption since 1970. Free, annual.
- **ANP general statistics portal** — biodiesel blend-mandate compliance, refining data. Free.
- **CONAB** — conab.gov.br — soybean/sugarcane crop data underlying feedstock-availability estimates. Free. (Not independently re-verified this pass — quick confirm before citing.)
- **Comex Stat / MDIC** — comexstat.mdic.gov.br — official Brazilian customs data (SISCOMEX), HS-code level. Free, monthly.
- **ABIOVE** — abiove.org.br/statistics — Brazilian vegetable-oil industry association's monthly soybean-complex export reports, easier-to-consume aggregation of Comex Stat. Free.

### Canada
- **ECCC Clean Fuel Regulations credit market reports** — canada.ca — quarterly credit generation by category (CC1/CC2/CC3), prices, trading activity. Free, quarterly. Confirms the draft's claim that SAF is a negligible share of CFR credits (0.8% in 2024).
- **NRCan Clean Fuels Fund** — natural-resources.canada.ca/energy-sources/clean-fuels — funds Imperial Oil (~$720M, >1B L/yr) and Tidewater (~$342M) projects, but has **no single consolidated public project table** — detail comes via CER market snapshots and company press releases rather than one database. Free but fragmented.
- **BC-LCFS registry** — no CARB-equivalent public dashboard confirmed; likely under gov.bc.ca low-carbon-fuels program. Flagged as unverified — worth a direct follow-up if BC mandate compliance becomes a bigger part of the write-up.
- **Statistics Canada** — general trade/energy tables, not SAF-specific. Free.

### Colombia / Chile / Mexico
- **Fedebiocombustibles** — fedebiocombustibles.com — Colombian biodiesel/ethanol sales volumes; industry-association data treated as sector record. Free, periodic.
- **Aerocivil / Resolution 00090 (SAF Roadmap)** — targets document, not a live data feed.
- **Chile CNE Anuario Estadístico** — energia.gob.cl — annual sector statistical yearbook. Free.
- **Mexico SIE (SENER)** — sie.energia.gob.mx — official national energy statistics portal. Free/institutional tiers, ongoing.
- **PEMEX Base de Datos Institucional (ebdi.pemex.com)** — operating statistics. Free. Neither Mexican source is SAF-specific given no domestic mandate exists yet.

### Singapore
- **CAAS newsroom/policy documents** — caas.gov.sg — SAF Levy mechanics and rate bands, SAFCo mandate. Not a live dataset, but the primary source of record — **check for the March 2026 deferral before citing dates** (see flags below).
- **Enterprise Singapore StatLink** — statlink.enterprisesg.gov.sg — official bilateral trade by HS/SITC. Free basic tier, monthly; paid for detailed bilateral extracts.
- **data.gov.sg / SingStat Table Builder** — free open datasets/API, monthly.
- **MPA (Maritime and Port Authority) bunkering statistics** — free, monthly; adjacent to SAF (marine biofuel, same trading-house infrastructure) rather than direct SAF data.

### International
- **ICAO SAF Production Facilities tracker** — icao.int/SAF/SAF-production-facilities — free, official list of existing + announced facilities. Primary source for capacity claims.
- **ICAO CORSIA Eligible Fuels registry / Docs 05 & 06** — icao.int/CORSIA — approved feedstocks, default lifecycle emissions values. Free, periodically updated — rules registry, not a volumes database.
- **IATA SAF facilities map + SAF Fact Sheet** — iata.org — location/technology/capacity/status; the "2.4Mt/0.8% of jet fuel in 2026" figure traces here. Free, ~semi-annual.
- **IATA/CADO SAF Registry** — likely restricted to CORSIA-participant airlines/states — flag as possibly access-gated.
- **IEA Bioenergy Task 39** — ieabioenergy.com — periodic global SAF commercialization progress reports. Free PDFs, not a live database.
- **UN Comtrade** — comtrade.un.org — free tier + paid API, ~200 reporters, HS 6-digit granularity, monthly/annual.

---

## 2. Trade & Feedstock-Flow Data

**Key limitation to carry into the write-up:** no HS code isolates "SAF" itself — it clears customs blended under jet-fuel codes (2710.19/2710.12 family) or isn't separately declared, since blending and book-and-claim structures mean the physical fuel and the sustainability claim often travel separately. HS-level data is a good proxy for **feedstock** flows (UCO, tallow, soy/palm oil) but cannot directly measure SAF trade.

**Relevant HS codes:** 1518 (UCO — also captures other hydrogenated/modified fats, so not cleanly isolated); 1502 (animal fats/tallow); 1507/1511/1514 (soybean/palm/canola oil); 2207 (ethanol); 3826 (biodiesel/blends); 2710.20 (fuel oils containing biodiesel).

- **UN Comtrade** — free/paid — baseline cross-country oils/UCO flows.
- **ITC Trade Map** — trademap.org — free (registration) + paid premium; 220 countries, HS 2/4/6-digit since 2001, adds market-share/unit-value analytics.
- **WITS** (World Bank) — wits.worldbank.org — free; layers UNCTAD TRAINS tariff data onto Comtrade — useful for tariff-driven diversion analysis (e.g., the 125% US tariff on Chinese UCO).
- **Trade Data Monitor / S&P Global GTA** — subscription-only; most granular bilateral HS data, industry standard for commodity trade desks. Best fit if the study has budget for it.
- **USITC DataWeb** — dataweb.usitc.gov — free, US Census-sourced, 1989–present, HTS 10-digit. Best free source for US-side UCO/tallow imports by origin.
- **US Census Bureau trade data** — census.gov/foreign-trade — free, underlies DataWeb.
- **GACC (China customs)** — underlying source but not easily queryable without Chinese-language access.
- **Fastmarkets** — fastmarkets.com/insights — confirmed live monthly China UCO/biodiesel export volume reports (e.g., May 2026: 310,000t UCO exports, +61% y/y; Jan–May 2026 cumulative 1.37Mt, +36.8% y/y). Paid platform, insight articles often free.
- **INDEC** (Argentina) — indec.gob.ar — free, monthly "Comercio Exterior" bulletins — needed to track the Argentina soy-oil→Canada corridor feeding Braya.
- **Argus Media / S&P Global Platts feedstock pricing** — separate US UCO, Asian UCO, European UCOME price assessments; used for supply-contract settlement. Paid.

**Judgment call from the research:** weight trade data as best for corroborating feedstock re-routing narratives (China→Europe, Argentina→Canada), not for estimating SAF volumes directly.

---

## 3. Market Intelligence, Pricing & Industry Associations

- **S&P Global Platts** — daily SAF (HEFA-SPK) CIF NW Europe price assessment (new methodology since March 2025, priced as premium to Jet CIF NWE forward curve). Subscription. Already underlies the draft's Platts volatility citation — worth pulling the live series rather than the single cited stat.
- **Argus Media** — Argus Biofuels (global SAF benchmark), Argus Americas Biofuels (US spot), Argus European SAF (ARA), new Argus e-SAF indexes, Biofuels Outlook/Analytics. Subscription. Fills the gap left by Platts' Europe-only citation with a US-specific benchmark.
- **ICIS, Mintec, OPIS** — general commodity platforms; no strong evidence of dedicated SAF assessments — secondary priority.
- **BloombergNEF** — SAF price-outlook research (e.g. "SAF Price Outlook: Leveling Off"); no standalone public facility database. Enterprise subscription.
- **Rystad Energy BioEnergy Solution** — has published Americas-relevant stats (US biofuel output +53% to 1.3M boepd by 2035; 43 oil-major biofuel projects, 286,000 bpd, ~90% HVO/SAF). Subscription.
- **Wood Mackenzie, Stratas Advisors** — general energy research; no confirmed SAF-specific product — verify directly before citing.
- **IATA** — Jet Fuel Price Monitor (joint w/ Platts), SAF Fact Sheet (updated June 2026). Free.
- **ICCT** — theicct.org/series/saf — free SAF cost/policy reports; source of the draft's 2–5x cost-multiple citation.
- **RSB & ISCC** — the two ICAO-recognized SAF certification schemes; **note the two don't mutually recognize each other's voluntary-market certifications** — relevant caveat for the Finboot/Acelen traceability discussion. Standards/documentation free; certification itself fee-based.
- **RBQAV** (rbqav.com.br) — Brazilian SAF/bio-kerosene network — direct primary source for the Brazil deep dive. Free.
- **Fedebiocombustibles / Fedepalma** (Colombia) — institutional landscape confirmation for the Colombia section. Free.
- **SEC EDGAR** — free; Valero 10-K corroborates DGD Port Arthur's 235M gal/yr SAF conversion; Darling Ingredients 10-K gives JV financial context; Calumet filings confirm Montana Renewables' phased 120–150M gal/yr (mid-2026) → 300M gal/yr (2028) ramp.
- **IJGlobal** — ijglobal.com/data — project-finance database (45,000+ assets), already has the Acelen $1.5B Bahia financing indexed. Enterprise subscription — best source for benchmarking comparable LatAm biorefinery deals.
- **SAF-specific trackers (mostly free):** ICAO SAF Production Facilities; IATA SAF facilities map; **SAF Investor** (safinvestor.com — 100+ tracked projects, reports 37 US projects under development); **SustainableAF** (sustainableaf.info — continuously updated global production/company/offtake database); **Boeing SAF Dashboard**; **ADI Analytics SAF Tracker** (biweekly newsletter, likely paid tier); **Sustainable Aviation Futures** (monthly SAF Spotlight, free); **RMI SAF Outlook** (saf.rmi.org, unverified in depth — follow up).

---

## 4. Company/Project-Level Primary Sources

| Company/Project | Source | Notes |
|---|---|---|
| Darling Ingredients / Diamond Green Diesel | ir.darlingii.com; SEC 8-K/10-Q | Verifies DGD's 235M gal/yr SAF nameplate directly from source. Free. |
| World Energy (Paramount, CA) | worldenergy.net/press-release | **Air Products exited the $2B expansion partnership in Feb 2025** — existing 250M gal/yr ops unaffected. Worth flagging as a project-risk update to the draft. Free. |
| Calumet / Montana Renewables | calumet.com; energy.gov/edf/montana-renewables | DOE loan drawdown structure: $782M first tranche + $150M Calumet equity, under Title 17 §1706 (Energy Infrastructure Reinvestment program), closed Jan 2025; total $1.67B incl. capitalized interest — refines the draft's flat "$1.44B" figure. Free. |
| Acelen Renewables (Mubadala) | trade press (S&P Global, ESG Today, bioenergyinternational.com) — no dedicated English IR page found | Confirms HSBC/IFC-led 10-institution consortium, ~90% volumes pre-contracted, ~3,600 peak construction jobs (distinct from FGV's separate 85,000 full-value-chain figure — don't conflate). |
| Imperial Oil / Tidewater Renewables | CER market snapshots; sustainablebiz.ca | Confirms both as NRCan Clean Fuels Fund recipients — grounds the draft's company mentions in an actual funding mechanism. Free. |
| Braya Renewable Fuels | fluor.com/projects/braya-renewable-fuels | Up to 18,000 bbl/day operational; SAF expansion planned. Free. |
| Petrobras / Ecopetrol | SEC EDGAR (Ecopetrol 6-K); Petrobras IR | **Gap: neither company has SAF-specific IR disclosures yet** — rely on ANP/Aerocivil filings and trade press instead, and say so explicitly in the study. |
| HIF Global | no company IR page surfaced despite two searches | Brazil ($4B e-fuels plant, Feb 2026) and Chile updates trace only to trade press — flag as a sourcing gap if the study leans on HIF-specific figures. |

**Government loan/grant trackers:**
- **DOE Loan Programs Office — Montana Renewables page** (energy.gov/lpo) — primary-source correction on the loan structure (above). Free.
- **FAA FAST Grants page** — confirms program closed at $291M/22 projects, no further rounds. Free.
- **NRCan Clean Fuels Fund** — fragmented, no consolidated project table (see §1 Canada).

---

## 5. Academic / Research Institutions

- **Insper Agro in Data** (agro.insper.edu.br/en/agro-in-data) — dedicated SAF/Brazil HEFA-vs-ATJ comparison series, English-language. Free.
- **FGV Acelen economic-impact study** — the $40B/85,000-jobs figure currently only confirmed via press coverage (clickpetroleoegas.com); the underlying FGV PDF itself wasn't located — would need a direct portal.fgv.br search.
- **MIT "Toward Sustainable Decarbonization of Aviation in Latin America"** (news.mit.edu/2025; sustainability.mit.edu) — the actual primary source behind the draft's Colombia claim. Findings: Colombia could reach ~250M L/yr SAF with a 20% palm/sugarcane output increase; regional SAF cost $1.11–2.86/L vs ~$0.70/L conventional across 6 LatAm countries studied. Free — **cite this directly instead of the draft's secondary paraphrase.**
- **Columbia SIPA capstone (Mexico UCO/SAF)** — confirmed real, client tied to SENER/Pemex, updated the 2017 SENER roadmap; exact document likely in sipa.columbia.edu/epd-capstone-directory, not independently indexed — needs a direct by-year directory search.
- **Embrapa / University of São Paulo** — draft's claim about macaúba/soy-residue research is **unconfirmed** — no SAF-specific publications surfaced; needs a direct repository search before citing further.
- **NREL/PNNL** — no SAF-specific publications surfaced despite targeted search; cite DOE's Bioenergy Technologies Office / 45ZCF-GREET documentation instead unless a follow-up finds named reports.

---

## 6. Certification & Traceability

- **RSB Document Library** (rsb.org/library) — incl. Sept 2024 "Sustainable Feedstock Assessment for SAF." Free.
- **ISCC System** (iscc-system.org) — searchable certificate registry, credit-transfer mechanics. Free to search.
- **SAFc Registry** (docs.safcregistry.org, founded by RMI + EDF) — the actual book-and-claim registry behind the American Airlines/Google deal cited in the draft — the draft doesn't name it; worth filling this gap. Free public documentation.
- **Finboot / MARCO Track & Trace** (finboot.com/acelen-use-case) — Finboot's own case-study page confirms the Acelen partnership scope (12-month term, land eligibility, farm-level production, emissions calculator, tokenization) — a stronger primary source than generic trade press. Free.

---

## 7. Trade Press for Ongoing Monitoring

- **GreenAir News** (greenairnews.com) — broke the Acelen-Finboot story first; monthly roundups. Free.
- **Biofuels Digest** (biofuelsdigest.com) — annual "Biofuels Mandates Around the World" (65 countries), 2026 "Multi-Slide Guide to SAF Regulatory Changes." Free, high signal.
- **SAF Investor** (safinvestor.com) — dedicated project/producer tracker, some content gated.
- **Sustainable Aviation Futures** (sustainableaviationfutures.com) — monthly SAF Spotlight, SAF Market Movers Guide. Free.
- **epbr / Valor Econômico** — active Brazilian SAF coverage, Portuguese-language, not deeply indexed in English search — needs direct site search for granular sourcing.
- **e-fuels.com/investor.html**, **RMI's saf.rmi.org** — supplementary project trackers, not in the original brief but worth a look.

---

## Corrections / flags for `workingdraft.md`

1. **Singapore SAF Levy date** — CAAS reportedly deferred the levy in March 2026: ticket sales still start Oct 2026, but actual flight-departure applicability was pushed to **Jan 2027**, not Oct 2026 as the draft states (§2.4). Verify against caas.gov.sg before the next draft pass.
2. **World Energy / Air Products** — Air Products exited the $2B Paramount, CA expansion partnership in Feb 2025. Existing 250M gal/yr operations are unaffected, but this is a live project-risk fact missing from the US section.
3. **Montana Renewables DOE loan** — actual structure is $782M first tranche + $150M Calumet equity under Title 17 §1706, $1.67B total including capitalized interest — more precise than the draft's flat "$1.44 billion."
4. **China UCO exports** — the draft cites a 55% YoY drop in China→US UCO (Jan–Nov 2024 vs 2025). Separately, China's *global* UCO exports were up 36.8% YoY in Jan–May 2026 (1.37Mt). These aren't necessarily contradictory (US-bound down, global/Europe-bound up) but should be reconciled explicitly rather than left as two disconnected stats.
5. **HS-code caveat** — no customs code isolates SAF itself; any trade-data-based claims in the study should be scoped to feedstock flows, not finished SAF volumes.
6. **Acelen jobs figures** — trade press cites ~3,600 peak construction jobs; FGV's 85,000 figure is a full-value-chain, ten-year estimate. These are different metrics and shouldn't be presented as if interchangeable.
7. **Petrobras / Ecopetrol** — neither has SAF-specific investor disclosures yet; the study should lean on ANP/Aerocivil regulatory filings and trade press for these two, and say so rather than imply IR-level confirmation.

"""Americas SAF Study — Quick Reference.

The primary entry point for this Streamlit app. Built for an associate who is
writing prose (not filtering data) — find the figure you need for the section
you're on, click straight through to the source, cite it, move on. The full
filterable stats explorer and the complete free-source catalog are one click
away in the sidebar for deeper digging.
"""

import pandas as pd
import streamlit as st

from stats_data import CORRECTIONS, STATS

st.set_page_config(page_title="Americas SAF Study — Reference", page_icon="🛩️", layout="wide")

df = pd.DataFrame(STATS)
for col in ("source_url", "as_of", "note"):
    if col not in df.columns:
        df[col] = None

st.title("🛩️ Americas SAF Study — Quick Reference")
st.caption(
    "Find the figure for the section you're writing, click the source link, cite it. "
    "👈 The sidebar has the full filterable **Stats Explorer** (all charts/filters) and the "
    "**Source Catalog** (all ~90 free sources for this study) if you need to dig deeper."
)
st.markdown(
    "**Key:** &nbsp;🔗 **Source** — click through, this figure was independently pulled from a live "
    "source and is safe to cite directly. &nbsp;·&nbsp; *(not yet independently verified)* — this figure "
    "is drawn from `workingdraft.md`'s prose only; confirm it against a source before citing it in the "
    "final study."
)
st.divider()

search = st.text_input(
    "🔍 Search for a figure — e.g. \"45Z\", \"CBIO\", \"credit price\", \"Acelen\"", ""
)

COUNTRY_ORDER = [
    "International", "United States", "Canada", "Brazil", "Chile", "Argentina", "Colombia", "Mexico",
    "Singapore",
]
CATEGORY_ORDER = [
    "Policy & Regulation", "Feedstock & Trade Flows", "Production Capacity",
    "Financing & Investment", "Pricing & Economics", "Market Outlook & Targets",
]


def ordered(values, priority):
    present = [v for v in priority if v in values]
    present += [v for v in sorted(set(values)) if v not in present]
    return present


def render_row(row):
    metric = row["metric"]
    value = row["value_display"]
    if pd.notna(row["source_url"]) and row["source_url"]:
        as_of = f" · as of {row['as_of']}" if pd.notna(row["as_of"]) and row["as_of"] else ""
        tail = f" &nbsp;[🔗 Source ↗]({row['source_url']}){as_of}"
    else:
        tail = " &nbsp;*(not yet independently verified)*"
    st.markdown(f"- **{metric}** — {value}{tail}")
    if pd.notna(row["note"]) and row["note"]:
        st.caption(row["note"])


present_countries = ordered(df["country"].unique(), COUNTRY_ORDER)

if search:
    mask = (
        df["metric"].str.contains(search, case=False)
        | df["value_display"].str.contains(search, case=False)
        | df["country"].str.contains(search, case=False)
        | df["category"].str.contains(search, case=False)
    )
    results = df[mask]
    st.subheader(f"Search results for “{search}” — {len(results)} found")
    if results.empty:
        st.info("No matches. Try the full Stats Explorer in the sidebar for broader filtering.")
    else:
        for country in ordered(results["country"].unique(), COUNTRY_ORDER):
            sub = results[results["country"] == country]
            st.markdown(f"#### {country}")
            for _, row in sub.iterrows():
                render_row(row)
else:
    tabs = st.tabs(present_countries)
    for tab, country in zip(tabs, present_countries):
        with tab:
            sub_country = df[df["country"] == country]
            n_sourced = int(sub_country["source_url"].notna().sum())
            st.caption(f"{len(sub_country)} data points · {n_sourced} directly source-linked")
            for cat in ordered(sub_country["category"].unique(), CATEGORY_ORDER):
                sub_cat = sub_country[sub_country["category"] == cat]
                st.markdown(f"**{cat}**")
                for _, row in sub_cat.iterrows():
                    render_row(row)
                st.markdown("")

st.divider()
with st.expander(f"⚠️ Known corrections & sourcing caveats ({len(CORRECTIONS)}) — worth a skim before citing"):
    st.write(
        "Items the research surfaced that correct, update or add caution to a claim in "
        "`workingdraft.md` — not tied to one specific figure above, so check here too."
    )
    for item in CORRECTIONS:
        st.markdown(f"**{item['title']}**")
        st.caption(item["detail"])

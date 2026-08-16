"""Americas SAF Study — Source Catalog.

The primary entry point for this Streamlit app. A curated, per-market
shortlist of pre-vetted, free/open-access portals for follow-up research
beyond the deck — click through to a market's primary source, pull the
underlying data, keep digging. The Quick Reference stat cards and the full
filterable stats explorer are one click away in the sidebar.
"""

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from data_sources import CORRECTIONS, SOURCES

st.set_page_config(page_title="Americas SAF Study — Source Catalog", page_icon="🛩️", layout="wide")

df = pd.DataFrame(SOURCES)
COST_ORDER = ["Free", "Freemium", "Paid", "Restricted", "Unknown"]

st.title("🗂️ Americas SAF Study — Source Catalog")
st.caption(
    "Curated, per-market shortlist of pre-vetted, free/open-access portals for follow-up research "
    "beyond the deck — one to a few best primary sources per market, not an exhaustive list. "
    "👈 The sidebar has the **Quick Reference** stat cards and the full filterable **Stats "
    "Explorer** for deeper digging. For the fuller raw-research archive (incl. paid/unconfirmed "
    "sources), see `Datasources.md`."
)

# ---------------- Sidebar filters ----------------
st.sidebar.header("Filters")
categories = sorted(df["category"].unique())
selected_categories = st.sidebar.multiselect("Category", categories, default=categories)

costs = [c for c in COST_ORDER if c in df["cost"].unique()]
selected_costs = st.sidebar.multiselect("Access cost", costs, default=costs)

regions = sorted(df["region"].unique())
selected_regions = st.sidebar.multiselect("Region", regions, default=regions)

search = st.sidebar.text_input("Search name/description", "")

if st.sidebar.button("Reset filters"):
    st.rerun()

filtered = df[
    df["category"].isin(selected_categories)
    & df["cost"].isin(selected_costs)
    & df["region"].isin(selected_regions)
]
if search:
    mask = filtered["name"].str.contains(search, case=False) | filtered["description"].str.contains(
        search, case=False
    )
    filtered = filtered[mask]

# ---------------- Summary metrics ----------------
m1, m2, m3, m4 = st.columns(4)
m1.metric("Sources shown", len(filtered))
m2.metric("Markets covered", filtered["region"].nunique())
m3.metric("Free / freemium", int(filtered["cost"].isin(["Free", "Freemium"]).sum()))
m4.metric("Categories", filtered["category"].nunique())

st.divider()

# ---------------- Charts ----------------
chart_col1, chart_col2 = st.columns(2)

REGION_PALETTE = [
    "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4",
    "#008300", "#4a3aa7", "#c0392b", "#16a2a2", "#8e6c3a",
    "#5d5d5d", "#a05dbd",
]

with chart_col1:
    st.subheader("Sources by market")
    region_counts = filtered["region"].value_counts().sort_values(ascending=True)
    fig = go.Figure(
        go.Bar(
            x=region_counts.values,
            y=region_counts.index,
            orientation="h",
            marker_color=[REGION_PALETTE[i % len(REGION_PALETTE)] for i in range(len(region_counts))],
            text=region_counts.values,
            textposition="outside",
            hovertemplate="%{y}: %{x} sources<extra></extra>",
        )
    )
    fig.update_layout(
        height=380,
        margin=dict(l=10, r=30, t=10, b=10),
        xaxis=dict(title="", showgrid=True, gridcolor="rgba(128,128,128,0.2)", zeroline=False),
        yaxis=dict(title=""),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    st.subheader("Sources by access cost")
    cost_counts = filtered["cost"].value_counts()
    cost_counts = cost_counts.reindex([c for c in COST_ORDER if c in cost_counts.index])
    palette_seq = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
    fig2 = go.Figure(
        go.Bar(
            x=cost_counts.index,
            y=cost_counts.values,
            marker_color=palette_seq[: len(cost_counts)],
            text=cost_counts.values,
            textposition="outside",
            hovertemplate="%{x}: %{y} sources<extra></extra>",
        )
    )
    fig2.update_layout(
        height=380,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(title=""),
        yaxis=dict(title="", showgrid=True, gridcolor="rgba(128,128,128,0.2)", zeroline=False),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ---------------- Tabs: browse table / corrections ----------------
tab1, tab2 = st.tabs(["Browse sources", "Corrections & flags for workingdraft.md"])

with tab1:
    st.dataframe(
        filtered[["category", "region", "name", "cost", "frequency", "description", "url"]].rename(
            columns={
                "category": "Category",
                "region": "Region",
                "name": "Name",
                "cost": "Cost",
                "frequency": "Frequency",
                "description": "What it provides",
                "url": "Link",
            }
        ),
        use_container_width=True,
        hide_index=True,
        height=600,
        column_config={
            "Link": st.column_config.LinkColumn("Link", display_text="Open ↗"),
        },
    )

with tab2:
    st.write(
        "Items the research surfaced that should be corrected or reconciled in `workingdraft.md` "
        "before the next pass."
    )
    for item in CORRECTIONS:
        with st.expander(item["title"]):
            st.write(item["detail"])

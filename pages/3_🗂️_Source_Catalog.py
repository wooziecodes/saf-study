import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from data_sources import CATEGORY_COLORS, CORRECTIONS, SOURCES

st.set_page_config(page_title="Americas SAF Study — Data Sources", page_icon="🛩️", layout="wide")

df = pd.DataFrame(SOURCES)
COST_ORDER = ["Free", "Freemium", "Paid", "Restricted", "Unknown"]

st.title("Americas SAF Study — Data Source Explorer")
st.caption(
    "Reference catalog of data sources that can support the Americas SAF study "
    "(government/regulatory, trade & feedstock flows, market intelligence, company/project, "
    "academic, certification, trade press). Companion to `Datasources.md`."
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
m2.metric("Free / freemium", int(filtered["cost"].isin(["Free", "Freemium"]).sum()))
m3.metric("Paid / restricted", int(filtered["cost"].isin(["Paid", "Restricted"]).sum()))
m4.metric("Categories", filtered["category"].nunique())

st.divider()

# ---------------- Charts ----------------
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Sources by category")
    cat_counts = filtered["category"].value_counts().sort_values(ascending=True)
    fig = go.Figure(
        go.Bar(
            x=cat_counts.values,
            y=cat_counts.index,
            orientation="h",
            marker_color=[CATEGORY_COLORS.get(c, "#999999") for c in cat_counts.index],
            text=cat_counts.values,
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

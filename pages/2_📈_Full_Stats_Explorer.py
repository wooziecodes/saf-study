import sys
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from stats_data import CATEGORY_COLORS, COUNTRY_COLORS, CORRECTIONS, MANDATE_TRAJECTORIES, STATS

st.set_page_config(page_title="Americas SAF Study — Stats Explorer", page_icon="📊", layout="wide")

df = pd.DataFrame(STATS)
df["flagged"] = ~df["confirmed"]

# Litres/yr -> US gallons/yr equivalent, for the one chart that compares
# across countries reporting capacity in different units. Only projects with
# a clean, unambiguous annual-volume figure are included — mass-based (tonnes)
# and rate-based (bbl/day) figures aren't converted, since that would require
# assumptions not present in workingdraft.md. Colombia and Mexico have no
# comparable large-scale annual-volume figure yet (consistent with the draft's
# own read that both remain trial-scale through the late 2020s).
LITRES_TO_GAL = 0.264172
CAPACITY_CHART_ROWS = [
    dict(project="Diamond Green Diesel — Port Arthur (US)", country="United States", mgy=235.0),
    dict(project="World Energy — Paramount, CA (US)", country="United States", mgy=250.0),
    dict(project="Montana Renewables (US, 2028 target)", country="United States", mgy=300.0),
    dict(project="Braya Renewable Fuels (Canada)", country="Canada", mgy=round(824 * LITRES_TO_GAL, 1)),
    dict(project="Tidewater Renewables (Canada)", country="Canada", mgy=round(170 * LITRES_TO_GAL, 1)),
    dict(project="Imperial Oil Strathcona (Canada)", country="Canada", mgy=round(1000 * LITRES_TO_GAL, 1)),
    dict(project="Acelen Bahia biorefinery, SAF+RD (Brazil, 2029 target)", country="Brazil",
         mgy=round(1000 * LITRES_TO_GAL, 1)),
    dict(project="Haru Oni later-phase target (Chile)", country="Chile", mgy=round(550 * LITRES_TO_GAL, 1)),
]
cap_df = pd.DataFrame(CAPACITY_CHART_ROWS).sort_values("mgy")

st.title("Americas SAF Study — Stats Explorer")
st.caption(
    "Structured statistics extracted from `workingdraft.md`, cross-referenced against the corrections "
    "surfaced in `Datasources.md`. Every entry here is independently sourced. Companion to the "
    "**Source Catalog** (home page)."
)

# ---------------- Sidebar filters ----------------
st.sidebar.header("Filters")
countries = sorted(df["country"].unique())
selected_countries = st.sidebar.multiselect("Country / region", countries, default=countries)

categories = sorted(df["category"].unique())
selected_categories = st.sidebar.multiselect("Category", categories, default=categories)

status_choice = st.sidebar.radio("Status", ["All", "Confirmed only", "Flagged only"], index=0)

search = st.sidebar.text_input("Search metric/value", "")

if st.sidebar.button("Reset filters"):
    st.rerun()

filtered = df[df["country"].isin(selected_countries) & df["category"].isin(selected_categories)]
if status_choice == "Confirmed only":
    filtered = filtered[~filtered["flagged"]]
elif status_choice == "Flagged only":
    filtered = filtered[filtered["flagged"]]
if search:
    mask = filtered["metric"].str.contains(search, case=False) | filtered["value_display"].str.contains(
        search, case=False
    )
    filtered = filtered[mask]

# ---------------- Summary metrics ----------------
m1, m2, m3, m4 = st.columns(4)
m1.metric("Stats shown", len(filtered))
m2.metric("Flagged / corrected", int(filtered["flagged"].sum()))
m3.metric("Categories", filtered["category"].nunique())
m4.metric("Countries / regions", filtered["country"].nunique())

st.divider()

# ---------------- Chart 1: mandate/target trajectories (fixed reference) ----------------
st.subheader("SAF mandate & target trajectories")
st.caption(
    "Fixed reference chart (not affected by sidebar filters) — the countries/regions in workingdraft.md with a "
    "genuine multi-year percentage pathway. Colombia's targets and the US SAF Grand Challenge target are "
    "volume-based, not percentage-based, so they aren't shown here — see the browse table below."
)
traj_colors = {
    "Brazil (ProBioQAV, well-to-wake emissions reduction)": "#2a78d6",
    "Canada — BC-LCFS (SAF blend mandate)": "#eb6834",
    "Singapore (SAF uplift target, upper bound)": "#1baf7a",
}
fig_traj = go.Figure()
for series_name, points in MANDATE_TRAJECTORIES.items():
    years = [p[0] for p in points]
    values = [p[1] for p in points]
    fig_traj.add_trace(
        go.Scatter(
            x=years,
            y=values,
            mode="lines+markers+text",
            name=series_name,
            line=dict(width=2, color=traj_colors[series_name]),
            marker=dict(size=8, color=traj_colors[series_name]),
            text=[None] * (len(points) - 1) + [f"{values[-1]}% by {years[-1]}"],
            textposition="middle right",
            hovertemplate=f"{series_name}<br>%{{x}}: %{{y}}%<extra></extra>",
        )
    )
fig_traj.update_layout(
    height=420,
    margin=dict(l=10, r=140, t=10, b=10),
    xaxis=dict(title="Year", showgrid=True, gridcolor="rgba(128,128,128,0.2)", zeroline=False),
    yaxis=dict(title="Target (%)", showgrid=True, gridcolor="rgba(128,128,128,0.2)", zeroline=False),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
st.plotly_chart(fig_traj, use_container_width=True)

st.divider()

# ---------------- Chart 2: production capacity by project ----------------
st.subheader("Production capacity by project (US gallons/yr equivalent)")
st.caption(
    "Curated subset with a clean, comparable annual-volume figure — converted to a common unit where the draft "
    "reports litres/yr. Filtered by the Country selection in the sidebar; excludes mass- or rate-based figures "
    "(tonnes/yr, bbl/day) that would need unstated assumptions to convert."
)
cap_filtered = cap_df[cap_df["country"].isin(selected_countries)]
fig_cap = go.Figure(
    go.Bar(
        x=cap_filtered["mgy"],
        y=cap_filtered["project"],
        orientation="h",
        marker_color=[COUNTRY_COLORS.get(c, "#999999") for c in cap_filtered["country"]],
        text=cap_filtered["mgy"],
        textposition="outside",
        hovertemplate="%{y}<br>%{x} million gal/yr equivalent<extra></extra>",
    )
)
fig_cap.update_layout(
    height=380,
    margin=dict(l=10, r=60, t=10, b=10),
    xaxis=dict(title="Million US gallons/yr (equivalent)", showgrid=True, gridcolor="rgba(128,128,128,0.2)", zeroline=False),
    yaxis=dict(title=""),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    showlegend=False,
)
st.plotly_chart(fig_cap, use_container_width=True)

st.divider()

# ---------------- Tabs: browse table / flags ----------------
tab1, tab2 = st.tabs(["Browse stats", "Flags & corrections"])

with tab1:
    display_df = filtered.copy()
    display_df["Status"] = display_df["flagged"].map({True: "⚠️ Flagged", False: "Confirmed"})
    st.dataframe(
        display_df[
            ["country", "category", "metric", "value_display", "year", "Status",
             "source_url", "as_of", "note"]
        ].rename(
            columns={
                "country": "Country / region",
                "category": "Category",
                "metric": "Metric",
                "value_display": "Value",
                "year": "Year",
                "source_url": "Source",
                "as_of": "Data as of",
                "note": "Note",
            }
        ),
        use_container_width=True,
        hide_index=True,
        height=600,
        column_config={
            "Source": st.column_config.LinkColumn("Source", display_text="Open ↗"),
        },
    )

with tab2:
    st.write(
        "Corrections and open discrepancies `Datasources.md` surfaced against `workingdraft.md`'s figures — "
        "the same list referenced by the 'Flagged' stats above."
    )
    for item in CORRECTIONS:
        with st.expander(item["title"]):
            st.write(item["detail"])

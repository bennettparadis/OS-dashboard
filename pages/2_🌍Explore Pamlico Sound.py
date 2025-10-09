import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from utils import text

# ==========================
# DATA LOADING (CACHED)
# ==========================
@st.cache_data
def load_data():
    df = pd.read_csv("data/2019-2025_oyster_densities.csv")
    OSMaterial = gpd.read_file("data/OS_material_storymap.shp").to_crs(epsg=4326)
    OSBoundaries = gpd.read_file("data/permit_boundaries.shp").to_crs(epsg=4326)
    return df, OSMaterial, OSBoundaries

df, OSMaterial, OSBoundaries = load_data()

# ==========================
# PAGE SETUP
# ==========================
text.display_text("🌍Explore Pamlico Sound", font_size=50, font_weight="bold")
text.pages_font()
text.display_text(
    "As of 2025, North Carolina has 17 oyster sanctuaries in Pamlico Sound, totaling 789 acres of permitted, protected subtidal habitat. "
    "Every year NCDMF's Habitat & Enhancement dive team visits each sanctuary to collect oyster data around the reefs. "
    "Explore the map to see how oyster densities differ across Pamlico Sound over the last few years."
)

with st.expander("Instructions"):
    st.info(
        """
        **Click and drag** the map to explore Pamlico Sound. Use the scroll-wheel to zoom in and out.  

        **Hold the right mouse button** to rotate the map.  

        The **red circles** show where our dive team has sampled at each sanctuary. Hover over one to see the observed oyster density.  

        **Select a year** from the drop down menu in the sidebar to see how densities change over time.
        """
    )

# ==========================
# SIDEBAR
# ==========================
st.sidebar.subheader(
    "Use the dropdown to select a year and explore oyster densities across the Oyster Sanctuary Network"
)

years = sorted(df["Year"].unique())
default_year = 2024
selected_year = st.sidebar.selectbox(
    "Select a Year:",
    years,
    index=years.index(default_year)
)

# ==========================
# FILTER DATA BY YEAR
# ==========================
df_selected = df.query("Year == @selected_year").dropna(subset=["Latitude", "Longitude", "total"])

# ==========================
# PLOTLY MAP
# ==========================
# Polygons for OSMaterial
fig = px.choropleth_mapbox(
    OSMaterial,
    geojson=OSMaterial.geometry,
    locations=OSMaterial.index,
    color_discrete_sequence=["red"],
    opacity=0.3
)

# Add oyster density points
fig.add_scattermapbox(
    lat=df_selected["Latitude"],
    lon=df_selected["Longitude"],
    mode="markers",
    marker=dict(
        size=df_selected["total"].apply(lambda x: max(5, x*0.5)),  # scale size
        color="red",
        opacity=0.7
    ),
    text=df_selected["total"],
    hovertemplate="Oysters/m²: %{text}<extra></extra>"
)

# Add centroids text labels for boundaries
centroids = OSBoundaries.geometry.centroid
fig.add_scattermapbox(
    lat=centroids.y,
    lon=centroids.x,
    mode="text",
    text=OSBoundaries["OS_Name"],
    textposition="top center",
    marker=dict(size=1, color="black")
)

# Layout
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_zoom=11.2,
    mapbox_center={"lat": 35.05, "lon": -76.4},
    margin={"r":0,"t":0,"l":0,"b":0},
    height=700
)

st.plotly_chart(fig, use_container_width=True)

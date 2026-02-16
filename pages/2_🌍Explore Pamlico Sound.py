import streamlit as st
import pandas as pd
import plotly.express as px
import json
import branca.colormap as cm
import geopandas as gpd
from utils import text

# Load data
df = pd.read_csv('data/2019-2025_oyster_densities.csv')
OSMaterial = gpd.read_file("data/OS_material_storymap.shp")
OSBoundaries = gpd.read_file("data/permit_boundaries.shp")

# PAGE SETUP
text.tab_display()
text.display_text("🌍Explore Pamlico Sound", font_size=50, font_weight='bold')
text.pages_font()
text.display_text("As of 2025, North Carolina has 17 oyster sanctuaries in Pamlico Sound, providing a total of 789 acres of protected subtidal habitat. Every year NCDMF's Habitat & Enhancement dive team visits each sanctuary to collect oyster data around the reefs. Explore the map to see how oyster densities differ across Pamlico Sound over the last few years.")

with st.expander("THIS PAGE IS UNDERGOING MAINTENANCE"):
    st.info("""
             **Please come back at another time to view an interactive map of the Pamlico Sound Oyster Sanctuary Network**

              
    """)
#SIDEBAR SETUP
st.sidebar.subheader("Use the dropdown to select a year and explore oyster densities across the Oyster Sanctuary Network")
default_year = 2025
default_year_index = list(df["Year"].unique()).index(default_year)

year = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    index=default_year_index,
    key=30
)

#IMPORT DATA
df_selection = df.query("Year == @year")

# Force lat/long to numeric, turn '#VALUE!' into NaN
df_selection["Latitude"] = pd.to_numeric(df_selection["Latitude"], errors="coerce")
df_selection["Longitude"] = pd.to_numeric(df_selection["Longitude"], errors="coerce")

# Now drop invalid rows
df_selection = df_selection.dropna(subset=["Latitude", "Longitude", "total"])

# Extract centroids for each geometry in OSBoundaries
OSBoundaries['centroid'] = OSBoundaries.geometry.centroid
OSBoundaries['Latitude'] = OSBoundaries.centroid.y
OSBoundaries['Longitude'] = OSBoundaries.centroid.x

# Convert centroids to a DataFrame
boundary_centroid_data = OSBoundaries[['OS_Name', 'Latitude', 'Longitude']]

# Convert GeoDataFrame to GeoJSON
material_geojson = json.loads(OSMaterial.to_crs(epsg=4326).to_json())

fig = px.scatter_mapbox(
    df_selection,
    lat="Latitude",
    lon="Longitude",
    size="total",
    size_max=25,
    color="total",
    color_continuous_scale=["red", "green"],  # <-- fixed red
    hover_name="SID",
    hover_data={"total": True, "Material":True, "Material_Age":True},
    zoom=11,
    center={"lat": 35.05, "lon": -76.4},
)

# Use free MapLibre tiles
fig.update_layout(
    mapbox_style="open-street-map",
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Add material polygons
fig.update_layout(
    mapbox_layers=[
        {
            "source": material_geojson,
            "type": "fill",
            "color": "orange",
            "opacity": 0.4
        }
    ]
)

st.plotly_chart(fig, use_container_width=True)




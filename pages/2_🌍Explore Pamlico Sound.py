import streamlit as st
import pandas as pd
import pydeck as pdk
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
text.display_text("As of 2025, North Carolina has 17 oyster sanctuaries in Pamlico Sound, totaling to 789 acres of permited, protected subtidal habitat. Every year NCDMF's Habitat & Enhancement dive team visits each sanctuary to collect oyster data around the reefs. Explore the map to see how oyster densities differ across Pamlico Sound over the last few years.")

with st.expander("Instructions"):
    st.info("""
             **Click and drag the map to explore Pamlico Sound. Use the scroll-wheel to zoom in and out.**

              **Hold the right mouse button to rotate the map.** 

             **The red bars show where our dive team has sampled at each sanctuary. Hover over one to see the observed oyster density.**

             **Select a year from the drop down menu in the sidebar to see how densities change over time.** 
    """)

#SIDEBAR SETUP
st.sidebar.subheader("Use the dropdown to select a year and explore oyster densities across the Oyster Sanctuary Network")
default_year = 2024
default_year_index = list(df["Year"].unique()).index(default_year)

year = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    index=default_year_index,
    key=30
)

#IMPORT DATA
df_selection = df.query("Year == @year")

# Remove rows with missing values in 'Latitude', 'Longitude', 'total'
df_selection = df_selection.dropna(subset=['Latitude', 'Longitude', 'total'])

# Extract centroids for each geometry in OSBoundaries
OSBoundaries['centroid'] = OSBoundaries.geometry.centroid
OSBoundaries['Latitude'] = OSBoundaries.centroid.y
OSBoundaries['Longitude'] = OSBoundaries.centroid.x

# Convert centroids to a DataFrame
boundary_centroid_data = OSBoundaries[['OS_Name', 'Latitude', 'Longitude']]

# Convert GeoDataFrame to GeoJSON dictionary
geojson_dict = OSMaterial.to_crs(epsg=4326).__geo_interface__

# Define layers
# TextLayer with positions of each geometry's centroid
text_layer = pdk.Layer(
    "TextLayer",
    data=boundary_centroid_data,
    get_position=["Longitude", "Latitude"],
    get_text="OS_Name",
    get_color=[0, 0, 0, 255],
    get_size=20,
    get_alignment_baseline="'top'",
)

# Material layer
material_layer = pdk.Layer(
    "GeoJsonLayer",
    data=geojson_dict,  
    get_fill_color=[255, 0, 0, 150],
    pickable=True,
)

max_total = df_selection['total'].max()

density_layer = pdk.Layer(
    "ColumnLayer",
    data=df_selection,
    get_position=["Longitude", "Latitude"],
    get_elevation="total",
    radius=8,
    elevation_scale=1,
    get_fill_color=[255, 0, 0, 150],
    pickable=True,
    auto_highlight=True,
)

tooltip = {
    "html": "<b>Oysters/m²:</b> {total}",
    "style": {
        "backgroundColor": "steelblue",
        "color": "white"
    }
}

# Display map
st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/outdoors-v9",
        initial_view_state={
            "latitude": 35.05,
            "longitude": -76.4,
            "zoom": 11.2,
            "pitch": 60,
        },
        layers=[text_layer, density_layer, material_layer],
        tooltip=tooltip  # Add the tooltip configuration
    ), use_container_width=True
)


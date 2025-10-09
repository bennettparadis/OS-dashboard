import streamlit as st
import pandas as pd
import pydeck as pdk
import geopandas as gpd

# Load raw data (cached)
@st.cache_data
def load_data():
    df = pd.read_csv("data/2019-2025_oyster_densities.csv")
    OSMaterial = gpd.read_file("data/OS_material_storymap.shp").to_crs(epsg=4326)
    OSBoundaries = gpd.read_file("data/permit_boundaries.shp")
    return df, OSMaterial, OSBoundaries

df, OSMaterial, OSBoundaries = load_data()

# Sidebar year selection
years = sorted(df["Year"].unique())
selected_year = st.sidebar.selectbox("Select Year", years, index=years.index(2024))

# Filter data once
df_selected = df.query("Year == @selected_year").dropna(subset=["Latitude","Longitude","total"])

# Precompute centroids
centroids = OSBoundaries.geometry.centroid
boundary_centroid_data = pd.DataFrame({
    "OS_Name": OSBoundaries["OS_Name"],
    "Latitude": centroids.y,
    "Longitude": centroids.x
})

# Convert GeoDataFrame to GeoJSON dict once
geojson_dict = OSMaterial.__geo_interface__

# Build layers in-place
text_layer = pdk.Layer(
    "TextLayer",
    data=boundary_centroid_data,
    get_position=["Longitude", "Latitude"],
    get_text="OS_Name",
    get_color=[0,0,0,255],
    get_size=20,
    get_alignment_baseline="'top'"
)

material_layer = pdk.Layer(
    "GeoJsonLayer",
    data=geojson_dict,
    get_fill_color=[255,0,0,150],
    pickable=True
)

density_layer = pdk.Layer(
    "ColumnLayer",
    data=df_selected,
    get_position=["Longitude","Latitude"],
    get_elevation="total",
    radius=8,
    elevation_scale=1,
    get_fill_color=[255,0,0,150],
    pickable=True,
    auto_highlight=True
)

deck = pdk.Deck(
    map_style="mapbox://styles/mapbox/outdoors-v9",
    initial_view_state={"latitude":35.05,"longitude":-76.4,"zoom":11.2,"pitch":60},
    layers=[text_layer,density_layer,material_layer],
    tooltip={"html":"<b>Oysters/m²:</b> {total}", "style":{"backgroundColor":"steelblue","color":"white"}}
)

st.pydeck_chart(deck, use_container_width=True)

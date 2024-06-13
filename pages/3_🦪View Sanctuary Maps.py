import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import geopandas as gpd
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Tab display 
st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

#IMPORT OS DATA (densities and extraction samples)
OSMaterial = gpd.read_file("C:/Users/bparadis/Documents/Python Scripts/dashboard/OS_material_storymap.shp")
df = pd.read_csv("C:/Users/bparadis/Documents/Python Scripts/dashboard/2019-2023_oyster_densities.csv")


#Sanctuary dictionary will relevant information
OS_dict = {
    'Croatan Sound': {
        'permit': 7.7, 
        'developed':7.7,
        'aggregate': '2,093',
        'established':1996,
        'recent':2013,
        'materials': ['Marl', 'Reef Ball', 'Shell']
    },
    'Deep Bay': {
        'permit': 17.2, 
        'developed':7.73,
        'aggregate': '1,749',
        'established':1996,
        'recent':2014,
        'materials':['Marl', 'Reef Ball', 'Shell']
    },
    'West Bay': {
        'permit': 6.6, 
        'developed':6.6,
        'aggregate': '2,329',
        'established':1996,
        'recent':2014,
        'materials':['Marl', 'Reef Ball', 'Shell']
    },
    'Crab Hole': {
        'permit': 30.5, 
        'developed':30.5,
        'aggregate': '36,489',
        'established':2003,
        'recent':2009,
        'materials':['Marl']
    },
    'Middle Bay': {
        'permit': 4.6, 
        'developed':4.6,
        'aggregate': '900',
        'established':2004,
        'recent':2004,
        'materials':['Marl']
    },
    'Neuse River': {
        'permit': 11.2, 
        'developed':11.2,
        'aggregate': '7,357',
        'established':2005,
        'recent':2008,
        'materials':['Marl']
    },
    'West Bluff': {
        'permit': 29.42, 
        'developed':10.0,
        'aggregate': '10,162',
        'established':2005,
        'recent':2013,
        'materials':['Marl', 'Reef Ball']
    },
    'Gibbs Shoal': {
        'permit': 54.7, 
        'developed':54.7,
        'aggregate': '22,447',
        'established':2009,
        'recent':2013,
        'materials':['Marl', 'Reef Ball']
    },
    'Long Shoal': {
        'permit': 10.0, 
        'developed':6.8,
        'aggregate': 'N/A (1,035 Reef Balls)',
        'established':2013,
        'recent':2013,
        'materials':['Reef Ball']
    },
    'Raccoon Island': {
        'permit': 10.0, 
        'developed':10.0,
        'aggregate': '1,824',
        'established':2013,
        'recent':2016,
        'materials':['Crushed Concrete', 'Consolidated Concrete', 'Reef Ball']
    },
    'Pea Island': {
        'permit': 46.4, 
        'developed':33.9,
        'aggregate': '3,420',
        'established':2015,
        'recent':2015,
        'materials':['Crushed Concrete', 'Consolidated Concrete', 'Reef Ball']
    },
    'Little Creek': {
        'permit': 20.7, 
        'developed':20.7,
        'aggregate': '5,700',
        'established':2016,
        'recent':2016,
        'materials':['Crushed Concrete', 'Consolidated Concrete', 'Reef Ball', 'Granite', 'Marl', 'Reef Ball']
    },
    'Swan Island': {
        'permit': 80.3, 
        'developed':62.6,
        'aggregate': '55,000',
        'established':2017,
        'recent':2021,
        'materials':['Granite', 'Marl']
    },
    'Cedar Island': {
        'permit': 75.0, 
        'developed':70.3,
        'aggregate': '51,800',
        'established':2021,
        'recent':2023,
        'materials':['Crushed Concrete', 'Marl']
    }
}

# --- HEADER & INFO TEXT ---
st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:50px; font-weight: bold;">🦪View Oyster Sanctuary Maps</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:20px;">North Carolina's Division of Marine Fisheries began the Oyster Sanctuary Program to create protected artificial reefs in an effort to restore the state's subtidal oyster population. Today, there are 15 oyster sanctuaries spanning 566 acres of protected subtidal habitat in Pamlico Sound. Each year, biologists conduct SCUBA surveys to collect oyster data on the performance of each sanctuary and the various materials used. Here you can explore the Oyster Sanctuary Program's extensive dataset!</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown("---")

# ----- SIDE BAR -----
sanctuary_names = sorted(df["OS_Name"].unique())
default_sanctuary1 = "Neuse River"

default_sanctuary_index1 = list(df["OS_Name"].unique()).index(default_sanctuary1)


st.sidebar.subheader("Use the filters to explore the different material footprints at each Sanctuary!")
st.sidebar.header("Select Filters:")

sanctuary1 = st.sidebar.selectbox(
    "Select an Oyster Sanctuary:",
    sanctuary_names,
    index=default_sanctuary_index1,
    key=11
)

# Filter the GeoDataFrame based on the selected sanctuary
filtered_material1 = OSMaterial[OSMaterial['OS_Site'] == sanctuary1]

# Configure map settings
# OS Map Zoom Dictionary
zoom_dict = {
    "West Bay": 17.5, "Swan Island": 15.5, "Croatan Sound": 17, "Deep Bay": 17, "Crab Hole": 16,
    "Middle Bay": 18.6, "Neuse River": 17.2, "West Bluff": 16.8, "Gibbs Shoal": 16.2, "Long Shoal": 16,
    "Raccoon Island": 17, "Pea Island": 16.2, "Little Creek": 16.8, "Cedar Island": 15.8
}


# Define the color mapping dictionary
color_scale = px.colors.qualitative.G10
unique_materials = df['Material'].unique()
color_discrete_map = {material: color_scale[i % len(color_scale)] for i, material in enumerate(unique_materials)}
transparency_value = 0.7



#MAP 1
st.subheader(f"Map of {sanctuary1}")
if not filtered_material1.empty:
    # Reproject the GeoDataFrame to WGS84 (EPSG:4326) if necessary
    if filtered_material1.crs != 'EPSG:4326':
        filtered_material1 = filtered_material1.to_crs(epsg=4326)

    # Convert GeoDataFrame to GeoJSON
    geojson1 = filtered_material1.__geo_interface__

    hover_columns = ["REEF_SITE", "OS_Site", "Material", "DeployYear", "DeployMont", "AREA_SQFT", "Latitude", "Longitude"]

    # Create a Plotly map
    fig1 = px.choropleth_mapbox(
        filtered_material1,
        geojson=geojson1,
        locations=filtered_material1.index,
        color="Material",
        color_discrete_map=color_discrete_map,
        mapbox_style="carto-positron",
        center={"lat": filtered_material1.geometry.centroid.y.mean(), "lon": filtered_material1.geometry.centroid.x.mean()},
        zoom=zoom_dict[sanctuary1],
        opacity=transparency_value,
        height=900,
        width=1200,
        hover_data=hover_columns
        #title=f"Map of {sanctuary1}"
    )

    st.plotly_chart(fig1)
else:
    st.warning("No map data available for the selected sanctuary.")


    #SANCTUARY SITE 1 INFORMATION
    st.subheader("Site Info")
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Permit Acreage: {OS_dict[sanctuary1]["permit"]} acres</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Developed Habitat: {OS_dict[sanctuary1]["developed"]} acres</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Year Established: {OS_dict[sanctuary1]["established"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Most Recent Addition: {OS_dict[sanctuary1]["recent"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Total Aggregate Rock: {OS_dict[sanctuary1]["aggregate"]} tons</p>', unsafe_allow_html=True)
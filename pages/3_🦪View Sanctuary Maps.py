import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import geopandas as gpd
import warnings
from utils import maps
from utils import text

# Suppress warnings
warnings.filterwarnings('ignore')

#PAGE SETUP
text.tab_display()

# --- HEADER & INFO TEXT ---
text.display_text("🦪View Oyster Sanctuary Maps", font_size=50, font_weight='bold')
text.pages_font()
text.display_text("Noth Carolina's oyster sanctuaries are large-scale restoration sites ranging from 4 to 80 acres. The sanctuaries have been built with a variety of materials such as crushed aggregate rock (marl limestone, granite, concrete, basalt), reef balls, concrete pipe, and recycled shell. Select an oyster sanctuary to view the material blueprint.")

with st.expander("Instructions"):
    st.info(
    """
    **Select an oyster sanctuary from the dropdown menu on the left to see the site information and map.**
     
    **Use the scroll-wheel to zoom in and out on the map.** 
    
    **Hover your cursor over the different polygons to see the material type, coordinates, deployment date, and area.**
    
    *NOTE: This geospatial data includes all materials deployed between 1996 and 2023. 
    """
    )

#IMPORT OS DATA (densities and extraction samples)
OSMaterial = gpd.read_file("data/OS_material_storymap.shp")
df = pd.read_csv("data/2019-2023_oyster_densities.csv")

# ----- SIDE BAR -----
sanctuary_names = sorted(df["OS_Name"].unique())
default_sanctuary1 = "Little Creek"

default_sanctuary_index1 = sorted(df["OS_Name"].unique()).index(default_sanctuary1)


st.sidebar.subheader("Choose an oyster sanctuary in the drop down to explore the different material footprints and layouts!")
#st.sidebar.header("Select Filters:")

sanctuary1 = st.sidebar.selectbox(
    "Select an Oyster Sanctuary:",
    sanctuary_names,
    index=default_sanctuary_index1,
    key=11
)

# Filter the GeoDataFrame based on the selected sanctuary
filtered_material1 = OSMaterial[OSMaterial['OS_Site'] == sanctuary1]

col1, col2 = st.columns([10,5])

with col1:
    #MAP
    maps.display_map(sanctuary1, filtered_material1, 600, 600)

with col2:
    #SANCTUARY SITE INFORMATION
    maps.site_info(sanctuary1)

    st.info("""
    *Permit acreage is the boundary area delineated as protected habitat under NC law
    
    *Developed habitat is the area covered by material and the space between mounds/ridges  
""")

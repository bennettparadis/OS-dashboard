import streamlit as st
import pandas as pd
import plotly.express as px
import json
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






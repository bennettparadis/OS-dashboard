import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import geopandas as gpd
import warnings
from utils import maps
from utils import densityhistograms
from utils import text

# Suppress warnings
warnings.filterwarnings('ignore')

# Tab display 
st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

#IMPORT OS DATA (densities and extraction samples)
df = pd.read_csv("data/2019-2023_oyster_densities.csv")
histdata = pd.read_csv("data/OSdata_extractions.csv")
OSMaterial = gpd.read_file("data/OS_material_storymap.shp")

# --- MAINPAGE ---
text.display_text("📊Compare Population Data", font_size=50, font_weight='bold')
text.display_text("The annual dive surveys provide snapshots of the oyster populations at each sanctuary. From those data we can estimate densities and visualize population structures. We can compare how these metrics change over time and how they vary by each material. Try it out and make some comparisons of your own!")

with st.expander("Instructions"):
        st.info("""
            **Use the filters in the sidebar to see how density estimates and population structures change between sanctuaries, materials, and from year to year.** 
            
            **The histogram below shows the frequency of each size class. Spat are 'baby' oysters (<26mm). Legal oysters are market sized (>75mm). Sublegal is everything in between.** 
                    
            **Below the histograms you can also see a map & site info for additional comparisons.**
        
            Want some examples? Try comparing **Swan Island** in **2022 & 2023**! Take it another step and choose **Swan Island 2023** for both selections, but compare **granite** & **marl**. How do the years and materials compare?
        """)

# ----- SIDE BAR -----
text.pages_font()

sanctuary_names = sorted(df["OS_Name"].unique())
default_year = 2023
default_sanctuary1 = "Neuse River"
default_sanctuary2 = "Middle Bay"

default_year_index = list(df["Year"].unique()).index(default_year)
default_sanctuary_index1 = list(df["OS_Name"].unique()).index(default_sanctuary1)
default_sanctuary_index2 = list(df["OS_Name"].unique()).index(default_sanctuary2)


st.sidebar.subheader("Use the filters on the left to make comparisons between sanctuaries, materials, and years!")
st.sidebar.header("Selection 1:")
year1 = st.sidebar.select_slider(
    "Select a Year:", 
    df["Year"].unique(),
    value=default_year,
    key=10
)

sanctuary1 = st.sidebar.selectbox(
    "Select an Oyster Sanctuary:",
    sanctuary_names,
    index=default_sanctuary_index1,
    key=11
)

materials1 = maps.OS_dict.get(sanctuary1, {}).get('materials', df["Material"].unique())
material_type1 = st.sidebar.multiselect(
    "Select a Material Type:",
    options=materials1,
    default=materials1,
    key=12
)

df_selection1 = df.query(
    "Year == @year1 & OS_Name == @sanctuary1 & Material == @material_type1"
)

hist_selection1 = histdata.query(
    "Year == @year1 & OS_Name ==@sanctuary1 & Material == @material_type1"
)

st.sidebar.header("Selection 2:")
year2 = st.sidebar.select_slider(
    "Select a Year:", 
    df["Year"].unique(),
    value=default_year,
    key=20
)

sanctuary2 = st.sidebar.selectbox(
    "Select an Oyster Sanctuary:",
    sanctuary_names,
    index=default_sanctuary_index2,
    key=21
)

materials2 = maps.OS_dict.get(sanctuary2, {}).get('materials', df["Material"].unique())
material_type2 = st.sidebar.multiselect(
    "Select a Material Type:",
    options=materials2,
    default=materials2,
    key=22
)

df_selection2 = df.query(
    "Year == @year2 & OS_Name == @sanctuary2 & Material == @material_type2"
)

hist_selection2 = histdata.query(
    "Year == @year2 & OS_Name ==@sanctuary2 & Material == @material_type2"
)

# Filter the GeoDataFrame based on the selected sanctuary
filtered_material1 = OSMaterial[OSMaterial['OS_Site'] == sanctuary1]
filtered_material2 = OSMaterial[OSMaterial['OS_Site'] == sanctuary2]

#DATAFRAME FORMATTING -- establish y-axis limit with histograms; logic of max_y_value(1 & 2) is so that the plots have the same limits
max_y_value = 0
max_y_value1 = 0
max_y_value2 = 0

histogram_df1 = None
histogram_df2 = None

if not hist_selection1.empty:
    bins = np.arange(1, hist_selection1['LVL'].max()+ 6, 5)
    labels = [f'{bins[i]}-{bins[i+1]-1}' for i in range(len(bins) -1 )]
    binned_data = pd.cut(hist_selection1['LVL'], bins = bins, labels = labels, right = False)
    counts = binned_data.value_counts().sort_index()
    
    quad_count = hist_selection1['Site'].nunique()
    standardized_counts = (counts / quad_count) *4

    histogram_df1 = pd.DataFrame({
        'Level Valve Length (mm)' : standardized_counts.index,
        'Frequency (oysters/m²)' : standardized_counts.values
    })
    max_y_value1 = standardized_counts.max()*1.2

if not hist_selection2.empty:
    bins2 = np.arange(1, hist_selection2['LVL'].max()+ 6, 5)
    labels2 = [f'{bins2[i]}-{bins2[i+1]-1}' for i in range(len(bins2) -1 )]
    binned_data2 = pd.cut(hist_selection2['LVL'], bins = bins2, labels = labels2, right = False)
    counts2 = binned_data2.value_counts().sort_index()
    
    quad_count2 = hist_selection2['Site'].nunique()
    standardized_counts2 = (counts2 / quad_count2) *4

    histogram_df2 = pd.DataFrame({
        'Level Valve Length (mm)' : standardized_counts2.index,
        'Frequency (oysters/m²)' : standardized_counts2.values
    })
    max_y_value2 = standardized_counts2.max()*1.2

max_y_value = max(max_y_value1, max_y_value2)

#SET UP COLUMNS W/ DATA
col1, col2, col3 = st.columns([10,0.5,10])

#SELECTION 1 COLUMN
with col1:
    st.header(f"{sanctuary1} ({year1})")
    
    # DENSITY METRICS FOR SELECTION 1
    densityhistograms.density_calc(df_selection1)

    #HISTOGRAM 1
    densityhistograms.make_histogram(df_selection1, histogram_df1, max_y_value)

    #SANCTUARY SITE 1 INFORMATION
    maps.site_info(sanctuary1)
    
    #MAP 1
    maps.display_map(sanctuary1, filtered_material1, 500, 450)
   

with col2:
    st.html(
        '''
                <div class="divider-vertical-line"></div>
                <style>
                    .divider-vertical-line {
                        border-left: 2px solid rgba(176, 206, 218);
                        height: 1800px;
                        margin: auto;
                    }
                </style>
            '''
    )

#SELECTION 2 COLUMN
with col3:
    st.header(f"{sanctuary2} ({year2})")
    
    # DENSITY METRICS FOR SELECTION 2
    densityhistograms.density_calc(df_selection2)

    #HISTOGRAM 2
    densityhistograms.make_histogram(df_selection2, histogram_df2, max_y_value)

    #SANCTUARY SITE 2 INFORMATION
    maps.site_info(sanctuary2)
    
    #MAP 2
    maps.display_map(sanctuary2, filtered_material2, 500, 450)

import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import geopandas as gpd
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

#IMPORT OS DATA (densities and extraction samples)
df = pd.read_csv("C:/Users/bparadis/Documents/Python Scripts/dashboard/2019-2023_oyster_densities.csv")
histdata = pd.read_csv("C:/Users/bparadis/Documents/Python Scripts/dashboard/OSdata_extractions.csv")

try:
    OSMaterial = gpd.read_file("C:/Users/bparadis/Documents/Python Scripts/dashboard/OS_material_storymap.shp")
except Exception as e:
    st.error(f"Error loading shapefile: {e}")
    st.stop()


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

# ----- SIDE BAR -----
sanctuary_names = sorted(df["OS_Name"].unique())
default_year = 2023
default_sanctuary1 = "Neuse River"
default_sanctuary2 = "Middle Bay"

default_year_index = list(df["Year"].unique()).index(default_year)
default_sanctuary_index1 = list(df["OS_Name"].unique()).index(default_sanctuary1)
default_sanctuary_index2 = list(df["OS_Name"].unique()).index(default_sanctuary2)

st.sidebar.subheader("Use the filters to explore and make comparisons between sanctuaries, materials, and years!")
st.sidebar.header("Select Filters:")
year1 = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    index=default_year_index,
    key=10
)

sanctuary1 = st.sidebar.selectbox(
    "Select an Oyster Sanctuary:",
    sanctuary_names,
    index=default_sanctuary_index1,
    key=11
)

materials1 = OS_dict.get(sanctuary1, {}).get('materials', df["Material"].unique())
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

year2 = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    index=default_year_index,
    key=20
)

sanctuary2 = st.sidebar.selectbox(
    "Select an Oyster Sanctuary:",
    sanctuary_names,
    index=default_sanctuary_index2,
    key=21
)

materials2 = OS_dict.get(sanctuary2, {}).get('materials', df["Material"].unique())
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

# --- MAINPAGE ---
st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:60px; font-weight: bold;">🦪 Oyster Sanctuary Dashboard 📊</p>
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

# Filter the GeoDataFrame based on the selected sanctuary
filtered_material1 = OSMaterial[OSMaterial['OS_Site'] == sanctuary1]
filtered_material2 = OSMaterial[OSMaterial['OS_Site'] == sanctuary2]

# Configure map settings
# OS Map Zoom Dictionary
zoom_dict = {
    "West Bay": 17.5, "Swan Island": 15.5, "Croatan Sound": 17, "Deep Bay": 17, "Crab Hole": 16,
    "Middle Bay": 18.6, "Neuse River": 17.2, "West Bluff": 16.8, "Gibbs Shoal": 16.2, "Long Shoal": 16,
    "Raccoon Island": 17, "Pea Island": 16.2, "Little Creek": 16.8, "Cedar Island": 15.8
}

#Label/units variable
oysters_per_sq_meter = "oysters/m²"

# Define the color mapping dictionary
color_scale = px.colors.qualitative.G10
unique_materials = df['Material'].unique()
color_discrete_map = {material: color_scale[i % len(color_scale)] for i, material in enumerate(unique_materials)}
transparency_value = 0.7


#DATAFRAME FORMATTING -- also establish y-axis limit with histograms; logic of max_y_value(1/2) is so that the plots have the same limits
max_y_value = 0
max_y_value1 = 0
max_y_value2 = 0

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

if max_y_value1 >= max_y_value2:
    max_y_value = max_y_value1
else:
    max_y_value = max_y_value2


#SET UP COLUMNS W/ DATA
col1, col2 = st.columns(2)

#SELECTION 1 COLUMN
with col1:
    st.header(f"{sanctuary1} ({year1})")

    # DENSITY METRICS FOR SELECTION 1
    st.subheader("Density Metrics")
    
    if df_selection1["total"].isnull().all():
        st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Total Oyster Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
    else:
        total_density1 = int(df_selection1["total"].mean())
        st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Total Oyster Density: {total_density1:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)
    
    if df_selection1["legal"].isnull().all():
        st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Legal Oyster Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
    else:
        legal_density1 = int(df_selection1["legal"].mean())
        st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Legal Oyster Density: {legal_density1:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)
    
    if df_selection1["sublegal"].isnull().all():
        st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Sublegal Oyster Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
    else:
        sublegal_density1 = int(df_selection1["sublegal"].mean())
        st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Sublegal Oyster Density: {sublegal_density1:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)

    if df_selection1["spat"].isnull().all():
        st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Spat Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
    else:
        spat_density1 = int(df_selection1["spat"].mean())
        st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Spat Density: {spat_density1:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)


    #HISTOGRAM 1
    st.subheader("Population Structure")

    if not hist_selection1.empty:
        # bins = np.arange(1, hist_selection1['LVL'].max()+ 6, 5)
        # labels = [f'{bins[i]}-{bins[i+1]-1}' for i in range(len(bins) -1 )]
        # binned_data = pd.cut(hist_selection1['LVL'], bins = bins, labels = labels, right = False)
        # counts = binned_data.value_counts().sort_index()
        
        # quad_count = hist_selection1['Site'].nunique()
        # standardized_counts = (counts / quad_count) *4

        # histogram_df1 = pd.DataFrame({
        #     'Level Valve Length (mm)' : standardized_counts.index,
        #     'Frequency (oysters/m²)' : standardized_counts.values
        # })

        # max_y_value = standardized_counts.max()*1.2

        hist_plot1 = px.bar(
            histogram_df1, 
            x= 'Level Valve Length (mm)', 
            y='Frequency (oysters/m²)', 
            color_discrete_sequence=['orange'],
            width=600,
            height=500)
        
        hist_plot1.update_traces(
            marker=dict(line=dict(color= 'black', width=1)), 
            selector=dict(type='bar'),
            hoverlabel=dict(bgcolor='white', font=dict(color='black', size =16))
        )
        
        hist_plot1.update_layout(
            paper_bgcolor = '#D6F2F4', 
            plot_bgcolor='#D6F2F4',
            bargap=0, 
            yaxis_range=[0,max_y_value],
            font=dict(color='black'),
            xaxis=dict(
                title=dict(text='Level Valve Length (mm)', font=dict(color='black', size =22)),
                tickfont=dict(color='black')
            ),
            yaxis=dict(
                title=dict(text='Frequency (oysters/m²)', font=dict(color='black', size =22)),
                tickfont=dict(color='black')
            )
        )

        hist_plot1.add_vline(x=4.5, line=dict(color='red', width=3, dash='dash'))
        hist_plot1.add_vline(x=14.5, line=dict(color='red', width=3, dash='dash'))

        hist_plot1.add_annotation(
            x = 2,
            y=max_y_value,
            text="Spat",
            showarrow=False,
            font=dict(color='black', size=14),
            xref="x",
            yref="y"
        )

        hist_plot1.add_annotation(
            x = 9,
            y=max_y_value,
            text="Sublegal",
            showarrow=False,
            font=dict(color='black', size=14),
            xref="x",
            yref="y"
        )

        hist_plot1.add_annotation(
            x = 19.5,
            y=max_y_value,
            text="Legal",
            showarrow=False,
            font=dict(color='black', size=14),
            xref="x",
            yref="y"
        )

        st.plotly_chart(hist_plot1, use_container_width=False)
    
    else:
        st.warning("No population data available.")


    #MAP 1
    st.subheader(f"Map of {sanctuary1}")
    if not filtered_material1.empty:
        # Reproject the GeoDataFrame to WGS84 (EPSG:4326) if necessary
        if filtered_material1.crs != 'EPSG:4326':
            filtered_material1 = filtered_material1.to_crs(epsg=4326)

        # Convert GeoDataFrame to GeoJSON
        geojson1 = filtered_material1.__geo_interface__

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
            height=650,
            width=650,
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


#SELECTION 2 COLUMN
with col2:
    st.header(f"{sanctuary2} ({year2})")

    # DENSITY METRICS FOR SELECTION 2
    st.subheader("Density Metrics")
    oysters_per_sq_meter = "oysters/m²"
    
    if df_selection2["total"].isnull().all():
        st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Total Oyster Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
    else:
        total_density2 = int(df_selection2["total"].mean())
        st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Total Oyster Density: {total_density2:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)
    
    if df_selection2["legal"].isnull().all():
        st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Legal Oyster Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
    else:
        legal_density2 = int(df_selection2["legal"].mean())
        st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Legal Oyster Density: {legal_density2:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)
    
    if df_selection2["sublegal"].isnull().all():
        st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Sublegal Oyster Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
    else:
        sublegal_density2 = int(df_selection2["sublegal"].mean())
        st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Sublegal Oyster Density: {sublegal_density2:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)

    if df_selection2["spat"].isnull().all():
        st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Spat Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
    else:
        spat_density2 = int(df_selection2["spat"].mean())
        st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Spat Density: {spat_density2:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)



    #HISTOGRAM 2
    st.subheader("Population Structure")

    if not hist_selection2.empty:
        # bins2 = np.arange(1, hist_selection2['LVL'].max()+ 6, 5)
        # labels2 = [f'{bins2[i]}-{bins2[i+1]-1}' for i in range(len(bins2) -1 )]
        # binned_data2 = pd.cut(hist_selection2['LVL'], bins = bins2, labels = labels2, right = False)
        # counts2 = binned_data2.value_counts().sort_index()
        
        # quad_count2 = hist_selection2['Site'].nunique()
        # standardized_counts2 = (counts2 / quad_count2) *4

        # histogram_df2 = pd.DataFrame({
        #     'Level Valve Length (mm)' : standardized_counts2.index,
        #     'Frequency (oysters/m²)' : standardized_counts2.values
        # })

        hist_plot2 = px.bar(
            histogram_df2, 
            x= 'Level Valve Length (mm)', 
            y='Frequency (oysters/m²)', 
            color_discrete_sequence=['orange'],
            width=600,
            height=500
            )
        
        hist_plot2.update_traces(
            marker=dict(line=dict(color= 'black', width=1)), 
            selector=dict(type='bar'),
            hoverlabel=dict(bgcolor='white', font=dict(color='black', size =16))
        )
        
        # max_y_value2 = standardized_counts2.max()*1.2
        
        hist_plot2.update_layout(
            paper_bgcolor = '#D6F2F4', 
            plot_bgcolor='#D6F2F4',
            bargap=0, 
            yaxis_range=[0,max_y_value],
            font=dict(color='black'),
            xaxis=dict(
                title=dict(text='Level Valve Length (mm)', font=dict(color='black', size =22)),
                tickfont=dict(color='black')
            ),
            yaxis=dict(
                title=dict(text='Frequency (oysters/m²)', font=dict(color='black', size =22)),
                tickfont=dict(color='black')
            )
        )

        hist_plot2.add_vline(x=4.5, line=dict(color='red', width=3, dash='dash'))
        hist_plot2.add_vline(x=14.5, line=dict(color='red', width=3, dash='dash'))

        hist_plot2.add_annotation(
            x = 2,
            y=max_y_value,
            text="Spat",
            showarrow=False,
            font=dict(color='black', size=14),
            xref="x",
            yref="y"
        )

        hist_plot2.add_annotation(
            x = 9,
            y=max_y_value,
            text="Sublegal",
            showarrow=False,
            font=dict(color='black', size=14),
            xref="x",
            yref="y"
        )

        hist_plot2.add_annotation(
            x = 19.5,
            y=max_y_value,
            text="Legal",
            showarrow=False,
            font=dict(color='black', size=14),
            xref="x",
            yref="y"
        )

        st.plotly_chart(hist_plot2, use_container_width=False)
    
    else:
        st.warning("No population data available.")

    #MAP 2
    st.subheader(f"Map of {sanctuary2}")
    if not filtered_material2.empty:
        # Reproject the GeoDataFrame to WGS84 (EPSG:4326) if necessary
        if filtered_material2.crs != 'EPSG:4326':
            filtered_material2 = filtered_material2.to_crs(epsg=4326)

        # Convert GeoDataFrame to GeoJSON
        geojson2 = filtered_material2.__geo_interface__

        # Create a Plotly map
        fig2 = px.choropleth_mapbox(
            filtered_material2,
            geojson=geojson2,
            locations=filtered_material2.index,
            color="Material",
            color_discrete_map=color_discrete_map,
            mapbox_style="carto-positron",
            center={"lat": filtered_material2.geometry.centroid.y.mean(), "lon": filtered_material2.geometry.centroid.x.mean()},
            zoom=zoom_dict[sanctuary2],
            opacity=transparency_value,
            height=650,
            width=680,
            #title=f"Map of {sanctuary2}"
        )

        st.plotly_chart(fig2)
    else:
        st.warning("No map data available for the selected sanctuary.")


    #SANCTUARY SITE 2 INFORMATION
    st.subheader("Site Info")
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Permit Acreage: {OS_dict[sanctuary2]["permit"]} acres</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Developed Habitat: {OS_dict[sanctuary2]["developed"]} acres</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Year Established: {OS_dict[sanctuary2]["established"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Most Recent Addition: {OS_dict[sanctuary2]["recent"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Total Aggregate Rock: {OS_dict[sanctuary2]["aggregate"]} tons</p>', unsafe_allow_html=True)

st.markdown("---")

#st.dataframe(df_selection1)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

# Tab display 
st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

# --- HEADER & INFO TEXT ---
st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:50px; font-weight: bold;">🤿Analyze Reef Materials</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Define the custom CSS for sidebar pages
custom_css = """
<style>
    /* Change the color and font of the page titles in the sidebar */
    .eczjsme13 {
        color: #00647B !important; /* Replace with your desired color */
        font-weight: bold !important;
        font-size: 16px !important;
    }
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)


st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:20px;">North Carolina's oldest oyster sanctuaries are nearly 30 years old. With a variety of materials used to build the sanctuaries, knowing how these materials persist over time is important for future oyster restoration efforts. Here you can analyze the relationship of material age and oyster density using a scatterplot and a boxplot.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.info("""
    **Analyze the past five years of oyster monitoring data by using the sidebar to set filters and interact with the graphs below.** 
""")

with st.expander("Scatterplot Instructions"):
    st.info("""
            **Each point is a density estimate collected during Sanctuary sampling. Hover over each sample to view the observed oyster density, material type & age, and collection date.**
            
            **Remove materials from your analysis by clicking on them in the legend. Double click a material to isolate it. Double click the legend again to reset the plot.**

            **Draw a square on the plot to zoom in on a particular set of data points. Double click to reset the plot.** 

            **Choose to view the densities for all oysters, or only legal, sublegal, spat, or non-spat (legal + sublegal).**
""")

df = pd.read_csv("data/2019-2023_oyster_densities.csv")

# Sidebar filters
st.sidebar.header("Select Filters:")

# Multiselect widget for years
years = st.sidebar.multiselect(
    "Filter by Year:", 
    df["Year"].unique().tolist(),  # Convert unique years to list
    default=df["Year"].unique().tolist(),  # Set default to all years
    key=40
)

# Radio button for size class filter
size_selection = st.sidebar.radio(
    "Filter by Size Class:", 
    options=["Total", "Legal", "Sub-Legal", "Spat", "Non-spat"],
    key=41
)

size_select_dict = {
    'Total': 'total',
    'Legal': 'legal',
    'Sub-Legal': 'sublegal',
    'Spat': 'spat',
    'Non-spat' : 'non_spat'
}

sanctuaries = st.sidebar.multiselect(
    "Filter by Sanctuary:", 
    df["OS_Name"].unique().tolist(),  # Convert unique years to list
    default=df["OS_Name"].unique().tolist(),  # Set default to all years
    key=42
)

# Filter dataframe based on selected years and sanctuary
if years:
    df_selection = df[df["Year"].isin(years)]
else:
    df_selection = df

if sanctuaries:
    df_selection = df_selection[df_selection["OS_Name"].isin(sanctuaries)]
else:
    df_selection = df

# Get the appropriate column based on size selection
size_column = size_select_dict[size_selection]

# Calculate Lowess trendline for the selected data
lowess = sm.nonparametric.lowess
trendline = lowess(df_selection[size_column], df_selection['Material_Age'], frac=0.25)

# Create scatter plot
fig1 = px.scatter(df_selection, 
                x='Material_Age', 
                y=size_column, 
                color="Material", 
                color_discrete_map={
                    'Marl':'#636EFA',
                    'Granite':'#EF553B',
                    'Basalt':'#00CC96',
                    'Crushed Concrete': '#AB63FA',
                    'Shell':'#FFA15A',
                    'Reef Ball':'#19D3F3',
                    'Consolidated Concrete':'#FF6692'
                },
                hover_data=['OS_Name', 'Year'],
                size_max=15,  # Set the maximum size of the markers
                height=600,
                width=950)

# Add Lowess trendline to the plot
fig1.add_trace(
    go.Scatter(
        x=trendline[:, 0], 
        y=trendline[:, 1], 
        mode='lines', 
        line=dict(color='black', width=2), 
        name='Lowess Trendline'
    )
)

fig1.update_traces(
    marker=dict(
        size=15,  # Set the size of the markers
        opacity=0.7,  # Adjust the transparency of the markers
        line=dict(color='black', width=1)  # Add a black outline
    ),
    selector=dict(type='scatter'),
    hoverlabel=dict(bgcolor='white', font=dict(color='black', size=16))
)

fig1.update_layout(
    yaxis_range=[-500,4700],
    xaxis_range=[0,30],
    paper_bgcolor='#D6F2F4', 
    plot_bgcolor='white',
    font=dict(color='black', size=18),  # Update general font settings
    xaxis=dict(
        title=dict(text='Material Age (years)', font=dict(color='black', size=22)),
        tickfont=dict(color='black', size=16)  # Update tick font size for x-axis
    ),
    yaxis=dict(
        title=dict(text=f'{size_selection} Oyster Density (per m²)', font=dict(color='black', size=22)),
        tickfont=dict(color='black', size=16)  # Update tick font size for y-axis
    ),
    legend=dict(
                title= dict(
                    text='Material',
                    font= dict(color='black', size=16)
                ),
                font=dict(color='black', size=16),
                orientation="v",
                yanchor='top',
                y=0.95,
                xanchor='right',
                x=0.99,
                bgcolor='rgba(255, 255, 255, 0.6)'
            ),
            margin=dict(l=0, r=0, t=0, b=0)
    )


st.plotly_chart(fig1)


with st.expander("Boxplot Instructions"):
    st.info("""
            **A boxplot can directly compare the efficacy of the various material types used in our oyster restoration efforts.**
            **This plot will also refresh with any filters you select in the sidebar.**

            **This also helps to visualize any statistical outliers. Which materials appear to be best for oysters? What about spat recruitment? Does any particular year show a different trend?**
            """)


fig2 = go.Figure()
fig2 = px.box(df_selection, 
                x='Material', 
                y=size_column, 
                color="Material", 
                color_discrete_map={
                    'Marl':'#636EFA',
                    'Granite':'#EF553B',
                    'Basalt':'#00CC96',
                    'Crushed Concrete': '#AB63FA',
                    'Shell':'#FFA15A',
                    'Reef Ball':'#19D3F3',
                    'Consolidated Concrete':'#FF6692'
                },
                hover_data=['OS_Name', 'Year'],
                height=600,
                width=950)

fig2.update_traces(
    marker=dict(
        size=15,  # Set the size of the markers
        opacity=0.7,  # Adjust the transparency of the markers
        line=dict(color='black', width=1)  # Add a black outline
    ),
    selector=dict(type='box'),
    hoverlabel=dict(bgcolor='white', font=dict(color='black', size=16))
)

fig2.update_layout(
    paper_bgcolor='#D6F2F4', 
    plot_bgcolor='white',
    font=dict(color='black', size=18),  # Update general font settings
    xaxis=dict(
        title=dict(text='Material Age (years)', font=dict(color='black', size=22)),
        tickfont=dict(color='black', size=16)  # Update tick font size for x-axis
    ),
    yaxis=dict(
        title=dict(text=f'{size_selection} Oyster Density (per m²)', font=dict(color='black', size=22)),
        tickfont=dict(color='black', size=16)  # Update tick font size for y-axis
    ),
    legend=dict(
                title= dict(
                    text='Material',
                    font= dict(color='black', size=16)
                ),
                font=dict(color='black', size=16),
                orientation="v",
                yanchor='top',
                y=0.95,
                xanchor='right',
                x=0.99,
                bgcolor='rgba(255, 255, 255, 0.6)'
            ),
            margin=dict(l=0, r=0, t=0, b=0)
    )

st.plotly_chart(fig2)



import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from utils import text

text.tab_display()
text.pages_font()

# --- MAINPAGE ---

text.display_text("🦪 NC's Oyster Sanctuary Data Explorer 📊", font_size=50, font_weight='bold')

st.markdown(
    '<p style="text-align: center; font-size: 16px;">A data visualization app created by <a href="https://www.linkedin.com/in/bennett-p-930542b6/" target="_blank">Bennett Paradis</a></p>', 
    unsafe_allow_html=True
)

st.info("**Hello and welcome to the Oyster Sanctuary Data Explorer! The dataset featured here is part of ongoing oyster restoration and monitoring efforts in North Carolina. "
           f"If you would like to learn more about the importance of oyster sanctuaries in North Carolina, how they are built, and current projects, please visit the [StoryMap](https://storymaps.arcgis.com/stories/d876f9b131174f859270c600ccf3545f)!**")

text.display_text("In 1996, the North Carolina Division of Marine Fisheries began building artificial reefs with the specific aim of creating protected habitat for subtidal oysters. These Oyster Sanctuaries are closed to harvest with the goal of creating a network of thriving and self-sustaining oyster reefs throughout Pamlico Sound. ")
text.display_text("NCDMF's dive team conducts annual monitoring to gather data used to quantify the performance & longevity of the oyster sanctuaries. This dashboard allows users to explore the data collected from these SCUBA surveys. See below to get started!")

st.write('---')

avg_densities = np.array([
    [2019, 285, 9, 183, 94], 
    [2020, 895, 38, 537, 320], 
    [2021, 802, 64, 397, 341], 
    [2022, 811, 59, 450, 302], 
    [2023, 1159, 124, 811, 398]
])

avg_dens_df = pd.DataFrame(avg_densities, columns=['Year', 'Total', 'Legal', 'Sublegal', 'Spat'])


df = pd.read_csv('data/OSdata_extractions.csv')

st.sidebar.subheader("Choose a year below to alter the donut chart on the right.")
year = st.sidebar.selectbox(
    "Select a Year:", 
    avg_dens_df["Year"].unique(),
    key=10
)


df_selection = avg_dens_df.query(
    "Year == @year"
)

col1, col2 = st.columns([0.8,1])



with col1:
    text.display_text("Throughout this app you can interact with the Oyster Sanctuary data that's been collected over five years!", font_size=18, align='left')
    text.display_text("Follow the steps below to get a general idea of how to select filters as you explore the dataset.", font_size=18, align='left')
   
    st.info("""
            1) Select a year in the sidebar on the left to change the graphic.
            2) The graphic will update with the applied filter.
            2) Move your cursor over the graphic to see more info.
        """)

    text.display_text("At the top of the the sidebar you can navigate to different pages & dive deeper into North Carolina's Oyster Sanctuary dataset:", font_size=18, font_weight='bold', align='left')

    methods = st.page_link("pages/1_📋Methodology.py", label="Learn about our methodology", icon="📋")
    pamlico = st.page_link("pages/2_🌍Explore Pamlico Sound.py", label="Explore the oyster sanctuaires in Pamlico Sound", icon="🌍")
    map_views = st.page_link("pages/3_🦪View Sanctuary Maps.py", label="View the blueprints for each sanctuary", icon="🦪")
    compare = st.page_link("pages/4_📊Compare Population Data.py", label="Compare oyster populations over time", icon="📊")
    analyze = st.page_link("pages/5_🤿Analyze Reef Materials.py", label="Analyze the efficacy of different reef materials", icon="🤿")


with col2:
    # Extract the data for the selected year
    legal_sum = df_selection['Legal'].values[0]
    sublegal_sum = df_selection['Sublegal'].values[0]
    spat_sum = df_selection['Spat'].values[0]

    # Donut chart
    labels = ['Legal (>75mm)', 'Sublegal (26mm < x < 76mm)', 'Spat (<26mm)']
    values = [legal_sum, sublegal_sum, spat_sum]

    fig = go.Figure(
        data=[go.Pie(labels=labels, values=values, hole=0.3)]
    )

    fig.update_traces(
        marker=dict(colors=['#636EFA', '#EF553B', '#00CC96'], line=dict(color='black', width=2)),
        hoverlabel=dict(bgcolor='white', font=dict(color='black', size=16)),
        textfont=dict(size=18)
    )

    fig.update_layout(
        title=dict(
            text=f"Oyster Size Class Densities ({year})",
            x=0.1,
            font=dict(size=24)
        ),
        legend=dict(
            title=dict(
                text="Oyster Size Classes",
                font=dict(size=18, color='black')
            ),
            font=dict(size=16),
            orientation="h",
            yanchor="top",
            y=-0.20,
            xanchor="center",
            x=0.5
        )
    )

    # Displaying the figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    text.display_text(
        "This donut chart illustrates how many legal, sublegal, and spat oysters were found on average across all sanctuaries in a given year. Select a year in the sidebar to change the data & the graph above."
    )

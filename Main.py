import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils import text

text.tab_display()
text.pages_font()

# --- MAINPAGE ---

# st.markdown('''
#             <style>
#             body {background-color: white;
#             }
#             <style>
#             ''', unsafe_allow_html=True)
text.display_text("🦪 NC's Oyster Sanctuary Dashboard 📊", font_size=50, font_weight='bold')

st.info("**Hello and welcome to the Oyster Sanctuary Data Visualization Dashboard! The dataset featured here is part of ongoing oyster restoration and monitoring efforts in North Carolina. "
           f"If you would like to learn more about the importance of Oyster Sanctuaries, how they are built in North Carolina, and current projects, please visit the [StoryMap](https://storymaps.arcgis.com/stories/d876f9b131174f859270c600ccf3545f)!**")

text.display_text("In 1996, the North Carolina Division of Marine Fisheries began building artificial reefs with the specific aim of creating protected habitat for subtidal oysters. These Oyster Sanctuaries are closed to harvest with the goal of creating a network of thriving and self-sustaining oyster reefs throughout Pamlico Sound. ")
text.display_text("DMF's dive team conducts annual monitoring to gather data with the aim of quantifying the performance and longevity of the sanctuaries. This dashboard allows users to explore the dataset collected from these yearly SCUBA surveys. Here you can interact with the data by choosing filters in the sidebar.")

st.write('---')

st.sidebar.success("Choose how you want to explore the dataset!")

df = pd.read_csv('data/2019-2023_oyster_densities.csv')

year = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    key=10
)

df_selection = df.query(
    "Year == @year"
)

sampling_effort = {
    '2019': {
        'samples':'109',
        'oysters': '4,995'
    },
    '2020': {
        'samples':'123',
        'oysters': '17,898'
    },
    '2021': {
        'samples':'128',
        'oysters':'16,637'
    },
    '2022': {
        'samples':'146',
        'oysters':'18,255'
    },
    '2023': {
        'samples':'136',
        'oysters':'26,652'
    },
}
col1, col2 = st.columns(2)

with col1:
    text.display_text("On this app you have the ability to interact with the Oyster Sanctuary dataset!", font_size=18, align='left')
    text.display_text("Follow the steps below to get a general idea of how to interact with the different pages.", font_size=18, align='left')
   
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
    # Donut chart
    legal_sum = df_selection['legal'].sum()
    sublegal_sum = df_selection['sublegal'].sum()
    spat_sum = df_selection['spat'].sum()

    labels = ['Legal (>75mm)', 'Sublegal (26mm< x <76mm)', 'Spat (<26mm)']
    values = [legal_sum, sublegal_sum, spat_sum]
    fig = go.Figure(
        data=[go.Pie(labels=labels, values=values, hole=0.3)]
    )
    fig.update_traces(
        marker=dict(colors=['#636EFA', '#EF553B', '#00CC96'], line=dict(color='black', width=2)),
        hoverlabel=dict(bgcolor='white', font=dict(color='black', size=16))
    )
           
    fig.update_layout(
        title=f"Size Class Breakdown - Sampling {year}",
        title_x=0.25,
    )
    # Displaying the figure in Streamlit
    st.plotly_chart(fig)

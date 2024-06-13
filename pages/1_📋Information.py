import streamlit as st


st.markdown(
    f"""
    <div style="text-align: left;">
        <p style="font-size:20px;">Oysters have experienced significant declines around the world over the past century due to overfishing, harvest gear impacts, pollution, disease, and decreasing water quality. 
        Because of their positive impacts on supporting biodiversity, water quality, and shoreline stabilization, interest in oyster restoration has grown significantly in recent decades.</p>
    <div style="text-align: left;">
        <p style="font-size:20px;">In 1996, the North Carolina Division of Marine Fisheries began building artificial reefs with the specific aim of creating protected habitat for subtidal oysters. 
        These protected areas are closed to harvest, allowing oysters to grow to adulthood and release massive amounts of larvae to nearby areas. These protected sites are called Oyster Sanctuaries. </p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="text-align: left;">
        <p style="font-size:20px;">Today there are <b>15 oyster sanctuaries</b> spanning <b>566 acres</b> of protected subtidal habitat in North Carolina’s Pamlico Sound. 
        DMF’s dive team conducts an annual monitoring survey of the sanctuaries to collect data and quantify oyster density over time.</p> 
    <div style="text-align: left;">
        <p style="font-size:20px;">This ‘dashboard’ offers users several ways to explore the extensive dataset by visualizing the results of North Carolina’s Oyster Sanctuary monitoring effort. 
        You can start by selecting a year on the left to see a breakdown of the size classes (<b>legal, sublegal, and spat oysters</b>) in our density samples.</p>
    <div style="text-align: left;">
        <p style="font-size:20px;">Visit the different pages to explore Pamlico Sound, view the blueprints for each sanctuary, compare oyster populations, and analyze the performance of different materials used on our reefs!</p>
    <div style="text-align: left;">
        <p style="font-size:20px;">If you would like to learn more about the importance of Oyster Sanctuaries and how they are built in North Carolina, please <a href="https://storymaps.arcgis.com/stories/d876f9b131174f859270c600ccf3545f"> visit the StoryMap! </a> </p>
    </div>
    """, 
    unsafe_allow_html=True
)
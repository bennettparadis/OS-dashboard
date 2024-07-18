import streamlit as st
from utils import text
from PIL import Image
import io
import base64

#PAGE SETUP
text.tab_display()
text.display_text("📋Methodology", font_size=50, font_weight='bold')
text.pages_font()

text.display_text("This page is dedicated to providing a detailed walkthrough of the methodology used to collect the data featured on this app. The annual scuba monitoring effort of the oyster sanctuaries has resulted in a long-term dataset of oyster density metrics and population data, which is used in the development of future oyster restoration projects.")

st.subheader('Monitoring Objectives')
container = st.container(border = False)
container.info('Evaluating performance of an oyster sanctuary involves monitoring the long-term stability of reef materials and quantifying their ability as reef habitat to host oysters over time. Monitoring oyster sanctuaries can benefit restoration practices by demonstrating which factors contribute to cost-effective restoration such as which materials yield consistently high oyster densities over time.')
container.info("""The primary objectives of this monitoring program are as follows:

1)	Evaluate material performance as oyster habitat.
2)	Evaluate material long-term durability and stability. 
3)	Evaluate overall material performance for reproductive potential and larval recruitment
4)	Evaluate oyster demographic trends at each sanctuary through time

                   """)

st.subheader('Obtaining Reef Footprint using Side-Scan Sonar')
col1, col2 = st.columns(2)
with col1:
    text.display_text('NCDMF utilizes an Edgetech 6205 system to collect side-scan and multibeam sonar data which are used to image artificial reefs, including the oyster sanctuaries.', align='left')
    text.display_text('As the survey vessel follows transect lines along the reef site, the sensors of the sonar equipment send and receive acoustic pulses. These sonar waves are sent out in a fan-shaped beam (similar to a flashlight) until they reach the seafloor. The waves will bounce of the bottom substrate and behave differently depending on where they land.', align='left') 
    text.display_text('The depth, or bathymetry, is computed by the time it takes for an acoustic wave to travel down, hit the bottom, and return to the boat. The deeper the water body, the long it will take for a sound wave to return to the vessel. On the right is a bathymetric map of Cedar Island. There the height of the marl ridges can easily be seen. At this 75-acre site, over 130 ridges, each ~200 ft long and 4-8 ft tall, provide oysters an elevated place to settle and grow.',align='left')
    text.display_text('Once a sanctuary has been mapped, the overall material footprint can be calculated. This is the area covered by alternative substrates (marl, granite, etc.) used to build a sanctuary.', align='left')

with col2:
    # Load an image from file
    bathymap = Image.open('imgs/Cedar_Island_final_bathy2023.jpg')

    # Resize the image
    width, height = bathymap.size
    new_width = 400
    new_height = int((new_width / width) * height)
    bathymap_resized = bathymap.resize((new_width, new_height))

    # Save the resized image to a BytesIO object
    bathy_bytes = io.BytesIO()
    bathymap_resized.save(bathy_bytes, format='PNG')
    bathy_bytes.seek(0)

    # Convert image bytes to base64
    bathy_base64 = base64.b64encode(bathy_bytes.read()).decode("utf-8")

    # Define the image and caption HTML template
    bathy_html = f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{bathy_base64}" width="{new_width}" height="{new_height}" />
            <p style="width: {new_width}px; margin: 0 auto;">Material footprint and bathymetric map of Cedar Island Oyster Sanctuary. This 75-acre site was build with mostly class B limestone marl and was completed in 2023.</p>
        </div>
    """

    # Display the image and caption using st.markdown
    st.markdown(bathy_html, unsafe_allow_html=True)

st.subheader('Collecting Oyster Data via Dive Surveys')

rand_select = st.container()

text.display_text("Once the Sanctuaries have been mapped out, the dive team has a reef 'footprint' that can be used as reference for where to visit and sample. Each Sanctuary may have a few different materials on it. Planning a survey begins with selecting randomly generated points using geospatial software. The team will visit a minimum of four sites for each material type. The sample size increases as the material footprint increases. For instance, Cedar Island...")

with st.expander("Random Selection"):
    st.info("""
            Before any diver gets in the water, sampling maps are created to plan where oyster data will be collected on each sanctuary. The number of samples is determined by the number of materials and the amount of each material present on each sanctuary.
    
            A minimum of 4 dives are conducted for each material type. If there is more than 2 acres covered by a material, then 5 samples are collected.  And so on. 

            Dive sites are randomly selected using geospatial software (ESRI's ArcGIS Pro). Once in the field, divers and support staff will mark the site with an anchored polyball. 

            Each day our dive team visits an oyster sanctuary, they record salinity, dissolved oxygen, and temperature levels via handheld YSI at the surface and at the bottom.

            Additionally, divers collect observational data on every site. This includes sample depth, sedimentation level, boring sponge (presence/absence), observed fish and invertebrates, and percent coverage for oysters and mussels.
            """)

with st.expander("Excavation samples"):
    st.info("""
            Certain materials are relatively easy for divers to remove from the reef. Various aggregate rocks have been used to build the sanctuaries and are typically the site of a basketball (Class B). 
            These include limestone marl, crushed granite, crushed concrete, and basalt. Various types of recycled shell were used at one point to 'refurbish' older sites. This included oyster shell and surf clam shell; however, these shells did not have the same longevity as other materials.
            
            When diving on these types of materials, divers are able to excavate the material and attached oysters by hand. Divers use a 1/4 square meter quadrat and remove the top 15-20cm to standardize the amount of material excavated. The oysters and rock are put into a tethered basket, which is then brought up to the boat. At the surface, the first 400 oysters are measured. The remaining sample is counted up. 
            """)

with st.expander("Observation samples"):
        st.info("""
            
            """)

import streamlit as st
from utils import text
from PIL import Image
import io
import base64

def display_image(image, new_width, caption):
        # Resize the image
        width, height = image.size
        new_height = int((new_width / width) * height)
        image_resized = image.resize((new_width, new_height))

        # Save the resized image to a BytesIO object
        image_bytes = io.BytesIO()
        image_resized.save(image_bytes, format='PNG')
        image_bytes.seek(0)

        # Convert image bytes to base64
        image_base64 = base64.b64encode(image_bytes.read()).decode("utf-8")

        # Define the image and caption HTML template
        image_html = f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_base64}" width="{new_width}" height="{new_height}" />
                <p style="width: {new_width}px; margin: 0 auto;">{caption}</p>
            </div>
        """
        # Display the image and caption using st.markdown
        st.markdown(image_html, unsafe_allow_html=True)

#PAGE SETUP
text.tab_display()
text.display_text("📋Methodology", font_size=50, font_weight='bold')
text.pages_font()

text.display_text("This page is dedicated to providing a detailed walkthrough of the methodology used to collect the data featured on this app. The annual scuba monitoring effort of the oyster sanctuaries has resulted in a long-term dataset of oyster density metrics and population data, which is used in the development of future oyster restoration projects.")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Monitoring Objectives", "Mapping with Sonar", "Sampling Design", "Observational Data", "Excavated Samples"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Monitoring Objectives')
        text.display_text('Evaluating the performance of an oyster sanctuary involves monitoring the long-term stability of reef materials and quantifying their ability to host oysters over time. Such monitoring efforts can be beneficial to future oyster restoration projects by revealing which factors contribute to cost-effective restoration such as which materials yield consistently high oyster densities over time.', align='left')
        text.display_text("""The primary objectives of NCDMF's oyster sanctuary monitoring are as follows:

        1)	Evaluate material performance as oyster habitat.
        2)	Evaluate material long-term durability and stability. 
        3)	Evaluate overall material performance for reproductive potential and larval recruitment.
        4)	Evaluate oyster demographic trends at each sanctuary through time.

        """, align='left')
    
    with col2:
        dive_team = Image.open('imgs/diveteam.jpg')
        dive_team_cap = ("NCDMF's Habitat & Enhancement Dive team conducts annual monitoring efforts of the Oyster Sanctuaries. Since revamping the sampling protocol in 2018, this effort typically involves visiting 14 sanctuaries, diving at 130+ locations, and measuring 20,000 oysters between June and August.")
        display_image(dive_team, 600, dive_team_cap)

with tab2:
    st.subheader('Obtaining Reef Footprint using Side-Scan Sonar')
    col1, col2 = st.columns(2)
    with col1:
        text.display_text('NCDMF utilizes an Edgetech 6205 system to collect side-scan and multibeam sonar data which are used to image artificial reefs, including the oyster sanctuaries.', align='left')
        text.display_text('As the survey vessel follows transect lines along the reef site, the sensors of the sonar equipment send and receive acoustic pulses. These sonar waves are sent out in a fan-shaped beam (similar to a flashlight) until they reach the seafloor. The waves will bounce off the bottom substrate and behave differently depending on the hardness of the bottom substrate.', align='left') 
        text.display_text('The depth, or bathymetry, is computed by the time it takes for an acoustic wave to travel down, hit the bottom, and return to the boat. The deeper the water body, the longer it will take for a sound wave to return to the vessel. On the right is a bathymetric map of Cedar Island. There the height of the marl ridges can easily be seen. At this 75-acre oyster sanctuary, there are 132 ridges, each ~200 ft long, 35 ft wide, and 4-8 ft tall. The vertical relief provided by these ridges provides oysters an elevated place to settle and grow.',align='left')
        text.display_text('Once a sanctuary has been mapped, the overall material footprint can be calculated. This is the area covered by alternative substrates (marl, granite, etc.) used in building a sanctuary.', align='left')

    with col2:
        # Load an image from file
        bathy_map = Image.open('imgs/Cedar_Island_final_bathy2023.jpg')
        bathy_cap = "Material footprint and bathymetric map of Cedar Island Oyster Sanctuary. This 75-acre site was build with mostly class B limestone marl and was completed in 2023."

        display_image(bathy_map, 450, bathy_cap)
 

with tab3:
    st.subheader("Sampling Design")
    col1,col2 = st.columns([0.8,1])
    with col1:
        text.display_text("With the oyster sanctuaries mapped out, the total material footprint can be determined using geospatial software (ESRI's ArcGIS Pro). Using the same software, random points can be generated on each of the different material types within a sanctuary.", align='left')
        text.display_text("The number of samples points is proportionate to the total area covered by each material. A minimum of 4 samples are collected for each material type that doesn't exceed 2 acres in cumulative coverage. For 2-3 acres of coverage, 5 samples are collected. Between 3-4 acres, 6 samples, and so on. A maximum of 8 samples are collected for materials that exceed 5 acres in total footprint.", align='left')
        text.display_text("The example on the right shows the sampling map for Swan Island. At this oyster sanctuary, divers collected data from 8 random points on marl limestone ridges and 7 points on granite ridges for a total of 15 samples. These points are marked with a polyball buoy tethered to a weighted shackle. Divers follow the line down to investigate the site and collect data." ,align='left')
        text.display_text("Depending on the material type, the divers will either follow protocol for collecting strictly observational data or will excavate material with any oysters attached.", align='left')
    
    with col2:
        swan_map = Image.open('imgs/SwanIsland2023.jpg')
        swan_cap = "The map used to collect oyster samples at randomly generated points along Swan Island. The number of samples collected by divers ranges between 4 and 8 for each material type and is determined by material footprint acreage."

        display_image(swan_map, 800, swan_cap)

with tab4:
    st.subheader("Observational Data")
    col1,col2 = st.columns(2)

    with col1:
        text.display_text("At every sample site, divers collect a series of observational data. This includes recording the sample depth & total depth (to estimate relief), visual inspection of percent cover for oysters, mussels, and algae, and observations for sedimentation, boring sponge, and observed fishes. Visibility is often limited to 5 ft (or less!) which can add another layer of diffuclty during sampling efforts.", align='left')
        text.display_text("For materials that cannot be brought to the surface (reef balls, consolidated concrete pipes, large basalt), counting and measuring oysters cannot be done on SCUBA. Instead, a 1/4 m² PVC quadrat with a 5x5 grid is used to estimate percent cover. Within this grid are 25 points of intersection. Each instance of an oyster (or mussel) under a point of intersection represents 4% of the quadrat area. This data is collected at all sites and is compared to excavated samples for estimating oyster density at observational sites.",align='left') 
        grid_quad = Image.open('imgs/GridQuad.jpg')
        grid_cap = "A 1/4 m² PVC quadrat is used to estimate percent cover for oysters, mussels, and algae. In this visualization, any oysters observed under an intersecting node are counted on this 5x5 grid."
        display_image(grid_quad, 450, grid_cap)
    with col2:
        
        obs_sheet = Image.open('imgs/OSDataSheetObs.jpg')
        obs_cap = "Data sheet for strictly observational dive sites where material cannot be brought to the surface for further examination."
        
        display_image(obs_sheet, 600, obs_cap)


with tab5:
    st.subheader("Excavated Samples")
    col1,col2 = st.columns(2)
    with col1:
        text.display_text("Throughout the history of the Oyster Sanctuary Program, various types of crushed aggregate rock have been used in the construction process. These include marl limestone, granite, and concrete. Recycled oyster and surf clam shells have also been used to 'refurbish' some ares of older sanctuaries. All of these material types can be easily dug up or excavated by divers and brought to the surface." , align= 'left')
        text.display_text("Divers collect all the observational data including percent coverage estimates before excavating material. A 1/4 m² PVC quadrat is placed in the same area as the grid quadrat. Any material and oysters in the quadrat are removed and placed into a basket which is tethered to the boat. Once the sample has been collected, the surface crew are signalled (three tugs on the line) to bring up the basket. The oyster rock is then pulled up to the boat where it will be processed.", align='left')
        text.display_text("On the boat, crew take a closer look at the oysters and also look for boring sponge. To get an idea of the size class structure within a sample the first 400 oysters are measured by their left valve length/height with calipers to the nearest mm. If there are more than 400 oysters, the remaining are counted. The total number of oysters in a sample multiplied by four gives an estimate of density (oysters/m²)." , align='left')
        text.display_text("Any oysters that are open, attatched at the hinge, and missing the meat inside are considered 'boxes'. Boxes are also measured but their lengths are recorded in the last columns of the excavation data sheet. ",align='left')
        text.display_text("For every day spent at an oyster sanctuary, water quality data is collected using a handheld YSI. This includes water temperature, salinity, and dissolved oxygen, which are recorded both at the surface and near the bottom. ", align='left')

        
    with col2:
        oyster_shell = Image.open('imgs/LVH.jpg')
        oyster_shell_cap = "An illustration for measuring shell height on an oyster."
        display_image(oyster_shell, 300, oyster_shell_cap)
        
        exc_sheet = Image.open('imgs/OSDataSheetExc.jpg')
        exc_cap = "Data sheet for excavated samples used during the annual Oyster Sanctuary monitoring efforts. Oysters are measured by their shell height to the nearest mm."

        display_image(exc_sheet, 600, exc_cap)

    # with st.expander("Subsampling Rationale"):
    #     st.write("To be added later...")

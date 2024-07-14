import streamlit as st

# Define the custom CSS
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
        <p style="font-size:50px; font-weight: bold;">📋Methodology</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.subheader('**THIS PAGE IS STILL IN DEVELOPMENT**')

st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:20px;">Annual monitoring efforts of the oyster sanctuaries have resulted in the accumulation of a high-resolution dataset which is used in the development of future habitat restoration and enhancement projects. This continuous dataset are now interactive in this dashboard. Below is an in-depth description of the methodology used by the dive team for collecting the oyster data on display here.</p>
    </div>
    """, 
    unsafe_allow_html=True
)


st.subheader('Objectives')
container = st.container(border = False)
container.info('Evaluating performance of an oyster sanctuary involves monitoring the long-term stability of reef materials and quantifying their ability as reef habitat to host oysters over time. Monitoring oyster sanctuaries can benefit restoration practices by demonstrating which factors contribute to effective restoration and which materials yield consistently high oyster densities over time.')
container.info("""The primary objectives of this monitoring program are as follows:

1)	Evaluate material performance as oyster habitat.
2)	Evaluate material long-term durability and stability. 
3)	Evaluate overall material performance for reproductive potential and larval recruitment
4)	Evaluate oyster demographic trends at each sanctuary through time

                   """)

st.subheader('Sampling Methodology')

rand_select = st.container()

rand_select.write("This is a test")

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

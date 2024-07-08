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
container.info('Evaluating performance of an oyster sanctuary involves monitoring the long-term stability of reef materials and quantifying their ability as reef habitat to host oysters over time. Monitoring oyster sanctuaries can benefit restoration practices by demonstrating which factors contribute to effective restoration and which materials are best suited for maximum performance. The primary objectives of this monitoring program are as follows:')
container.info("""
1)	Evaluate material performance as oyster habitat.
2)	Evaluate material long-term durability and stability. 
3)	Evaluate overall material performance for reproductive potential and larval recruitment
4)	Evaluate oyster demographic trends at each sanctuary through time

                   """)

st.subheader('Sampling Methodology')

#rand_select = st.container()

with st.expander("Random Selection"):
    col1, col2 = st.columns(2)
        with col1:
            st.info('test')
        with col2:
            st.info('test')

with st.expander("Excavation samples"):
    st.write('test')

with st.expander("Observation samples"):
    st.write('test')

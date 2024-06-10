import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

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

st.sidebar.success("Choose how you want to explore the dataset!")

df = pd.read_csv("C:/Users/bparadis/Documents/Python Scripts/dashboard/2019-2023_oyster_densities.csv")
year = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    key=10
)

df_selection = df.query(
    "Year == @year"
)

col1, col2 = st.columns(2)

with col1:
    pass

with col2:
    #Donut chart
    legal_sum = df_selection['legal'].sum()
    sublegal_sum = df_selection['sublegal'].sum()
    spat_sum = df_selection['spat'].sum()

    labels = ['Legal (>75mm)', 'Sublegal (26mm< x <76mm)', 'Spat (<26mm)']
    values = [legal_sum, sublegal_sum, spat_sum]
    fig = go.Figure(data=[go.Pie(labels=labels, values= values, hole=0.3)])
    fig.update_traces(marker=dict(colors=['#636EFA', '#EF553B', '#00CC96']))

    # Displaying the figure in Streamlit
    st.plotly_chart(fig)
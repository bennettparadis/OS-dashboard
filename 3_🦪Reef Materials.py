import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("C:/Users/bparadis/Documents/Python Scripts/dashboard/2019-2023_oyster_densities.csv")

fig = px.scatter(df, x ='Material_Age', y='total', color ="Material", hover_data=['OS_Name', 'Year'])

st.plotly_chart(fig)
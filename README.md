# 🦪 North Carolina Oyster Sanctuary Data Explorer

An interactive Streamlit app for exploring and visualizing annual SCUBA survey data from NC's Oyster Sanctuary Program.

🔗 **Live App:** https://ncos-data.streamlit.app/

<img width="1704" height="815" alt="OSWebApp_hist png" src="https://github.com/user-attachments/assets/a4319f4e-9c0f-471c-aee3-66b40f80f1d2" />


## Overview
North Carolina's Division of Marine Fisheries has been constructing and  monitoring oyster sanctuaries in Pamlico Sound since 1996. Each year, 
SCUBA-certified biologists survey each site to collect data on oyster density, population structure, and material performance. This dashboard 
makes that dataset explorable and interactive.

## Features
- 🦪 View blueprints and maps of the oyster sanctuaries
- 📊 Explore size-class distributions and population structure
- 🤿 Compare performance across different reef construction materials
- 📈 Visualize oyster size class density trends time
- 🦀 Filter by site, year, material type, and size-class
- 📋 Read about the survey methodology

<img width="1675" height="803" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/e8752ac8-3a63-4583-96d0-0acaa4a79bbe" />


## Getting Started
### Run locally
pip install -r requirements.txt
streamlit run app.py

### Dependencies
- Python 3.11.7
- streamlit==1.36.0
- numpy==2.0.0
- pandas==2.2.2
- geopandas==1.0.0
- plotly==5.22.0
- pydeck==0.9.1
- statsmodels

## Data
- GIS Shapefile of Oyster Sanctuary Reefs
- Annual SCUBA survey data from NC oyster sanctuaries (2019-2025) 
Data collected and maintained by NCDMF's Habitat Enhancement Section.


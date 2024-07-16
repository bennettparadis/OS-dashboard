
# Oyster Sanctuary Monitoring Data Visualizer
#*UNDER DEVELOPMENT* 

Python script for an interactive streamlit app that allows users to explore and visualize NC's Oyster Sanctuary data

[https://streamlit.app.ncos-dashboard](https://ncos-dashboard.streamlit.app/)

## Summary
North Carolina's Division of Marine Fisheries began the Oyster Sanctuary Program to create protected artificial reefs in an effort to restore the state's subtidal oyster population. 
Today, there are 15 oyster sanctuaries spanning 566 acres of protected subtidal habitat in Pamlico Sound. 
Each year, biologists conduct SCUBA surveys to collect oyster data on the performance of each sanctuary and the various materials used to build each reef. 
The code here utilizes streamlit to create an interactive dashboard that summarizes and visualizes the dataset from 2019-2023. 
The dashboard allows users to explore the Oyster Sanctuary Program's dataset and look for temporal changes and differences in how materials perform at the sanctuaries!

## Folder structure
For the streamlit app to work, the python scripts should be organized as follows:
- Main.py should be in the same directory as the data (csv, shp files)
- config.toml needs to be in a subfolder named .streamlit
- a subfolder named "pages" should contain the enumerated python scripts

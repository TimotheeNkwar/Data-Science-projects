import plotly.express as px

import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
# load the data
data = pd.read_csv("C://Users//KOVVO//.cache//kagglehub//datasets//dataanalyst001//world-population-by-country-2024//versions//1//World Population by country 2024.csv")

st.write(data.head(10))


# let't create the choropleth map with all the available data
fig = px.choropleth(
    data,                     
    locations="Country",            
    locationmode="country names", # Use country names as locations
    color="Country",  # Use population 2024 as color
    hover_name="Country",  # show the name of the country in the hover
    hover_data={  # show the data in the hover
        "Population 2024": True,
        "Population 2023": True,
        "Area (km2)": True,
        "Density (/km2)": True,
        "Growth Rate": True,
        "World %": True
    },
    title="Population of the world (2024)",  # title of the plot    
    color_continuous_scale="inferno_r" # reverse the color scale
)

fig.update_geos(projection_type="orthographic")  # the projection type
fig.update_layout(width=1000, height=900)  # size of the plot
st.plotly_chart(fig)

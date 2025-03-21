import plotly.express as px
import streamlit as st
import pandas as pd

# Configurer la page
st.set_page_config(layout="wide")
st.title("World Data")

# Charger les données
@st.cache_data
def load_data():
    return pd.read_csv("C://Users//KOVVO//Desktop//Streamlit//World Population by country 2024.csv")

data = load_data()
st.write("Overview of data:", data.head())

# --- TOP 5 Country ---
st.sidebar.subheader("Top 5 most populous Countries")
top_Country = ["INDIA", "CHINA", "USA", "INDONESIA", "PAKISTAN"]

for i, country in enumerate(top_Country):
    if st.sidebar.button(f"{i+1}. {country}"):
        Country_choose = country  # Sélectionne automatiquement le pays si cliqué

# --- BODY ---
col_left, col_center, col_right = st.columns([1, 2, 1])

# LISTE DES PAYS
with col_left:
    st.subheader("Select a Country")
    Country_choose = st.selectbox("Select a country:", data["Country"])

# INFOS DÉTAILLÉES
with col_right:
    st.subheader(f"Statistics of {Country_choose}")
    Country_data = data[data["Country"] == Country_choose]
    
    if not Country_data.empty:
        st.metric("Population 2024", Country_data["Population 2024"].values[0])
        st.metric("Density (hab/km²)", Country_data["Density (/km2)"].values[0])
        st.metric("Area (km²)", Country_data["Area (km2)"].values[0])
        st.metric("Growth Rate)", Country_data["Growth Rate"].values[0])
        st.metric("World %)", Country_data["World %"].values[0])
        st.metric("World Rank)", Country_data["World Rank"].values[0])
# MAP AVEC LE PAYS SÉLECTIONNÉ EN COULEUR DISTINCTE
with col_center:
    data["highlight"] = data["Country"].apply(lambda x: 1 if x == Country_choose else 0)

    fig = px.choropleth(
        data,                     
        locations="Country",            
        locationmode="country names", 
        color="highlight",  # Mettre en évidence le pays sélectionné
        hover_name="Country",
        hover_data={
            "Population 2024": True,
            "Population 2023": True,
            "Area (km2)": True,
            "Density (/km2)": True,
            "Growth Rate": True,
            "World %": True
        },
        title="World Map",
        color_continuous_scale=["lightgray", "yellow"]  # Rouge pour le pays sélectionné
    )

    fig.update_geos(projection_type="orthographic")
    fig.update_layout(width=1000, height=600)  
    st.plotly_chart(fig, use_container_width=True)
# MAP OF WORLD
with col_center:
    fig = px.choropleth(
    data,                     
    locations="Country",            
    locationmode="country names", # Use country names as locations
    color="Population 2024",  # Use population 2024 as color
    hover_name="Country",  # show the name of the country in the hover
    hover_data={  # show the data in the hover
        "Population 2024": True,
    },
    title="Population of the world (2024)",  # title of the plot    
    color_continuous_scale="inferno_r", # reverse the color scale
 
    )

fig.update_geos(projection_type="orthographic")  # the projection type
fig.update_layout(width=1200, height=800)  # size of the plot
st.plotly_chart(fig, use_container_width=False)
#import useful libraries
import plotly.express as px
import streamlit as st
import pandas as pd
import os

# Configure the page
st.set_page_config(layout="wide")
st.title("World Data")

# --- Vérifier si le fichier CSV existe ---
csv_path = "Streamlit/World Population by country 2024.csv"
if not os.path.exists(csv_path):
    st.error(f"Le fichier CSV '{csv_path}' est introuvable. Vérifiez son emplacement.")
    st.stop()  # Arrête l'exécution si le fichier est manquant

# Charge data avec gestion d'erreur
@st.cache_data
def load_data():
    try:
        data = pd.read_csv(csv_path)
        st.write("✅ Données chargées avec succès :", data.head())  # Debugging
        return data
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        st.stop()

data = load_data()

# --- Vérifier la liste des pays disponibles ---
st.write("🔍 Liste des pays disponibles :", data["Country"].unique())

# --- TOP 5 Country ---
st.sidebar.subheader("Top 5 most populous Countries")
top_Country = ["INDIA", "CHINA", "USA", "INDONESIA", "PAKISTAN"]

for i, country in enumerate(top_Country):
    if st.sidebar.button(f"{i+1}. {country}"):
        st.session_state["Country_choose"] = country  # Sauvegarde le pays sélectionné

# --- Sélection du pays ---
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_left:
    st.subheader("Select a Country")
    Country_choose = st.selectbox("Select a country:", data["Country"].unique())
    st.session_state["Country_choose"] = Country_choose  # Sauvegarde dans la session

# --- INFOS DÉTAILLÉES ---
with col_right:
    st.subheader(f"Statistics of {Country_choose}")
    
    # Vérifier si le pays existe dans le dataset
    Country_data = data[data["Country"] == Country_choose]
    
    if not Country_data.empty:
        st.metric("Population 2024", Country_data["Population 2024"].values[0])
        st.metric("Density (hab/km²)", Country_data["Density (/km2)"].values[0])
        st.metric("Area (km²)", Country_data["Area (km2)"].values[0])
        st.metric("Growth Rate", Country_data["Growth Rate"].values[0])
        st.metric("World %", Country_data["World %"].values[0])
        st.metric("World Rank", Country_data["World Rank"].values[0])
    else:
        st.warning("🚨 Le pays sélectionné n'existe pas dans la base de données.")

# --- MAP ---
with col_center:
    # Ajouter une colonne pour surligner le pays sélectionné
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
        color_continuous_scale=["lightgray", "yellow"]  # Couleur pour le pays sélectionné
    )

    fig.update_geos(projection_type="orthographic")
    fig.update_layout(width=1000, height=600)  
    st.plotly_chart(fig, use_container_width=True)

# --- MAP OF WORLD ---
with col_center:
    fig = px.choropleth(
        data,                     
        locations="Country",            
        locationmode="country names", # Utiliser les noms des pays
        color="Population 2024",  # Coloration selon la population
        hover_name="Country",
        hover_data={"Population 2024": True},
        title="Population of the world (2024)",
        color_continuous_scale="inferno_r"  # Échelle de couleur inversée
    )

    fig.update_geos(projection_type="orthographic")
    fig.update_layout(width=1200, height=800)
    st.plotly_chart(fig, use_container_width=False)

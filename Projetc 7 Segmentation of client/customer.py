import streamlit as st
import plotly.express as px
import pandas as pd
# Titre de l'app
st.title("Segmentation des clients - Mall Customers")

# Charger les données
df = pd.read_csv("Mall_Customers.csv")
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Normalisation
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Options de visualisation
graph_type = st.selectbox("Choisir un type de graphique", ["Scatter", "Barplot", "Boxplot"])

# SCATTER PLOT
if graph_type == "Scatter":
    fig = px.scatter(
        df, x='Annual Income (k$)', y='Spending Score (1-100)',
        color='Cluster',
        title="Répartition des clusters",
        hover_data=['CustomerID']
    )
    st.plotly_chart(fig)

# BARPLOT
elif graph_type == "Barplot":
    metric = st.selectbox("Choisir la variable à comparer", ['Annual Income (k$)', 'Spending Score (1-100)'])
    df_grouped = df.groupby('Cluster')[metric].mean().reset_index()
    fig = px.bar(df_grouped, x='Cluster', y=metric, title=f"{metric} moyen par cluster")
    st.plotly_chart(fig)

# BOXPLOT
elif graph_type == "Boxplot":
    metric = st.selectbox("Choisir la variable à afficher", ['Annual Income (k$)', 'Spending Score (1-100)'])
    fig = px.box(df, x='Cluster', y=metric, title=f"Distribution de {metric} par cluster")
    st.plotly_chart(fig)

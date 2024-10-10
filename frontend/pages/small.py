import streamlit as st


def show_page():
    st.title("Petits Animaux")
    st.write("Voici notre sélection de petits animaux de compagnie !")

# Navigation
page = st.selectbox("Choisissez une catégorie d'animaux :",
                    ["Accueil", "Animaux Exotiques", "Animaux Normaux", "Petits Animaux"])

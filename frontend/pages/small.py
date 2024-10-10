import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from frontend.template.animal_template import display_animal_list, get_animals,test_display_animal

def show_page():
    st.title("Petits Animaux")
    st.write("Voici notre sélection de petits animaux de compagnie !")

# Navigation
page = st.selectbox("Choisissez une catégorie d'animaux :",
                    ["Accueil", "Animaux Exotiques", "Animaux Normaux", "Petits Animaux"])
# Présentation des animaux
test_display_animal(
    name="Kim-Jong Un",
    age=5,
    image_url="images/small/maxresdefault.jpg",
    description="Max est un chien énergique et joueur, parfait pour les familles actives.",
    price=500
)

# Présentation des animaux
test_display_animal(
    name="Macron",
    age=5,
    image_url="images/small/Sans titre.jpg",
    description="Max est un chien énergique et joueur, parfait pour les familles actives.",
    price=500
)
# Présentation des animaux
test_display_animal(
    name="Jean-cache-Sex",
    age=5,
    image_url="images/small/hamster.jpg",
    description="Max est un chien énergique et joueur, parfait pour les familles actives.",
    price=500
)
# Présentation des animaux
test_display_animal(
    name="Fabrice Eboué",
    age=5,
    image_url="images/small/maxresdefault.jpg",
    description="Max est un chien énergique et joueur, parfait pour les familles actives.",
    price=500
)
# Présentation des animaux
test_display_animal(
    name="Griffondor",
    age=5,
    image_url="images/small/hasmter2.jpg",
    description="Max est un chien énergique et joueur, parfait pour les familles actives.",
    price=500
)
# Présentation des animaux
test_display_animal(
    name="Bou-che-ra",
    age=5,
    image_url="images/small/hasmter.jpg",
    description="Max est un chien énergique et joueur, parfait pour les familles actives.",
    price=500
)
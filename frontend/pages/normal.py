import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from  frontend.template.animal_template import display_animal

def show_page():
    st.title("Animaux Normaux")
    st.write("Découvrez nos animaux domestiques classiques, parfaits pour la maison.")

display_animal(
    name="Whiskers",
    age=3,
    image_url="images/whiskers.jpg",
    description="Whiskers est un chat affectueux qui aime se prélasser au soleil.",
    price=300
)

# Présentation des animaux
display_animal(
    name="Max",
    age=5,
    image_url="images/max.jpg",
    description="Max est un chien énergique et joueur, parfait pour les familles actives.",
    price=500
)
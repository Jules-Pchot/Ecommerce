import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from frontend.template.animal_template import display_animal_list, get_animals,test_display_animal

def show_page():
    st.title("Animaux Exotiques")  # ou "Animaux Normaux" ou "Petits Animaux"
    animals = get_animals(category="exotic")  # ou "normal" ou "small"
    if animals:
        display_animal_list(animals)
    else:
        st.error("Impossible de récupérer la liste des animaux exotiques.")

test_display_animal(
    name="Arnul",
    age=2,
    image_url="https://media-cdg4-2.cdn.whatsapp.net/v/t61.24694-24/362963464_315200977625871_6300899902763330161_n.jpg?ccb=11-4&oh=01_Q5AaIJ5nKZnYItuIgQak-0d9zercabuQu_dWVsdPzgTokG8P&oe=6711466E&_nc_sid=5e03e0&_nc_cat=107",
    description="Gros singe",
    price=200
)
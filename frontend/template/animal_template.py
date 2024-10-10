import streamlit as st

def display_animal(name, age, image_url, description, price):
    """
    Affiche les informations d'un animal avec une image, un nom, un âge, une description et un prix.
    :param name: Nom de l'animal
    :param age: Âge de l'animal
    :param image_url: Lien de l'image de l'animal
    :param description: Description de l'animal
    :param price: Prix de l'animal
    """
    st.image(image_url, caption=name, use_column_width=True)  # Afficher l'image
    st.write(f"**Nom**: {name}")  # Afficher le nom
    st.write(f"**Âge**: {age} ans")  # Afficher l'âge
    st.write(f"**Description**: {description}")  # Afficher la description
    st.write(f"**Prix**: {price} €")  # Afficher le prix
    st.markdown("---")  # Séparateur
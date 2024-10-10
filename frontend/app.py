import streamlit as st
import pages.exotic as exotic_animals
import pages.normal as normal_animals
import pages.small as small_animals
from template.animal_template import display_animal


# Titre de la page principale
st.title("Bienvenue sur le site de Revente d'Animaux")

# Description du site
st.write("""
Bienvenue sur notre plateforme de revente d'animaux où vous trouverez une variété d'animaux à adopter.
Notre objectif est de vous offrir une expérience agréable et sécurisée pour trouver l'animal parfait qui correspond à vos besoins.
Que vous soyez à la recherche d'un animal exotique, d'un compagnon domestique classique ou d'un petit animal, nous avons tout ce qu'il vous faut !
""")

# Message de bienvenue
st.header("Message de Bienvenue")
st.write("Merci de nous rendre visite ! Explorez notre sélection d'animaux et trouvez le compagnon idéal pour vous.")

# Liens vers les pages des animaux
st.subheader("Nos catégories d'animaux :")
st.write("Choisissez une catégorie d'animaux pour explorer nos offres :")

# Navigation avec clé unique
page = st.selectbox("Choisissez une catégorie d'animaux :",
                    ["Accueil", "Animaux Exotiques", "Animaux Normaux", "Petits Animaux"],
                    key="animal_category_selectbox")  # Ajoute une clé unique ici

if page == "Accueil":
    st.write("Merci de nous rendre visite ! Explorez notre sélection d'animaux.")
elif page == "Animaux Exotiques":
    exotic_animals.show_page()  # Appelle la fonction pour afficher le contenu de la page
elif page == "Animaux Normaux":
    normal_animals.show_page()  # Appelle la fonction pour afficher le contenu de la page
elif page == "Petits Animaux":
    small_animals.show_page()  # Appelle la fonction pour afficher le contenu de la page

# Présentation des animaux
display_animal(
    name="Max",
    age=5,
    image_url="images/max.jpg",
    description="Max est un chien énergique et joueur, parfait pour les familles actives.",
    price=500
)

display_animal(
    name="Whiskers",
    age=3,
    image_url="images/whiskers.jpg",
    description="Whiskers est un chat affectueux qui aime se prélasser au soleil.",
    price=300
)

display_animal(
    name="Arnul",
    age=2,
    image_url="https://media-cdg4-2.cdn.whatsapp.net/v/t61.24694-24/362963464_315200977625871_6300899902763330161_n.jpg?ccb=11-4&oh=01_Q5AaIJ5nKZnYItuIgQak-0d9zercabuQu_dWVsdPzgTokG8P&oe=6711466E&_nc_sid=5e03e0&_nc_cat=107",
    description="Gros singe",
    price=200
)
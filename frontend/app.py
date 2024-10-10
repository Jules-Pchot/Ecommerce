import streamlit as st
import requests
import pages.exotic as exotic_animals
import pages.normal as normal_animals
import pages.small as small_animals
import login
import payment
from template.animal_template import display_animal

# Configuration de l'URL de base de l'API
API_BASE_URL = "http://localhost:5000/api"


# Fonction pour faire des requêtes API
def api_request(endpoint, method="GET", data=None, token=None):
    url = f"{API_BASE_URL}{endpoint}"
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, json=data, headers=headers)

    return response.json() if response.status_code == 200 else None


# Fonction pour récupérer la liste des animaux
def get_animals():
    return api_request("/animals")


# Titre de la page principale
st.title("Bienvenue sur le site de Revente d'Animaux")

# ... (le reste de votre code reste inchangé jusqu'à la partie d'affichage des animaux)

# Récupération et affichage des animaux depuis l'API
animals = get_animals()
if animals:
    for animal in animals:
        display_animal(
            name=animal['name'],
            age=animal['age'],
            image_url=animal['image_url'],
            description=animal['description'],
            price=animal['price']
        )
else:
    st.error("Impossible de récupérer la liste des animaux depuis l'API.")

# Gestion de la connexion
if st.button("Se connecter"):
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Valider"):
        response = api_request("/login", method="POST", data={"username": username, "password": password})
        if response and "access_token" in response:
            st.session_state["token"] = response["access_token"]
            st.success("Connexion réussie!")
        else:
            st.error("Échec de la connexion. Veuillez réessayer.")

# Exemple d'utilisation du token pour une requête authentifiée
if "token" in st.session_state and st.button("Afficher les commandes"):
    orders = api_request("/orders", token=st.session_state["token"])
    if orders:
        st.write(orders)
    else:
        st.error("Impossible de récupérer les commandes.")
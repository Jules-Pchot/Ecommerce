import streamlit as st
import requests

def show_login():
    st.title("Connexion")

    # Formulaire de connexion
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    # Message de succès ou d'erreur
    if st.button("Se connecter"):
        # Envoyer la requête au backend Flask
        response = requests.post("http://127.0.0.1:5000/api/users/login", json={
            "username": username,
            "password": password
        })

        if response.status_code == 200:
            token = response.json().get("access_token")
            st.success("Connexion réussie!")
            st.session_state['access_token'] = token  # Stocker le jeton dans la session
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
import streamlit as st
import requests

API_BASE_URL = "http://localhost:5000/api"


def api_request(endpoint, method="GET", data=None, token=None):
    url = f"{API_BASE_URL}{endpoint}"
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Erreur API: {response.status_code}")
        return None


def display_animal(animal_id, name, age, image_url, description, price):
    """
    Affiche les informations d'un animal avec une image, un nom, un âge, une description et un prix.
    Permet également d'ajouter l'animal au panier ou de l'acheter directement.
    """
    col1, col2 = st.columns([2, 3])

    with col1:
        st.image(image_url, caption=name, use_column_width=True)

    with col2:
        st.subheader(name)
        st.write(f"**Âge**: {age} ans")
        st.write(f"**Prix**: {price} €")
        st.write(f"**Description**: {description}")

        # Vérifier si l'utilisateur est connecté
        if "token" in st.session_state:
            if st.button("Ajouter au panier", key=f"add_cart_{animal_id}"):
                response = api_request("/cart/add", method="POST", data={"animal_id": animal_id},
                                       token=st.session_state["token"])
                if response:
                    st.success(f"{name} a été ajouté à votre panier!")
                else:
                    st.error("Erreur lors de l'ajout au panier. Veuillez réessayer.")

            if st.button(f"Acheter maintenant", key=f"buy_now_{animal_id}"):
                st.session_state['animal_to_buy'] = {
                    'id': animal_id,
                    'name': name,
                    'price': price
                }
                st.experimental_rerun()  # Rediriger vers la page de paiement
        else:
            st.warning("Veuillez vous connecter pour acheter ou ajouter au panier.")
            if st.button("Se connecter"):
                st.session_state['page'] = 'login'
                st.experimental_rerun()

    st.markdown("---")


def display_animal_list(animals):
    """
    Affiche une liste d'animaux en utilisant la fonction display_animal.
    """
    for animal in animals:
        display_animal(
            animal_id=animal['id'],
            name=animal['name'],
            age=animal['age'],
            image_url=animal['image_url'],
            description=animal['description'],
            price=animal['price']
        )


def get_animals(category=None):
    """
    Récupère la liste des animaux depuis l'API, éventuellement filtrée par catégorie.
    """
    endpoint = "/animals"
    if category:
        endpoint += f"?category={category}"
    return api_request(endpoint)


import streamlit as st


def test_display_animal(name, age, image_url, description, price):
    """
    Affiche les informations d'un animal avec une image, un nom, un âge, une description et un prix.
    :param name: Nom de l'animal
    :param age: Âge de l'animal
    :param image_url: Lien de l'image de l'animal
    :param description: Description de l'animal
    :param price: Prix de l'animal
    """
    st.image(image_url, caption=name, use_column_width=True)
    st.write(f"**Nom**: {name}")
    st.write(f"**Âge**: {age} ans")
    st.write(f"**Description**: {description}")
    st.write(f"**Prix**: {price} €")

    # Ajouter un bouton Acheter
    if st.button(f"Acheter {name}"):
        # Rediriger vers la page de paiement
        st.session_state['animal_to_buy'] = {
            'name': name,
            'price': price
        }
        st.experimental_rerun()  # Rafraîchir la page pour rediriger l'utilisateur
    st.markdown("---")

# Exemple d'utilisation
if __name__ == "__main__":
    st.title("Liste des animaux")
    animals = get_animals()
    if animals:
        display_animal_list(animals)
    else:
        st.error("Impossible de récupérer la liste des animaux.")
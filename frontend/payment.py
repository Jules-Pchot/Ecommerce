import streamlit as st

def show_payment():
    st.title("Page de paiement")

    # Récupérer les informations de l'animal depuis la session
    if 'animal_to_buy' in st.session_state:
        animal = st.session_state['animal_to_buy']
        st.write(f"Vous êtes sur le point d'acheter **{animal['name']}** pour **{animal['price']} €**.")

        # Simuler un bouton de paiement
        if st.button("Procéder au paiement"):
            st.success("Le paiement a été effectué avec succès ! Merci pour votre achat.")
            # Nettoyer la session après le paiement
            del st.session_state['animal_to_buy']
    else:
        st.warning("Aucun animal sélectionné pour le paiement.")
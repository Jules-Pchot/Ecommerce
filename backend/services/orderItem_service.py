from backend.models.orderItem import OrderItem
from backend.models.animal import Animal
from backend.models.orders import Order
from backend.app import db


def create_order(user_id, items):
    """
    Crée une commande et des éléments de commande.
    :param user_id: ID de l'utilisateur
    :param items: Liste des items (chaque élément doit contenir animal_id et quantity)
    """
    total_price = 0
    order_items = []

    # Calculer le prix total et préparer les OrderItems
    for item in items:
        animal = Animal.query.get(item['animal_id'])
        if animal and animal.stock >= item['quantity']:
            animal.stock -= item['quantity']  # Réduire le stock de l'animal
            total_price += animal.price * item['quantity']
            order_item = OrderItem(animal_id=animal.id, quantity=item['quantity'], price=animal.price)
            order_items.append(order_item)
        else:
            return None, f"Animal {item['animal_id']} non disponible ou stock insuffisant"

    # Créer la commande
    new_order = Order(user_id=user_id, total_price=total_price)

    # Ajouter les éléments de commande à la commande
    new_order.items.extend(order_items)

    # Ajouter la commande et les OrderItems à la session et commiter
    db.session.add(new_order)
    db.session.commit()

    return new_order, None
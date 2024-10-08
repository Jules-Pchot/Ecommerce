from models.orders import Order
from app import db

def create_order(data):
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return order

def get_order(id):
    return Order.query.get(id)

def get_user_orders(user_id):
    return Order.query.filter_by(user_id=user_id).all()
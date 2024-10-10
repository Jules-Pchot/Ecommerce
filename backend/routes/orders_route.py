from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.services import orders_service
from backend.schemas.orders import OrderSchema
from backend.services.orderItem_service import create_order  # Importer le service ici

bp = Blueprint('orders', __name__, url_prefix='/api/orders')
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

@bp.route('/', methods=['POST'])
@jwt_required()
def create_order():
    data = request.json
    data['user_id'] = get_jwt_identity()
    order = orders_service.create_order(data)
    return jsonify(order_schema.dump(order)), 201

@bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_orders():
    user_id = get_jwt_identity()
    orders = orders_service.get_user_orders(user_id)
    return jsonify(orders_schema.dump(orders))

@bp.route('/', methods=['POST'])
@jwt_required()
def create_order_route():
    user_id = request.json.get('user_id')
    items = request.json.get('items')

    if not user_id or not items:
        return jsonify({"error": "Invalid request data"}), 400

    order, error = create_order(user_id, items)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "Order created successfully", "order_id": order.id}), 201

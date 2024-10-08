from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services import orders_service
from schemas.orders import OrderSchema

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

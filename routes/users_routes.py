# Dans routes/user_routes.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from services import users_services
from schemas.users import UserSchema

bp = Blueprint('users', __name__, url_prefix='/api/users')
user_schema = UserSchema()

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = users_services.create_user(data)
    return jsonify(user_schema.dump(user)), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users_services.authenticate_user(data['username'], data['password'])
    if not user:
        return jsonify({"message": "Invalid username or password"}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

@bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = users_services.get_user(current_user_id)
    return jsonify(user_schema.dump(user))

@bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user_id = get_jwt_identity()
    data = request.json
    user = users_services.update_user(current_user_id, data)
    return jsonify(user_schema.dump(user))

@bp.route('/profile', methods=['DELETE'])
@jwt_required()
def delete_profile():
    current_user_id = get_jwt_identity()
    users_services.delete_user(current_user_id)
    return '', 204
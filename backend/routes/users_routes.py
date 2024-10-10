from flask import Blueprint, request, jsonify
from backend.models.users import User
from backend.app import db
from werkzeug.security import generate_password_hash

bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"message": "Tous les champs sont obligatoires"}), 400

    # Vérifier si l'utilisateur existe déjà
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Nom d'utilisateur déjà pris"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email déjà utilisé"}), 400

    # Créer l'utilisateur
    new_user = User(
        username=username,
        email=email,
        password_hash=generate_password_hash(password)
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Utilisateur créé avec succès"}), 201

from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Nom d'utilisateur et mot de passe requis"}), 400

    # Rechercher l'utilisateur dans la base de données
    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"message": "Identifiants invalides"}), 401

    # Créer un jeton JWT
    access_token = create_access_token(identity=user.id)

    return jsonify({"access_token": access_token}), 200
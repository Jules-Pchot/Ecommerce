from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
# Importer le service à l'intérieur des fonctions pour éviter une boucle
from backend.schemas.animal_schema import AnimalSchema

bp = Blueprint('animals', __name__, url_prefix='/api/animals')
animal_schema = AnimalSchema()
animals_schema = AnimalSchema(many=True)

@bp.route('/', methods=['GET'])
def get_animals():
    from backend.services import animal_service
    animals = animal_service.get_all_animals()
    return jsonify(animals_schema.dump(animals))

@bp.route('/<int:id>', methods=['GET'])
def get_animal(id):
    from backend.services import animal_service
    animal = animal_service.get_animal(id)
    if animal is None:
        return jsonify({"message": "Animal not found"}), 404
    return jsonify(animal_schema.dump(animal))

@bp.route('/', methods=['POST'])
@jwt_required()
def create_animal():
    from backend.services import animal_service
    data = request.json
    animal = animal_service.create_animal(data)
    return jsonify(animal_schema.dump(animal)), 201

@bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_animal(id):
    from backend.services import animal_service
    data = request.json
    animal = animal_service.update_animal(id, data)
    if animal is None:
        return jsonify({"message": "Animal not found"}), 404
    return jsonify(animal_schema.dump(animal))

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_animal(id):
    from backend.services import animal_service
    result = animal_service.delete_animal(id)
    if result is False:
        return jsonify({"message": "Animal not found"}), 404
    return '', 204
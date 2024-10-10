# services/animal_service.py

def get_all_animals():
    from backend.models.animal import Animal  # Importation différée
    return Animal.query.all()

def get_animal(animal_id):
    from backend.models.animal import Animal  # Importation différée
    return Animal.query.get(animal_id)

def create_animal(data):
    from backend.models.animal import Animal  # Importation différée
    from backend.app import db  # Importation différée
    new_animal = Animal(**data)
    db.session.add(new_animal)
    db.session.commit()
    return new_animal

def update_animal(animal_id, data):
    from backend.app import db  # Importation différée
    animal = get_animal(animal_id)
    if animal:
        for key, value in data.items():
            setattr(animal, key, value)
        db.session.commit()
    return animal

def delete_animal(animal_id):
    from backend.app import db  # Importation différée
    animal = get_animal(animal_id)
    if animal:
        db.session.delete(animal)
        db.session.commit()
        return True
    return False
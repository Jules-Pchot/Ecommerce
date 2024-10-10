from backend.app import ma
from backend.models.animal import Animal

class AnimalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Animal
        load_instance = True
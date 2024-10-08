from app import ma
from models.animal import Animal

class AnimalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Animal
        load_instance = True
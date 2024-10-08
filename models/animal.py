from app import db  # Assurez-vous que ceci ne cause pas un cycle d'importation

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Animal {self.name}>'
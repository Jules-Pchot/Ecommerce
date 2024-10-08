import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///animal_shop.db'  # ou votre URI de base de données
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your-secret-key'  # à changer en production
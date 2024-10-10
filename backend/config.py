import os

# URI de connexion à la base de données MySQL
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mdpmysql@localhost/Ecommerce'
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your-secret-key'  # à changer en production
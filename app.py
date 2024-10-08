from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')

# Initialiser les extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Importer les blueprints après l'initialisation de l'application
def register_blueprints(app):
    from routes import animals_route, orders_route, users_routes
    app.register_blueprint(animals_route.bp)
    app.register_blueprint(orders_route.bp)
    app.register_blueprint(users_routes.bp)

# Appeler la fonction pour enregistrer les blueprints
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
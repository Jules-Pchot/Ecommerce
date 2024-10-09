from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialiser les extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Importer et enregistrer les blueprints
    with app.app_context():
        from routes import animals_route, orders_route, users_routes
        app.register_blueprint(animals_route.bp)
        app.register_blueprint(orders_route.bp)
        app.register_blueprint(users_routes.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
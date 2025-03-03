from flask import Flask
from flask_restx import Api
<<<<<<< Updated upstream
from app.api.v1.places import api as place_ns
from app.api.v1.users import api as user_ns


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API',
              description='HBnB Application API', doc='/api/v1/')

    # Placeholder for API namespaces (endpoints will be added later)
    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(user_ns, path="/api/v1/users")
    # Additional namespaces for places, reviews, and amenities will
    # be added later
=======
from app.api.v1.users import api as users_namespace  # Import de ton fichier contenant les routes

def create_app():
    app = Flask(__name__)

    # Initialisation de l'API Flask-RESTx
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

    # Enregistrement du namespace pour les utilisateurs
    api.add_namespace(users_namespace, path='/users')
>>>>>>> Stashed changes

    return app


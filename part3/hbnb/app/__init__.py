from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.extensions import db, bcrypt, jwt 
from app.api.v1.places import api as place_ns
from app.api.v1.users import api as user_ns
from app.api.v1.amenities import api as amenity_ns
from app.api.v1.reviews import api as review_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.protected import api as protected_ns
import config
from app.models.user import User

def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialisation des extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Initialisation de l'API
    api = Api(app, version='1.0', title='HBnB API',
              description='HBnB Application API', doc='/api/v1/')

    # Enregistrement des endpoints
    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(user_ns, path="/api/v1/users")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(review_ns, path="/api/v1/reviews")
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(protected_ns, path='/api/v1')

    return app

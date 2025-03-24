from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.extensions import db, bcrypt, jwt
import config
from config import Config

# ✅ Renommé pour éviter conflit avec module app.api
rest_api = Api(
    version='1.0',
    title='HBnB API',
    description='HBnB Application API',
    doc='/api/v1/'
)

def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config.from_object(Config)

    # Initialisation des extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Enregistrement de l'API sur l'app Flask
    rest_api.init_app(app)

    # Enregistrement des namespaces
    from app.api.v1.places import api as place_ns
    from app.api.v1.users import api as user_ns
    from app.api.v1.amenities import api as amenity_ns
    from app.api.v1.reviews import api as review_ns
    from app.api.v1.auth import api as auth_ns
    from app.api.v1.protected import api as protected_ns

    rest_api.add_namespace(place_ns, path="/api/v1/places")
    rest_api.add_namespace(user_ns, path="/api/v1/users")
    rest_api.add_namespace(amenity_ns, path="/api/v1/amenities")
    rest_api.add_namespace(review_ns, path="/api/v1/reviews")
    rest_api.add_namespace(auth_ns, path="/api/v1/auth")
    rest_api.add_namespace(protected_ns, path="/api/v1")

    return app

# ✅ À instancier à la fin
from app.services.facade import HBnBFacade
facade = HBnBFacade()

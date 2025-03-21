from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager

from app.api.v1.places import api as place_ns
from app.api.v1.users import api as user_ns
from app.api.v1.amenities import api as amenity_ns
from app.api.v1.reviews import api as review_ns


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    jwt = JWTManager(app)

    api = Api(app, version='1.0', title='HBnB API',
              description='HBnB Application API', doc='/api/v1/')

    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(user_ns, path="/api/v1/users")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(review_ns, path="/api/v1/reviews")

    return app

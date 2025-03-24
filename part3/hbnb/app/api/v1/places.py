from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
})

place_update_model = api.model('PlaceUpdate', {
    "title": fields.String(),
    "description": fields.String(),
    "number_rooms": fields.Integer(),
    "number_bathrooms": fields.Integer(),
    "max_guest": fields.Integer(),
    "price_by_night": fields.Integer(),
    "price": fields.Float(),
    "latitude": fields.Float(),
    "longitude": fields.Float(),
    "owner_id": fields.String()
})


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model, validate=True)
    @api.response(201, 'Place created successfully')
    @api.response(400, 'Invalid input')
    def post(self):
        """Create a new place"""
        place_data = api.payload
        try:
            new_place = facade.create_place(place_data)
            return {"id": new_place.id}, 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Get all places"""
        places = facade.get_all_places()
        return [{"id": p.id, "title": p.title, "price": p.price} for p in places], 200

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Retrieve a place by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude
        }, 200

    @jwt_required()
    @api.expect(place_update_model, validate=True)
    def put(self, place_id):
        """Update a place"""
        current_user = get_jwt_identity()
        is_admin = current_user.get("is_admin", False)
        user_id = current_user.get("id")

        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        if not is_admin and place.owner_id != user_id:
            return {"error": "Unauthorized action"}, 403

        updated_place = facade.update_place(place_id, api.payload)
        return {"message": "Place updated successfully", "id": updated_place.id}


    @jwt_required()
    def delete(self, place_id):
        """Delete a place"""
        current_user = get_jwt_identity()
        is_admin = current_user.get("is_admin", False)
        user_id = current_user.get("id")

        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        if not is_admin and place.owner_id != user_id:
            return {"error": "Unauthorized action"}, 403

        success = facade.place_repository.delete(place_id)
        if not success:
            return {"error": "Failed to delete place"}, 500
        return {"message": "Place deleted successfully"}, 200

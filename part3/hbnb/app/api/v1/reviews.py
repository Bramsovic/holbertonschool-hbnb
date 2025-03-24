from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from app.services.facade import facade

api = Namespace('reviews', description='Review operations') 

review_ns = Namespace("reviews", description="Review related operations")

review_model = review_ns.model("Review", {
    "content": fields.String(required=True),
    "rating": fields.Integer(required=True),
    "place_id": fields.String(required=True),
    "user_id": fields.String(required=True)
})

review_update_model = review_ns.model("ReviewUpdate", {
    "content": fields.String(),
    "rating": fields.Integer()
})

@review_ns.route('/')
class ReviewListResource(Resource):
    @jwt_required()
    def get(self):
        """Get all reviews"""
        reviews = facade.get_all_reviews()
        return [review.to_dict() for review in reviews], 200

    @jwt_required()
    @review_ns.expect(review_model, validate=True)
    def post(self):
        """Create a new review"""
        current_user = get_jwt_identity()
        user_id = current_user.get("id")
        data = request.get_json()

        if data["user_id"] != user_id:
            return {"error": "You can only create reviews for yourself"}, 403

        place = facade.get_place(data["place_id"])
        if not place:
            return {"error": "Place not found"}, 404

        if place.owner_id == user_id:
            return {"message": "You cannot review your own place"}, 400

        review = facade.create_review(data)
        return {"message": "Review created successfully", "id": review.id}, 201


@review_ns.route('/<string:review_id>')
class ReviewResource(Resource):
    @jwt_required()
    @review_ns.expect(review_update_model, validate=True)
    def put(self, review_id):
        """Update a review"""
        current_user = get_jwt_identity()
        user_id = current_user.get("id")

        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        if review.user_id != user_id:
            return {"error": "Unauthorized action"}, 403

        updated_review = facade.update_review(review_id, request.get_json())
        return {"message": "Review updated successfully", "id": updated_review.id}, 200

    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        current_user = get_jwt_identity()
        user_id = current_user.get("id")

        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        if review.user_id != user_id:
            return {"error": "Unauthorized action"}, 403

        success = facade.delete_review(review_id)
        if not success:
            return {"error": "Failed to delete review"}, 500

        return {"message": "Review deleted successfully"}, 200

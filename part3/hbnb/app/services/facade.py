#!/usr/bin/env python3
"""
Module defining the HBnBFacade class to manage user, place, review, and
amenity storage and operations.
"""

from datetime import datetime
from app.persistence.repository import user_repository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import (
    user_repository,
    amenity_repository,
    place_repository,
    review_repository
)

class HBnBFacade:
    """
    Facade class to interact with the repositories (User, Place, Review, Amenity).
    """

    def __init__(self):
        self.user_repo = user_repository

    # ------------------ USERS ------------------
    def create_user(self, user_data):
        user = User(**user_data)
        user_repository.add(user)
        return user

    def get_user(self, user_id):
        return user_repository.get(user_id)

    def get_user_by_email(self, email):
        return user_repository.get_by_attribute('email', email)

    def update_user(self, user_id, update_data):
        user = user_repository.get(user_id)
        if user is None:
            return None
        for key, value in update_data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        user.updated_at = datetime.utcnow()
        return user_repository.update(user_id, update_data)
    
    def delete_user(self, user_id):
        """
        Deletes a user by their unique ID.

        Args:
            user_id (str): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted, False otherwise.
        """
        return self.user_repo.delete(user_id)


    def get_all_users(self):
        return user_repository.get_all()

    # ------------------ ADMIN USERS ------------------
    def create_user_admin(self, data):
        user = User(**data)
        user_repository.add(user)
        return user

    def update_user_admin(self, user_id, data):
        return user_repository.update(user_id, data)

    # ------------------ PLACES ------------------
    def create_place(self, place_data):
        price = place_data.get("price")
        latitude = place_data.get("latitude")
        longitude = place_data.get("longitude")

        if price is None or price < 0:
            raise ValueError("Price must be a non-negative float")
        if latitude is None or not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if longitude is None or not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180")

        place = Place(**place_data)
        place_repository.add(place)
        return place

    def get_place(self, place_id):
        return place_repository.get(place_id)

    def get_all_places(self):
        return place_repository.get_all()

    def update_place(self, place_id, place_data):
        place = place_repository.get(place_id)
        if not place:
            return None
        for key, value in place_data.items():
            if hasattr(place, key):
                setattr(place, key, value)
        return place_repository.update(place_id, place_data)

    # ------------------ ADMIN PLACES ------------------
    def update_any_place_admin(self, place_id, data, is_admin, user_id):
        place = place_repository.get(place_id)
        if not place:
            return None
        if not is_admin and place.owner_id != user_id:
            return {"error": "Unauthorized action"}, 403
        return place_repository.update(place_id, data)

    # ------------------ REVIEWS ------------------
    def create_review(self, review_data):
        review = Review(**review_data)
        review_repository.add(review)
        return review

    def get_review(self, review_id):
        review = review_repository.get(review_id)
        if not review:
            raise ValueError("Review does not exist")
        return review

    def get_all_reviews(self):
        return self.review_repository.get_all()

    def get_reviews_by_place(self, place_id):
        return review_repository.get_by_attribute("place_id", place_id)

    def update_review(self, review_id, review_data):
        review = review_repository.get(review_id)
        if not review:
            raise ValueError("Review does not exist")
        for key, value in review_data.items():
            if hasattr(review, key):
                setattr(review, key, value)
        return review_repository.update(review_id, review_data)

    def delete_review(self, review_id):
        review = review_repository.get(review_id)
        if not review:
            raise ValueError("Review does not exist")
        return review_repository.delete(review_id)

    # ------------------ ADMIN REVIEWS ------------------
    def update_any_review_admin(self, review_id, data, is_admin, user_id):
        review = review_repository.get(review_id)
        if not review:
            return None
        if not is_admin and review.user_id != user_id:
            return {"error": "Unauthorized action"}, 403
        return review_repository.update(review_id, data)

    # ------------------ AMENITIES ------------------
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        amenity_repository.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return amenity_repository.get(amenity_id)

    def get_all_amenities(self):
        return amenity_repository.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = amenity_repository.get(amenity_id)
        if amenity is None:
            return None
        for key, value in amenity_data.items():
            if hasattr(amenity, key):
                setattr(amenity, key, value)
        return amenity_repository.update(amenity_id, amenity_data)

    # ------------------ ADMIN AMENITIES ------------------
    def create_amenity_admin(self, data):
        amenity = Amenity(**data)
        amenity_repository.add(amenity)
        return amenity

    def update_amenity_admin(self, amenity_id, data):
        return amenity_repository.update(amenity_id, data)

facade = HBnBFacade()

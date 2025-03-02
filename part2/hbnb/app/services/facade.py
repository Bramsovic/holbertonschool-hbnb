#!/usr/bin/env python3
"""
Module defining the HBnBFacade class to manage user, place, review, and
amenity storage and operations.
"""

from app.models.user import User
from app.models.place import Place
from datetime import datetime
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    """
    Facade class to interact with the repositories (User, Place, Review,
    Amenity).
    """

    def __init__(self):
        """
        Initializes the Facade with separate InMemoryRepository instances for
        each entity.
        """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        """
        Creates a new user and adds it to the repository.

        Args:
            user_data (dict): Dictionary containing user details.

        Returns:
            User: The newly created user.
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        Retrieves a user by their unique ID.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            User or None: The user instance if found, otherwise None.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        Retrieves a user by their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            User or None: The user instance if found, otherwise None.
        """
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, update_data):
        """
        Updates user attributes based on the provided data.

        Args:
            user_id (str): The unique identifier of the user to update.
            update_data (dict): Dictionary containing the attributes to update.

        Returns:
            User or None: The updated user instance if found, otherwise None.
        """
        user = self.user_repo.get(user_id)
        if user is None:
            return None

        for key, value in update_data.items():
            if hasattr(user, key):
                setattr(user, key, value)

        user.updated_at = datetime.utcnow()
        self.user_repo.update(user)
        return user

    def get_all_users(self):
        """Retrieves all users"""
        return self.user_repo.get_all()

    # Place methods
    def create_place(self, place_data):
        """Creates a new place (logic to be implemented later)."""
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
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Retrieves a place by its ID."""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Retrieves all place"""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Update a place"""
        place = self.place_repo.get(place_id)
        if not place:
            return None
        for key, value in place_data.items():
            if hasattr(place, key):
                setattr(place, key, value)
        self.place_repo.update(place)
        return {"message": "Place updated successfully"}, 200

    def create_review(self, review_data):
        """Creates a new review (logic to be implemented later)."""
        pass

    def get_review(self, review_id):
        """Retrieves a review by its ID (logic to be implemented later)."""
        pass

    def create_amenity(self, amenity_data):
        """Creates a new amenity (logic to be implemented later)."""
        pass

    def get_amenity(self, amenity_id):
        """Retrieves an amenity by its ID (logic to be implemented later)."""
        pass

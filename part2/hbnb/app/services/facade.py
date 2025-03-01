#!/usr/bin/env python3
"""
Module defining the HBnBFacade class to manage user, place, review, and amenity storage and operations.
"""

from app.models.user import User
from datetime import datetime
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    """
    Facade class to interact with the repositories (User, Place, Review, Amenity).
    """

    def __init__(self):
        """
        Initializes the Facade with separate InMemoryRepository instances for each entity.
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


    def create_place(self, place_data):
        """Creates a new place (logic to be implemented later)."""
        pass

    def get_place(self, place_id):
        """Retrieves a place by its ID (logic to be implemented later)."""
        pass

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
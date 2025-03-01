#!/usr/bin/env python3
"""
Module defining the HBnBFacade class to manage user storage and operations.
"""

from models.user import User
from datetime import datetime
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    """
    Facade class to interact with the user repository.
    """

    def __init__(self):
        """
        Initializes the Facade with an InMemoryRepository instance.
        """
        self.user_repo = InMemoryRepository()

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

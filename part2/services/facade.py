#!/usr/bin/env python3
"""
Module defining the UserRepository class for managing user storage and operations.
"""

from models.user import User
from datetime import datetime


class UserRepository:
    """
    Repository class for managing User instances.
    """

    def __init__(self):
        """
        Initializes an empty user repository.
        """
        self.users = {}

    def create_user(self, user_data):
        """
        Creates a new user if the email does not already exist in the repository.
        Args:
            user_data (dict): Dictionary containing user details (first_name, last_name, email).
        Returns:
            User: The newly created user or an existing user if the email is already in use.
        """
        for user in self.users.values():
            if user.email == user_data['email']:
                return user
        new_user = User(
            user_data['first_name'], 
            user_data['last_name'], 
            user_data['email']
        )
        self.users[new_user.id] = new_user
        return new_user

    def get_user(self, user_id):
        """
        Retrieves a user by their unique ID.
        Args:
            user_id (str): The unique identifier of the user.
        Returns:
            User or None: The user instance if found, otherwise None.
        """
        return self.users.get(user_id, None)
    
    def get_user_by_email(self, email):
        """
        Retrieves a user by their email address.
        Args:
            email (str): The email address of the user.
        Returns:
            User or None: The user instance if found, otherwise None.
        """
        if not email:
            return None
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    def update_user(self, user_id, update_data):
        """
        Updates user attributes based on the provided data.
        Args:
            user_id (str): The unique identifier of the user to update.
            update_data (dict): Dictionary containing the attributes to update.
        Returns:
            User or None: The updated user instance if found, otherwise None.
        """
        user = self.get_user(user_id)
        if user is None:
            return None  

        for key, value in update_data.items():
            if hasattr(user, key):
                setattr(user, key, value)

        user.updated_at = datetime.utcnow()
        return user

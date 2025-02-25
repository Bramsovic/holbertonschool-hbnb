#!/usr/bin/env python3
"""
Module defining the UserRepository class for managing user storage and retrieval.
"""

from datetime import datetime

class UserRepository:
    """
    Repository class for storing and managing User instances.
    """

    def __init__(self):
        """
        Initializes an empty user repository.
        """
        self.users = {}

    def add(self, user):
        """
        Adds a user to the repository.

        Args:
            user (User): The user instance to be added.
        """
        self.users[user.id] = user
    
    def get(self, user_id):
        """
        Retrieves a user by their unique ID.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            User or None: The user instance if found, otherwise None.
        """
        return self.users.get(user_id, None)

    def get_by_email(self, email):
        """
        Retrieves a user by their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            User or None: The user instance if found, otherwise None.
        """
        for user in self.users.values():
            if user.email == email:
                return user
        return None 
    
    def update(self, user):
        """
        Updates an existing user in the repository.

        Args:
            user (User): The user instance with updated data.

        Returns:
            User or None: The updated user instance if found, otherwise None.
        """
        if user.id in self.users:
            user.updated_at = datetime.utcnow()
            self.users[user.id] = user
            return user
        else:
            return None

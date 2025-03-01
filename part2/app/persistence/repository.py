#!/usr/bin/env python3
"""
Module defining the UserRepository class for managing user storage and retrieval.
"""

from datetime import datetime
from abc import ABC, abstractmethod
from app.models.user import User


class Repository(ABC):
    """
    Abstract Base Class for a generic repository.
    """

    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    """
    Concrete implementation of the Repository class for storing and managing User instances in-memory.
    """

    def __init__(self):
        """
        Initializes an empty in-memory user repository.
        """
        self._storage = {}

    def add(self, user):
        """
        Adds a user to the repository.

        Args:
            user (User): The user instance to be added.
        """
        self._storage[user.id] = user

    def get(self, user_id):
        """
        Retrieves a user by their unique ID.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            User or None: The user instance if found, otherwise None.
        """
        return self._storage.get(user_id)

    def get_all(self):
        """
        Retrieves all users from the repository.

        Returns:
            list: A list of all User instances.
        """
        return list(self._storage.values())

    def update(self, user_id, data):
        """
        Updates an existing user in the repository.

        Args:
            user_id (str): The unique identifier of the user to update.
            data (dict): Dictionary containing updated attributes.

        Returns:
            User or None: The updated user instance if found, otherwise None.
        """
        user = self.get(user_id)
        if user:
            for key, value in data.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            user.updated_at = datetime.utcnow()
            return user
        return None

    def delete(self, user_id):
        """
        Deletes a user from the repository.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            bool: True if the user was deleted, False otherwise.
        """
        if user_id in self._storage:
            del self._storage[user_id]
            return True
        return False

    def get_by_attribute(self, attr_name, attr_value):
        """
        Retrieves a user by a specific attribute.

        Args:
            attr_name (str): The attribute name to search by.
            attr_value (str): The attribute value to search for.

        Returns:
            User or None: The user instance if found, otherwise None.
        """
        return next((user for user in self._storage.values() if getattr(user, attr_name, None) == attr_value), None)

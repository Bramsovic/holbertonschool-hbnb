#!/usr/bin/env python3
"""
Module defining the User class for managing user information.
"""

from .base_model import BaseModel
from datetime import datetime
from app import bcrypt


class User(BaseModel):
    """
    Represents a system user with personal
    information, timestamps, and relationships.

    Attributes:
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        email (str): User's email address.
        is_admin (bool): Indicates whether
        the user has administrative privileges.
        places (list): List of places owned by the user.
    """

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """
        Initializes a new user with a unique ID and personal information.

        Args:
            first_name (str): First name of the user (max 50 chars).
            last_name (str): Last name of the user (max 50 chars).
            email (str): User's email address.
            is_admin (bool, optional): Indicates if the user
            is an admin. Defaults to False.
        """
        super().__init__()  # Call parent to generate UUID & timestamps

        if len(first_name) > 50 or len(last_name) > 50:
            raise ValueError(
                "First and last names must be less than 50 characters")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.places = []  # List to store places owned by the user

    def add_place(self, place):
        """
        Adds a place to the user's list of places.

        Args:
            place (Place): The place to be added.
        """
        self.places.append(place)

    def update(self):
        """
        Updates the `updated_at` timestamp to the current time.
        """
        self.updated_at = datetime.utcnow()

    def hash_password(self, password):
        """
        Hashes the password before storing it.
        """
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """
        Verifies if the provided password matches the hashed password.
        """
        return bcrypt.check_password_hash(self.password, password)

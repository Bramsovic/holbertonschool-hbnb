#!/usr/bin/env python3
"""
Module defining the User class for managing user information.
"""

from app import db
from .base_model import BaseModel
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
import re


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

    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    _password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    @validates("first_name", "last_name")
    def validate_name(self, key, value):
        """
        Check the lenght of first and last name

        Args:
            key (string): field when you add the value
            value (string): the value add

        Raises:
            ValueError: error message for indicate the good format
        """
        if len(value) > 50:
            raise ValueError(
                "First and last names must be less than 50 characters")

    @validates("email")
    def validate_email(self, key, value):
        """
        Check format email

        Args:
            key (string): field when you add the value
            value (string): Value for the check

        Raises:
            ValueError: error message format invalid

        Returns:
            string: Convert email to lowercase to avoid duplicates
        """
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, value):
            raise ValueError("Email invalid")
        return value.lower()

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

    @hybrid_property
    def password(self):
        raise AttributeError("The password cannot be read directly.")

    @password.setter
    def password(self, password):
        """
        Hashes the password before storing it.
        """
        from app import bcrypt

        pass_regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

        if " " in password:
            raise ValueError("Password need don't contain a space")
        if not re.match(pass_regex, password):
            raise ValueError(
                "The password must contain at least 8 characters, "
                "one capital letter, one number, and one special character."
            )

        self._password = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def verify_password(self, password):
        """
        Verifies if the provided password matches the hashed password.
        """
        from app import bcrypt
        return bcrypt.check_password_hash(self._password, password)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, is_admin={self.is_admin})>"

#!/usr/bin/env python3
"""
Module defining the User class for managing user information.
"""

from app.extensions import db, bcrypt
from datetime import datetime
from .base_model import BaseModel


class User(BaseModel, db.Model):
    """
    Represents a system user with personal
    information, timestamps, and relationships.

    Attributes:
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        email (str): User's email address.
        password (str): Hashed password.
        is_admin (bool): Indicates whether the user has administrative privileges.
    """

    __tablename__ = "users"

    id = db.Column(db.String(60), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """
        Initializes a new user with a unique ID and personal information.
        """
        super().__init__()  # Generates id, created_at, updated_at
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    @classmethod
    def hash_password(cls, raw_password):
        """
        Hashes the password before storing it.
        """
        return bcrypt.generate_password_hash(raw_password).decode('utf-8')

    def verify_password(self, input_password):
        """
        Verifies if the provided password matches the hashed password.
        """
        return bcrypt.check_password_hash(self.password, input_password)

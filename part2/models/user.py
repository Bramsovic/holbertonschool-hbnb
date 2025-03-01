#!/usr/bin/env python3
"""
Module defining the User class for managing user information.
"""

import uuid
from datetime import datetime

class User:
    """
    Represents a user with personal information and timestamps for creation and updates.

    Attributes:
        id (str): Unique identifier for the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        email (str): User's email address.
        created_at (datetime): Timestamp of user creation.
        updated_at (datetime): Timestamp of the last user update.
    """

    def __init__(self, first_name, last_name, email, created_at=None, updated_at=None):
        """
        Initializes a new user with a unique ID and personal information.

        Args:
            first_name (str): First name of the user.
            last_name (str): Last name of the user.
            email (str): User's email address.
            created_at (datetime, optional): Creation timestamp (default: datetime.utcnow()).
            updated_at (datetime, optional): Last update timestamp (default: datetime.utcnow()).
        """
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_at = updated_at if updated_at is not None else datetime.utcnow()

    def update(self):
        """
        Updates the `updated_at` timestamp to the current time.
        """
        self.updated_at = datetime.utcnow()

#!/usr/bin/env python3
"""
Module defining the HBnBFacade class to manage user, place, review, and
amenity storage and operations.
"""

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from datetime import datetime
from app.persistence.repository import InMemoryRepository
from app.models.amenity import Amenity


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
        self.user_repo.update(user_id, update_data)
        return user

    def get_all_users(self):
        """Retrieves all users"""
        return self.user_repo.get_all()

    # Place methods
    def create_place(self, place_data):
        """
        Creates a new place.

        Args:
            place_data (dict): Dictionary containing place details.

        Raises:
            ValueError: For negative float price.
            ValueError: For latitude outside of -90 to 90.
            ValueError: For longitude outside of -180 to 180.

        Returns:
            place: The newly created place.
        """
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
        """
        Retrieves a place by its ID.

        Args:
            place_id (str): The unique identifier of the place.

        Returns:
            place: The place instance if found.
        """
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """
        Retrieves all place.

        Returns:
            place: The place instance if found.
        """
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """
        Update a place.

        Args:
            place_id (str): The unique identifier of the place.
            place_data (dict): Dictionary containing place details.

        Returns:
            place or None: The updated place instance if found, otherwise None.
        """
        place = self.place_repo.get(place_id)
        if not place:
            return None
        for key, value in place_data.items():
            if hasattr(place, key):
                setattr(place, key, value)
        self.place_repo.update(place_id, place.to_dict())
        return place

    # Review methods
    def create_review(self, review_data):
        """Creates a new review."""
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        """Retrieves a review by its ID."""
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review does not exist")
        return review

    def get_all_reviews(self):
        """Retrieves all reviews."""
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        """Retrieves all reviews for a place."""
        return self.review_repo.get_by_attribute("place_id", place_id)

    def update_review(self, review_id, review_data):
        """Updates a review."""
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review does not exist")

        if "text" in review_data:
            review.text = review_data["text"]
        if "rating" in review_data:
            review.rating = review_data["rating"]

        return self.review_repo.update(review_id)

    def delete_review(self, review_id):
        """Deletes a review."""
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review does not exist")
        return self.review_repo.delete(review_id)

    def create_amenity(self, amenity_data):
        """
        Creates a new amenity and adds it to the repository.

        Args:
            amenity_data (dict): Dictionary containing amenity details.

        Returns:
            Amenity: The newly created amenity.
        """
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """
        Retrieves an amenity by its unique ID.

        Args:
            amenity_id (str): The unique identifier of the amenity.

        Returns:
            Amenity or None: The amenity instance if found, otherwise None.
        """
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """
        Retrieves all amenities from the repository.

        Returns:
            list: A list of all Amenity instances.
        """
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """
        Updates an amenity's attributes based on the provided data.

        Args:
            amenity_id (str): The unique identifier of the amenity to update.
            amenity_data (dict): Dictionary containing
            the attributes to update.

        Returns:
            Amenity or None: The updated amenity instance if found,
            otherwise None.
        """
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            return None

        for key, value in amenity_data.items():
            if hasattr(amenity, key):
                setattr(amenity, key, value)

        self.amenity_repo.update(amenity, amenity_data)
        return amenity

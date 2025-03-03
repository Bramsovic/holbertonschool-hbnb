from .base_model import BaseModel


class Place(BaseModel):
    """Represents a location might be rented"""

    def __init__(self, title, description, price, latitude,
                 longitude, owner_id):
        super().__init__()

        if len(title) > 100:
            raise ValueError("Title must be less than 100 characters")
        if price <= 0:
            raise ValueError("Price must be positive")
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """Add an review to the list of place reviews"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the list of place amenities"""
        self.amenities.append(amenity)

    def to_dict(self):
        """Convert the Place object to a dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
        }

from .base_model import BaseModel
from app.extensions import db
from uuid import uuid4

class Place(BaseModel, db.Model):
    """Represents a location might be rented"""

    __tablename__ = 'places'

    id = db.Column(db.String(60), primary_key=True, default=lambda: str(uuid4()))
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    number_rooms = db.Column(db.Integer, nullable=False)
    number_bathrooms = db.Column(db.Integer, nullable=False)
    max_guest = db.Column(db.Integer, nullable=False)
    price_by_night = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

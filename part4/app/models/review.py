from app import db
from sqlalchemy.orm import validates, relationship
from .base_model import BaseModel


class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)

    user = relationship("User", back_populates="reviews")
    place = relationship("Place", back_populates="reviews")

    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    @validates('text')
    def validate_text(self, key, text):
        if not text or text.strip() == "":
            raise ValueError("Review text cannot be empty")
        return text

    @validates('rating')
    def validate_rating(self, key, rating):
        try:
            rating = int(rating)
            if not (1 <= rating <= 5):
                raise ValueError("Rating must be an integer between 1 and 5")
        except (ValueError, TypeError):
            raise ValueError("Rating must be an integer between 1 and 5")
        return rating

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def to_dict_basic(self):
        return {
            'text': self.text,
            'rating': self.rating,
            'user': {
                'first_name': self.user.first_name if self.user else "Utilisateur",
                'last_name': self.user.last_name if self.user else ""
            }
        }

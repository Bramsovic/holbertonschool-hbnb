from .base_model import BaseModel


class Review(BaseModel):
    """Represent an review by the user on the place"""

    def __init__(self, text, rating, user_id, place_id):
        super().__init__()

        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        self.text = text
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id

from .base_model import BaseModel
from datetime import datetime, timezone

class Amenity(BaseModel):
    """Represent an amenity of a place"""
    
    def __init__(self, name):
        super().__init__()

        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        
        self.name = name
        self.updated_at = datetime.now(timezone.utc)

    def update(self, name=None):
        """
        Update the amenity attributes and refresh the updated_at timestamp.

        Args:
            name (str, optional): The new name for the amenity.
        """
        if name:
            if len(name) > 50:
                raise ValueError("Name must be less than 50 characters")
            self.name = name
        self.updated_at = datetime.now(timezone.utc)

from .base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity of a place"""
    
    def __init__(self, name):
        super().__init__()

        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        
        self.name = name

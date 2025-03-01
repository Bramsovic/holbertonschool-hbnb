from .base_model import BaseModel


class User(BaseModel):
    """Represents a system user"""
    
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        if len(first_name) > 50 or len(last_name) > 50:
            raise ValueError("Name must be less than 50 characters")
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
    
    def add_place(self, place):
        """Add a place to the list of place from the user"""
        self.places.append(place)

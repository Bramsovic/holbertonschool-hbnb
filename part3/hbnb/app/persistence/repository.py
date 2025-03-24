from datetime import datetime
from abc import ABC, abstractmethod
from app.extensions import db 
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        return self.model.query.all()

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()
            return obj
        return None

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
            return True
        return False

    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter_by(**{attr_name: attr_value}).first()

# Specific repositories
user_repository = SQLAlchemyRepository(User)
amenity_repository = SQLAlchemyRepository(Amenity)
place_repository = SQLAlchemyRepository(Place)
review_repository = SQLAlchemyRepository(Review)

# User methods
def create_user(data):
    new_user = User(
        email=data.get("email"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        password=data.get("password"),
        is_admin=data.get("is_admin", False)
    )
    user_repository.add(new_user)
    return new_user

def update_user(user_id, data):
    return user_repository.update(user_id, data)

# Amenity methods
def create_amenity(data):
    new_amenity = Amenity(name=data.get("name"))
    amenity_repository.add(new_amenity)
    return new_amenity

def update_amenity(amenity_id, data):
    return amenity_repository.update(amenity_id, data)

# Place methods
def update_place(place_id, data):
    return place_repository.update(place_id, data)

# Review methods
def update_review(review_id, data):
    return review_repository.update(review_id, data)

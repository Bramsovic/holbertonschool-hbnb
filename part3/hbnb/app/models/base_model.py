import uuid
from datetime import datetime
from app.extensions import db



class BaseModel:

    id = db.Column(db.String(60), primary_key=True, default=lambda: str(uuid4()))

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.created_at = kwargs.get("created_at", datetime.now())
        self.updated_at = kwargs.get("updated_at", datetime.now())

        for key, value in kwargs.items():
            if key not in ("id", "created_at", "updated_at"):
                setattr(self, key, value)

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object
        based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp

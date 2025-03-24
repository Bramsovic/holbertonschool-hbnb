from app.models.user import User
from app.extensions import db

class UserRepository:
    def __init__(self):
        self.model = User

    def add(self, user):
        """Add an user to the db"""
        db.session.add(user)
        db.session.commit()

    def get(self, user_id):
        """Get an user by his ID"""
        return self.model.query.get(user_id)

    def get_user_by_email(self, email):
        """Get an user by his email"""
        return self.model.query.filter_by(email=email).first()

    def get_all(self):
        """Get all users"""
        return self.model.query.all()

    def delete(self, user):
        """Delete an user from the db"""
        db.session.delete(user)
        db.session.commit()

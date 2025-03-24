from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from app.services.auth_utils import admin_required

facade = HBnBFacade()

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True,
                                description='First name of the user'),
    'last_name': fields.String(required=True,
                               description='Last name of the user'),
    'email': fields.String(required=True,
                           description='Email of the user'),
    'password': fields.String(required=True,
                              description='Password of the user')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        user_data['password'] = User.hash_password(user_data['password'])

        new_user = facade.create_user(user_data)
        return {
            'id': new_user.id,
            'message': 'User successfully created'
        }, 201

    @api.response(200, 'Users list retrieved successfully')
    def get(self):
        """Retrieve the list of all users"""
        users = facade.get_all_users()
        return [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        } for user in users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, user_id):
        """Update user details"""
        current_user = get_jwt_identity()
        if str(user_id) != str(current_user["id"]):
            return {'error': 'Unauthorized action'}, 403

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        data = api.payload
        if "email" in data or "password" in data:
            return {'error': 'You cannot modify email or password'}, 400

        updated_user = facade.update_user(user_id, data)
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200

    @api.response(200, 'User successfully deleted')
    @api.response(404, 'User not found')
    @api.response(403, 'Unauthorized action')
    @api.response(500, 'Failed to delete user')
    @jwt_required()
    def delete(self, user_id):
        """Delete a user account"""
        current_user = get_jwt_identity()

        if str(user_id) != str(current_user["id"]):
            return {'error': 'Unauthorized action'}, 403

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        deleted = facade.delete_user(user_id)

        if not deleted:
            return {'error': 'Failed to delete user'}, 500

        return {'message': 'User deleted successfully'}, 200

@api.route('/admin')
class AdminUserCreate(Resource):
    #@jwt_required()
    #@admin_required
    def post(self):
        """Admin: Create a new user (with optional is_admin)"""
        user_data = request.json
        email = user_data.get('email')

        if not email:
            return {'error': 'Email is required'}, 400

        existing_user = facade.get_user_by_email(email)
        if existing_user:
            return {'error': 'Email already registered'}, 400

        user_data['password'] = User.hash_password(user_data['password'])
        new_user = facade.create_user_admin(user_data)
        return {'id': new_user.id, 'email': new_user.email}, 201

@api.route('/admin/<string:user_id>')
class AdminUserUpdate(Resource):
    @jwt_required()
    @admin_required
    def put(self, user_id):
        """Admin: Update any user's information"""
        data = request.json
        email = data.get('email')

        if email:
            existing = facade.get_user_by_email(email)
            if existing and existing.id != user_id:
                return {'error': 'Email already in use'}, 400

        if 'password' in data:
            data['password'] = User.hash_password(data['password'])

        updated = facade.update_user_admin(user_id, data)
        if not updated:
            return {'error': 'User not found'}, 404

        return {'message': 'User updated successfully'}

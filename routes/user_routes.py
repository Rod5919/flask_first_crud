from flask import Blueprint, request, redirect, jsonify
from controllers.user_controller import create_user, get_all_users, get_one_user, patch_user, delete_user

user_routes = Blueprint('user_routes', __name__)

## Get all users
@user_routes.route('/', methods=['GET'])
def get_all():
    # Query params: limit, offset
    limit = request.args.get('limit', 10)
    offset = request.args.get('offset', 0)
    
    users = get_all_users(limit, offset)
        
    return jsonify({'users': users})

## Get single user
@user_routes.route('/<id>', methods=['GET'])
def get_one(id):
    user = get_one_user(id)
    
    if not user:
        return jsonify({'message': 'No user found!'})
    
    return jsonify({'user': user})

## Create user
@user_routes.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    phone_number = request.form.get('phone_number')
    
    create_user(name, email, password, phone_number)
    
    return redirect('/')

## Patch user
@user_routes.route('/<id>', methods=['PATCH'])
def patch(id):
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    phone_number = request.json.get('phone_number')
    
    user = patch_user(id, name, email, password, phone_number)
    
    if not user:
        return jsonify({'message': 'No user found!'})
    
    return jsonify({'message': f"User {user.id} updated successfully!"})

## Delete user
@user_routes.route('/<id>', methods=['DELETE'])
def delete(id):
    user = delete_user(id)
    
    if not user:
        return jsonify({'message': 'No user found!'})
    
    return jsonify({'message': f"User {user.id} deleted successfully!"})
#!/usr/bin/python3
"""Handles the RESTFul API actions for the state object"""


import app_views from api.v1.views
import jsonify, abort, request, make_response from flask
import storage from models
import User from models.user


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():"""
    retrieves a list of all users"""
    all_users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(all_users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves user by id"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.todict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a user"""
    user = storage.get(User, user_id)
    if user = None:
        abort(404)
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ Create a user"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if ('email' not in request.get_json():
        abort(400, description="Missing email")
    if ('password' not in request.get_json():
        abort(400, description="Missing password")
    data = request.get_json()
    new_user = State(**data)
    new_user.save()
    return make_response(jsonify(new_user.to_dict()), 201)

@app_views.route('users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update a user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)

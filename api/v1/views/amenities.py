#!/usr/bin/python3
"""Handles the RESTFul API actions for the state object"""


import app_views from api.v1.views
import jsonify, abort, request, make_response from flask
import storage from models
import Amenity from models.amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_all_amenities():
    """retrieves a list of all amenities"""
    all_amenities = [amenity.to_dict() for amenity in storage.all(Amenity).values()]
    return jsonify(all_amenities)

@app_views.route('/amenities/<amenity_id>/', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):"""
    Retrieves amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.todict())

@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """Delete a amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity = None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_aminity():
    """ Create a amenity"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    new_amenity = Amenity(**data)
    new_amenity.save()
    return make_response(jsonify(new_amenity.to_dict()), 201)

@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    """Update a amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 200)

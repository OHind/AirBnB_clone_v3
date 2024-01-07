#!/usr/bin/python3
"""Handles the RESTFul API actions for the city object"""


import app_views from api.v1.views
import jsonify, abort, request, make_response from flask
import storage from models
import State from models.state
import City from models.city
import Place from models.place
import User from models.user
import Amnity from models.amenity


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_all_places(city_id):
    """retrieves a list of all places within a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    all_places = [place.to_dict() for place in city.places]
    return jsonify(all_places)

@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """Retrieves place by id"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.todict())

@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """Delete a place"""
    place = storage.get(Place, place_id)
    if place = None:
        abort(404)
    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """ Create a place within a city"""
    city = storage.get(City, city_id)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")
    data = request.get_json()
    user = storage.get(user, data['user_id']
    if not user:
        abort(400, description="Missing name")
    data["city_id"] = city_id
    new_place = Place(**data)
    new_place.save()
    return make_response(jsonify(new_place.to_dict()), 201)

@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Update a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)

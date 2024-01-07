#!/usr/bin/python3
"""Handles the RESTFul API actions for the city object"""


import app_views from api.v1.views
import jsonify, abort, request, make_response from flask
import storage from models
import State from models.state
import City from models.city


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_all_cities(state_id):
    """retrieves a list of all cities"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    all_cities = [city.to_dict() for city in state.cities]
    return jsonify(all_cities)

@app_views.route('cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves city by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.todict())

@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Delete a city"""
    city = storage.get(City, city_id)
    if city = None:
        abort(404)
    storage.delete(city)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """ Create a city within a state"""
    state = storage.get(State, state_id)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    new_city = City(**data)
    new_city.state_id = state.id
    new_city.save()
    return make_response(jsonify(new_city.to_dict()), 201)

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_state(city_id):
    """Update a city"""
    city = storage.get(city, city_id)
    if not city:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)

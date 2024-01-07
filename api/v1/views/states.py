#!/usr/bin/python3
"""Handles the RESTFul API actions for the state object"""


import app_views from api.v1.views
import jsonify, abort, request, make_response from flask
import storage from models
import State from models.state


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """
    retrieves a list of all states
    """
    all_states = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(all_states)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """
    Retrieves state by id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.todict())

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Delete a state"""
    state = storage.get(State, state_id)
    if state = None:
        abort(404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ Create a state"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    new_state = State(**data)
    new_state.save()
    return make_response(jsonify(new_state.to_dict()), 201)

@app_views.route('states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Update a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated']:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)

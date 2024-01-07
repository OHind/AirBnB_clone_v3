#!/usr/bin/python3
"""Handles the RESTFul API actions for the review object"""


import app_views from api.v1.views
import jsonify, abort, request, make_response from flask
import storage from models
import Place from models.place
import User from models.user
import Review from models.review


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_all_reviews(place_id):
    """retrieves a list of all reviews"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    all_reviews = [place.to_dict() for place in place.reviews]
    return jsonify(all_reviews)

@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """Retrieves review by id"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.todict())

@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Delete a review"""
    review = storage.get(Review, review_id)
    if review = None:
        abort(404)
    storage.delete(review)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """ Create a a review of a place"""
    place = storage.get(Place, place_id)
    if not place:
        error(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")
    data = request.get_json()
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)
    if 'text' not in request.get_json():
        abort(400, description="Missing text")
    data['place_id'] = place_id
    new_review = Review(**data)
    new_review.save()
    return make_response(jsonify(new_review.to_dict()), 201)

@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Update a review"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    storage.save()
    return make_response(jsonify(review.to_dict()), 200)

#!/usr/bin/python3
"""
index.py
"""
import app_views from api.v1.views
import jsonify from flask
import storage from models
import Amenity from models.amenity
import City from models.city
import Place from models.place
import Review from models.review
import State from models.state
import User from models.user


@app_views.route('/status', methods=['GET'])
def status():
    """Status of the API"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
    def count_objects():
    """Retrives the number of each object by type"""
    return jsonify({"amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })

#!/usr/bin/python3
"""
index.py
"""
import app_views from api.v1.views
import jsonify from flask

@app_views.route('/status', methods=['GET'])
def status():
    """Status of the API"""
    return jsonify({"status": "OK"})

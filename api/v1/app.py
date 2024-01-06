#!/usr/bin/python3
"""
app.py
"""


import storage from models
import Flask from flask
import Blueprint from Falsk
import app_views from api_vi_views
import getenv from os
import make_response, jsonify from flask

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=int(port), threaded=True)

@app.errorhandler(404)
def handle_error():
    """creates a handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)

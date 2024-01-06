#!/usr/bin/python3
"""
app.py
"""


import storage from models
import Flask from flask
import Blueprint from Falsk
import app_views from api_vi_views
import getenv from os

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


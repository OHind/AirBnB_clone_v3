#!/usr/bin/python3
"""Blueprint for API"""
import Flask from flask


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

import * from api.v1.views.index
import * from api.v1.views.state
import * from api.v1.views.cities
import * from api.v1.views.amenities
import * from api.v1.views.users
import * from api.v1.views.places
import * from api.v1.views.places_reviews

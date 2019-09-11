#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app_views.route('/status')
def status():
    """This route returns a json codified message """
    return jsonify(status="OK")


@app_views.route('/api.v1/stats')
def stats():
    """ This script retrieves the number of objects by type """
    dictio = {}
    for clase in classes.keys():
        dictio[clase] = storage.count(clase)
        return dictio

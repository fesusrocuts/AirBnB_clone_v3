#!/usr/bin/python3
""" This file sets the States view"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/states')
def list_states():
    """ This view is for listing all the states"""
    lista = storage.all("State")
    ouch = []
    for items in lista.values():
        ouch.append(items.to_dict())
    return jsonify(ouch)




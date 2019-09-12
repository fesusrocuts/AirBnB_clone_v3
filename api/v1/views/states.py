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


@app_views.route('/states/<state_id>')
def get_states(state_id):
    """ This view is for getting a specific state """
    estadito = storage.get("State", state_id)
    estadito = estadito.to_dict()
    return jsonify(estadito)

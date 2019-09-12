#!/usr/bin/python3
""" This file sets the States view"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage


@app_views.route('/states', methods=['GET'])
def list_states():
    """ This view is for listing all the states"""
    lista = storage.all("State")
    ouch = []
    for items in lista.values():
        ouch.append(items.to_dict())
    return jsonify(ouch)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_states(state_id):
    """ This view is for getting a specific state """
    estadito = storage.get("State", state_id)
    if estadito is None:
        return abort(404)
    estadito = estadito.to_dict()
    return jsonify(estadito)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ This view allows to erase an state"""
    estadito = storage.get("State", state_id)
    if estadito is None:
        return abort(404)
    estadito.delete()
    storage.save()
    dictio = {}
    return dictio, 200

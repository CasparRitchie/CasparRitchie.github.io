from flask import Blueprint, jsonify, request
from gestion_restaurants import (
    ajouter_restaurant, afficher_restaurants, modifier_restaurant, 
    visualiser_restaurant, supprimer_restaurant
)
from flask_cors import CORS

restaurants_api = Blueprint('restaurants_api', __name__)
CORS(restaurants_api, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])

@restaurants_api.route('/', methods=['POST'])
def add_restaurant():
    data = request.json
    result = ajouter_restaurant(data)
    return jsonify(result)

@restaurants_api.route('/', methods=['GET'])
def get_restaurants():
    restaurants = afficher_restaurants()
    return jsonify(restaurants=restaurants)

@restaurants_api.route('/<int:restaurant_id>', methods=['GET'])
def get_specific_restaurant(restaurant_id):
    restaurant = visualiser_restaurant(restaurant_id)
    if restaurant:
        return jsonify(restaurant=restaurant)
    else:
        return jsonify(message="Restaurant not found"), 404

@restaurants_api.route('/<int:restaurant_id>', methods=['PUT'])
def update_restaurant(restaurant_id):
    data = request.json
    result = modifier_restaurant(restaurant_id, data)  # Assuming you modify the function to accept parameters.
    return jsonify(result)

@restaurants_api.route('/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    result = supprimer_restaurant(restaurant_id)  # Assuming you modify the function to accept the restaurant_id parameter.
    return jsonify(result)


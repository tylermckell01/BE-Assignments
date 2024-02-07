from flask import Blueprint, request

import controllers

categories = Blueprint('categories', __name__)

# category CREATE routes
@categories.route('/category', methods=['POST'])
def create_new_category():
    return controllers.create_category(request)


# category READ routes
@categories.route('/categories', methods=['GET'])
def read_all_categories():
    return controllers.read_categories()


@categories.route('/categories/<id>', methods=['GET'])
def read_by_category_id(id):
    return controllers.read_by_category_id(id)


# category UPDATE routes
@categories.route('/category/<id>', methods=['PUT'])
def update_category_name_by_id(id):
    return controllers.update_category_name(request, id)


# category DELETE routes
@categories.route('/category/<id>', methods=['DELETE'])
def delete_category_by_id(id):
    return controllers.delete_category(id)

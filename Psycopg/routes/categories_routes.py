from flask import Blueprint

import controllers

categories = Blueprint('categories', __name__)

# category CREATE routes
@categories.route('/categories', methods=['POST'])
def create_new_category():
    return controllers.create_category()


# category READ routes
@categories.route('/categories', methods=['GET'])
def read_all_categories():
    return controllers.read_categories()


@categories.route('/categories/<id>', methods=['GET'])
def read_by_category_id(id):
    return controllers.read_by_category_id(id)


# category UPDATE routes
@categories.route('/categories/<id>', methods=['PUT'])
def update_category_name_by_id(id):
    return controllers.update_category_name(id)
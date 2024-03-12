from flask import Blueprint, request

import controllers

exercises = Blueprint('exercises', __name__)

# category CREATE routes


@exercises.route('/category', methods=['POST'])
def create_new_category():
    return controllers.create_category(request)


# category READ routes
@exercises.route('/categories', methods=['GET'])
def read_all_categories():
    return controllers.read_categories(request)


@exercises.route('/category/<id>', methods=['GET'])
def read_by_category_id(id):
    return controllers.read_by_category_id(request, id)


# category UPDATE routes
@exercises.route('/category/<id>', methods=['PUT'])
def update_category_name_by_id(id):
    return controllers.update_category_name(request, id)


# category DELETE routes
@exercises.route('/category/delete/<id>', methods=['DELETE'])
def delete_category_by_id(id):
    return controllers.delete_category(request, id)

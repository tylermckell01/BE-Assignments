from flask import Blueprint, request

import controllers

workout = Blueprint('workout', __name__)


# product CREATE routes

@workout.route('/product', methods=['POST'])
def create_new_product():
    return controllers.create_product(request)


# product READ routes
@workout.route('/products', methods=['GET'])
def read_all_products():
    return controllers.read_products(request)


@workout.route('/products/active', methods=['GET'])
def read_all_active_products():
    return controllers.read_active_products(request)


@workout.route('/products/company/<id>', methods=['GET'])
def read_all_products_by_company_id(id):
    return controllers.read_products_by_company_id(request, id)


@workout.route('/product/<id>', methods=["GET"])
def read_product_by_product_id(id):
    return controllers.read_product_by_id(request, id)


# product UPDATE route
@workout.route('/product/<id>', methods=['PUT'])
def update_product(id):
    return controllers.update_product_by_id(request, id)


# CREATE xref route
@workout.route('/product/category', methods=['POST'])
def add_xref():
    return controllers.product_add_category(request)

# product DELETE route


@workout.route('/product/delete/<id>', methods=['DELETE'])
def delete_product_by_id(id):
    return controllers.delete_product(request, id)

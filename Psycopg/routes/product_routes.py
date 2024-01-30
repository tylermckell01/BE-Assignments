from flask import Blueprint

import controllers

product = Blueprint('product', __name__)


# product CREATE routes
@product.route('/products', methods=['POST'])
def create_new_product():
    return controllers.create_product()


# product READ routes
@product.route('/products', methods=['GET'])
def read_all_products():
    return controllers.read_products()

@product.route('/products/active', methods=['GET'])
def read_all_active_products():
    return controllers.read_active_products()

@product.route('/products/companies/<id>', methods=['GET'])
def read_all_products_by_company_id(id):
    return controllers.read_products_by_company_id(id)

@product.route('/product/<id>', methods=["GET"])
def read_product_by_product_id(id):
    return controllers.read_product_by_id(id)


# product UPDATE route
@product.route('/product/<id>', methods=['PUT'])
def update_product_active_status(id):
    return controllers.update_product_by_id(id)


# product DELETE route
@product.route('/product/delete/<id>', methods=['DELETE'])
def delete_product_by_id(id):
    return controllers.delete_product(id)
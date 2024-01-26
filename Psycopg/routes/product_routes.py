from flask import Blueprint

import controllers

product = Blueprint('product', __name__)


# product CREATE routes
@product.route('/products', methods=['POST'])
def create_new_product():
    return controllers.create_product()

@product.route('/products/categories', methods=['POST'])
def create_new_association():
    return controllers.create_association()


# product READ routes
@product.route('/products', methods=['GET'])
def read_all_products():
    return controllers.read_products()

@product.route('/products/active', methods=['GET'])
def read_all_active_products():
    return controllers.read_active_products()

@product.route('/products/companies/<id>', methods=['GET'])
def read_all_products_by_company_id():
    return controllers.read_products_by_company_id()

@product.route('/products/<id>', methods=["GET"])
def read_product_by_product_id(id):
    return controllers.read_product_by_id(id)


# product UPDATE routes
@product.route('/products/<id>', methods=['PUT'])
def update_product_description(id):
    return controllers.update_product(id)

@product.route('/productscategories/<id>/<id>', methods=['PUT'])
def update_product_xref_category_id(category, new_id):
    return controllers.update_product_xref(category, new_id)


# product DELETE route
@product.route('products/delete', methods=['DELETE'])
def delete_product_by_id(id):
    return controllers.delete_product(id)
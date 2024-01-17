from flask import Blueprint

from controllers import products_controller

product = Blueprint('product', __name__)

@product.route('/create/product', methods=['POST'])
def create_new_product():
    return products_controller.create_product()


@product.route('/products/get', methods=['GET'])
def read_all_products():
    return products_controller.read_all_products()


@product.route('/products/get/active', methods=['GET'])
def read_active_products():
    return products_controller.read_products_active()


@product.route('/products/get/<id>', methods=['GET'])
def read_products_by_id(id):
    return products_controller.read_products_by_id(id)


@product.route('/update/product/<id>', methods=['PUT'])
def update_product(id):
    return products_controller.update_product(id)

@product.route('/delete/product/<id>', methods=['DELETE'])
def delete_product_by_id(id):
    return products_controller.delete_product(id)
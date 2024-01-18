from flask import jsonify, request

from data import product_records


# create functions
def create_product():
    data = request.form if request.form else request.json
    product = {}

    product['product_id'] = data['product_id']
    product['name'] = data['name']
    product['description'] = data['description']
    product['price'] = data['price']

    product_records.append(product)

    return jsonify({'message': f'{product.name} created'}), 201


# read functions
def read_all_products():
    return jsonify({'message': 'products found', 'results': f'{product_records}'}), 200


def read_products_active():
    for product in product_records:
        if product['active'] == True:
            return jsonify({'message': 'product is active', 'results': product}), 201
    return jsonify({'message': f'{product} is not active'}), 500


def read_products_by_id(id):
    for product in product_records:
        if product['product_id'] == int(id):
            return jsonify({'message': 'product found', 'results': product}), 201
    return jsonify({'message': f'Product with id {id} not found'}), 404


# update function
def update_product(id):
    data = request.form if request.form else request.json
    product = {}

    for record in product_records:
        if record['product_id'] == int(id):
            product = record

    product['name'] = data.get('name', product['name'])
    product['description'] = data.get('description', product['description'])
    product['price'] = data.get('price', product['price'])

    return jsonify({'message': 'product updated', 'results': product}), 201


# delete function
def delete_product(id):

    for record in product_records:
        if record['product_id'] == int(id):
            product_records.remove(record)
    return jsonify({'message': f'product {id} has been removed successfully'}), 201

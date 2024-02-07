from flask import jsonify, Request 

from db import db
from models.product import Products


# product CREATE functions
def create_product(req):
    post_data = req.form if req.form else req.json

    fields = ['product_name', 'description', 'price', 'company_id']
    required_fields = ['product_name', 'price', 'company_id']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required_fields and not field_data:
            return jsonify({'message': f'{field} is required '}), 400

        values[field] = field_data

    new_product = Products(values['product_name'], values['description'], values['price'], values['company_id'])

    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'unable to create product'}), 400

    query = db.session.query(Products).filter(Products.product_name == values['product_name']).first()

    values['product_id'] = query.product_id

    return jsonify({'message': 'product created', 'result': values}), 201

    # post_data = req.form if req.form else req.json
    
    # product_name = post_data.get['product_name']

    # if description not in post_data:
    #     description = ''
    # else:
    #     description = post_data.get['description']

    # price = post_data.get['price']
    # company_id = post_data.get['company_id']

    # new_product = Products(product_name, description, price, company_id)

    # try:
    #     db.session.add(new_product)
    #     db.session.commit()
    # except:
    #     db.session.rollback()
    #     return jsonify({'message': 'unable to create product'}), 400

    # query = db.session.query(Products).filter(Products.product_name == product_name).first()

    # query['product_id'] = query.product_id

    # return jsonify({'message': 'product created', 'result': new_product}), 201


# product read functions
def read_products():
    query = db.session.query(Products).all()

    products_list = []

    for product in query.Products:
        products_list.append({
            'product_id': product.product_id,
            'product_name': product.product_name,
            'description': product.description,
            'price': product.price,
            'active': product.active,
            'company_id': product.company_id
        })

    return jsonify({'message': 'products found', 'result': products_list}), 200


def read_active_products():
    query = db.session.query(Products).filter(active = True).all()

    products_list = []

    for product in query.Products:
        products_list.append({
            'product_id': product.product_id,
            'product_name': product.product_name,
            'description': product.description,
            'price': product.price,
            'active': product.active,
            'company_id': product.company_id
        })

    return jsonify({'message': 'products found', 'result': products_list}), 200


def read_products_by_company_id(company_id):
    query = db.session.query(Products).filter(Products.company_id == company_id).all()

    products_list = []

    for product in query.Products:
        products_list.append({
            'product_id': product.product_id,
            'product_name': product.product_name,
            'description': product.description,
            'price': product.price,
            'active': product.active,
            'company_id': product.company_id
        })

    return jsonify({'message': 'products found', 'result': products_list}), 200


def read_product_by_id(product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).first()
    if not query:
        return jsonify({'message': f'product with id {product_id} does not exist'}), 400

    query_dict = {
        'product_name': query.product_name,
        'description': query.description,
        'price': query.price,
        'product_id': query.product_id,
        'active': query.active
    }

    return jsonify({'message': 'company found', 'result': query_dict}), 200


# product update functions
def update_product_by_id(req, product_id):
    post_data = req.form if req.form else req.json
    query = db.session.query(Products).filter(Products.product_id == product_id).first()

    query.product_name = post_data.req.get('product_name', query.product_name)
    query.description = post_data.req.get('description', query.description)
    query.price = post_data.req.get('price', query.price)
    query.active = post_data.req.get('active', query.active)


    try:
        db.session.commit()
        return jsonify({'message': f'product {product_id} has been successfully updated'}), 200
    except:
        db.session.rollback()
        return jsonify({'message': f'product {product_id} could not be updated'}), 400


# product delete function
def delete_product(product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not query:
        return jsonify({"message": f"product by id {product_id} does not exist"}), 400    

    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "product deleted", "results": query}), 200

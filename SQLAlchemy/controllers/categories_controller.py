from flask import jsonify, Request

from db import db
from models.category import Categories

# category CREATE functions

def create_category(req):
    post_data = req.form if req.form else req.json

    fields = ['category_name']
    required_fields = ['category_name']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required_fields and not field_data:
            return jsonify({'message': f'{field} is required '}), 400

        values[field] = field_data

    new_category = Categories(values['category_name'])

    try:
        db.session.add(new_category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'unable to create record'}), 400

    query = db.session.query(Categories).filter(Categories.category_name == values['category_name']).first()

    values['category_id'] = query.category_id

    return jsonify({'message': 'category created', 'result': values}), 201


# category READ functions
def read_categories():
    query = db.session.query(Categories).all()

    categories_list = []

    for category in query:
        categories_list.append({
            'category_name': category.category_name,
            'category_id': category.category_id
        })

    return jsonify({'message': 'category found', 'result': categories_list}), 200


def read_by_category_id(category_id):
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()
    if not query:
        return jsonify({'message': f'category with id {category_id} does not exist'}), 400

    query_dict = {
        'category_name': query.category_name,
        'category_id': query.category_id
    }

    return jsonify({'message': 'company found', 'result': query_dict}), 200


# category UPDATE functions
def update_category_name(req, category_id):

    post_data = req.form if req.form else req.json
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    query.category_name = post_data.get('category_name', query.category_name)

    try:
        db.session.commit()
        return jsonify({'message': f'category has been successfully updated'})
    except:
        db.session.rollback()
        return jsonify({'message': f'category could not be updated'})


# category DELETE functions
def delete_category(category_id):
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    if not query:
        return jsonify({"message": f"category does not exist"}), 400    

    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "category deleted", "results": query}), 200

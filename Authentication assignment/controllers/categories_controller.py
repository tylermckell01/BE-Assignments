from flask import jsonify

from db import db
from lib.authenticate import auth, auth_admin
from models.category import Categories, category_schema, categories_schema
from util.reflection import populate_object


# category CREATE functions
@auth_admin
def create_category(req):
    post_data = req.form if req.form else req.json

    category_name = post_data.get('category_name')
    exists_query = db.session.query(Categories).filter(Categories.category_name == category_name).first()

    if exists_query:
        return jsonify({'message': f'category "{category_name}" already exists in the database'}), 400

    new_category = Categories.new_category_obj()
    populate_object(new_category, post_data)

    try:
        db.session.add(new_category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'category could not be created'}), 400

    return jsonify({'message': 'category created', 'result': category_schema.dump(new_category)}), 201


# category READ functions
@auth
def read_categories(req):
    category_query = db.session.query(Categories).all()

    return jsonify({'message': 'categories found', 'result': categories_schema.dump(category_query)}), 200


@auth
def read_by_category_id(req, category_id):
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    return jsonify({'message': 'category found', 'result': category_schema.dump(category_query)}), 200


# category UPDATE functions
@auth_admin
def update_category_name(req, category_id):
    post_data = req.form if req.form else req.json
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    populate_object(category_query, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'category could not be updated'}), 400

    return jsonify({'message': 'category updated', 'result': category_schema.dump(category_query)}), 200


# category DELETE functions
@auth_admin
def delete_category(req, category_id):
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    if not query:
        return jsonify({"message": f"category does not exist"}), 400

    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "category deleted"}), 200

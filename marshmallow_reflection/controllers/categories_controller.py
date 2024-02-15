from flask import jsonify

from db import db
from models.category import Categories, category_schema, categories_schema
from util.reflection import populate_object


# category CREATE functions


def create_category(req):
    post_data = req.form if req.form else req.json

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
def read_categories():
    category_query = db.session.query(Categories).all()

    return jsonify({'message': 'categories found', 'result': categories_schema.dump(category_query)}), 200


def read_by_category_id(category_id):
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    return jsonify({'message': 'category found', 'result': category_schema.dump(category_query)}), 200


# category UPDATE functions
def update_category_name(req, category_id):
    post_data = req.form if req.form else req.json
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    populate_object(category_query, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'category could not be updated'})

    return jsonify({'message': 'category updated'})


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

    return jsonify({"message": "category deleted"}), 200

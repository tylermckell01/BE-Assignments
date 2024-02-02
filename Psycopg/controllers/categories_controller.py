import os

from flask import jsonify, request
import psycopg2

database_name = os.environ.get('DATABASE_NAME')
conn = psycopg2.connect(f"dbname={database_name}")
cursor = conn.cursor()

# category CREATE functions


def create_category():
    post_data = request.form if request.form else request.json

    category_name = post_data.get('category_name')

    if not category_name:
        return jsonify({"message": "category_name is a required field"}), 400

    cursor.execute("SELECT * FROM categories WHERE category_name=%s", [category_name])
    result = cursor.fetchone()

    if result:
        return jsonify({"message": 'category already exists'}), 400

    cursor.execute(""" 
        INSERT INTO categories
        (category_name)
        VALUES (%s);
""", [category_name])
    conn.commit()

    return jsonify({"message": f"category '{category_name}' added to DB"}), 201


# category READ functions
def read_categories():
    cursor.execute(""" 
    SELECT * FROM categories;
""")

    results = cursor.fetchall()

    record_list = []
    for record in results:
        record = {
            'category_id': record[0],
            'category_name': record[1],
        }
        record_list.append(record)

    return jsonify({"message": "categories found", "results": record_list}), 200


def read_by_category_id(id):

    cursor.execute(""" 
    SELECT * FROM categories
    WHERE category_id = %s;
""", [id])

    results = cursor.fetchall()

    record_list = []
    for record in results:
        record = {
            'category_id': record[0],
            'category_name': record[1]
        }
        record_list.append(record)

    return jsonify({"message": "category found", "results": record_list}), 200


# category UPDATE functions
def update_category_name(id):

    post_data = request.form if request.form else request.json

    category_name = post_data.get('category_name')
    # category_id = post_data.get('category_name')

    cursor.execute(""" 
    UPDATE categories
    SET category_name=%s
    WHERE category_id=%s;
""", [category_name, id])

    conn.commit()

    return jsonify({"message": f"category {id} has been changed to '{category_name}'"}), 200


# category DELETE functions
def delete_category(category_id):

    cursor.execute("""
    DELETE from products, categories
    WHERE category_id=%s;
""", [category_id])

    conn.commit()
    return jsonify({"message": f"category {category_id} has been deleted"}), 200

import os

from flask import jsonify, request
import psycopg2

database_name = os.environ.get('DATABASE_NAME')
conn = psycopg2.connect(f"dbname={database_name}")
cursor = conn.cursor()


# product CREATE functions
def create_product():
    post_data = request.form if request.form else request.json

    product_name = post_data.get('product_name')
    description = post_data.get('description')
    price = post_data.get('price')

    if not product_name:
        return jsonify({"message": "product_name is a required field"}), 400
    
    cursor.execute("SELECT * FROM products WHERE product_name=%s", [product_name])
    result = cursor.fetchone()

    if result:
        return jsonify({"message": 'Product already exists'}), 400
    
    cursor.execute(""" 
        INSERT INTO products
        (product_name, description, price)
        VALUES (%s, %s, %s)
""", [product_name, description, price])
    conn.commit()

    return jsonify({"message": f"product '{product_name}' added to DB"}), 201



# product read functions
def read_products():

    cursor.execute(""" 
    SELECT * FROM products;
""")
    results = cursor.fetchall()

    record_list = []
    for record in results:
        record = {
            'product_id': record[0],
            'company_id': record[1],
            'product_name': record[2],
            'description': record[3],
            'price': record[4],
            'active': record[5]
        }
        record_list.append(record)

    return jsonify({"message": "products are found", "results": record_list}), 200


def read_active_products():

    cursor.execute(""" 
    SELECT * FROM products
    WHERE active = True;
""")
    results = cursor.fetchall()

    record_list = []
    for record in results:
        record = {
            'product_id': record[0],
            'company_id': record[1],
            'product_name': record[2],
            'description': record[3],
            'price': record[4],
            'active': record[5]
        }
        record_list.append(record)

    return jsonify({"message": "products found", "results": record_list}), 200


def read_products_by_company_id(id):

    cursor.execute(""" 
    SELECT * FROM products
    WHERE company_id = %s
                ;
""", [id])
    results = cursor.fetchall()

    record_list = []
    for record in results:
        record = {
            'product_id': record[0],
            'company_id': record[1],
            'product_name': record[2],
            'description': record[3],
            'price': record[4],
            'active': record[5]
        }
        record_list.append(record)

    return jsonify({"message": "products found", "results": record_list}), 200


def read_product_by_id(id):

    cursor.execute(""" 
    SELECT * FROM products
    WHERE product_id = %s;
""", [id])
    
    results = cursor.fetchall()

    record_list = []
    for record in results:
        record = {
            'product_id': record[0],
            'company_id': record[1],
            'product_name': record[2],
            'description': record[3],
            'price': record[4],
            'active': record[5]
        }
        record_list.append(record)

        return jsonify({"message": "product found", "results": record_list}), 200


# product update functions
def update_product_by_id(id):
    post_data = request.form if request.form else request.json

    active = post_data.get('active')
    # product_id = post_data.get('product_id')

    cursor.execute("""
    UPDATE products
    SET active=%s
    WHERE product_id=%s;
""", [active, id])
    
    conn.commit()
    return jsonify({"message": "product updated", "results": id}), 200


# product delete function
def delete_product(product_id):

    cursor.execute("""
    DELETE from products
    WHERE product_id=%s;
""", [product_id])
    
    conn.commit()
    return jsonify({"message": f"product {2} has been deleted"}), 200
import os

from flask import jsonify, request
import psycopg2

database_name = os.environ.get('DATABASE_NAME')
conn = psycopg2.connect(f"dbname={database_name}")
cursor = conn.cursor()


# company CREATE functions
def create_company():
    post_data = request.form if request.form else request.json

    company_name = post_data.get('company_name')

    if not company_name:
        return jsonify({"message": "company_name is a required field"}), 400

    cursor.execute("SELECT * FROM companies WHERE company_name=%s", [company_name])
    result = cursor.fetchone()

    if result:
        return jsonify({"message": 'Company already exists'}), 400

    cursor.execute(""" 
        INSERT INTO companies
        (company_name)
        VALUES (%s);
""", [company_name])
    conn.commit()

    return jsonify({"message": f"Company '{company_name}' added to DB"}), 201

# company READ functions


def read_companies():
    cursor.execute(""" 
    SELECT * FROM companies;
""")

    results = cursor.fetchall()

    record_list = []
    for record in results:
        record = {
            'company_id': record[0],
            'company_name': record[1],
        }
        record_list.append(record)

    return jsonify({"message": "Companies found", "results": record_list}), 200


def read_company_by_id(id):
    cursor.execute(""" 
    SELECT * FROM companies
    WHERE company_id = %s;
""", [id])
    results = cursor.fetchall()

    record_list = []
    for record in results:
        record = {
            'company_id': record[0],
            'company_name': record[1]
        }
        record_list.append(record)

    return jsonify({"message": f"company {id} found", "results": record_list}), 200


# company UPDATE function
def update_company_name(id):
    post_data = request.form if request.form else request.json

    company_name = post_data.get('company_name')
    # company_id = post_data.get('company_id')

    if not company_name:
        return jsonify({"message": "company_name is a required field"}), 400

    cursor.execute("SELECT * FROM companies WHERE company_name=%s", [company_name])
    result = cursor.fetchone()

    if result:
        return jsonify({"message": 'Company already exists'}), 400

    cursor.execute(""" 
        UPDATE companies
        SET company_name=%s
        WHERE company_id=%s;
""", [company_name, id])
    conn.commit()

    return jsonify({"message": f"Company '{company_name}' added to DB"}), 201


# company DELETE function
def delete_company(company_id):

    cursor.execute("""
    DELETE from products, categories
    WHERE company_id=%s;
""", [company_id])

    conn.commit()
    return jsonify({"message": f"company {company_id} has been deleted"}), 200

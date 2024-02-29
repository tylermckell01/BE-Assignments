from flask import jsonify

from db import db
from lib.authenticate import auth, auth_admin
from models.company import Companies, company_schema, companies_schema
from util.reflection import populate_object

# company CREATE functions


@auth_admin
def create_company(req):
    post_data = req.form if req.form else req.json

    company_name = post_data.get('company_name')
    exists_query = db.session.query(Companies).filter(Companies.company_name == company_name).first()

    if exists_query:
        return jsonify({'message': f'company "{company_name}" already exists in the database'}), 400

    new_company = Companies.new_company_obj()
    populate_object(new_company, post_data)

    try:
        db.session.add(new_company)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'company could not be created'}), 400

    return jsonify({'message': 'company created', 'result': company_schema.dump(new_company)}), 201


# company READ functions
@auth
def read_companies(req):
    company_query = db.session.query(Companies).all()

    return jsonify({'message': 'companies found', 'result': companies_schema.dump(company_query)}), 200


@auth
def read_company_by_id(req, company_id):
    company_query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

    return jsonify({'message': 'company found', 'result': company_schema.dump(company_query)}), 200


# company UPDATE function
@auth_admin
def update_company_name(req, company_id):
    post_data = req.form if req.form else req.json
    company_query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

    populate_object(company_query, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'company could not be updated'}), 400

    return jsonify({'message': 'company updated', 'result': company_schema.dump(company_query)}), 200


# company DELETE function
@auth_admin
def delete_company(req, company_id):
    query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

    if not query:
        return jsonify({"message": f"that company does not exist"}), 400

    try:
        db.session.delete(query)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "company deleted"}), 200

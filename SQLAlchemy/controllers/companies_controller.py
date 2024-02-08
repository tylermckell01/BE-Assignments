from flask import jsonify

from db import db
from models.company import Companies


# company CREATE functions
def create_company(req):
    post_data = req.form if req.form else req.json

    fields = ['company_name']
    required_fields = ['company_name']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required_fields and not field_data:
            return jsonify({'message': f'{field} is required '}), 400

        values[field] = field_data

    new_company = Companies(values['company_name'])

    try:
        db.session.add(new_company)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'unable to create record'}), 400

    query = db.session.query(Companies).filter(Companies.company_name == values['company_name']).first()

    values['company_id'] = query.company_id

    return jsonify({'message': 'company created', 'result': values}), 201


# company READ functions
def read_companies():
    query = db.session.query(Companies).all()

    if not query:
        return jsonify({"message": f"no companies exist yet"}), 400

    companies_list = []

    for company in query:
        companies_list.append({
            'company_name': company.company_name,
            'company_id': company.company_id
        })

    return jsonify({'message': 'companies found', 'result': companies_list}), 200


def read_company_by_id(company_id):
    query = db.session.query(Companies).filter(Companies.company_id == company_id).first()
    if not query:
        return jsonify({'message': f'company with id {company_id} does not exist'}), 400

    query_dict = {
        'company_name': query.company_name,
        'company_id': query.company_id
    }

    return jsonify({'message': 'company found', 'result': query_dict}), 200


# company UPDATE function
def update_company_name(req, company_id):
    post_data = req.form if req.form else req.json
    query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

    query.company_name = post_data.get('company_name', query.company_name)

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({'message': f'company could not be updated'}), 400

    updated_data = {
        'company_name': query.company_name,
        'company_id': query.company_id
    }

    return jsonify({'message': f'company has been successfully updated', 'results': updated_data}), 200

# company DELETE function


def delete_company(company_id):
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

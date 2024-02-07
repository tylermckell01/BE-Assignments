from flask import Blueprint, request

import controllers

companies = Blueprint('companies', __name__)


# company CREATE routes
@companies.route('/company', methods=['POST'])
def create_new_company():
    return controllers.create_company(request)


# company READ routes
@companies.route('/companies', methods=['GET'])
def read_all_companies():
    return controllers.read_companies()


@companies.route('/company/<id>', methods=['GET'])
def read_company_by_id(id):
    return controllers.read_company_by_id(request, id)


# company UPDATE route
@companies.route('/company/<id>', methods=['PUT'])
def update_company_name_by_id(id):
    return controllers.update_company_name(id)


# company DELETE route
@companies.route('/company/<id>', methods=['DELETE'])
def delete_company_by_id(id):
    return controllers.delete_company(id)

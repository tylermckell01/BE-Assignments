from flask import Blueprint

import controllers

companies = Blueprint('companies', __name__)


# company CREATE routes
@companies.routes('/companies', methods=['POST'])
def create_new_company():
    return controllers.create_company()


# company READ routes
@companies.routes('/companies', methods =['GET'])
def read_all_companies():
    return controllers.read_companies()

@companies.routes('/companies/<id>', methods=['GET'])
def read_company_by_id(id):
    return controllers.read_company(id)


# company UPDATE route
@companies.routes('/companies/<id>', methods=['PUT'])
def update_company_name_by_id(id):
    return controllers.update_company_name(id)
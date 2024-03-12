from flask import Blueprint, request

import controllers

gyms = Blueprint('gyms', __name__)


# company CREATE routes
@gyms.route('/company', methods=['POST'])
def create_new_company():
    return controllers.create_company(request)


# company READ routes
@gyms.route('/companies', methods=['GET'])
def read_all_companies():
    return controllers.read_companies(request)


@gyms.route('/company/<id>', methods=['GET'])
def read_company_by_id(id):
    return controllers.read_company_by_id(request, id)


# company UPDATE route
@gyms.route('/company/<id>', methods=['PUT'])
def update_company_name_by_id(id):
    return controllers.update_company_name(request, id)


# company DELETE route
@gyms.route('/company/delete/<id>', methods=['DELETE'])
def delete_company_by_id(id):
    return controllers.delete_company(request, id)

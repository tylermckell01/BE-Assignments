from flask import Blueprint, request

import controllers

gyms = Blueprint('gyms', __name__)


# gym CREATE routes
@gyms.route('/gym', methods=['POST'])
def create_new_gym():
    return controllers.create_gym(request)


# gym READ routes
@gyms.route('/gyms', methods=['GET'])
def read_all_gyms():
    return controllers.read_gyms(request)


@gyms.route('/gym/<id>', methods=['GET'])
def read_gym_by_id(id):
    return controllers.read_gym_by_id(request, id)


# gym UPDATE route
@gyms.route('/gym/<id>', methods=['PUT'])
def update_gym_name_by_id(id):
    return controllers.update_gym_name(request, id)


# gym DELETE route
@gyms.route('/gym/delete/<id>', methods=['DELETE'])
def delete_gym_by_id(id):
    return controllers.delete_gym(request, id)

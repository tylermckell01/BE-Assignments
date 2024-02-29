from flask import Blueprint, request

import controllers

users = Blueprint('users', __name__)

# User CREATE route


@users.route('/user', methods=['POST'])
def add_user():
    return controllers.add_user(request)


# User READ route
@users.route('/users', methods=['GET'])
def read_all_users():
    return controllers.read_users(request)


# User UPDATE route
@users.route('/user/<id>', methods=['PUT'])
def update_user(id):
    return controllers.update_user_by_id(request, id)


# User DELETE route
@users.route('/user/delete/<id>', methods=['DELETE'])
def delete_user(id):
    return controllers.delete_user(request, id)

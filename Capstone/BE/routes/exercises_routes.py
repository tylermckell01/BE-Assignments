from flask import Blueprint, request

import controllers

exercises = Blueprint('exercises', __name__)

# exercise CREATE routes


@exercises.route('/exercise', methods=['POST'])
def create_new_exercise():
    return controllers.create_exercise(request)


# exercise READ routes
@exercises.route('/exercises', methods=['GET'])
def read_all_exercises():
    return controllers.read_exercises(request)


@exercises.route('/exercise/<id>', methods=['GET'])
def read_by_exercise_id(id):
    return controllers.read_by_exercise_id(request, id)


# exercise UPDATE routes
@exercises.route('/exercise/<id>', methods=['PUT'])
def update_exercise_name_by_id(id):
    return controllers.update_exercise_name(request, id)


# exercise DELETE routes
@exercises.route('/exercise/delete/<id>', methods=['DELETE'])
def delete_exercise_by_id(id):
    return controllers.delete_exercise(request, id)

from flask import Blueprint, request

import controllers

workout = Blueprint('workout', __name__)


# workouts CREATE routes

@workout.route('/workout', methods=['POST'])
def create_new_workout():
    return controllers.create_workout(request)


# workout READ routes
@workout.route('/workouts', methods=['GET'])
def read_all_workouts():
    return controllers.read_workouts(request)


@workout.route('/workouts/length', methods=['GET'])
def read_workouts_by_length():
    return controllers.read_workouts_by_length(request)


# @workout.route('/workouts/gym/<id>', methods=['GET'])
# def read_all_workouts_by_gym_id(id):
#     return controllers.read_workouts_by_gym_id(request, id)


@workout.route('/workout/<id>', methods=["GET"])
def read_workout_by_workout_id(id):
    return controllers.read_workout_by_id(request, id)


# workout UPDATE route
@workout.route('/workout/<id>', methods=['PUT'])
def update_workout(id):
    return controllers.update_workout_by_id(request, id)


# CREATE xref route
@workout.route('/workout/exercise', methods=['POST'])
def add_xref():
    return controllers.workout_add_exercise(request)

# workout DELETE route


@workout.route('/workout/delete/<id>', methods=['DELETE'])
def delete_workout_by_id(id):
    return controllers.delete_workout(request, id)

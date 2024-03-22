import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from .workouts_exercises_xref import workouts_exercises_association_table


class Workouts(db.Model):
    __tablename__ = "Workouts"

    workout_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workout_name = db.Column(db.String(), nullable=False, )
    description = db.Column(db.String())
    length = db.Column(db.Float(), nullable=False)
    # gym_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Gyms.gym_id", ondelete='CASCADE'), nullable=False)

    # gym = db.relationship("Gyms", foreign_keys="[Workouts.gym_id]", back_populates='workouts')
    exercises = db.relationship("Exercises", secondary=workouts_exercises_association_table, back_populates='workouts')

    def __init__(self, workout_name, description, length):
        self.workout_name = workout_name
        self.description = description
        self.length = length
        # self.gym_id = gym_id

    def new_workout_obj():
        return Workouts('', '', 0)


class WorkoutsSchema(ma.Schema):
    class Meta:
        fields = ['workout_id', 'workout_name', 'description', 'length', 'gym', 'exercises']
    # gym = ma.fields.Nested('GymsSchema', exclude=['workouts'])
    exercises = ma.fields.Nested('ExercisesSchema', many=True, exclude=['workouts'])


workout_schema = WorkoutsSchema()
workouts_schema = WorkoutsSchema(many=True)

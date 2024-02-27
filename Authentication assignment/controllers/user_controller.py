from flask import jsonify, request
from flask_bcrypt import generate_password_hash

from db import db
from models.users import Users, user_schema, users_schema
from util.reflection import populate_object


def add_user(req):
    post_data = req.form if req.form else req.json

    new_user = Users.get_new_user()

    populate_object(new_user, post_data)

    new_user.password = generate_password_hash(new_user.password).decode('utf8')

    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": 'user could not be created'}), 400

    return jsonify({"message": "user created", "results": user_schema.dump(new_user)})

import functools
from flask import Response, jsonify
from datetime import datetime
from uuid import UUID

from db import db
from models.users import Users, user_schema
from models.auth_token import AuthTokens


def validate_uuid4(uuid_string):
    try:
        UUID(uuid_string, version=4)
        return True
    except:
        return False


def validate_token(arg_zero):
    auth_token = arg_zero.headers['auth']

    if not auth_token or not validate_uuid4(auth_token):
        return False

    existing_token = db.session.query(AuthTokens).filter(AuthTokens.auth_token == auth_token).first()

    if existing_token:
        if existing_token.expiration > datetime.utcnow():
            return existing_token

    else:
        return False


def fail_response():
    return jsonify({"message": "authentication required"}), 401


def auth(func):
    @functools.wraps(func)
    def wrapper_auth_return(*args, **kwargs):
        print(args)
        auth_info = validate_token(args[0])

        if auth_info:
            return func(*args, **kwargs)

        else:
            return fail_response()

    return wrapper_auth_return


def auth_admin(func):
    @functools.wraps(func)
    def wrapper_auth_return(*args, **kwargs):
        auth_info = validate_token(args[0])
        admin_query = db.session.query(Users).filter(Users.user_id == auth_info.user.user_id).first()

        if admin_query.role == "admin" and auth_info:
            return func(*args, **kwargs)

        elif auth_info:
            return jsonify({"message": "you must be an admin to perform this action"}), 401

        else:
            return fail_response()

    return wrapper_auth_return

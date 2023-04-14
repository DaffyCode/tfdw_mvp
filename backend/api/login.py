import json

import jwt
import os

from flask import Flask, jsonify, request, Blueprint, make_response, Response
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta

from models.user import User, user_schema
from api.user import token_required

login_route = Blueprint('login_route', __name__)


@login_route.route('/api/login', methods=['POST'])
def login():
    auth = request.json
    print(auth)
    print(os.environ.get('SECRET_KEY'))

    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm = "Login required!!"'}
        )

    user = User.query.filter_by(email=auth.get('email')).first()
    print(user)

    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify!',
            401,
            {'WWW-Authenticate:' 'Basic realm = "User does not exist!!"'}
        )

    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, os.environ.get('SECRET_KEY'))
        refresh_token = jwt.encode({
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }, os.environ.get('SECRET_KEY'))

        response_object = [
            {'id': user.id,
             'first_name': user.first_name,
             'last_name': user.last_name,
             'email': user.email,
             'phone': user.phone,
             'street': user.street,
             'zip_code': user.zip_code,
             'city': user.city,
             'region': user.region,
             'role': user.role,
             'club_name': user.club_name},
            {'token': token.decode('UTF-8')},
            {'refresh_token': refresh_token.decode('UTF-8')}
        ]

        return make_response(jsonify(response_object), 201)

    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm = "Wrong Password!!'}
    )


@login_route.route('/api/refresh', methods=['POST'])
@token_required(refresh=True)
def refresh(current_user):
    """
    Token refresh route, generates new access token.
    Args:
        current_user: User object

    Returns: new x-access-token

    """
    # generates new JWT Token
    token = jwt.encode({
        'id': current_user.id,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, os.environ.get('SECRET_KEY'))
    return make_response(jsonify({'token': token.decode('UTF-8')}), 201)


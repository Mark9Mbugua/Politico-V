from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.user_models import User
from app.api.v2.models.party_models import PoliticalParties
from app.api.v2.models.office_models import PoliticalOffices
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

uv2 = Blueprint('up1', __name__, url_prefix='/api/v2')


@uv2.route('/auth/signup', methods=['POST'])
def post_user():
    """Route for registering a user"""
    try:
        data = request.get_json()
        email = data['email']
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        phone = data['phone']
        password = data['password']

        response = Validators().user_sign_up_validator(firstname, lastname, email, phone, password)
    except KeyError:
        return Serializer.error_serializer('One or more keys is missing', 400), 400
    
    if response == True:
        if User().userIsValid(username) == True:
            return Serializer.error_serializer('user already exists', 400), 400

        password = User().generate_hash(password)
        new_user = User().register(firstname, lastname, username, email, phone, password)
        return Serializer.json_serializer('User signed up successfully', new_user, 201), 201
    return make_response(jsonify(response), 400)


@uv2.route('/auth/signin', methods=['POST'])
def login():
    """ Route for signing in a user"""
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
    except KeyError:
        return Serializer.error_serializer('One or more keys is missing', 400), 400

    if User().userIsValid(username) == True:
        if User().password_is_valid(username, password) == True:
            access_token = User().user_login(username)

            if access_token:
                return Serializer.signup_serializer('You are now logged in', access_token, 201), 201
            
        return Serializer.error_serializer('Check if credentials are correct', 400), 400
    
    return Serializer.error_serializer('User does not exist', 404), 404


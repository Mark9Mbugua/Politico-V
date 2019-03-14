from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.user_models import User
from app.api.v2.models.party_models import PoliticalParties
from app.api.v2.models.office_models import PoliticalOffices
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import psycopg2

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
        password = data['password']
        try:
            phone = data['phone']
        except Exception as e:
            return Serializer.json_error(e, 400), 400
        
    except KeyError:
        return Serializer.json_error('Check if all fields exist', 400), 400

    """Checks if fields are either of type string or integer"""
    Validators().is_str_or_int(firstname, lastname, username, password, phone)

    """Checks if fields are empty"""
    Validators().is_space_or_empty(firstname, lastname, username, email, phone, password,
    firstname=firstname, lastname=lastname,username=username, email=email, phone=phone, password=password)
    
    """Checks if firstname and lastname contain any digits"""
    Validators().is_digit(firstname, lastname)
   
    """Checks if phone number contain any digits"""
    Validators().is_not_digit(phone)

    """Checks if field content has spaces in between"""
    Validators().has_space(firstname, lastname, username, password, phone)
    
    """Checks if password is valid"""
    Validators().check_valid_password(password)
    
    """Checks if email is valid"""
    Validators().valid_email(email)
    
    """Checks if phone number is valid"""
    Validators().valid_phone_number(phone)

    if User().get_user_by_username(username):
        return Serializer.json_error('user already exists', 400), 400

    password = User().generate_hash(password)
    new_user = User().register(firstname, lastname, username, email, phone, password)
    return Serializer.json_success('User signed up successfully', new_user, 201), 201
 
@uv2.route('/auth/signin', methods=['POST'])
def login():
    """ Route for signing in a user"""
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
    except KeyError:
        return Serializer.json_error('One or more keys is missing', 400), 400

    if User().get_user_by_username(username):
        if User().password_is_valid(username, password) == True:
            access_token = User().user_login(username)

            if access_token:
                return Serializer.signup_success('You are now logged in', access_token, 201), 201
            
        return Serializer.json_error('Check if credentials are correct', 400), 400
    
    return Serializer.json_error('User does not exist', 404), 404


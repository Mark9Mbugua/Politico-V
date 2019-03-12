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
        
    except KeyError:
        return Serializer.json_error('One or more keys is missing', 400), 400

    if Validators().is_str(firstname) == False:
        return Serializer.json_error('First name should be in string format', 400), 400
        
    if Validators().is_str(email) == False:
        return Serializer.json_error('Email Address should be in string format', 400), 400
    
    if Validators().is_str(lastname) == False:
        return Serializer.json_error('Last name should be in string format', 400), 400
    
    if Validators().is_str(username) == False:
        return Serializer.json_error('Username should be in string format', 400), 400
    
    if Validators().is_str(password) == False:
        return Serializer.json_error('Password should be in string format', 400), 400
    
    if Validators().is_str(phone) == False:
        return Serializer.json_error('Phone number should be in string format', 400), 400

    if Validators().is_digit(firstname) == True:
        return Serializer.json_error('First name should only have letters', 400), 400
    
    if Validators().is_digit(lastname) == True:
        return Serializer.json_error('Last name should only have letters', 400), 400
    
    if Validators().is_digit(phone) == False:
        return Serializer.json_error('Phone number should only have digits', 400), 400
    
    if Validators().is_empty(firstname) == True:
        return Serializer.json_error('First name is required', 400), 400
    
    if Validators().is_empty(lastname) == True:
        return Serializer.json_error('Last name is required', 400), 400
    
    if Validators().is_empty(username) == True:
        return Serializer.json_error('Username is required', 400), 400
    
    if Validators().is_empty(email) == True:
        return Serializer.json_error('Email address is required', 400), 400
    
    if Validators().is_empty(phone) == True:
        return Serializer.json_error('Phone number is required', 400), 400
    
    if Validators().is_empty(password) == True:
        return Serializer.json_error('Password is required', 400), 400

    if Validators().is_space(firstname) == True:
        return Serializer.json_error('First name should not have spaces', 400), 400
    
    if Validators().is_space(lastname) == True:
        return Serializer.json_error('Last name should not have spaces', 400), 400
    
    if Validators().is_space(username) == True:
        return Serializer.json_error('Username should not have spaces', 400), 400
    
    if Validators().is_space(password) == True:
        return Serializer.json_error('Password should not have spaces', 400), 400
    
    if Validators().is_space(phone) == True:
        return Serializer.json_error('Phone number should not have spaces', 400), 400
    
    if Validators().password_short(password) == True:
        return Serializer.json_error('Password should have at least 8 characters', 400), 400
    
    if Validators().caps_password(password) == True:
        return Serializer.json_error('Password should have atleast one capital letter', 400), 400
    
    if Validators().small_letter_password(password) == True:
        return Serializer.json_error('Password should have atleast one lowercase letter', 400), 400
    
    if Validators().integer_password(password) == True:
        return Serializer.json_error('Password should have atleast one number', 400), 400
    
    if Validators().valid_email(email) == False:
        return Serializer.json_error('Email address is invalid.\
            Kindly enter a valid email address', 400), 400
    
    if Validators().short_phone_no(phone) == True:
        return Serializer.json_error('Phone number should have 12 digits \
            starting with the country code for example: 254712345678', 400), 400
    
    if User().userIsValid(username) == True:
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

    if User().userIsValid(username) == True:
        if User().password_is_valid(username, password) == True:
            access_token = User().user_login(username)

            if access_token:
                return Serializer.signup_success('You are now logged in', access_token, 201), 201
            
        return Serializer.json_error('Check if credentials are correct', 400), 400
    
    return Serializer.json_error('User does not exist', 404), 404


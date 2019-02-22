from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.user_models import User, Candidate
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
    
    if User().userIsValid(username) == True:
        return Serializer.error_serializer('user already exists', 400), 400

    if response == True:
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
            user = User().login(username, password)
            access_token = create_access_token(identity = user)

            if access_token:
                return Serializer.json_serializer('You are now logged in', access_token, 200), 200
            
        return Serializer.error_serializer('Enter correct password', 400), 400
    
    return Serializer.error_serializer('User is not registered', 400), 400

@uv2.route('/office/<int:office_id>/register', methods=['POST'])
@jwt_required
def post_candidate(office_id):
    current_user = get_jwt_identity()
    if current_user ['username'] == "admin": 
        """ Route for registering a candidate"""
        try:
            data = request.get_json()
            office = data['office']
            email = data['email']
            party = data['party']
            candidate = data['candidate']
            
        except KeyError:
            return Serializer.error_serializer('One or more keys is missing', 400), 400
        
        if Candidate().check_candidate_registered(candidate, office):
            return Serializer.error_serializer('Office does not exist', 400), 400

        if PoliticalOffices().check_office_exists(office) == True:

            if PoliticalParties().check_party_exists(party) == True:

                candidate = Candidate().register_candidate(office, party, email, candidate)

                return Serializer.json_serializer('Candidate successfully registered', candidate, 200), 200

            return Serializer.error_serializer('Party does not exist', 400), 400

        return Serializer.error_serializer('Office does not exist', 400), 400

    return Serializer.error_serializer('User not authorized to make this request', 401), 401
    

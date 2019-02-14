from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.user_models import User
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer

uv2 = Blueprint('up1', __name__, url_prefix='/api/v2')


@uv2.route('/auth/signup', methods=['POST']) 
def post_user():
    """Route for registering a user"""
    try:
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']       
        response = Validators().user_sign_up_validator(username, email, password)
    except KeyError:
        return Serializer.error_serializer('One or more keys is missing', 400), 400

    if response == True:
        password = User().generate_hash(password)
        new_user = User().register(username, email, password)
        return Serializer.json_serializer('User sign up is succesfull', new_user, 201), 201
    return make_response(jsonify(response), 400)
    
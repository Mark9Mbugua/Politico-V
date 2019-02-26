from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.party_models import PoliticalParties
from app.api.v2.models.user_models import User
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.logo_validator import LogoUrlValidator
from app.api.v2.utils.serializer import Serializer
from flask_jwt_extended import get_jwt_identity, jwt_required

pv2 = Blueprint('ap4', __name__, url_prefix='/api/v2')


@pv2.route('/parties', methods=['POST'])
@jwt_required 
def post_party():
    current_user = get_jwt_identity()
    if current_user['username'] == "admin":
        """route for creating a new political party"""
        try:
            data = request.get_json()
            party_name = data['party_name']
            hqAddress = data['hqAddress']
            logoUrl = data['logoUrl']
            party = PoliticalParties().create(party_name, hqAddress, logoUrl)
            response = Validators().party_data_validator(party_name, hqAddress)
            result = LogoUrlValidator().validate_logo_url(logoUrl)
        except KeyError:
            return Serializer.error_serializer('One or more keys is missing', 400), 400

        if response == True:
            if result == True:
                return Serializer.json_serializer('Political party created successfully', party, 201), 201
            return make_response(jsonify(result), 400)
        
        return make_response(jsonify(response), 400)      

    return Serializer.error_serializer('User not authorized to make this request', 401), 401

@pv2.route('/parties', methods=['GET'])
@jwt_required
def get_parties():
    parties = PoliticalParties().get_all_parties()
    if parties:
        return Serializer.json_serializer('All political parties retrieved successfully', parties, 200), 200
    
    return Serializer.error_serializer('Political parties cannot be found', 404), 404

@pv2.route('/parties/<int:party_id>', methods=['GET'])
@jwt_required
def get_party(party_id):
    party = PoliticalParties().get_one_party(party_id)
    if party:
       return Serializer.json_serializer('Political party retrieved successfully', party, 200), 200
    
    return Serializer.error_serializer('Political party cannot be found', 404), 404


@pv2.route('/parties/<int:party_id>', methods=['PATCH'])
@jwt_required
def update_party(party_id):
    current_user = get_jwt_identity()
    if current_user ['username'] == "admin":
        try:
            data = request.get_json()
            party_name = data['party_name']
            edit_party = PoliticalParties().edit_party(party_id, party_name)
        except KeyError:
            return Serializer.error_serializer('Party name key is missing', 400), 400

        if edit_party:
            if party_name == "" or party_name.isspace():
                return Serializer.error_serializer('Party name is required', 400), 400
            
            if not all(x.isalpha() or x.isspace() for x in party_name):
                return Serializer.error_serializer('Name should only have letters and spaces', 400), 400
            
            return Serializer.json_serializer('Political party updated successfully', edit_party, 200), 200
        
        return Serializer.error_serializer('Political party cannot be found', 404), 404

    return Serializer.error_serializer('User not authorized to make this request', 401), 401
    

@pv2.route('/parties/<int:party_id>', methods=['DELETE'])
@jwt_required
def delete_party(party_id):
    current_user = get_jwt_identity()
    if current_user ['username'] == "admin":
        party = PoliticalParties().get_one_party(party_id)
        delete_party = PoliticalParties().delete_party(party_id)
       
        if party:
            return Serializer.json_serializer('Political Party deleted successfully', delete_party, 200), 200
        
        return Serializer.error_serializer('Political party cannot be found', 404), 404
        
    return Serializer.error_serializer('User not authorized to make this request', 401), 401
    

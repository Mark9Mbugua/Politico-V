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
    if User().i_am_admin(get_jwt_identity()):
        """route for creating a new political party"""
        try:
            data = request.get_json()
            party_name = data['party_name']
            hqAddress = data['hqAddress']
            logoUrl = data['logoUrl']
        
        except KeyError:
            return Serializer.json_error('One or more keys is missing', 400), 400
        
        if Validators().is_str(party_name) == False:
            return Serializer.json_error('Name should be in string format', 400), 400
        
        if Validators().is_str(hqAddress) == False:
            return Serializer.json_error('hqAddress should be in string format', 400), 400
        
        if Validators().is_digit(hqAddress) == True:
            return Serializer.json_error('hqAddress should have letters too', 400), 400

        if Validators().is_alpha_or_space(party_name) == False:
            return Serializer.json_error('Name should also have letters and spaces', 400), 400

        if Validators().is_empty(party_name) == True:
            return Serializer.json_error('Party name is required', 400), 400
        
        if Validators().is_empty(hqAddress) == True:
            return Serializer.json_error('hqAddress is required', 400), 400
        
        if Validators().is_str(logoUrl) == False:
            return Serializer.json_error('logoUrl should be in string format', 400), 400
        
        if Validators().is_empty(logoUrl) == True:
            return Serializer.json_error('logoUrl is required', 400), 400
        
        if Validators().valid_logo_url(logoUrl) == False:
            return Serializer.json_error("logoUrl should be in the example format 'https://www.twitter.com/profile/img.jpg'", 400), 400

        if PoliticalParties().check_party_exists_by_name(party_name):
            return Serializer.json_error('Political party already exists', 400), 400
        
        party = PoliticalParties().create(party_name, hqAddress, logoUrl)
        
        return Serializer.json_success('Political party created successfully', party, 201), 201      

    return Serializer.json_error('User not authorized to make this request', 401), 401

@pv2.route('/parties', methods=['GET'])
def get_parties():
    parties = PoliticalParties().get_all_parties()
    if parties:
        return Serializer.json_success('All political parties retrieved successfully', parties, 200), 200
    
    return Serializer.json_error('Political parties cannot be found', 404), 404

@pv2.route('/parties/<int:party_id>', methods=['GET'])
def get_party(party_id):
    party = PoliticalParties().get_one_party(party_id)
    if party:
       return Serializer.json_success('Political party retrieved successfully', party, 200), 200
    
    return Serializer.json_error('Political party cannot be found', 404), 404


@pv2.route('/parties/<int:party_id>', methods=['PATCH'])
@jwt_required
def update_party(party_id):
    if User().i_am_admin(get_jwt_identity()):
        try:
            data = request.get_json()
            party_name = data['party_name']
            edit_party = PoliticalParties().edit_party(party_id, party_name)
        except KeyError:
            return Serializer.json_error('Party name key is missing', 400), 400

        if edit_party:
            if party_name == "" or party_name.isspace():
                return Serializer.json_error('Party name is required', 400), 400
            
            if not all(x.isalpha() or x.isspace() for x in party_name):
                return Serializer.json_error('Name should only have letters and spaces', 400), 400
            
            return Serializer.json_success('Political party updated successfully', edit_party, 200), 200
        
        return Serializer.json_error('Political party cannot be found', 404), 404

    return Serializer.json_error('User not authorized to make this request', 401), 401
    

@pv2.route('/parties/<int:party_id>', methods=['DELETE'])
@jwt_required
def delete_party(party_id):
    if User().i_am_admin(get_jwt_identity()):
        party = PoliticalParties().get_one_party(party_id)
        delete_party = PoliticalParties().delete_party(party_id)
       
        if party:
            return Serializer.json_success('Political Party deleted successfully', delete_party, 200), 200
        
        return Serializer.json_error('Political party cannot be found', 404), 404
        
    return Serializer.json_error('User not authorized to make this request', 401), 401
    

from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.party_models import PoliticalParties
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.logo_validator import LogoUrlValidator
from app.api.v2.utils.serializer import Serializer

pv2 = Blueprint('ap4', __name__, url_prefix='/api/v2')


@pv2.route('/parties', methods=['POST']) 
def post_party():
    """route for creating a new political party"""
    parties = PoliticalParties().get_all_parties()
    try:
        data = request.get_json()
        party_name = data['party_name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']
        for one_party in parties:
            if one_party['name'] == party_name:
                return Serializer.error_serializer('Party already exists', 400), 400
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
    

@pv2.route('/parties', methods=['GET']) 
def get_parties():
    parties = PoliticalParties().get_all_parties()
    if parties:
        return Serializer.json_serializer('All political parties retrieved successfully', parties, 200), 200
    
    return Serializer.error_serializer('Political parties cannot be found', 404), 404

@pv2.route('/parties/<int:party_id>', methods=['GET']) 
def get_party(party_id):
    party = PoliticalParties().get_one_party(party_id)
    
    if party:
       return Serializer.json_serializer('Political party retrieved successfully', party, 200), 200
    
    return Serializer.error_serializer('Political party cannot be found', 404), 404


@pv2.route('/parties/<int:party_id>', methods=['PATCH']) 
def update_party(party_id):
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

@pv2.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    delete_party = PoliticalParties().delete_party(party_id)
    if delete_party:
        return Serializer.json_serializer('Political Party deleted successfully', None, 200), 200
    
    return Serializer.error_serializer('Political party cannot be found', 404), 404

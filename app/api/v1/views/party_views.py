from flask import abort, Flask, jsonify, request, make_response, Blueprint
from app.api.v1.models.party_models import PoliticalParties
from app.api.v1.utils.validators import Validators
from app.api.v1.utils.logo_validator import LogoUrlValidator
from app.api.v1.utils.serializer import Serializer

pv1 = Blueprint('ap1', __name__, url_prefix='/api/v1')


@pv1.route('/parties', methods=['POST']) 
def post_party():
    """route for creating a new political party"""
    parties = PoliticalParties().get_all_parties()
    data = request.get_json()
    try:
        party_name = data['party_name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']
        for one_party in parties:
            if one_party['party_name'] == party_name and one_party['hqAddress'] == hqAddress and one_party['logoUrl'] == logoUrl:
                return Serializer.error_fn('This party already exists', 400), 400
        
        party = PoliticalParties().create_party(party_name, hqAddress, logoUrl)
        response = Validators().party_data_validator(party_name, hqAddress)
        result = LogoUrlValidator().validate_logo_url(logoUrl)
    except KeyError:
        abort(Serializer.error_fn(400, 'One or more keys is missing'))
    
    if response == True:
        if result == True:
            return Serializer.json_success('Political party created successfully', data, 201), 201
        return make_response(jsonify(result), 400)
    
    return make_response(jsonify(response), 400)
    

@pv1.route('/parties', methods=['GET']) 
def get_parties():
    parties = PoliticalParties().get_all_parties()
    if parties:
        return Serializer.json_success('All political parties retrieved successfully', parties, 200), 200
    
    abort(Serializer.error_fn(404, 'Political parties cannot be found'))

@pv1.route('/parties/<int:party_id>', methods=['GET']) 
def get_party(party_id):
    party = PoliticalParties().get_one_party(party_id)
    
    if party:
       return Serializer.json_success('Political party retrieved successfully', party, 200), 200
    
    abort(Serializer.error_fn(404, 'Political party cannot be found'))


@pv1.route('/parties/<int:party_id>', methods=['PATCH']) 
def update_party(party_id):
    try:
        data = request.get_json()
        party_name = data['party_name']
        edit_party = PoliticalParties().edit_party(party_id, party_name)
    except KeyError:
        abort(Serializer.error_fn(400, 'Party name key is missing'))

    if edit_party:
        if party_name == "" or party_name.isspace():
            abort(Serializer.error_fn(400, 'Party name is required'))
        
        if not all(x.isalpha() or x.isspace() for x in party_name):
            abort(Serializer.error_fn(400, 'Name should only have letters and spaces'))
        
        return Serializer.json_success('Political party updated successfully', edit_party, 200), 200
    
    abort(Serializer.error_fn(404, 'Political party cannot be found'))

@pv1.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    delete_party = PoliticalParties().delete_party(party_id)
    if delete_party:
        return Serializer.json_success('Political Party deleted successfully', None, 200), 200
    
    abort(Serializer.error_fn(404, 'Political party cannot be found'))
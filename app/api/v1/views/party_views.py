from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v1.models.party_models import PoliticalParties
from app.api.v1.utils.validators import Validators

pv1 = Blueprint('ap1', __name__, url_prefix='/api/v1')

@pv1.route('/parties', methods=['POST']) 
def post_party():
    """route for creating a new political party"""
    data = request.get_json()
    party_name = data['party_name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']
    party = PoliticalParties().create_party(party_name, hqAddress, logoUrl)
    response = Validators().party_data_validator(party_name, hqAddress, logoUrl)
    
    if response == True:
        return make_response(jsonify({
        'message': 'Political party created successfully',
        'data' : party
        }), 201)
    
    return make_response(jsonify(response), 400)

@pv1.route('/parties', methods=['GET']) 
def get_parties():
    parties = PoliticalParties().get_all_parties()
    if parties:
        return make_response(jsonify({
            'message': 'All political parties retrieved successfully',
            'data' : parties
        }), 200)
    return make_response(jsonify({
            'Error': 'Political parties cannot be found',
        }), 404)

@pv1.route('/parties/<int:party_id>', methods=['GET']) 
def get_party(party_id):
    party = PoliticalParties().get_one_party(party_id)
    
    if party:
        return make_response(jsonify({
            'message': 'Political party has been successfully retrieved',
            'data' : party
        }), 200)
    
    return make_response(jsonify({
        'Error': 'This political party cannot be found',
    }), 404)


@pv1.route('/parties/<int:party_id>', methods=['PATCH']) 
def update_party(party_id):
    data = request.get_json()
    party_name = data['party_name']
    edit_party = PoliticalParties().edit_party(party_id, party_name)
    if edit_party:
        return make_response(jsonify({
            'message': 'Political party updated successfully',
            'data' : edit_party
        }), 200)
    
    return make_response(jsonify({
        'Error': 'This political party cannot be found',
    }), 404)

@pv1.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    if delete_party:
        delete_party = PoliticalParties().delete_party(party_id)
        return make_response(jsonify({
            'message': "Political Party has been deleted successfully",
            'data' : delete_party
        }), 200)
    
    return make_response(jsonify({
        'Error': 'This political party cannot be found',
    }), 404)
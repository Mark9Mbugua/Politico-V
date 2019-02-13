from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v1.models.party_models import PoliticalParties

pv2 = Blueprint('ap4', __name__, url_prefix='/api/v2')


@pv2.route('/parties', methods=['POST']) 
def post_party():
    return None
    
@pv2.route('/parties', methods=['GET']) 
def get_parties():
    return None

@pv2.route('/parties/<int:party_id>', methods=['GET']) 
def get_party(party_id):
    return None

@pv2.route('/parties/<int:party_id>', methods=['PATCH']) 
def update_party(party_id):
    return None

@pv2.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    return None
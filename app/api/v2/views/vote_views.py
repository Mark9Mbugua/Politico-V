from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.vote_models import Vote
from app.api.v2.models.user_models import Candidate
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer
from flask_jwt_extended import get_jwt_identity, jwt_required

vv2 = Blueprint('vp1', __name__, url_prefix='/api/v2')


@vv2.route('/vote', methods=['POST']) 
@jwt_required
def vote():
    """Route for casting a vote"""
    if User().admin_is_me(get_jwt_identity()):   
        try:
            data = request.get_json()
            office_id = data['office_id']
            voter_id = data['voter_id']
            candidate_id = data['candidate_id']   

        except KeyError:
            return Serializer.error_serializer('One or more keys is missing', 400), 400

        candidate_registered = Candidate().check_candidate_registered(candidate_id, office_id)
        if candidate_registered:
            if Vote().has_voted(office_id, voter_id):
                return Serializer.error_serializer('You have already voted for a candidate in this office', 400), 400

            response = Vote().cast_vote(office_id, voter_id, candidate_id)

            return Serializer.json_serializer('You successfully cast your vote', response, 201), 201
            
        return Serializer.error_serializer('Candidate not registered', 400), 400
        
    return Serializer.error_serializer('User not authorized to make this request', 401), 401


@vv2.route('/office/<int:office_id>/result', methods=['GET'])
@jwt_required
def get_results(office_id):
    """Get election results"""
    results = Vote().results_per_office(office_id)
    return Serializer.json_serializer("Election results retrieved successfully", results, 200), 200
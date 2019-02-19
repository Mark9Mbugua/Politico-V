from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.vote_models import Vote
from app.api.v2.models.user_models import Candidate
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer
vv2 = Blueprint('vp1', __name__, url_prefix='/api/v2')


@vv2.route('/vote', methods=['POST']) 
def vote():
    """Route for casting a vote"""
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
        return Serializer.json_serializer('You successfully cast your vote',response, 201), 201
    return Serializer.error_serializer('Candidate not registered', 400), 400

    

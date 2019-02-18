from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.vote_models import Vote
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer
vv2 = Blueprint('vp1', __name__, url_prefix='/api/v2')


@vv2.route('/vote', methods=['POST']) 
def vote():
    """Route for casting a vote"""
    try:
        data = request.get_json()
        office_name = data['office_name']
        candidate_id = data['candidate_id']
        cd_firstname = data['cd_firstname']
        cd_lastname = data['cd_lastname']
        voter_id = data['voter_id']

    except KeyError:
        return Serializer.error_serializer('One or more keys is missing', 400), 400

    new_vote = Vote().cast_vote(office_name, candidate_id, cd_firstname, cd_lastname, voter_id)
    return Serializer.json_serializer("Vote has been cast successfully", new_vote, 201), 201
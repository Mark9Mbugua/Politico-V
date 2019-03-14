from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v2.models.vote_models import Vote
from app.api.v2.models.candidate_models import Candidate
from app.api.v2.models.office_models import PoliticalOffices
from app.api.v2.models.user_models import User
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer
from flask_jwt_extended import get_jwt_identity, jwt_required

vv2 = Blueprint('vp1', __name__, url_prefix='/api/v2')


@vv2.route('/vote', methods=['POST']) 
@jwt_required
def vote():
    """Route for casting a vote"""
    current_user = get_jwt_identity()
    if not User().i_am_admin(current_user):  
        try:
            user_id = current_user
        
        except KeyError:
            return Serializer.json_error('You are not registered', 400), 400
        
        try:
            data = request.get_json()
            office = data['office']
            candidate = data['candidate']   

        except KeyError:
            return Serializer.json_error('One or more keys is missing', 400), 400
        
        """Checks if fields are integers"""
        Validators().is_int(office, candidate) 
        
        if not User().find_by_user_id(candidate):
            return Serializer.json_error('User does not exist', 400), 400

        if not PoliticalOffices().check_office_exists(office):
            return Serializer.json_error('Office does not exist', 400), 400

        candidate_registered = Candidate().check_candidate_registered(candidate, office)
        if candidate_registered:
            if Vote().has_voted(office, user_id):
                return Serializer.json_error('You have already voted for a candidate in this office', 400), 400

            response = Vote().cast_vote(office, user_id, candidate)

            return Serializer.json_success('You successfully cast your vote', response, 201), 201
            
        return Serializer.json_error('Candidate not registered', 400), 400
        
    return Serializer.json_error('User not authorized to make this request', 401), 401


@vv2.route('/office/<int:office_id>/result', methods=['GET'])
def get_results(office_id):
    """Get election results"""
    results = Vote().results_per_office(office_id)
    return Serializer.json_success("Election results retrieved successfully", results, 200), 200
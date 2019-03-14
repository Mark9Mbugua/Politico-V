from flask import abort, Flask, jsonify, request, make_response, Blueprint
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
            abort(Serializer.error_fn(400, 'You are not registered'))
        
        try:
            data = request.get_json()
            office = data['office']
            candidate = data['candidate']   

        except KeyError:
            abort(Serializer.error_fn(400, 'Check if all fields exist'))
        
        """Checks if fields are integers"""
        Validators().is_int(office, candidate) 
        
        if not User().find_by_user_id(candidate):
            abort(Serializer.error_fn(400, 'User does not exist'))

        if not PoliticalOffices().check_office_exists(office):
            abort(Serializer.error_fn(400, 'Office does not exist'))

        candidate_registered = Candidate().check_candidate_registered(candidate, office)
        if not candidate_registered:
            abort(Serializer.error_fn(400, 'Candidate not registered'))
        
        if Vote().has_voted(office, user_id):
            abort(Serializer.error_fn(400, 'You have already voted for a candidate in this office'))

        response = Vote().cast_vote(office, user_id, candidate)
        return Serializer.json_success('You successfully cast your vote', response, 201), 201
        
    abort(Serializer.error_fn(401, 'User not authorized to make this request'))


@vv2.route('/office/<int:office_id>/result', methods=['GET'])
def get_results(office_id):
    """Get election results"""
    results = Vote().results_per_office(office_id)
    return Serializer.json_success("Election results retrieved successfully", results, 200), 200
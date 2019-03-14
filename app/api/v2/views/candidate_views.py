from flask import Flask, abort, jsonify, request, make_response, Blueprint
from app.api.v2.models.candidate_models import Candidate
from app.api.v2.models.user_models import User 
from app.api.v2.models.party_models import PoliticalParties
from app.api.v2.models.office_models import PoliticalOffices
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

cv2 = Blueprint('cp1', __name__, url_prefix='/api/v2')


@cv2.route('/office/<int:office_id>/register', methods=['POST'])
@jwt_required
def post_candidate(office_id):
    if User().i_am_admin(get_jwt_identity()): 
        """ Route for registering a candidate"""
        try:
            data = request.get_json()
            party = data['party']
            candidate = data['candidate']
            
        except KeyError:
            abort(Serializer.error_fn(400, 'Check if all fields exist'))
        
        """Checks if fields are integers"""
        Validators().is_int(party, candidate, office_id)
       
        """cannot register admin as a candidate"""
        if User().get_admin_by_id(candidate):
            abort(Serializer.error_fn(400, 'You are not authorized to register admin as a candidate'))
  
        if not User().find_by_user_id(candidate):
            abort(Serializer.error_fn(404, 'Candidate does not exist'))

        if not PoliticalOffices().check_office_exists(office_id):
            abort(Serializer.error_fn(404, 'Office does not exist'))

        if not PoliticalParties().check_party_exists(party):
            abort(Serializer.error_fn(404, 'Party does not exist'))
                
        if Candidate().check_candidate_registered(candidate, office_id):
            abort(Serializer.error_fn(400, 'Candidate is already registered'))

        candidate = Candidate().register_candidate(office_id, party, candidate)
        return Serializer.json_success('Candidate registered successfully', candidate, 201), 201          

    abort(Serializer.error_fn(401, 'User not authorized to make this request'))
    
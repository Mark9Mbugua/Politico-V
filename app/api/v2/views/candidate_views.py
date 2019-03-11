from flask import Flask, jsonify, request, make_response, Blueprint
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
            return Serializer.error_serializer('One or more keys is missing', 400), 400
        
        if User().is_digit(party) == False:
            return Serializer.error_serializer('Party should be a digit', 400), 400

        if User().is_digit(candidate) == False:
            return Serializer.error_serializer('Candidate should be a digit', 400), 400        
        
        if User().is_digit(office_id) == False:
            return Serializer.error_serializer('Office should be a digit', 400), 400
        
        # cannot register admin as a candidate
        if User().get_admin_by_id(candidate):
            return Serializer.error_serializer('You are not authorized to register admin as a candidate', 400), 400
  
        if User().find_by_user_id(candidate):

            if PoliticalOffices().check_office_exists(office_id):

                if PoliticalParties().check_party_exists(party):
                
                    if not Candidate().check_candidate_registered(candidate, office_id):

                        candidate = Candidate().register_candidate(office_id, party, candidate)

                        return Serializer.json_serializer('Candidate registered successfully', candidate, 201), 201

                    return Serializer.error_serializer('Candidate is already registered', 400), 400

                return Serializer.error_serializer('Party does not exist', 404), 404
                
            return Serializer.error_serializer('Office does not exist', 404), 404

        return Serializer.error_serializer('Candidate does not exist', 404), 404

    return Serializer.error_serializer('User not authorized to make this request', 401), 401
    
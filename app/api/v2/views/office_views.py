from flask import abort, Flask, jsonify,request, Blueprint, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.api.v2.models.office_models import PoliticalOffices
from app.api.v2.models.user_models import User
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer

ov2 = Blueprint('ap3', __name__, url_prefix='/api/v2')

@ov2.route('/offices', methods=['POST'])
@jwt_required
def post_office():
    if User().i_am_admin(get_jwt_identity()):
        data = request.get_json()
        try:
            office_name = data["office_name"]
            office_type = data["office_type"]
            location = data["location"]
            
        except KeyError:
            return Serializer.json_error('One or more keys is missing', 400), 400
        
        types_of_offices = ['Legislative', 'Executive', 'County']

        """Check if fields are strings"""
        Validators().is_str_or_int(office_type, office_name, location)
        
        """Check if fields have digits"""
        Validators().is_digit(office_name, office_type, location)
        
        """Checks if fields are empty"""
        Validators().is_space_or_empty(office_type, office_name, location, 
        office_type=office_type, office_name=office_name, location=location)
        
        """Checks if office type is valid"""
        Validators().valid_office_type(office_type, types_of_offices)

        """Checks if office type matches office name"""
        Validators().valid_legilative_office(office_type, office_name)

        Validators().valid_executive_office(office_type, office_name)
        
        Validators().valid_executive_location(office_type, location)

        Validators().valid_county_office(office_type, office_name)

        if PoliticalOffices().check_office_exists_by_name(office_name, location):
            abort(Serializer.error_fn(400, 'Political office already exists'))

        office = PoliticalOffices().create_office(office_name, office_type, location)
        return Serializer.json_success('Political office created successfully', office, 201), 201

    abort(Serializer.error_fn(401, 'User not authorized to make this request'))

@ov2.route('/offices', methods=['GET'])
def get_all_offices():
    offices = PoliticalOffices().get_all_offices()
    if offices:     
        return Serializer.json_success('All political offices retrieved successfully', offices, 200), 200
    
    abort(Serializer.error_fn(404, 'Political office cannot be found'))

@ov2.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    office = PoliticalOffices().get_one_office(office_id)
    if office:
        return Serializer.json_success('Political office retrieved successfully', office, 200), 200
    
    abort(Serializer.error_fn(404, 'Political office cannot be found'))

@ov2.route('/offices/<int:office_id>', methods=['DELETE'])
@jwt_required
def delete_office(office_id):
    if User().i_am_admin(get_jwt_identity()):
        office = PoliticalOffices().get_one_office(office_id)
        delete_office = PoliticalOffices().delete_office(office_id)
       
        if office:
            return Serializer.json_success('Political Office deleted successfully', delete_office, 200), 200
        
        abort(Serializer.error_fn(404, 'Political office cannot be found'))
        
    abort(Serializer.error_fn(401, 'User not authorized to make this request'))
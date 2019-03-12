from flask import Flask, jsonify,request, Blueprint, make_response
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
        types_of_offices = ['Legislative', 'Executive', 'County']
        data = request.get_json()
        try:
            office_name = data["office_name"]
            office_type = data["office_type"]
            location = data["location"]
            
        except KeyError:
            return Serializer.json_error('One or more keys is missing', 400), 400
        
        if Validators().is_str(office_type) == False:
            return Serializer.json_error('Office type should be in string format', 400), 400
        
        if Validators().is_str(office_name) == False:
            return Serializer.json_error('Name should be in string format', 400), 400
        
        if Validators().is_str(location) == False:
            return Serializer.json_error('Location should be in string format', 400), 400
        
        if Validators().is_digit(office_name) == True:
            return Serializer.json_error('Name should only have letters', 400), 400
        
        if Validators().is_digit(office_type) == True:
            return Serializer.json_error('Office type should only have letters', 400), 400
        
        if Validators().is_digit(location) == True:
            return Serializer.json_error('Location should only have letters', 400), 400
        
        if Validators().is_empty(office_type) == True:
            return Serializer.json_error('Office type is required', 400), 400
        
        if Validators().is_empty(office_name) == True:
            return Serializer.json_error('Office name is required', 400), 400
        
        if Validators().is_empty(location) == True:
            return Serializer.json_error('Location is required', 400), 400
        
        if Validators().valid_office_type(office_type, types_of_offices) == False:
            return Serializer.json_error('Office type must either be Legislative, Executive or County', 400), 400

        if Validators().valid_legilative_office(office_type, office_name) == False:
            return Serializer.json_error('Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office', 400), 400
        
        if Validators().valid_executive_office(office_type, office_name) == False:
            return Serializer.json_error('Only the President or the Prime Minister can occupy an executive office', 400), 400
        
        if Validators().valid_executive_location(office_type, location) == False:
            return Serializer.json_error('The location of an executive office can only be Kenya', 400), 400

        if Validators().valid_county_office(office_type, office_name) == False:
            return Serializer.json_error('Only a Governor or an MCA can occupy a county office', 400), 400

        if PoliticalOffices().check_office_exists_by_name(office_name, location):
                return Serializer.json_error('Political office already exists', 400), 400

        office = PoliticalOffices().create_office(office_name, office_type, location)
        return Serializer.json_success('Political office created successfully', office, 201), 201

    return Serializer.json_error('User not authorized to make this request', 401), 401

@ov2.route('/offices', methods=['GET'])
def get_all_offices():
    offices = PoliticalOffices().get_all_offices()
    if offices:     
        return Serializer.json_success('All political offices retrieved successfully', offices, 200), 200
    
    return Serializer.json_error('Political office cannot be found', 404), 404

@ov2.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    office = PoliticalOffices().get_one_office(office_id)
    if office:
        return Serializer.json_success('Political office retrieved successfully', office, 200), 200
    
    return Serializer.json_error('Political office cannot be found', 404), 404

@ov2.route('/offices/<int:office_id>', methods=['PATCH'])
@jwt_required
def update_office(office_id):
    if User().i_am_admin(get_jwt_identity()):
        try:
            data = request.get_json()
            office_name = data['office_name']
            edit_office = PoliticalOffices().edit_office(office_id, office_name)
        except KeyError:
            return Serializer.json_error('Office name key is missing', 400), 400

        if edit_office:
            if office_name == "" or office_name.isspace():
                return Serializer.json_error('Office name is required', 400), 400
            
            if not all(x.isalpha() or x.isspace() for x in office_name):
                return Serializer.json_error('Name should only have letters and spaces', 400), 400
            
            return Serializer.json_success('Political office updated successfully', edit_office, 200), 200
        
        return Serializer.json_error('Political office cannot be found', 404), 404

    return Serializer.json_error('User not authorized to make this request', 401), 401
    

@ov2.route('/offices/<int:office_id>', methods=['DELETE'])
@jwt_required
def delete_office(office_id):
    if User().i_am_admin(get_jwt_identity()):
        office = PoliticalOffices().get_one_office(office_id)
        delete_office = PoliticalOffices().delete_office(office_id)
       
        if office:
            return Serializer.json_success('Political Office deleted successfully', delete_office, 200), 200
        
        return Serializer.json_error('Political office cannot be found', 404), 404
        
    return Serializer.json_error('User not authorized to make this request', 401), 401
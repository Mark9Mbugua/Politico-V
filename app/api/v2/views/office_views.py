from flask import Flask, jsonify,request, Blueprint, make_response
from app.api.v2.models.office_models import PoliticalOffices
from app.api.v2.utils.validators import Validators
from app.api.v2.utils.serializer import Serializer

ov2 = Blueprint('ap3', __name__, url_prefix='/api/v2')

@ov2.route('/offices', methods=['POST'])
def post_office():
    data = request.get_json()
    try:
        office_name = data["office_name"]
        office_type = data["office_type"]
        office = PoliticalOffices().create_office(office_name, office_type)
        response = Validators().office_data_validator(office_name, office_type)
    except KeyError:
        return Serializer.error_serializer('One or more keys is missing', 400), 400
    
    if response == True:
        return Serializer.json_serializer('Political office created successfully', office, 201), 201

    return make_response(jsonify(response), 400)

@ov2.route('/offices', methods=['GET'])
def get_all_offices():
    offices = PoliticalOffices().get_all_offices()
    if offices:     
        return Serializer.json_serializer('All political offices retrieved successfully', offices, 200), 200
    
    return Serializer.error_serializer('Political office cannot be found', 404), 404

@ov2.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    office = PoliticalOffices().get_one_office(office_id)
    if office:
        return Serializer.json_serializer('Political office retrieved successfully', office, 200), 200
    
    return Serializer.error_serializer('Political office cannot be found', 404), 404
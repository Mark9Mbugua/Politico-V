from flask import Flask, jsonify,request, Blueprint, make_response
from app.api.v1.models.office_models import PoliticalOffices
from app.api.v1.utils.validators import Validators
from app.api.v1.utils.serializer import Serializer

ov1 = Blueprint('ap2', __name__, url_prefix='/api/v1')


@ov1.route('/offices', methods=['POST'])
def post_office():
    data = request.get_json()
    try:
        office_type = data["office_type"]
        name = data["name"]
        office = PoliticalOffices().create_office(office_type, name)
        response = Validators().office_data_validator(office_type, name)
    except KeyError:
        return Serializer.error_serializer('One or more keys is missing', 400), 400
    
    if response == True:
        return Serializer.json_serializer('Political office created successfully', office, 201), 201

    return make_response(jsonify(response), 400)

@ov1.route('/offices', methods=['GET'])
def get_all_offices():
    offices = PoliticalOffices().get_offices()
    if offices:     
        Serializer.json_serializer('All political offices retrieved successfully', offices, 200), 200
    
    return Serializer.error_serializer('Political office cannot be found', 404), 404

@ov1.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    office = PoliticalOffices().get_one_office(office_id)
    if office:
        return Serializer.json_serializer('Political office retrieved successfully', office, 200), 200
    
    return Serializer.error_serializer('Political office cannot be found', 404), 404
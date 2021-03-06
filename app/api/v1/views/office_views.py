from flask import abort,Flask, jsonify,request, Blueprint, make_response
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
        abort(Serializer.error_fn(400, 'One or more keys is missing'))
    
    if response == True:
        return Serializer.json_success('Political office created successfully', office, 201), 201

    return make_response(jsonify(response), 400)

@ov1.route('/offices', methods=['GET'])
def get_all_offices():
    offices = PoliticalOffices().get_offices()
    if offices:     
        return Serializer.json_success('All political offices retrieved successfully', offices, 200), 200
    
    abort(Serializer.error_fn(404, 'Political office cannot be found'))

@ov1.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    office = PoliticalOffices().get_one_office(office_id)
    if office:
        return Serializer.json_success('Political office retrieved successfully', office, 200), 200
    
    abort(Serializer.error_fn(404, 'Political office cannot be found'))
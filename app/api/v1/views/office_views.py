from flask import Flask, jsonify,request, Blueprint, make_response
from app.api.v1.models.offices_models import PoliticalOffices
from app.api.v1.utils.validators import Validators

ov1 = Blueprint('ap2', __name__, url_prefix='/api/v1')


@ov1.route('/offices', methods=['POST'])
def post_office():
    data = request.get_json()
    office_type = data["office_type"]
    name = data["name"]
    office = PoliticalOffices().create_office(office_type, name)
    response = Validators().office_data_validator(office_type, name)
    
    if response == True:
        return make_response(jsonify({
        'Message': 'Political office created successfully',
        "data" : office
    }), 201)
    
    return make_response(jsonify(response), 400)

@ov1.route('/offices', methods=['GET'])
def get_all_offices():
    offices = PoliticalOffices().get_offices()
    if offices:     
        return make_response(jsonify({
            'message': 'All political offices retrieved successfully',
            "data" : offices
        }), 200)
    
    return make_response(jsonify({
            'Error': 'Political offices cannot be found',
        }), 404)
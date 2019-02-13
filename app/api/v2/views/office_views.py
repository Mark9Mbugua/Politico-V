from flask import Flask, jsonify,request, Blueprint, make_response
from app.api.v1.models.office_models import PoliticalOffices

ov2 = Blueprint('ap3', __name__, url_prefix='/api/v2')

@ov2.route('/offices', methods=['POST'])
def post_office():
    pass

@ov2.route('/offices', methods=['GET'])
def get_all_offices():
    pass

@ov2.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    pass
from flask import Flask, jsonify,request, Blueprint, make_response

ov1 = Blueprint('ap2', __name__, url_prefix='/api/v1')


@ov1.route('/offices', methods=['POST'])
def post_office():
    pass

@ov1.route('/offices', methods=['GET'])
def get_all_offices():
    pass  

@ov1.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
   pass
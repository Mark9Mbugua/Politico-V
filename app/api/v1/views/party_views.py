from flask import Flask, jsonify, request, make_response, Blueprint


pv1 = Blueprint('ap1', __name__, url_prefix='/api/v1')

@pv1.route('/parties', methods=['POST']) 
def post_party():
   pass


@pv1.route('/parties', methods=['GET']) 
def get_parties():
    pass

@pv1.route('/parties/<int:party_id>', methods=['GET']) 
def get_party(party_id):
    pass

@pv1.route('/parties/<int:party_id>', methods=['PATCH']) 
def update_party(party_id):
    pass
@pv1.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    pass
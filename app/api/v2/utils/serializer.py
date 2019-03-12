from flask import jsonify, make_response

class Serializer:
    "Serialize outputs"
    @classmethod
    def json_success(cls, message, data, status):
        resp = make_response(jsonify({'message': message, 'data': data, 'status': status}))
        return resp
    
    @classmethod
    def json_error(cls, message, status):
        resp = make_response(jsonify({'Error': message, 'status': status}))
        return resp
    
    @classmethod
    def signup_success(cls, message, token, status):
        resp = make_response(jsonify({'message': message, 'token': token, 'status': status}))
        return resp
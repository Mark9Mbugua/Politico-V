from flask import jsonify, make_response

class Serializer:
    "Serialize outputs"
    @classmethod
    def json_serializer(cls, message, data, status):
        resp = make_response(jsonify({'message': message, 'data': data, 'status': status}))
        return resp
    
    @classmethod
    def error_serializer(cls, message, status):
        resp = make_response(jsonify({'Error': message, 'status': status}))
        return resp
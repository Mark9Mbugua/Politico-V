from flask import jsonify, make_response

class Serializer:
    "Serialize outputs"
    @classmethod
    def json_success(cls, message, data, status):
        resp = make_response(jsonify({'message': message, 'data': data, 'status': status}))
        return resp
    
    @classmethod
    def signup_success(cls, message, user, token, status):
        resp = make_response(jsonify({'message': message, 'token': token, 'user': user, 'status': status}))
        return resp

    @classmethod
    def error_fn(cls, status, message):
        if status in (404, 400, 405, 409, 401, 500):
            resp = make_response(jsonify({'status': status, 'Error': message}), status)
            return resp
import os
from app.api.v2.models.user_models import User
from app.db_config import Database
from app import create_app
from flask import Flask, jsonify, request
from flask_jwt_extended.exceptions import NoAuthorizationError

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)

with app.app_context():
    Database().create_tables()
    User().create_admin()


@app.errorhandler(404)
def invalid_url(error=None):
    """Handle invalid url"""
    return jsonify({
        'Error': '{} is not a valid url'.format(request.url)
    }), 404

@app.errorhandler(400)
def invalid_request(error=None):
    """Handle invalid requests"""
    return jsonify({
        'Error': 'content_type should be application/json'
    }), 400

@app.errorhandler(405)
def invalid_method(error=None):
    """Handle invalid URL methods"""
    return jsonify({
        'Error': '{} is not allowed for this endpoint'.format(request.method)
    }), 405

@app.errorhandler(500)
def server_error(error=None):
    """Handle internal server error"""
    return jsonify({
        'Error': 'Check if the request causes a server error'
    }), 500


@app.errorhandler(NoAuthorizationError)
def unauthorized(error=None):
    """Handle no authorization error"""
    return jsonify({
        'Message': 'You are not authorized to make this request. Check if you are logged in.'
    })


if __name__ == '__main__':
    app.run(debug=True)

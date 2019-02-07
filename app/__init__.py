from flask import Flask, Blueprint, request, jsonify
from instance.config import app_config

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from .api.v1.views.office_views import ov1
    app.register_blueprint(ov1)

    from .api.v1.views.party_views import pv1
    app.register_blueprint(pv1)

    return app
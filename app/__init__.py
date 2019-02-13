from flask import Flask, Blueprint, request, jsonify
from instance.config import app_config
from .db_config import create_tables, drop_tables

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from .api.v1.views.office_views import ov1
    app.register_blueprint(ov1)

    from .api.v1.views.party_views import pv1
    app.register_blueprint(pv1)

    from .api.v2.views.office_views import ov2
    app.register_blueprint(ov2)

    from .api.v2.views.party_views import pv2
    app.register_blueprint(pv2)

    create_tables()
    
    return app
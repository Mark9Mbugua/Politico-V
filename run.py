import os
from app.api.v2.models.user_models import User
from app import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)

with app.app_context():
    User().create_admin()

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from route import request_api

app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config ={
        'app_name' : "Python-Flask-REST"
    }
)

app.register_blueprint(swaggerui_blueprint , url_prefix=SWAGGER_URL)
app.register_blueprint(request_api.get_blueprint())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
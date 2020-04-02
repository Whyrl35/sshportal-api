from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import yaml
import os

with open("conf.yml", 'r') as config_file:
    configuration = yaml.load(config_file, Loader=yaml.FullLoader)

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['JWT_SECRET_KEY'] = configuration['jwt_secret_key']
app.config['JWT_AUTH_URL_RULE'] = '/api/auth'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['DATABASE'] = configuration['database']

api = Api(app)
jwt = JWTManager(app)

from resources import *  # noqa


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    import resources

    jti = decrypted_token['jti']
    return resources.models.RevokedTokenModel.is_jti_blacklisted(jti)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

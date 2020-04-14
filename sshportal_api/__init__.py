from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restful_swagger_3 import Api
import yaml
import os


if "CONF_PATH" in os.environ:
    conf_path = os.environ['CONF_PATH']
else:
    conf_path = "."

with open("{conf_path}/conf.yml".format(conf_path=conf_path), 'r') as config_file:
    configuration = yaml.load(config_file, Loader=yaml.FullLoader)

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['JWT_SECRET_KEY'] = configuration['jwt_secret_key']
app.config['JWT_AUTH_URL_RULE'] = '/api/auth'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['DATABASE'] = configuration['database']
app.config['SWAGGER_PROD_URL'] = configuration['swagger']['prod']['url']

api = Api(app, version='0.1',
          api_spec_url="/v1/spec",
          servers=[{"url": app.config['SWAGGER_PROD_URL'], "description": "Production server"}],
          contact='ludovic.houdayer@gm@il.com',
          description="An API over the moul/sshportal project, SSH bastion.",
          license="MIT",
          components={"securitySchemes": {"bearerAuth": {"type": "https", "scheme": "bearer", "bearerFormat": "Bearer"}}}
          # security={"bearerAuth": []},
          )
jwt = JWTManager(app)

from sshportal_api.resources import *  # noqa


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    import sshportal_api.models

    jti = decrypted_token['jti']
    return sshportal_api.models.RevokedTokenModel.is_jti_blacklisted(jti)

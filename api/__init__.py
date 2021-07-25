from flask import Flask
from flask_cors import CORS
from flask_restx import Api

app = Flask(__name__, static_folder=None)
app.config['ERROR_404_HELP'] = False
restx_api = Api(app)
CORS(app)

from api.controllers import errors, thread, stats, files

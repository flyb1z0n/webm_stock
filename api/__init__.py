from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_folder=None)
CORS(app)

from api.controllers import errors, thread, stats, files

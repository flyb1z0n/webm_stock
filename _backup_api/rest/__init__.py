from flask import Flask

app = Flask(__name__, static_folder=None)

from rest.controllers import errors, thread, stats

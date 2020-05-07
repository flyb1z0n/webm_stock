from flask import Flask

app = Flask(__name__)

from rest.controllers import thread, stats

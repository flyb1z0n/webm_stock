from flask import jsonify
from werkzeug.exceptions import HTTPException
from api import app


@app.errorhandler(HTTPException)
def page_not_found(e):
    return jsonify(error=str(e.description)), e.code

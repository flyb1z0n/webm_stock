from flask import request
from flask import jsonify

from restapi import app


@app.route('/hello', methods=['POST'])
def hello_world():
    print(request.json)
    return jsonify({
        'status': 'ok'
    })

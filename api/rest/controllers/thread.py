from flask import request
from flask import jsonify

from rest import app


@app.route('/hello', methods=['POST'])
def hello_world():
    print(request.json)
    return jsonify({
        'status': 'ok'
    })

@app.route('/thread/', methods=['GET'])
def get_thread(id):
    return jsonify()
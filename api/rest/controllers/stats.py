from flask import jsonify
from rest import app


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok'
    })

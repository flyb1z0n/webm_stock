from flask import jsonify, request

from api import app
from api.services import file_service


@app.route('/files', methods=['GET'])
def get_files():
    size = request.args.get('size', 30, int)
    page = request.args.get('page', 1, int)

    return jsonify(file_service.get_new_files(size, page))

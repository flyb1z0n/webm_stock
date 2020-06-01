from flask import jsonify, abort, request

from api import app
from api.services import thread_service


# TODO open when security comes in
# @app.route('/thread', methods=['POST'])
# def create_thread():
#     thread = thread_service.create_thread(request.json)
#     return jsonify(thread)

@app.route('/thread/<int:num>', methods=['GET'])
def get_thread(num):
    thread = thread_service.get_thread(num)
    if thread is None:
        abort(404, 'Thread num #' + str(num) + ' does not exist.')
    return jsonify(thread)


# TODO open when security comes in
# @app.route('/thread', methods=['POST'])
# def create_thread():
#     thread = thread_service.create_thread(request.json)
#     return jsonify(thread)


# TODO open when security comes in
# @app.route('/thread/<int:num>', methods=['PUT'])
# def update_thread(num):
#     thread = thread_service.update_thread(num, request.json)
#     return jsonify(thread)

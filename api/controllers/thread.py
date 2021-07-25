from flask import abort
from flask_restx import Resource
from api import restx_api
from api.services import thread_service

@restx_api.route(
    '/thread/<int:num>',
    doc={
        "description": "API for interaction with threads."
    }
)
class GetThread(Resource):
    
    @restx_api.response(404, 'Thread not found')
    @restx_api.response(200, 'Thread found')
    def get(self, num):
        thread = thread_service.get_thread(num)
        if thread is None:
            restx_api.abort(404, 'Thread num #' + str(num) + ' does not exist.')
        return thread



# @app.route('/thread/<int:num>', methods=['GET'])
# def get_thread(num):
#     thread = thread_service.get_thread(num)
#     if thread is None:
#         abort(404, 'Thread num #' + str(num) + ' does not exist.')
#     return jsonify(thread)

## Legacy code: (befor the flask_restx has been introduced)

# TODO open when security comes in
# @app.route('/thread', methods=['POST'])
# def create_thread():
#     thread = thread_service.create_thread(request.json)
#     return jsonify(thread)

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

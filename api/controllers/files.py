from flask import jsonify, request

from api import restx_api
from flask_restx import Resource
from api.services import file_service

DEFAULT_PAGE_SIZE = 30
DEFAULT_PAGE_IDX = 1

@restx_api.route(
    '/files',
    doc={
        "description": "Search for parsed WEBMs"
    }
)
@restx_api.doc(
    params={
	'size': {'in': 'query', 'description': 'The number of items in result', 'default': str(DEFAULT_PAGE_SIZE)},
	'page': {'in': 'query', 'description': 'Requested page number', 'default': str(DEFAULT_PAGE_IDX)}
    })
class Files(Resource):
    def get(self):
        size = request.args.get('size', DEFAULT_PAGE_SIZE, int)
        page = request.args.get('page', DEFAULT_PAGE_IDX, int)
        return jsonify(file_service.get_new_files(size, page))

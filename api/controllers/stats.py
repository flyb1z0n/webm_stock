from api import restx_api
from flask_restx import Resource

@restx_api.route(
    '/health',
    doc={
        "description": "Lightweight API for health check."
    }
)
class Health(Resource):
    def get(self):
        return { 'status': 'ok'}

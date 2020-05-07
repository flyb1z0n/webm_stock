from rest.data import mongodb
from werkzeug.exceptions import BadRequest, NotFound

ALLOWED_THREAD_STATUSES = {'ACTIVE', 'IN-ACTIVE'}


def validate_creation(payload):
    if not payload.get('num'):
        raise BadRequest("'num' field is required")

    if mongodb.get_thread_by_num(str(payload.get('num'))) is not None:
        raise BadRequest("Thread #" + str(payload.get('num')) + " already exist")

    if payload.get('status') and payload.get('status') not in ALLOWED_THREAD_STATUSES:
        raise BadRequest("'status' must be one of " + str(ALLOWED_THREAD_STATUSES))


def validate_update(num, payload):
    thread = mongodb.get_thread_by_num(str(num))
    if thread is not None:
        raise NotFound('Thread num #' + str(num) + ' does not exist.')

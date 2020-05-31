from data import mongodb
from api.services.validators import thread_validator as validator
from datetime import datetime



def _convert_to_thread(db_entry):
    if db_entry is None:
        return None
    db_entry.pop('_id')
    if db_entry.get('last_sync_date', '') and isinstance(db_entry['last_sync_date'], datetime):
        db_entry['last_sync_date'] = db_entry['last_sync_date'].isoformat()

    if db_entry.get('creation_date', '') and isinstance(db_entry['creation_date'], datetime):
        db_entry['creation_date'] = db_entry['creation_date'].isoformat()

    if db_entry.get('last_update_date', '') and isinstance(db_entry['last_update_date'], datetime):
        db_entry['last_update_date'] = db_entry['last_update_date'].isoformat()
    return db_entry


def get_thread(num):
    return _convert_to_thread(mongodb.get_thread_by_num(str(num)))


def create_thread(payload):
    validator.validate_creation(payload)
    num = str(payload['num'])
    status = str(payload.get('status', 'ACTIVE'))
    mongodb.insert_thread(num, status)
    return get_thread(num)


def update_thread(num, payload):
    validator.validate_update(num, payload)

    data = {}
    if payload.get('last_post_num', ''):
        data['last_post_num'] = str(payload['last_post_num'])

    if payload.get('status', ''):
        data['status'] = str(payload['status'])

    if payload.get('fail_count', ''):
        data['fail_count'] = str(payload['fail_count'])

    if payload.get('last_sync_date', ''):
        data['last_sync_date'] = datetime.fromisoformat(payload['last_sync_date'])

    mongodb.update_thread_by_num(num, data)
    return get_thread(num)

from werkzeug.exceptions import BadRequest
from datetime import datetime
from dynaconf import settings

from data import mongodb

def get_new_files(size, page):
    if size <= 0:
        raise BadRequest("Size cannot be less than 1")
    if page <= 0:
        raise BadRequest("Page cannot be less than 1")

    result = []
    for file in mongodb.get_new_files(size, (page - 1)*size):
        result.append(_convert_to_file(file))
    return result


def _convert_to_file(db_entry):
    if db_entry is None:
        return None
    db_entry['id'] = str(db_entry.pop('_id'))
    db_entry['base_url'] = settings.BASE_2CH_URL

    if db_entry.get('creation_date', '') and isinstance(db_entry['creation_date'], datetime):
        db_entry['creation_date'] = db_entry['creation_date'].isoformat()

    return db_entry

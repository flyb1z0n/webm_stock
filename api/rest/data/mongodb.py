from pymongo import MongoClient
from datetime import datetime, timedelta
from dynaconf import settings

client = MongoClient(settings.DB_URL, settings.DB_PORT)
db = client[settings.DB_NAME]


def test():
    return db[settings.DB_COLLECTION_TEST]


def api_response_collection():
    return db[settings.DB_API_RESPONSES]


def threads_collection():
    return db[settings.DB_THREADS]


def files_collection():
    return db[settings.DB_FILES]


def get_thread_by_num(num):
    return threads_collection().find_one({'num': num})


def update_thread_by_num(num, data):
    data['last_update_date'] = datetime.now()
    res = threads_collection().update({'num': str(num)}, {'$set': data})
    return res


def insert_thread(num, status):
    threads_collection().insert_one({
        'num': num,
        'status': status,
        'creation_date' : datetime.now(),
        'last_sync_date' : datetime.fromtimestamp(0)
        })


# retrieves threads that were processed more than THREAD_MONITOR_THREAD_REQUEST_DELAY_SECONDS seconds ago 
def get_next_thread_to_process():
    date = datetime.now() - timedelta(seconds=settings.THREAD_MONITOR_THREAD_REQUEST_DELAY_SECONDS)
    return threads_collection().find({'status': 'ACTIVE', 'last_sync_date': {"$lt": date}}).sort([('last_sync_date', 1)]).limit(1)


def update_thread(num, status='ACTIVE', fail_count=0, last_post_num=None):
    data = {
        'last_sync_date':  datetime.now(),
        'status': status,
        'fail_count': fail_count
    }
    if last_post_num is not None:
        data['last_post_num'] = last_post_num

    threads_collection().update({'num': num}, {'$set': data})


def add_file(num, file):
    file['thread_num'] = num
    file['creation_date'] = datetime.now()
    file['status'] = 'NEW' 
    files_collection().insert_one(file)

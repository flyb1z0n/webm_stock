from pymongo import MongoClient
import config 
import datetime

client = MongoClient(config.DB_URL,config.DB_PORT);
db = client[config.DB_NAME]

def test():
    return db[config.DB_COLLECTION_TEST]

def api_response_collection():
    return db[config.DB_API_RESPONSES]

def threads_collection():
    return db[config.DB_THREADS]

def save_api_response(response):
    entry = {
        'url' : response.url,
        'status_code' : response.status_code,
        'content' : response.text,
        'date' : str(datetime.datetime.now())
    }
    api_response_collection().insert_one(entry)

def get_thread_by_num(num):
    return threads_collection().find_one({'num':num});

def insert_thread(num, status):
    threads_collection().insert_one({'num':num, 'status': status})
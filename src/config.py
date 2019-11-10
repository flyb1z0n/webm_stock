import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(threadName)s] - %(message)s")

DB_URL = 'webm_db'
DB_PORT = 27017
DB_NAME = 'webm_stock'


DB_COLLECTION_TEST = 'test'
DB_API_RESPONSES = 'api_responses'
DB_THREADS = 'threads'
DB_FILES = 'files'


BOARD_MONITOR_DELAY_SECONDS = 60
THREAD_MONITOR_THREAD_REQUEST_DELAY_SECONDS = 60  
THREAD_FAIL_COUNT_LIMIT = 5

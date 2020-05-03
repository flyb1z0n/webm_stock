import requests 
import traceback
import time
from crawler.data import mongodb
import logging
import threading


class BoardMonitor(threading.Thread):

    def __init__(self, url, delay):
        self.url = url
        self.delay = delay
        threading.Thread.__init__(self)
    
    def run(self):
        while(True):
            try:
                self._process_updates()
            except:
                logging.info("An exception occurred")
                traceback.print_exc() 
            logging.info("Sleeping for " + str(self.delay) + " seconds.")
            time.sleep(self.delay)
    
    # one iteration -> checks new threads
    def _process_updates(self):
        threads = self._get_threads()
        saved_count = self._save_new_threads(threads)
        self._log_result(saved_count)

    def _get_threads(self):
        logging.info("Requesting " + self.url)
        r = requests.get(url = self.url, timeout=10) 
        mongodb.save_api_response(r)
        if r.status_code != requests.codes.ok:
            logging.info('Request failed.')
            return []
        logging.info("Response status code: " + str(r.status_code))
        return r.json()['threads']

    @staticmethod
    def _save_new_threads(threads):
        num_saved = 0;
        if threads == []:
            return num_saved
        for thread in threads:
            found = mongodb.get_thread_by_num(thread['num'])
            if found is None:
                mongodb.insert_thread(num = thread['num'], status = 'ACTIVE')
                num_saved += 1
        return num_saved


    def _log_result(self, saved_count):
        if saved_count == 0:
            logging.info('0 new threads.')
        else:
            logging.info(str(saved_count) + ' new threads.')
        return 


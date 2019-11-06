import requests 
import traceback
import time
import config
import mongodb
import logging
import threading

class BoardMonitor(threading.Thread):
    THREAD_URL = "https://2ch.hk/b/threads.json";

    def __init__(self, delay = 0):
        self.delay = delay;
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
    
    def _process_updates(self):
        threads = self._get_threads()

        saved_count = self._save_new_threads(threads)
        self._log_result(saved_count)

    def _get_threads(self):
        r = requests.get(url = self.THREAD_URL, timeout=10) 
        mongodb.save_api_response(r)
        if(r.status_code != requests.codes.ok):
            logging.info('Request failed.')
            return []
        return r.json()['threads']

    def _save_new_threads(self, threads):
        num_saved = 0;
        if threads == []:
            return num_saved;
        for thread in threads:
            found = mongodb.get_thread_by_num(thread['num'])
            if found is None:
                mongodb.insert_thread(num = thread['num'], status = 'ACTIVE')
                num_saved += 1
        return num_saved;

    def _log_result(self, saved_count):
        if saved_count == 0:
            logging.info('0 new threads.')
        else:
            logging.info(str(saved_count) + ' new threads.')
        return 
        
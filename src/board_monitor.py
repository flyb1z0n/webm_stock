import requests 
import traceback
import time
import config
import mongodb

class BoardMonitor:
    THREAD_URL = "https://2ch.hk/b/threads.json";
    delay = 0

    def __init__(self, delay):
        self.delay = delay;
    
    def monitor(self):
        while(True):
            try:
                self._process_updates()
            except:
                print("An exception occurred")
                traceback.print_exc() 
            print("Sleeping for " + str(self.delay) + " seconds.")
            time.sleep(self.delay)
    
    def _process_updates(self):
        threads = self._get_threads()

        saved_count = self._save_new_threads(threads)
        self._log_result(saved_count)

    def _get_threads(self):
        r = requests.get(url = self.THREAD_URL, timeout=10) 
        mongodb.save_api_response(r)
        if(r.status_code != requests.codes.ok):
            print('Request failed.')
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
            print('0 new threads.')
        else:
            print(str(saved_count) + ' new threads.')
        return 
        

# print(config.BOARD_MONITOR_DELAY_SECONDS)

# id = mongodb.test().insert_one({'first':'value1', 'second':'value2'}).inserted_id
# print(id)
BoardMonitor(config.BOARD_MONITOR_DELAY_SECONDS).monitor();
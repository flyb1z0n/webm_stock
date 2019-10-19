import requests 
import traceback
import time
import config




class BoardMonitor:
    THREAD_URL = "https://2ch.hk/b/threads.json";
    OK_STATUS_CODE = 200;
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
        if(r.status_code != self.OK_STATUS_CODE):
            print('Request failed.')
            return []
        return r.json()['threads']
    
    def _save_new_threads(self, threads):
        if threads == []:
            return 0;
        print(threads[0])

    def _log_result(self, saved_count):
        if saved_count == 0:
            print('No new threads.')
        else:
            print(str(saved_count) + ' new threads.')
        return 
        

print(config.BOARD_MONITOR_DELAY_SECONDS)

BoardMonitor(config.BOARD_MONITOR_DELAY_SECONDS).monitor();
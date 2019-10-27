import traceback
import config
import time
import mongodb

class ThreadMonitor:

    def __init__(self, delay = 0):
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
        while True:
            # threads - should always have size of 0 or 1
            threads = mongodb.get_next_thread_to_process();
            if threads is None:
                return
            for thread in threads:
                self._proces_thread(thread)
    
    def _proces_thread(self, thread):
        print(thread)
        mongodb.update_thread_sync_date(thread['num']);
        
        


ThreadMonitor(config.BOARD_MONITOR_DELAY_SECONDS).monitor();
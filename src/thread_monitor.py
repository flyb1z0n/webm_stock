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

        # todo implement
        for r in mongodb.get_next_thread_to_process():
            print(r)
        


ThreadMonitor(config.BOARD_MONITOR_DELAY_SECONDS).monitor();
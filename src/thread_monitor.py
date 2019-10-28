import traceback
import config
import time
import mongodb
import requests

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
            threads = mongodb.get_next_thread_to_process()
            if threads is None:
                return
            for thread in threads:
                self._proces_thread(thread)
    
    def _proces_thread(self, thread):
        print(thread)
        thread_num = thread['num']
        last_post_num = thread.get('last_post_num', 0)
        try:
            posts = self._get_posts(thread_num)
            posts = [x for x in posts if x['num'] > last_post_num]
            max_post_num = max((x['num'] for x in posts))
            files = sum([x['files'] for x in posts],[])
            for file in files:
                mongodb.add_file(thread_num, file)
            print("Thread # "+ str(thread_num) + ' added '+ str(len(files)) + " files to download")
            mongodb.update_thread(thread_num, last_post_num = max_post_num)
        except:
            print("Error during getting content of thread # " + str(thread_num))
            traceback.print_exc() 
            fail_count = thread.get('fail_count', 0);
            fail_count += 1
            status = 'IN-ACTIVE' if fail_count > config.THREAD_FAIL_COUNT_LIMIT else 'ACTIVE'
            mongodb.update_thread(thread_num, status = status, fail_count = fail_count)      
        
    def _get_posts(self, num):
        url = 'https://2ch.hk/b/res/'+ str(num) + '.json'
        r = requests.get(url = url, timeout=10)
        if(r.status_code != requests.codes.ok):
            raise Exception(url+" responds with " +str(r.status_code))
        return r.json()['threads'][0]['posts']
        


ThreadMonitor(config.BOARD_MONITOR_DELAY_SECONDS).monitor();

# ThreadMonitor()._proces_thread({'num':206331907, 'last_post_num':206342171})
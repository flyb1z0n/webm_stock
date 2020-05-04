import traceback
import time
from crawler.data import mongodb
import requests
import threading
import logging
import os


class ThreadMonitor(threading.Thread):

    def __init__(self, url, delay, fail_limit, media_extensions):
        self.url = url
        self.delay = delay
        self.fail_limit = fail_limit
        print(media_extensions)
        self.media_extensions = set(media_extensions.split(' '))
        threading.Thread.__init__(self)

    def run(self):
        logging.info("Thread monitor has been started.")
        while True:
            try:
                self._process_updates()
            except:
                logging.info("An exception occurred")
                traceback.print_exc() 
            logging.info("Sleeping for " + str(self.delay) + " seconds.")
            time.sleep(self.delay)

    # one iteration -> process one 2ch thread
    def _process_updates(self):
        # threads - should always have size of 0 or 1
        threads = mongodb.get_next_thread_to_process()
        if threads is None:
            return
        for thread in threads:
            self._process_thread(thread)
    
    def _process_thread(self, thread):
        logging.info(thread)
        thread_num = thread['num']
        last_post_num = thread.get('last_post_num', 0)
        try:
            posts = self._get_posts(thread_num)
            posts = [x for x in posts if x['num'] > last_post_num]
            if not posts:
                mongodb.update_thread(thread_num, last_post_num=last_post_num)
                logging.info("No new posts for thread # " + str(thread_num))
                return
            max_post_num = max((x['num'] for x in posts))
            files = sum([x['files'] for x in posts], [])
            count_media_files = 0
            for file in files:
                name, ext = os.path.splitext(file['name'])
                if ext.lower() in self.media_extensions:
                    mongodb.add_file(thread_num, file)
                    count_media_files += 1
            logging.info("Updates for thread #" + str(thread_num)
                         + ' found ' + str(len(files)) + " files"
                         + ' added ' + str(count_media_files) + " media files")
            mongodb.update_thread(thread_num, max_post_num)
        except:
            logging.info("Error during getting content of thread # " + str(thread_num))
            traceback.print_exc() 
            fail_count = thread.get('fail_count', 0)
            fail_count += 1
            logging.info("Fail count: " + str(fail_count))
            status = 'IN-ACTIVE' if fail_count > self.fail_limit else 'ACTIVE'
            mongodb.update_thread(thread_num, status, fail_count)
        
    def _get_posts(self, num):
        url = self.url.format(str(num))
        logging.info("Requesting " + url)
        r = requests.get(url=url, timeout=10)
        if r.status_code != requests.codes.ok:
            raise Exception(url + " responds with " + str(r.status_code))
        return r.json()['threads'][0]['posts']

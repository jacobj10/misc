import requests
import argparse
import sleek_logger
import re
import hashlib
import threading
import queue 

MAX_NUM_THREADS = 3

class RequestMachine(object):
    def __init__(self, *args, **kwargs):
        args = self.parse_args()
        self.url = args.url
        self.extension = self.url.split('.')[-1]
        self.logged = {}
        self.queue = queue.Queue()
        self.threads = []
        self.init_threads()
        self.hasher = hashlib.md5
        self.logger = sleek_logger.SleekLogger('SiteTrav.log')
        self.scrape_urls(self.url)

    def worker(self):
        while True:
            current = self.queue.get()
            if current is None:
                break
            try:
                resp = requests.get(current).text
            except requests.exceptions.ConnectionError:
                self.logger.log('Error handling ' + current, 'error')
            else:
                matches = re.findall('href=[\'"]?([^\'" >]+)', resp)
                for match in matches:
                    new_url = self.url + match
                    _hash = self.hasher(new_url.encode()).hexdigest()
                    if _hash in self.logged or (not match.startswith('/') and not match.startswith('#')):
                        continue
                    else:
                        self.logged[_hash] = new_url
                        self.logger.log('Traversing: ' + new_url)
                        self.scrape_urls(new_url)
                    
    def init_threads(self):
        for i in range(MAX_NUM_THREADS):
            t = threading.Thread(target=self.worker)
            t.start()
            self.threads.append(t)

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Args for brute forcing requests.')
        parser.add_argument('url', help='an integer for the accumulator')
        args = parser.parse_args()
        return args

    def test_connection(self):
        counter = 0
        return requests.get(self.url).status_code == 200


    def scrape_urls(self, current):
        self.queue.put(current)

if __name__ == '__main__':
    x = RequestMachine()

import requests
import argparse
import sleek_logger
import re

class RequestMachine(object):
    def __init__(self, *args, **kwargs):
        args = self.parse_args()
        self.url = args.url
        self.extension = self.url.split('.')[-1]
        self.logged = []
        self.logger = sleek_logger.SleekLogger('SiteTrav.log')

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Args for brute forcing requests.')
        parser.add_argument('url', help='an integer for the accumulator')
        args = parser.parse_args()
        return args

    def test_connection(self):
        counter = 0
        return requests.get(self.url).status_code == 200


    def scrape_urls(self, current):
        try:
            resp = requests.get(current).text
        except requests.exceptions.ConnectionError:
            self.logger.log('Error handling ' + current, 'error')
        else:
            matches = re.findall('href=[\'"]?([^\'" >]+)', resp)
            for match in matches:
                new_url = self.url + match
                if new_url in self.logged or (not match.startswith('/') and not match.startswith('#')):
                    continue
                else:
                    self.logged.append(new_url)
                    self.logger.log('Traversing: ' + new_url)
                    self.scrape_urls(new_url)
if __name__ == '__main__':
    x = RequestMachine()
    x.test_connection()
    x.scrape_urls(x.url)

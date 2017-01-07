import requests
import argparse

class RequestMachine(object):
    def __init__(self, *args, **kwargs):
        args = self.parse_args()
        self.wordlist = args.wordlist
        self.url = args.url

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Args for brute forcing requests.')
        parser.add_argument('url', help='an integer for the accumulator')
        parser.add_argument('--wordlist', default='wordlist.txt', help='alternative wordlist')
        args = parser.parse_args()
        return args

    def test_connection(self):
        while requests.get(self.url).status_code != 200:
            

if __name__ == '__main__':
    x = RequestMachine()
    x.test_connection()

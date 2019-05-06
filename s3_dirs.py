import sys
import requests
import queue
import os
import urllib

from xml.etree import ElementTree

URL = sys.argv[1]
initial_val = "{}?list-type=2".format(URL)
NEW_URL = "{}&continuation-token={}"

DIRS = []

worklist = queue.Queue()
worklist.put(initial_val)
while (worklist.qsize() != 0):
    item = worklist.get()
    resp = requests.get(item)
    resp_as_xml = ElementTree.fromstring(resp.text)
    logs = False
    for node in resp_as_xml:
        parsed_name = node.tag.split('}')[-1]
        if parsed_name == "NextContinuationToken":
            new_url = NEW_URL.format(initial_val, urllib.parse.quote_plus(node.text))
            worklist.put(new_url)
        elif parsed_name == "Contents":
            key = node[0].text
            to_print = os.path.dirname(key)
            if "logs" in key:
                logs = True
                break
            print(key)
    if logs:
        break

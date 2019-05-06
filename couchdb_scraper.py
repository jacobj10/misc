import requests
import sys
import json

URL = sys.argv[1]
DB_DMP = "{}/{}/_all_docs?include_docs=true"
resp = json.loads(requests.get(URL + '/_all_dbs').text)

for db in resp:
    print(db)
    print(requests.get(DB_DMP.format(URL, db)).text)

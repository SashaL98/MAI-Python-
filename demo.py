import requests
import json

BASE_URL = "https://api.covid19api.com"
ENDPOINT = "/summary"

def get_info_from_api():
    info = requests.get(BASE_URL+ENDPOINT)
    return info

INFO = get_info_from_api()

STATUS_CODE = INFO.status_code
BODY = INFO.json()

print(STATUS_CODE, INFO.ok)
print(BODY.keys())



#print(COUNTRIES[1]["Country"])
print(json.dumps(BODY["Message"], indent=4))
print(json.dumps(BODY["Global"], indent=4))
print(json.dumps(BODY["Countries"], indent=4))
print(json.dumps(BODY["Date"], indent=4))

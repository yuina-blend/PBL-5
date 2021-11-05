import requests
import json
import os

s = str(input())

WEB_HOOK_URL = os.environ['SLACK_TOKEN']

requests.post(WEB_HOOK_URL, data=json.dumps({
    "text" : s,
}))
print ("ok")

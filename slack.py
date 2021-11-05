import requests
import json
import os

WEB_HOOK_URL = os.environ['SLACK_TOKEN']

requests.post(WEB_HOOK_URL, data=json.dumps({
    "text" : "テストおおおおおおおおおおおお",
}))
print ("ok")

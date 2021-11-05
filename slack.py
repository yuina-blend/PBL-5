
class slack:
    import requests
    import json
    import os
    def slack(self,s):
        WEB_HOOK_URL = os.environ['SLACK_TOKEN']

        requests.post(WEB_HOOK_URL, data=json.dumps({
            "text" : s,
        }))
        print ("ok")

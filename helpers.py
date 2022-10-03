import requests
import json
from base64 import b64encode


def request_get_v1():
  count_request = requests.get(f"https://{self.instance_url}.app.liongard.com/api/v2/environments/count", headers=self.headers)
  count = json.loads(count_request.content)

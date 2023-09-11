"""
The model uses the requests moduleno to fetch and get request from alu-intranet
"""

import requests

req = requests.get("https://alu-intranet.hbtn.io/status")
print("Body response:\n\t- type: {}\n\t- content: {}".format(type(req.text),req.text))
import sys
import os
import time
from time import sleep
import requests
import urllib3
import json
cert = False

def ListAllCompGroup(url_link_final, tenant1key):
    payload  = {}
    url = url_link_final + 'api/computergroups'
    headers = {
        "api-secret-key": tenant1key,
        "api-version": "v1",
        "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=cert)
    describe = str(response.text)
    index = 0
    oldcompgroupname = []
    oldcompgroupid = []
    namejson = json.loads(describe)
    for here in namejson['computerGroups']:
        oldcompgroupname.append(str(here['name']))
        oldcompgroupid.append(str(here['ID']))

    return oldcompgroupname, oldcompgroupid
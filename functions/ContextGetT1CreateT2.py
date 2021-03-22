import sys
import os
import time
from time import sleep
import requests
import urllib3
import json
cert = False

def ContextGet(url_link_final, tenant1key):
    t1contextall = []
    t1contextname = []
    t1contextid = []
    print("Getting All Context Configuration...", flush=True)
    payload  = {}
    url = url_link_final + 'api/contexts'
    headers = {
        "api-secret-key": tenant1key,
        "api-version": "v1",
        "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=cert)
    describe = str(response.text)
    describe2 = str(response.text)
    namejson = json.loads(describe)
    for count, here in enumerate(namejson['contexts']):
        t1contextall.append(str(json.dumps(here)))
        t1contextname.append(str(here['name']))
        print("#" + str(count) + " Context Config name: " + str(here['name']), flush=True)
        t1contextid.append(str(here['ID']))
        print("#" + str(count) + " Context Config ID: " + str(here['ID']), flush=True)

    #print(t1contextid)
    print("Done", flush=True)
    return t1contextall, t1contextname, t1contextid

def ContextCreate(t1contextall, t1contextname, url_link_final_2, tenant2key):
    t2contextid = []
    print("Transfering All Context Configuration...", flush=True)
    if t1contextname:
        for count, dirlist in enumerate(t1contextname):
            payload = "{\"searchCriteria\": [{\"fieldName\": \"name\",\"stringValue\": \"" + dirlist + "\"}]}"
            url = url_link_final_2 + 'api/contexts/search'
            headers = {
            "api-secret-key": tenant2key,
            "api-version": "v1",
            "Content-Type": "application/json",
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
            describe = str(response.text)
            taskjson = json.loads(describe)
            if not 'message' in taskjson:
                if taskjson['contexts']:
                    for here in taskjson['contexts']:
                        indexid = here['ID']
                        payload = t1contextall[count]
                        url = url_link_final_2 + 'api/contexts/' + str(indexid)
                        headers = {
                        "api-secret-key": tenant2key,
                        "api-version": "v1",
                        "Content-Type": "application/json",
                        }
                        response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
                        describe = str(response.text)
                        taskjson1 = json.loads(describe)
                        t2contextid.append(str(taskjson1['ID']))
                        print("#" + str(count) + " Context Config name: " + taskjson1['name'], flush=True)
                        print("#" + str(count) + " Context Config ID: " + str(taskjson1['ID']), flush=True)
                else:
                    payload = t1contextall[count]
                    url = url_link_final_2 + 'api/contexts'
                    headers = {
                    "api-secret-key": tenant2key,
                    "api-version": "v1",
                    "Content-Type": "application/json",
                    }
                    response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
                    describe = str(response.text)
                    taskjson = json.loads(describe)
                    t2contextid.append(str(taskjson['ID']))
                    print("#" + str(count) + " Context Config name: " + taskjson['name'], flush=True)
                    print("#" + str(count) + " Context Config ID: " + str(taskjson['ID']), flush=True)
            else:
                print(describe, flush=True)
                print(payload, flush=True)
    #print(t2contextid)
    print("Done!", flush=True)
    return t2contextid

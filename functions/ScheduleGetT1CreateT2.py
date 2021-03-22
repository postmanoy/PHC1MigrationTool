import sys
import os
import time
from time import sleep
import requests
import urllib3
import json
cert = False

def ScheduleGet(url_link_final, tenant1key):
    t1scheduleall = []
    t1schedulename = []
    t1scheduleid = []
    print("Getting All Schedule Configuration...", flush=True)
    payload  = {}
    url = url_link_final + 'api/schedules'
    headers = {
        "api-secret-key": tenant1key,
        "api-version": "v1",
        "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=cert)
    describe = str(response.text)
    describe2 = str(response.text)
    namejson = json.loads(describe)
    for count, here in enumerate(namejson['schedules']):
        t1scheduleall.append(str(json.dumps(here)))
        t1schedulename.append(str(here['name']))
        print("#" + str(count) + " Schedule Config name: " + str(here['name']), flush=True)
        t1scheduleid.append(str(here['ID']))
        print("#" + str(count) + " Schedule Config ID: " + str(here['ID']), flush=True)

    #print(t1scheduleid)
    print("Done", flush=True)
    return t1scheduleall, t1schedulename, t1scheduleid

def ScheduleCreate(t1scheduleall, t1schedulename, url_link_final_2, tenant2key):
    t2scheduleid = []
    print("Transfering All Schedule Configuration...", flush=True)
    if t1schedulename:
        for count, dirlist in enumerate(t1schedulename):
            payload = "{\"searchCriteria\": [{\"fieldName\": \"name\",\"stringValue\": \"" + dirlist + "\"}]}"
            url = url_link_final_2 + 'api/schedules/search'
            headers = {
            "api-secret-key": tenant2key,
            "api-version": "v1",
            "Content-Type": "application/json",
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
            describe = str(response.text)
            taskjson = json.loads(describe)
            if not 'message' in taskjson:
                if taskjson['schedules']:
                    for here in taskjson['schedules']:
                        indexid = here['ID']
                        payload = t1scheduleall[count]
                        url = url_link_final_2 + 'api/schedules/' + str(indexid)
                        headers = {
                        "api-secret-key": tenant2key,
                        "api-version": "v1",
                        "Content-Type": "application/json",
                        }
                        response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
                        describe = str(response.text)
                        taskjson1 = json.loads(describe)
                        t2scheduleid.append(str(taskjson1['ID']))
                        print("#" + str(count) + " Schedule Config name: " + taskjson1['name'], flush=True)
                        print("#" + str(count) + " Schedule Config ID: " + str(taskjson1['ID']), flush=True)
                else:
                    payload = t1scheduleall[count]
                    url = url_link_final_2 + 'api/schedules'
                    headers = {
                    "api-secret-key": tenant2key,
                    "api-version": "v1",
                    "Content-Type": "application/json",
                    }
                    response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
                    describe = str(response.text)
                    taskjson = json.loads(describe)
                    t2scheduleid.append(str(taskjson['ID']))
                    print("#" + str(count) + " Schedule Config name: " + taskjson['name'], flush=True)
                    print("#" + str(count) + " Schedule Config ID: " + str(taskjson['ID']), flush=True)
            else:
                print(describe, flush=True)
                print(payload, flush=True)
    #print(t2scheduleid)
    print("Done!", flush=True)
    return t2scheduleid
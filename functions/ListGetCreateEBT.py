import sys
import os
import time
from time import sleep
import requests
import urllib3
import json

cert = False

def ListEventTask(url_link_final, tenant1key):
    payload = {}
    url = url_link_final + 'api/eventbasedtasks'
    headers = {
    "api-secret-key": tenant1key,
    "api-version": "v1",
    "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=cert)
    describe = str(response.text)
    index = 0
    oldetname = []
    oldetid = []
    namejson = json.loads(describe)
    for here in namejson['eventBasedTasks']:
        oldetname.append(str(here['name']))
        oldetid.append(str(here['ID']))

                    
    return oldetname, oldetid

def GetEventTask(etIDs, oldpolicyname, oldpolicyid, oldcompgroupname, oldcompgroupid, url_link_final, tenant1key, url_link_final_2, tenant2key):
    allet = []
    nameet = []
    print ('Getting Target Task...', flush=True)
    if etIDs:
        for count, part in enumerate(etIDs):
            payload = {}
            url = url_link_final + 'api/eventbasedtasks/' + str(part)
            headers = {
            "api-secret-key": tenant1key,
            "api-version": "v1",
            "Content-Type": "application/json",
            }
            response = requests.request("GET", url, headers=headers, data=payload, verify=cert)
            describe = str(response.text)
            taskjson = json.loads(describe)
            checker = 0
            print("#" + str(count) + " Event Based Task name: " + str(taskjson['name']), flush=True)
            for count, atype in enumerate(taskjson['actions']):
                typekey = atype['type']
                if typekey == 'assign-policy':
                    if 'parameterValue' in atype:
                        param = atype['parameterValue']
                        indexnum = oldpolicyid.index(str(param))
                        polname = str(oldpolicyname[indexnum])
                        payload = "{\"searchCriteria\": [{\"fieldName\": \"name\",\"stringValue\": \"" + polname + "\"}]}"
                        url = url_link_final_2  + 'api/policies/search'
                        headers = {
                        "Authorization": "ApiKey " + tenant2key,
                        "api-version": "v1",
                        "Content-Type": "application/json",
                        }
                        response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
                        policyjson1 = json.loads(str(response.text))
                        if policyjson1['policies']:
                            idjson = policyjson1['policies']
                            taskjson['actions'][count]['parameterValue'] = str(idjson[0]['ID'])
                        else:
                            print("Policy did not found. Will skip this Event based Task.")
                            checker = checker + 1
                elif typekey == 'assign-relay':
                    if 'parameterValue' in atype:
                        del taskjson['actions'][count]['parameterValue']
                elif typekey == 'assign-group':
                    if 'parameterValue' in atype:
                        param = atype['parameterValue']
                        indexnum = oldcompgroupid.index(str(param))
                        polname = str(oldcompgroupname[indexnum])
                        payload = "{\"searchCriteria\": [{\"fieldName\": \"name\",\"stringValue\": \"" + polname + "\"}]}"
                        url = url_link_final_2  + 'api/computergroups/search'
                        headers = {
                        "Authorization": "ApiKey " + tenant2key,
                        "api-version": "v1",
                        "Content-Type": "application/json",
                        }
                        response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
                        policyjson1 = json.loads(str(response.text))
                        if policyjson1['computerGroups']:
                            idjson = policyjson1['computerGroups']
                            taskjson['actions'][count]['parameterValue'] = str(idjson[0]['ID'])
                            #will not be skipped
                            describe1 = json.dumps(taskjson)
                            allet.append(str(describe1))
                            nameet.append(str(taskjson['name']))
                        else:
                            print("Computer Group did not found. Will skip this Event based Task.")
                            checker = checker + 1
            if checker == 0:
                describe1 = json.dumps(taskjson)
                allet.append(str(describe1))
                nameet.append(str(taskjson['name']))
            
    #print(allet, flush=True)
    #print(nameet, flush=True)
    return allet, nameet

def CreateEventTask(allet, nameet, url_link_final_2, tenant2key):
    if nameet:
        print ('Creating Task to target Account...', flush=True)
        for count, dirlist in enumerate(nameet):
            payload = "{\"searchCriteria\": [{\"fieldName\": \"name\",\"stringValue\": \"" + dirlist + "\"}]}"
            url = url_link_final_2 + 'api/eventbasedtasks/search'
            headers = {
            "Authorization": "ApiKey " + tenant2key,
            "api-version": "v1",
            "Content-Type": "application/json",
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
            describe = str(response.text)
            taskjson = json.loads(describe)
            if not 'message' in taskjson:
                if taskjson['eventBasedTasks']:
                    for here in taskjson['eventBasedTasks']:
                        indexid = here['ID']
                        payload = allet[count]
                        url = url_link_final_2 + 'api/eventbasedtasks/' + str(indexid)
                        headers = {
                        "Authorization": "ApiKey " + tenant2key,
                        "api-version": "v1",
                        "Content-Type": "application/json",
                        }
                        response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
                        describe = str(response.text)
                        taskjson2 = json.loads(describe)
                        print("#" + str(count) + " Event Based Task name: " + str(taskjson2['name']), flush=True)
                        print("#" + str(count) + " Event Based ID: " + str(taskjson2['ID']), flush=True)
                else:
                    payload = allet[count]
                    url = url_link_final_2 + 'api/eventbasedtasks'
                    headers = {
                    "Authorization": "ApiKey " + tenant2key,
                    "api-version": "v1",
                    "Content-Type": "application/json",
                    }
                    response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
                    describe = str(response.text)
                    taskjson2 = json.loads(describe)
                    
                    if not 'message' in taskjson2:
                        print("#" + str(count) + " Event Based Task name: " + str(taskjson2['name']), flush=True)
                        print("#" + str(count) + " Event Based ID: " + str(taskjson2['ID']), flush=True)
                    else:
                        print(describe, flush=True)
                        print(payload, flush=True)
            else:
                print(describe, flush=True)
                print(payload, flush=True)
            #print(str(response.text), flush=True)
    print("DONE!")

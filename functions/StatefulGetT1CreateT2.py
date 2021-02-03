import sys
import os
import time
from time import sleep
import requests
import urllib3

cert = False

def StatefulGet(url_link_final, tenant1key):
    t1statefulall = []
    t1statefulname = []
    t1statefulid = []
    print("Getting All Stateful Configuration...", flush=True)
    payload  = {}
    url = url_link_final + 'api/statefulconfigurations'
    headers = {
        "api-secret-key": tenant1key,
        "api-version": "v1",
        "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=cert)
    describe = str(response.text)
    describe2 = str(response.text)
    index = describe.find('\"statefulConfigurations\"')
    if index != -1:
        indexpart = describe[index+24:]
        startIndex = 0
        while startIndex != -1: 
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex:endIndex+1]
                    t1statefulall.append(str(indexid))
                    indexpart = indexpart[endIndex:]
    count = 0
    while index != -1:
        index = describe2.find('\"name\"')
        if index != -1:
            indexpart = describe2[index+6:]
            startIndex = indexpart.find('\"')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find(',', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex-1]
                    t1statefulname.append(str(indexid))
                    print("#" + str(count) + " Stateful Config name: " + str(indexid), flush=True)
                    describe2 = indexpart[endIndex:]
                    index = describe2.find('\"ID\"')
                    if index != -1:
                        indexpart = describe2[index+3:]
                        startIndex = indexpart.find(':')
                        if startIndex != -1: #i.e. if the first quote was found
                            endIndex = indexpart.find('}', startIndex + 1)
                            if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                                indexid = indexpart[startIndex+1:endIndex]
                                t1statefulid.append(str(indexid))
                                describe2 = indexpart[endIndex:]
                                print("#" + str(count) + " Stateful Config ID: " + indexid, flush=True)
        count += 1

    #print(t1statefulid)
    print("Done", flush=True)
    return t1statefulall, t1statefulname, t1statefulid

def StatefulCreate(t1statefulall, t1statefulname, url_link_final_2, tenant2key):
    t2statefulid = []
    print("Transfering All Stateful Configuration...", flush=True)
    for count, dirlist in enumerate(t1statefulname):
        payload = "{\"searchCriteria\": [{\"fieldName\": \"name\",\"stringValue\": \"" + dirlist + "\"}]}"
        url = url_link_final_2 + 'api/statefulconfigurations/search'
        headers = {
        "api-secret-key": tenant2key,
        "api-version": "v1",
        "Content-Type": "application/json",
        }
        response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
        describe = str(response.text)
        index = describe.find(dirlist)
        if index != -1:
            index = describe.find("\"ID\"")
            if index != -1:
                indexpart = describe[index+4:]
                startIndex = indexpart.find(':')
                if startIndex != -1: #i.e. if the first quote was found
                    endIndex = indexpart.find('}', startIndex + 1)
                    if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                        indexid = indexpart[startIndex+1:endIndex]
                        payload = t1statefulall[count]
                        url = url_link_final_2 + 'api/statefulconfigurations/' + str(indexid)
                        headers = {
                        "api-secret-key": tenant2key,
                        "api-version": "v1",
                        "Content-Type": "application/json",
                        }
                        response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
                        t2statefulid.append(str(indexid))
                        print("#" + str(count) + " Stateful Config ID: " + indexid, flush=True)
            else:
                print(describe, flush=True)
                print(payload, flush=True)
        else:
            payload = t1statefulall[count]
            url = url_link_final_2 + 'api/statefulconfigurations'
            headers = {
            "api-secret-key": tenant2key,
            "api-version": "v1",
            "Content-Type": "application/json",
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
            describe = str(response.text)
            index = describe.find("\"ID\"")
            if index != -1:
                indexpart = describe[index+4:]
                startIndex = indexpart.find(':')
                if startIndex != -1: #i.e. if the first quote was found
                    endIndex = indexpart.find(',', startIndex + 1)
                    if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                        indexid = indexpart[startIndex+1:endIndex]
                        t2statefulid.append(str(indexid))
                        print("#" + str(count) + " Stateful Config ID: " + indexid, flush=True)
            else:
                print(describe, flush=True)
    #print(t2statefulid)
    print("Done!", flush=True)
    return t2statefulid

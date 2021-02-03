import sys
import os
import time
from time import sleep
import requests
import urllib3

cert = False

def ListScheduledTask(url_link_final, tenant1key):
	payload = {}
	url = url_link_final + 'api/scheduledtasks'
	headers = {
		"api-secret-key": tenant1key,
		"api-version": "v1",
		"Content-Type": "application/json",
	}
	response = requests.request("GET", url, headers=headers, data=payload, verify=cert)
	describe = str(response.text)
	index = 0
	oldstname = []
	oldstid = []
	while index != -1:
	    index = describe.find('\"name\"')
	    if index != -1:
	        indexpart = describe[index+6:]
	        startIndex = indexpart.find('\"')
	        if startIndex != -1: 
	            endIndex = indexpart.find(',', startIndex + 1)
	            if startIndex != -1 and endIndex != -1: 
	                indexid = indexpart[startIndex+1:endIndex-1]
	                oldstname.append(str(indexid))
	    index = describe.find('\"ID\"')
	    if index != -1:
	        indexpart = describe[index+4:]
	        startIndex = indexpart.find(':')
	        if startIndex != -1: 
	            endIndex = indexpart.find(',', startIndex + 1)
	            if startIndex != -1 and endIndex != -1: 
	                indexid = indexpart[startIndex+1:endIndex]
	                oldstid.append(str(indexid))
	                describe = indexpart[endIndex:]
	            else:
	                endIndex = indexpart.find('}', startIndex + 1)
	                if startIndex != -1 and endIndex != -1: 
	                    indexid = indexpart[startIndex+1:endIndex]
	                    oldstid.append(str(indexid))
	                    describe = indexpart[endIndex:]
        
                    
	return enumerate(oldstname), oldstid

def GetScheduledTask(stIDs, url_link_final, tenant1key):
    allst = []
    namest = []
    print ('Getting Target Task...', flush=True)
    for part in stIDs:
        payload = {}
        url = url_link_final + 'api/scheduledtasks/' + str(part)
        headers = {
        "api-secret-key": tenant1key,
        "api-version": "v1",
        "Content-Type": "application/json",
        }
        response = requests.request("GET", url, headers=headers, data=payload, verify=cert)
        describe = str(response.text)
        allst.append(describe)
        index = describe.find('\"name\"')
        if index != -1:
            indexpart = describe[index+6:]
            startIndex = indexpart.find('\"')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find(',', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex-1]
                    namest.append(str(indexid))
                    describe = indexpart[endIndex:]
    print(allst, flush=True)
    print(namest, flush=True)
    return allst, namest

def CreateScheduledTask(allst, namest, url_link_final_2, tenant2key):
    print ('Creating Task to target Account...', flush=True)
    for count, dirlist in enumerate(namest):
        print(dirlist, flush=True)
        payload = "{\"searchCriteria\": [{\"fieldName\": \"name\",\"stringValue\": \"" + dirlist + "\"}]}"
        url = url_link_final_2 + 'api/scheduledtasks/search'
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
                        payload = allst[count]
                        url = url_link_final_2 + 'api/scheduledtasks/' + str(indexid)
                        headers = {
                        "api-secret-key": tenant2key,
                        "api-version": "v1",
                        "Content-Type": "application/json",
                        }
                        response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
        else:
            payload = allst[count]
            url = url_link_final_2 + 'api/scheduledtasks'
            headers = {
            "api-secret-key": tenant2key,
            "api-version": "v1",
            "Content-Type": "application/json",
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=cert)
            
        print(str(response.text), flush=True)
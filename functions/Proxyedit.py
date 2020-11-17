import sys
import os
import time
from time import sleep
import requests
import urllib3

def ProxyEdit(allofpolicy, t1iplistid, t2iplistid, t1portlistid, t2portlistid):
    for count, describe in enumerate(allofpolicy):
        index = describe.find('antiMalwareSettingSmartProtectionGlobalServerUseProxyEnabled')
        if index != -1:
            indexpart = describe[index:]
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex]
                    value = indexid.find("true")
                    if value != -1:
                        describe = describe[:index+startIndex+value+1] + "false" + describe[index+endIndex-1:]
        index = describe.find('webReputationSettingSmartProtectionGlobalServerUseProxyEnabled')
        if index != -1:
            indexpart = describe[index:]
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex]
                    value = indexid.find("true")
                    if value != -1:
                        describe = describe[:index+startIndex+value+1] + "false" + describe[index+endIndex-1:]
        index = describe.find('platformSettingSmartProtectionGlobalServerUseProxyEnabled')
        if index != -1:
            indexpart = describe[index:]
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex]
                    value = indexid.find("true")
                    if value != -1:
                        describe = describe[:index+startIndex+value+1] + "false" + describe[index+endIndex-1:]
        index = describe.find('platformSettingSmartProtectionAntiMalwareGlobalServerProxyId')
        if index != -1:
            indexpart = describe[index:]
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex]
                    value = indexid.find("value")
                    if value != -1:
                        valuepart = indexid[value+7:]
                        startvalue = valuepart.find('\"')
                        if startvalue != -1:
                            endvalue = valuepart.find('\"', startvalue+1)
                            if startvalue != -1 and endvalue != -1:
                                describe = describe[:index+startIndex+value+7+startvalue+2] + "" + describe[index+startIndex+value+7+startvalue+endvalue+1:]
        index = describe.find('webReputationSettingSmartProtectionWebReputationGlobalServerProxyId')
        if index != -1:
            indexpart = describe[index:]
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex]
                    value = indexid.find("value")
                    if value != -1:
                        valuepart = indexid[value+7:]
                        startvalue = valuepart.find('\"')
                        if startvalue != -1:
                            endvalue = valuepart.find('\"', startvalue+1)
                            if startvalue != -1 and endvalue != -1:
                                describe = describe[:index+startIndex+value+7+startvalue+2] + "" + describe[index+startIndex+value+7+startvalue+endvalue+1:]
        index = describe.find('platformSettingSmartProtectionGlobalServerProxyId')
        if index != -1:
            indexpart = describe[index:]
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex]
                    value = indexid.find("value")
                    if value != -1:
                        valuepart = indexid[value+7:]
                        startvalue = valuepart.find('\"')
                        if startvalue != -1:
                            endvalue = valuepart.find('\"', startvalue+1)
                            if startvalue != -1 and endvalue != -1:
                                describe = describe[:index+startIndex+value+7+startvalue+2] + "" + describe[index+startIndex+value+7+startvalue+endvalue+1:]
        index = describe.find('firewallSettingReconnaissanceExcludeIpListId')
        if index != -1:
            indexpart = describe[index:]
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex]
                    value = indexid.find("value")
                    if value != -1:
                        valuepart = indexid[value+7:]
                        startvalue = valuepart.find('\"')
                        if startvalue != -1:
                            endvalue = valuepart.find('\"', startvalue+1)
                            if startvalue != -1 and endvalue != -1:
                                indexid1 = valuepart[startvalue+1:endvalue]
                                if indexid1 != "" and indexid1 != 'NONE':
                                    indexid5 = describe[index:index+endIndex]
                                    indexnum = t1iplistid.index(indexid1)
                                    listpart = indexid5.replace(indexid1, t2iplistid[indexnum])
                                    describe = describe.replace(indexid5, listpart)
        index = describe.find('firewallSettingReconnaissanceIncludeIpListId')
        if index != -1:
            indexpart = describe[index:]
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex]
                    value = indexid.find("value")
                    if value != -1:
                        valuepart = indexid[value+7:]
                        startvalue = valuepart.find('\"')
                        if startvalue != -1:
                            endvalue = valuepart.find('\"', startvalue+1)
                            if startvalue != -1 and endvalue != -1:
                                indexid1 = valuepart[startvalue+1:endvalue]
                                if indexid1 != "" and indexid1 != 'NONE':
                                    indexid5 = describe[index:index+endIndex]
                                    indexnum = t1iplistid.index(indexid1)
                                    listpart = indexid5.replace(indexid1, t2iplistid[indexnum])
                                    describe = describe.replace(indexid5, listpart)
        index = describe.find('firewallSettingEventLogFileIgnoreSourceIpListId')
        if index != -1:
            indexpart = describe[index:]
            startIndex = indexpart.find('{')
            if startIndex != -1: #i.e. if the first quote was found
                endIndex = indexpart.find('}', startIndex + 1)
                if startIndex != -1 and endIndex != -1: #i.e. both quotes were found
                    indexid = indexpart[startIndex+1:endIndex]
                    value = indexid.find("value")
                    if value != -1:
                        valuepart = indexid[value+7:]
                        startvalue = valuepart.find('\"')
                        if startvalue != -1:
                            endvalue = valuepart.find('\"', startvalue+1)
                            if startvalue != -1 and endvalue != -1:
                                indexid1 = valuepart[startvalue+1:endvalue]
                                if indexid1 != "" and indexid1 != 'NONE':
                                    indexid5 = describe[index:index+endIndex]
                                    indexnum = t1iplistid.index(indexid1)
                                    listpart = indexid5.replace(indexid1, t2iplistid[indexnum])
                                    describe = describe.replace(indexid5, listpart)
        
        allofpolicy[count] = describe
    return allofpolicy
import sys
import os
import time
from time import sleep
import requests
import urllib3
import json

cert = False

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def CheckAPIAccess(url_specified, tenantkey):

	url = url_specified + "api/apikeys/current"
	result = None
	try:
		payload={}
		headers = {
		'api-secret-key': tenantkey,
		'api-version': 'v1',
		'Content-Type': 'application/json',
		}
		response = requests.request("GET", url, headers=headers, data=payload, verify=cert)
		print("For API Key: " + tenantkey, flush=True)
		print(response.text, flush=True)
		print("", flush=True)
		if "active" and "true" in response.text:
			result = True
		else:
			result = False
	except Exception as e:
		print("For API Key: " + tenantkey, flush=True)
		print(e, flush=True)
		print("", flush=True)
		result = False

	return result
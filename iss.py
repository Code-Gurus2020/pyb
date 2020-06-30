#!/usr/bin/phthon3
import json
import requests
'''issloc = {"message": "success", "timestamp": 1593527888, "iss_position": {"longitude": "28.8827", "latitude": "-48.9697"}}

print (issloc["message"])

print (issloc["timestamp"])

print (issloc["iss_position"]["longitude"])'''

def main():
    location = request.get("http://api.open-notify.org/iss-now.json")
    issData = information.json()




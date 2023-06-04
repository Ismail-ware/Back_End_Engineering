import requests
import json
import pandas.io.json as pd_json
import pandas as pd
from datetime import datetime

base_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1/"
API_KEY = "EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"
Site_ID = "norwich-pear-tree"

def main_request(method, endpoint, params=None, data=None):
    headers = {"x-api-key": API_KEY}
    url = base_url + endpoint

    response = requests.request(method, url, params=params, data=data, headers=headers)

    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed with status code {response.status_code}")

## Task i
outages = main_request("GET", "outages")
indented_outages = json.dumps(outages, indent=2) #indentation 
print(indented_outages)

## Task ii
site_info = main_request("GET", f"site-info/{Site_ID}")
indented_site_info = json.dumps(site_info, indent=2) #indentation 
print(indented_site_info)

#Test if it's a list of dict
def is_list_of_dicts(obj):
    return isinstance(obj, list) and all(isinstance(item, dict) for item in obj)
print(is_list_of_dicts(site_info))

## Task iii
devices = site_info["devices"] # List of dictionaries
print(devices)
filtered_outages = [outage for outage in outages
                    if (outage['begin'] < '2022-01-01T00:00:00.000Z') or (outage['id'] not in [device['id'] for device in devices])]

print(filtered_outages)

## Task iv
outages_after_2022_in_device = [outage for outage in outages
                    if (outage['begin'] >= '2022-01-01T00:00:00.000Z') and (outage['id'] in [device['id'] for device in devices])]

print(outages_after_2022_in_device)

remaining_outages = []
for outage in outages_after_2022_in_device:
    outage_id = outage['id']
    for device in devices:
        if device['id'] == outage_id:
            outage['device_name'] = device['name']
            break
    remaining_outages.append(outage)

print(remaining_outages)

## Task v
type(remaining_outages)
#modifying data schema to confirm to the post schema given

filtered_outages = []

for outage in remaining_outages:
    filtered_outage = {
        "id": outage['id'],
        "name": outage['device_name'],
        "begin": outage['begin'],
        "end": outage['end']
    }
    filtered_outages.append(filtered_outage)

print(filtered_outages)

# Convert filtered_outages to JSON
filtered_outages_json = json.dumps(filtered_outages)
print(filtered_outages_json)

main_request("POST", f"site-outages/{Site_ID}", data=filtered_outages_json)
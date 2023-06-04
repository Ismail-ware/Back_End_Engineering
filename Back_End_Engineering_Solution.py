#import relevant libraries
import requests
import json
import pandas.io.json as pd_json
import pandas as pd

# Set the base URL and API key
base_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1/"
API_KEY = "EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"
Site_ID = "norwich-pear-tree"

#create a helper function `main_request` for reusability
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

## Task I
outages = main_request("GET", "outages")
indented_outages = json.dumps(outages, indent=2) #indenting the output for better visualization
print(indented_outages)

## Task II
site_info = main_request("GET", f"site-info/{Site_ID}")
indented_site_info = json.dumps(site_info, indent=2) ##indenting the output for better visualization
print(indented_site_info)

## Task III
devices = site_info["devices"]  ##subsetting devices from `site_info`
print(devices)

#filtering outages with a start time less than `2022` or whose `id` is not in devices
filtered_outages = [outage for outage in outages
                    if (outage['begin'] < '2022-01-01T00:00:00.000Z') or (outage['id'] not in [device['id'] for device in devices])]

print(filtered_outages)

## Task IV
#filtering outages after 2022 whose `id` are in devices
outages_after_2022_in_devices = [outage for outage in outages
                    if (outage['begin'] >= '2022-01-01T00:00:00.000Z') and (outage['id'] in [device['id'] for device in devices])]

print(outages_after_2022_in_devices)

#appending `device_name` to `outages_after_2022_in_device`
remaining_outages = []
for outage in outages_after_2022_in_devices:
    outage_id = outage['id']
    for device in devices:
        if device['id'] == outage_id:
            outage['device_name'] = device['name']
            break
    remaining_outages.append(outage)

print(remaining_outages)

## Task V
#modifying data schema to conform to the payload requirement
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

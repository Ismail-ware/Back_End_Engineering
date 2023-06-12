import requests
import json
import logging

base_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1/"
API_KEY = "undisclosed"
Site_ID = "norwich-pear-tree"

def main_request(method, endpoint, params=None, data=None):
    headers = {"x-api-key": API_KEY}
    url = base_url + endpoint

    try:
        response = requests.request(method, url, params=params, data=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {str(e)}")
        raise

def get_outages():
    return main_request("GET", "outages")

def get_site_info(site_id):
    endpoint = f"site-info/{site_id}"
    return main_request("GET", endpoint)

def filter_outages(outages, devices):
    filtered_outages = []
    for outage in outages:
        if outage['begin'] < '2022-01-01T00:00:00.000Z' or outage['id'] not in [device['id'] for device in devices]:
            filtered_outages.append(outage)
    return filtered_outages

def get_outages_after_2022_in_device(outages, devices):
    outages_after_2022 = []
    for outage in outages:
        if outage['begin'] >= '2022-01-01T00:00:00.000Z' and outage['id'] in [device['id'] for device in devices]:
            outages_after_2022.append(outage)
    return outages_after_2022

def attach_device_names(outages, devices):
    for outage in outages:
        for device in devices:
            if device['id'] == outage['id']:
                outage['device_name'] = device['name']
                break
    return outages

def transform_outages(outages):
    transformed_outages = []
    for outage in outages:
        transformed_outage = {
            "id": outage['id'],
            "name": outage['device_name'],
            "begin": outage['begin'],
            "end": outage['end']
        }
        transformed_outages.append(transformed_outage)
    return transformed_outages

def post_outages(site_id, outages):
    endpoint = f"site-outages/{site_id}"
    data = json.dumps(outages)
    return main_request("POST", endpoint, data=data)

def run_task():
    outages = get_outages()
    site_info = get_site_info(Site_ID)
    devices = site_info.get("devices", [])

    filtered_outages = filter_outages(outages, devices)
    outages_after_2022 = get_outages_after_2022_in_device(outages, devices)
    remaining_outages = attach_device_names(outages_after_2022, devices)
    transformed_outages = transform_outages(remaining_outages)

    response = post_outages(Site_ID, transformed_outages)
    print(response)

if __name__ == '__main__':
    run_task()

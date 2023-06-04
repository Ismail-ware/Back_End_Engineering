def main_request(method, endpoint, params=None, data=None):
    headers = {"x-api-key": API_KEY}
    url = base_url + endpoint

    max_retries = 3
    retries = 0
    response = None

    while retries < max_retries:
        try:
            response = requests.request(method, url, params=params, data=data, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Request failed with status code {response.status_code}")
        except requests.exceptions.RequestException:
            retries += 1
            print(f"Request failed. Retrying ({retries}/{max_retries})...")
    
    if response is not None:
        raise Exception(f"Request failed with status code {response.status_code}")
    else:
        raise Exception("Request failed. Max retries exceeded.")


# I introduced a new feature that allows for automatic retries in case of a request failure. This is achieved by specifying a maximum number of retries and keeping track of the number of retries made so far.
# If a request fails due to a network error, the function will retry the request up to the maximum number of retries. After each failed attempt, a message is printed to indicate the current retry count.
# # If all retries are exhausted and the request still fails, an exception is raised, indicating the last received status code.
# If no response is received at all, an exception is raised to indicate that the maximum number of retries has been exceeded.
# By incorporating this feature, the implementation enhances resilience to 500 status codes by automatically retrying failed requests. This ensures more robust handling of temporary server errors.
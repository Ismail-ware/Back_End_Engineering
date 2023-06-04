# Back_End_Engineering

# Repository Name
Back_End_Engineering

## Description
This repository contains code for fetching outage information from the KrakenFlex API and performing various tasks on the data.

## Installation
To use the code in this repository, you need to have the following dependencies installed:
- requests
- pandas
- json

You can install these dependencies using pip:

```
pip install requests pandas
```

## Usage
1. Clone the repository to your local machine.
2. Open the terminal and navigate to the repository's directory.
3. Run the following command to execute the code:

```
python Back_End_Engineering_Solution.py
```
## Code Explanation
The code in `Back_End_Engineering_Solution.py` performs the following tasks:

1. Fetches outage information from the KrakenFlex API and prints the response content.
2. Fetches site information for a specific site ID and prints the response content.
3. Tests if the site\outage information is a list of dictionaries.
4. Filters outages based on specific conditions and prints the filtered outages.
5. Filters outages that occurred after 2022 and are associated with devices from the site information.
6. Attaches device names to the remaining outages and prints the updated outages.
7. Modifies the data schema of the remaining outages to conform to a specific post schema.
8. Converts the filtered outages to JSON format and prints the JSON data.
9. Makes a POST request to the KrakenFlex API to send the filtered outages.

Please make sure to replace the API key and site ID variables (`API_KEY` and `Site_ID`) with your own values before running the code.

**#Unit test--500_status_code**

## Functionality
The `main_request` function defined in the script handles making HTTP requests to a specified API endpoint. It takes the following parameters:

- `method`: The HTTP method (e.g., "GET", "POST") for the request.
- `endpoint`: The API endpoint to send the request to.
- `params` (optional): Query parameters for the request.
- `data` (optional): Request data.

The function also implements retries in case of network errors. It allows a maximum number of retries (default: 3) and prints a retry message for each failed attempt. If all retries are exhausted and the request still fails, an exception is raised with the last received status code. If no response was received at all, an exception indicating that the max retries were exceeded is raised.

## Requirements

To run the script, you need to have the following installed:

- Python 3.x
- Requests library (`pip install requests`)

## Usage

To execute the script, follow these steps:

1. Clone the repository or download the `500_status_code.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `500_status_code.py` file is located.
4. Run the following command to execute the script:

   ```shell
   python 500_status_code.py
   ```
## Contributions
Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.


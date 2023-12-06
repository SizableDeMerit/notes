#splunk.md
import requests
import json

# Your JSON data from the Python script
data_to_send = {
    "key1": "value1",
    "key2": "value2"
    # Add your generated JSON data here
}

# Splunk HEC URL and token
splunk_hec_url = "https://your_splunk_server:8088/services/collector"
splunk_token = "your_splunk_token"

# Prepare headers and data for HEC
headers = {
    "Authorization": f"Splunk {splunk_token}",
    "Content-Type": "application/json"
}

# Send data to Splunk's HEC
response = requests.post(splunk_hec_url, headers=headers, data=json.dumps(data_to_send))

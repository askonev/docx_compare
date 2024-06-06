import requests
import json

# URL to send the POST request to
serve = "161.35.214.46"
url = f"http://{serve}/docbuilder"

# Data to send in the POST request
data = {
    "async": False,
    "url": f"http://{serve}:9090/db_scripts/CDE/test_jpeg_compare.js",
    "argument": {"key": "string"}
}

print(data)

# Sending the POST request with JSON data
response = requests.post(url, json=data)

res_json = json.loads(response.text)

# Path where you want to save the downloaded file
local_filename = 'Result.docx'

# Send a GET request to the URL
response = requests.get(res_json['urls'][local_filename], stream=True)

# Open the local file in write-binary mode and write the contents of the response to it
with open(local_filename, 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)

print(f"File downloaded as {local_filename}")

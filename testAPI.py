import requests
import json

url = "https://06fhdauxeb.execute-api.us-east-1.amazonaws.com/default/logging-to-sqs-lambdaxx"
data =  {
"datetime": "01-01-2023",
"master_customer_id": "master_customer_id",
"app_name": "Bulk export",
"process_name": "process_name",
"version": "1",
"pid": "request_id",
"level": "level",
"details": "details",
"error": "error",
"time_elapsed": "time_elapsed",
"spu_id": "",
"practice_id": "wd"
}

data = json.dumps(data)
headers = {"Content-Type": "application/json"}
response = requests.request("POST",url, data=data, headers=headers)
print(f"response.status_code: {response.status_code}")

if response.status_code == 200:
    print("Success")
else:
    print("Failed")

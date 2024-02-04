import requests
import json
from configuration import whereby_api_key
import streamlit as st


API_KEY = whereby_api_key

data = {
    "endDate": "2099-02-18T14:23:00.000Z",
    "fields": ["hostRoomUrl"],
    "isLocked": True
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = requests.post(
    "https://api.whereby.dev/v1/meetings",
    headers=headers,
    json=data
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("Room URL:", data["roomUrl"])
print("Host room URL:", data["hostRoomUrl"])

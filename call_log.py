import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")

# Replace with the specific contact ID you want to query
CONTACT_ID = 'MBKnjdToxNZ5Tg4XAx9n'

# GHL Base API URL
BASE_URL = 'https://rest.gohighlevel.com/v1'

# Set up request headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# API endpoint to fetch contact activities
url = f'{BASE_URL}/contacts/{CONTACT_ID}'

# Send GET request
response = requests.get(url, headers=headers)

print(f"Fetching activities for contact ID: {response.text}")


# Handle response
if response.ok:
    activities = response.json().get('activities', [])
    call_logs = [a for a in activities if a.get('type') == 'call']

    if call_logs:
        print(f"📞 Found {len(call_logs)} call logs for contact {CONTACT_ID}:")
        for call in call_logs:
            print(f" - Timestamp: {call.get('timestamp')} | Duration: {call.get('duration')} sec")
    else:
        print(f"❌ No call logs found for contact {CONTACT_ID}.")
else:
    print("🚨 Error:", response.status_code, response.text)

import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")

# Replace with the specific contact ID you want to query
CONTACT_ID = 'zjxCl4wsyIsdsuOmZloc'

# GHL Base API URL
BASE_URL = 'https://rest.gohighlevel.com/v1'

# Set up request headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# API endpoint to fetch contact activities
url = f'{BASE_URL}/contacts/{CONTACT_ID}/notes'

# Send GET request
response = requests.get(url, headers=headers)

# print(f"Fetching notes for contact ID: {response.text}")


# Handle response
if response.ok:
    notes = response.json().get('notes', [])

    # print(notes)

    call_logs = [a for a in notes if a.get('type') == 'call']

    if notes:
        print(f"📞 Found {len(notes)} notes for contact {CONTACT_ID}:")
        for note in notes:
            print(f" - ID: {note.get('id')} | Created  : {note.get('createdAt')} | Body: {note.get('body')}")
    else:
        print(f"❌ No notes found for contact {CONTACT_ID}.")
else:
    print("🚨 Error:", response.status_code, response.text)

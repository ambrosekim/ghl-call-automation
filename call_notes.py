import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = 'https://rest.gohighlevel.com/v1'

# Post transcript to GHL
def post_to_ghl(contact_id, transcript):
    url = f"{BASE_URL}/contacts/{contact_id}/notes"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "body": f"Transcript:\n{transcript}",
        "title": "3CX Call Transcript",
        "type": "NOTE"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


contact_id = 'zjxCl4wsyIsdsuOmZloc'  # Replace with the specific contact ID you want to query
transcript = "This is a sample transcript of the call."  # Replace with the actual transcript
response = post_to_ghl(contact_id, transcript)

print(f"Response from GHL: {response}")
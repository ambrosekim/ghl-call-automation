import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

BASE_URL = 'https://rest.gohighlevel.com/v1'


def fetch_contacts(limit=100):
    """Fetch all contacts using pagination."""
    contacts = []
    next_page_token = ''
    
    while True:
        params = {'limit': limit}
        if next_page_token:
            params['startAfterId'] = next_page_token

        print(f"Fetching contacts with params: {params}")
        
        response = requests.get(f'{BASE_URL}/contacts/', headers=HEADERS, params=params)
        print(response.text)
        if not response.ok:
            print("Error fetching contacts:", response.status_code, response.text)
            break
        
        data = response.json()
        print(f"Response data: {data}")
        batch = data.get('contacts', [])
        contacts.extend(batch)

        print(f"Fetched {len(batch)} contacts... Total so far: {len(contacts)}")

        # print(f"Next page token: {data.get('meta', 'None').get('startAfterId', 'None')}")

        # print(f"Next page URL: {data['meta']['startAfterId']}")

        # Check if there's a next page
        print(f"Next page URL: {data.get('nextPageUrl', 'None')}")
        print(f"Next page token: {data.get('meta', 'None').get('startAfterId', 'None')}")


        if 'nextPageUrl' in data and data['meta']['startAfterId']:
            next_page_token = data.get('meta', 'None').get('startAfterId', 'None')
            time.sleep(0.5)  # avoid hitting rate limits
        else:
            break

    return contacts


def fetch_call_logs(contact_id):
    """Fetch call logs from contact activity feed."""
    url = f'{BASE_URL}/contacts/{contact_id}/activities'
    response = requests.get(url, headers=HEADERS)

    if not response.ok:
        print(f"Failed to get activities for contact {contact_id}")
        return []

    activities = response.json().get('activities', [])
    return [a for a in activities if a.get('type') == 'call']


def main():
    all_contacts = fetch_contacts()

    print(f"Total contacts fetched: {len(all_contacts)}")
    
    for contact in all_contacts:
        name = f"{contact.get('firstName', '')} {contact.get('lastName', '')}".strip()
        contact_id = contact.get('id')
        
        print(f"\n📇 Contact: {name or '[Unnamed]'}")
        call_logs = fetch_call_logs(contact_id)

        if not call_logs:
            print("  ❌ No call logs found.")
        else:
            for call in call_logs:
                print(call)
                exit(0)
                ts = call.get('timestamp', 'N/A')
                duration = call.get('duration', 'N/A')
                print(f"  📞 Call at: {ts} | Duration: {duration} sec")


if __name__ == '__main__':
    main()

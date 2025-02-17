import requests
import json

def fetch_all_items():
    url = "https://raw.communitydragon.org/pbe/cdragon/tft/en_us.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        items = data['items']
        with open('/Users/jerry/Desktop/TFT Battle Sim/items.json', 'w') as f:
            json.dump(items, f)
        return items
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def load_items():
    try:
        with open('/Users/jerry/Desktop/TFT Battle Sim/items.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return fetch_all_items()

all_items = load_items()
print(all_items)
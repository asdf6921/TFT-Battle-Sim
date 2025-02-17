import requests
import json

def fetch_all_champions():
    url = "https://raw.communitydragon.org/pbe/cdragon/tft/en_us.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        champions = data['sets']['13']['champions']
        with open('/Users/jerry/Desktop/TFT Battle Sim/champions.json', 'w') as f:
            json.dump(champions, f)
        return champions
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def load_champions():
    try:
        with open('/Users/jerry/Desktop/TFT Battle Sim/champions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return fetch_all_champions()

all_champions = load_champions()

def get_champion(api_name):
    if all_champions:
        for champion in all_champions:
            if champion['apiName'] == api_name:
                return champion
    return None

champion = get_champion("TFT13_Rell")
if champion:
    print(champion)
else:
    print("Champion not found.")
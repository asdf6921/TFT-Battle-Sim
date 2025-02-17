import json

def get_champion_names(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        champion_names = [champion['name'] for champion in data]
    return champion_names

def get_item_names(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        item_names = [item['name'] for item in data]
    return item_names
champ_file_path = '/Users/jerry/Desktop/TFT Battle Sim/second_filtered_champions.json'
item_file_path = '/Users/jerry/Desktop/TFT Battle Sim/final_items.json'
names = get_champion_names(champ_file_path)
items = get_item_names(item_file_path)
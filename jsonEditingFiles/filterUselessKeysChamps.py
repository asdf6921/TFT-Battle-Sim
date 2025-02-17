import json

# Load the JSON data from the file
with open('/Users/jerry/Desktop/TFT Battle Sim/filtered_champions.json', 'r') as file:
    data = json.load(file)

# Define the keys to be removed
keys_to_remove = ['apiName', 'characterName', 'icon', 'role', 'squareIcon', 'tileIcon']

# Iterate over each champion and remove the specified keys
for champion in data:
    for key in keys_to_remove:
        if key in champion:
            del champion[key]
    if 'ability' in champion and 'icon' in champion['ability']:
        del champion['ability']['icon']

# Save the filtered data back to the file
with open('/Users/jerry/Desktop/TFT Battle Sim/second_filtered_champions.json', 'w') as file:
    json.dump(data, file, indent=4)
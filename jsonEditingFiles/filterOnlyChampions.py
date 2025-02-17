import json

# Load the JSON data from the file
with open('/Users/jerry/Desktop/TFT Battle Sim/champions.json', 'r') as file:
    data = json.load(file)

# Filter the data
filtered_data = [item for item in data if item.get('apiName', '').startswith('TFT13')]

# Save the filtered data back to a new JSON file
with open('/Users/jerry/Desktop/TFT Battle Sim/filtered_champions.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)
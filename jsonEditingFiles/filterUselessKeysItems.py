import json

# Load the JSON data from the file
with open('/Users/jerry/Desktop/TFT Battle Sim/filtered_items.json', 'r') as file:
    data = json.load(file)

# Define the keys to be removed
keys_to_remove = ['apiName', 'associatedTraits', 'composition', 'desc', 'from', 'icon', 'id', 'incompatibleTraits']

# Iterate over each champion and remove the specified keys
for item in data:
    for key in keys_to_remove:
        if key in item:
            del item[key]

# Save the filtered data back to the file
with open('/Users/jerry/Desktop/TFT Battle Sim/final_items.json', 'w') as file:
    json.dump(data, file, indent=4)
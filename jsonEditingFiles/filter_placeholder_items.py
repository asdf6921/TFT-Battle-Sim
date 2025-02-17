import json

# Path to the JSON file
file_path = '/Users/jerry/Desktop/TFT Battle Sim/second_filtered_champions.json'

# Load the JSON data
with open(file_path, 'r') as file:
    data = json.load(file)

# Filter out entries where cost > 7
filtered_data = [entry for entry in data if entry.get('cost', 0) <= 7]

# Save the filtered data back to the JSON file
with open(file_path, 'w') as file:
    json.dump(filtered_data, file, indent=4)

print("Filtered data saved successfully.")
import json

# Load the JSON data from the file
with open('/Users/jerry/Desktop/TFT Battle Sim/items.json', 'r') as file:
    data = json.load(file)
tft_set13_items = ["AdaptiveHelm", "ArchangelsStaff", "Bloodthirster", "BlueBuff", "BrambleVest", "Crownguard", "Deathblade", "DragonsClaw", "GuardianAngel", "SpectralGauntlet", "GargoyleStoneplate",
                   "MadredsBloodrazor", "PowerGauntlet", "GuinsoosRageblade", "UnstableConcoction", "HextechGunblade", "InfinityEdge", "IonicSpark", "JeweledGauntlet", "LastWhisper",
                   "Morellonomicon", "Leviathan", "FrozenHeart", "Quicksilver", "RabadonsDeathcap", "RapidFirecannon", "Redemption", "RunaansHurricane", "SpearOfShojin", "StatikkShiv", 
                   "NightHarvester", "SteraksGage", "RedBuff", "TitansResolve", "WarmogsArmor"
]
tft_set13_items = ["TFT_Item_" + item for item in tft_set13_items]
print(len(tft_set13_items))
# Filter the data
filtered_data = [item for item in data if item.get('apiName', '') in tft_set13_items]

# Save the filtered data back to a new JSON file
with open('/Users/jerry/Desktop/TFT Battle Sim/filtered_items.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)
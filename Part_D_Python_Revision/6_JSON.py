# json.dump() -> Saves Python data into a JSON file

# json.load() -> Reads data from a JSON file and converts it back into Python data.

import json

clients = [
    {"name": "Ali", "country": "Pakistan", "monthly_fee": 1200},
    {"name": "Sara", "country": "USA", "monthly_fee": 1500},
    {"name": "John", "country": "UK", "monthly_fee": 800},
    {"name": "Ayesha", "country": "Pakistan", "monthly_fee": 2000},
    {"name": "David", "country": "Canada", "monthly_fee": 900}
]

# Save data into JSON file
with open("clients.json", "w") as file:
    json.dump(clients, file, indent=4)

print("Clients saved successfully!")

# Read data from JSON file
with open("clients.json", "r") as file:
    loaded_clients = json.load(file)

print("Clients loaded from JSON:")
print(loaded_clients)

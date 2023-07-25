import json

# Read the data from "data.txt"
with open("data.txt", "r") as file_read:
    lines = file_read.readlines()

# Process the data and create the dictionary
country_data = {}
for i in range(0, len(lines), 3):
    country_code = lines[i + 1].strip().lower()  # Convert the country code to lowercase
    country_name = lines[i].strip()
    country_data[country_code] = country_name

# Write the dictionary to a JSON file
with open("country-codes.json", "w") as json_file:
    json.dump(country_data, json_file, indent=4)

print("Data written to country-codes.json.")

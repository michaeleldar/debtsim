import json

# Open the input file for reading
with open("pop2.txt", "r") as file_read:
    lines = file_read.readlines()

# Initialize dictionaries to store the extracted data
country_codes_data = {}
country_data = {}

# Loop through the lines and extract the data
for i in range(0, len(lines), 11):  # Assuming each entry is 11 lines long
    country_name = lines[i + 1].strip()
    country_code = lines[i + 2].strip()
    population = lines[i + 5].strip()

    # Exclude countries with a population of 0, Netherlands Antilles, and Ceuta and Melilla
    if population != "0" and country_name not in {
        "Netherlands Antilles",
        "Ceuta and Melilla",
    }:
        country_codes_data[country_code.lower()] = country_name
        country_data[country_name] = {
            "code": country_code,
            "population": int(
                population.replace(",", "")
            ),  # Convert population to integer
        }

# Write the data to a JSON file named "country-codes.json"
with open("country-codes.json", "w") as json_file1:
    json.dump(country_codes_data, json_file1, indent=4)

# Write the data to a JSON file named "country_data.json"
with open("country_data.json", "w") as json_file2:
    json.dump(country_data, json_file2, indent=4)

print("Conversion to 'country-codes.json' and 'country_data.json' complete.")

print("Conversion to 'country_data.json' complete.")

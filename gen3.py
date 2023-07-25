# Open the input file for reading
with open("pop2.txt", "r") as file_read:
    lines = file_read.readlines()

# Initialize lists to store the extracted data
country_names = []
country_codes = []
populations = []

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
        country_names.append(country_name)
        country_codes.append(country_code)
        populations.append(population)

# Write the extracted data to a new file named "data.txt"
with open("data.txt", "w") as file2:
    for name, code, population in zip(country_names, country_codes, populations):
        file2.write(f"{name}\n{code}\n{population}\n")

print("Extraction and writing to 'data.txt' complete.")

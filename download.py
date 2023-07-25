import json
import requests

file = open("country-codes.json", "r")

data = json.load(file)

for country in data:
    response = requests.get(f"https://flagcdn.com/w160/{country}.png")
    open(f"flags/{data[country]}.png", "wb").write(response.content)

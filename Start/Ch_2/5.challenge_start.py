# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data
# Show all events by their type and count

import json
from collections import Counter 

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

quakes = list(map(lambda q:q["properties"]["type"], data["features"]))

for type,count in Counter(quakes).items():
    print(f'{type}:{count}')
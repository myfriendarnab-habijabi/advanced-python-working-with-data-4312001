# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a JSON file

from json import (
    load, 
    dump,
    dumps)
from datetime import date


# read in the contents of the JSON file
with open("../../30DayQuakes.json", "r") as datafile:
    data = load(datafile)

def isbigQuake(x):
    mag = x["properties"]["mag"]
    quake = x["properties"]["type"]
    return mag is not None and mag > 5 and quake == "earthquake"

# TODO: define a function to transform complex JSON to simpler JSON
def prettyQuake(quake):
    return {
                "place":quake["properties"]["place"], 
                "magnitude": quake["properties"]["mag"], 
                "quake-date": str(date.fromtimestamp(int(quake["properties"]["time"]/1000))),
                "link": quake["properties"]["url"]
            }

# filter the data to only include large quakes
largequakes = list(filter(isbigQuake, data["features"]))

# TODO: transform the data to a JSON format we want to save
largePrettyQuakes = list(map(prettyQuake, largequakes))

# TODO: use the dumps() function to write json to a string
largequakesAsJsonStr = dumps(largePrettyQuakes, sort_keys=True, indent=4)
print(largequakesAsJsonStr)

# TODO: use the dump() function to write json to a file
with open('largequakes.json','w', encoding="utf-8") as jsonOutputFile:
    dump(largePrettyQuakes, jsonOutputFile, sort_keys=True, indent=4)
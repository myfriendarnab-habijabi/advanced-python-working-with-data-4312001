# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
from datetime import date

# read in the contents of the JSON file
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# method definitions
def isbigQuake(x):
    mag = x["properties"]["mag"]
    quake = x["properties"]["type"]
    return mag is not None and mag > 5 and quake == "earthquake"

def prettyQuake(quake):
    quakedate = date.fromtimestamp(
        int(quake["properties"]["time"]/1000))
    return [quake["properties"]["place"], quake["properties"]
                ["mag"], quakedate, quake["properties"]["url"]]

# Filter the data by quakes that are larger than 5 magnitude
largequakes = list(filter(isbigQuake, data["features"]))

# TODO: Create the header and row structures for the data
header = ["place", "magnitude", "date", "link"]

# TODO: populate the rows with the resulting quake data
rows = list(map(prettyQuake, largequakes))

# TODO: write the results to the CSV file
with open("largequakes.csv","w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)
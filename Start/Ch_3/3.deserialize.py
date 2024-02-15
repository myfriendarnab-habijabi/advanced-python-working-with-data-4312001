# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

from csv import (reader, Sniffer)
import pprint

def desrialize(row):
    return {
            "place": row[0],
            "magnitude": row[1],
            "date": row[2],
            "link": row[3]
        }

# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading
with open('largequakes.csv','r') as csvInputFile:
    rdr = reader(csvInputFile)
    sample = csvInputFile.read(10240)
    # set starting line at
    csvInputFile.seek(0)
    if Sniffer().has_header(sample):
        next(rdr)
    result = list(map(desrialize, list(rdr)))

pprint.pp(result)
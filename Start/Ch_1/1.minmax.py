# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value
print(f'minimum of values:{min(values)}')
print(f'minimum of strings:{min(strings)}')

# TODO: The max() function finds the maximum value
print(f'maximum of values:{max(values)}')
print(f'maximum of strings:{max(strings)}')

# TODO: define a custom "key" function to extract a data field
print(f'minimum of strings based on length:{min(strings,key=len)}')
print(f'maximum of strings based on length:{max(strings,key=len)}')

# TODO: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def getmag(data):
    magnitude = data["properties"]["mag"]
    if magnitude is None:
        magnitude=0
    return float(magnitude)

print(f'Getting below insights from {data["metadata"]["title"]}')
print(f'which has seismic data for {len(data["features"])}')
print(f'maximum magnitude is {max(data["features"], key=getmag)}')
print(f'minimum magnitude is {min(data["features"], key=getmag)}')

         
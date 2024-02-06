# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# for this challenge, we're going to summarize the earthquake data as follows:

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1: How many quakes are there in total?
print(f'total number of quakes: {len(data["features"])}')    

# 2: How many quakes were felt by at least 100 people?
def feltByAtleast100(q):
    return (q["properties"]["felt"] is not None and q["properties"]["felt"]>=100)

print(f'quakes were felt by at least 100 people: {len(list(filter(feltByAtleast100, data["features"])))}')

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def simplifyByNameAndFelt(q):
    return {
        "name": q["properties"]["place"],
        "felt": q["properties"]["felt"] or 0 # null coalescing or operator
    }

simplifiedFelt = list(map(simplifyByNameAndFelt, data["features"]))
maxFelt = max(simplifiedFelt, key=lambda x: x["felt"])
print(f'{maxFelt["name"]} whose quake was felt by the most people, with the # of reports: {maxFelt["felt"]}')

# 4: Print the top 10 most significant events, with the significance value of each
def simplifyByNameAndSig(q):
    return {
        "name": q["properties"]["place"],
        "sig": q["properties"]["sig"] or 0 # null coalescing or operator
    }

sortedsimplifyByNameAndSig = sorted(list(map(simplifyByNameAndSig, data["features"])), key=lambda x: x["sig"], reverse=True)

for i in range(0,10):
    print(f'{sortedsimplifyByNameAndSig[i]["name"]} felt quake of significance:{sortedsimplifyByNameAndSig[i]["sig"]} and rank {i+1}')
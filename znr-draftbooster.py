import requests

minPrice = 0.5

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Ac").json())

commons = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    commons.append([response[:response.find("'lang'") - 3], response[response.find("'usd'") + 8:response.find("'usd_foil'") - 3]])

    try:
        commons[-1][1] = float(commons[-1][1])
    except:
        commons[-1][1] = 0
    
    if commons[-1][1] < minPrice:
        commons[-1][1] = 0

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Au").json())

uncommons = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    uncommons.append([response[:response.find("'lang'") - 3], response[response.find("'usd'") + 8:response.find("'usd_foil'") - 3]])

    try:
        uncommons[-1][1] = float(uncommons[-1][1])
    except:
        uncommons[-1][1] = 0
    
    if uncommons[-1][1] < minPrice:
        uncommons[-1][1] = 0

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Ar").json())

rares = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    rares.append([response[:response.find("'lang'") - 3], response[response.find("'usd'") + 8:response.find("'usd_foil'") - 3]])

    try:
        rares[-1][1] = float(rares[-1][1])
    except:
        rares[-1][1] = 0
    
    if rares[-1][1] < minPrice:
        rares[-1][1] = 0

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Am").json())

mythics = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    mythics.append([response[:response.find("'lang'") - 3], response[response.find("'usd'") + 8:response.find("'usd_foil'") - 3]])

    try:
        mythics[-1][1] = float(mythics[-1][1])
    except:
        mythics[-1][1] = 0
    
    if mythics[-1][1] < minPrice:
        mythics[-1][1] = 0

for index in range(len(commons)):
    if commons[index][0].find("//") != -1:
        commons[index + 1] = "remove"
        commons[index + 2] = "remove"

commons = [item for item in commons if item != "remove"]

for index in range(len(uncommons)):
    if uncommons[index][0].find("//") != -1:
        uncommons[index + 1] = "remove"
        uncommons[index + 2] = "remove"

uncommons = [item for item in uncommons if item != "remove"]

for index in range(len(rares)):
    if rares[index][0].find("//") != -1:
        rares[index + 1] = "remove"
        rares[index + 2] = "remove"

rares = [item for item in rares if item != "remove"]

for index in range(len(mythics)):
    if mythics[index][0].find("//") != -1:
        mythics[index + 1] = "remove"
        mythics[index + 2] = "remove"

mythics = [item for item in mythics if item != "remove"]

costs = [0, 0, 0, 0]

for item in commons:
    costs[0] += item[1]
for item in uncommons:
    costs[1] += item[1]
for item in rares:
    costs[2] += item[1]
for item in mythics:
    costs[3] += item[1]

for index in range(4):
    costs[index] = round(costs[index], 2)

ev = 0

ev += 11 * (costs[0] / len(commons))
ev += 3 * (costs[1] / len(uncommons))
ev += (6.4 / 7.4) * (costs[2] / len(rares))
ev += (1 / 7.4) * (costs[3] / len(mythics))

ev = round(ev, 2)

print("EV of Draft Booster: " + str(ev))
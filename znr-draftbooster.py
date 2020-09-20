import requests

minPrice = 0.5

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Ac+-t%3A\"basic+land\"").json())

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

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Au+-t%3A\"basic+land\"").json())

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

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Ar+-t%3A\"basic+land\"").json())

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

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Am+-t%3A\"basic+land\"").json())

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

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+t%3A\"basic+land\"+unique%3Aprints").json())

basics = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    basics.append([response[:response.find("'lang'") - 3], response[response.find("'usd'") + 8:response.find("'usd_foil'") - 3]])

    try:
        basics[-1][1] = float(basics[-1][1])
    except:
        basics[-1][1] = 0
    
    if basics[-1][1] < minPrice:
        basics[-1][1] = 0

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Ac+-t%3A\"basic+land\"").json())

foilC = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    foilC.append([response[:response.find("'lang'") - 3], response[response.find("'usd_foil'") + 13:response.find("'eur'") - 3]])

    try:
        foilC[-1][1] = float(foilC[-1][1])
    except:
        foilC[-1][1] = 0
    
    if foilC[-1][1] < minPrice:
        foilC[-1][1] = 0

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Au+-t%3A\"basic+land\"").json())

foilU = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    foilU.append([response[:response.find("'lang'") - 3], response[response.find("'usd_foil'") + 13:response.find("'eur'") - 3]])

    try:
        foilU[-1][1] = float(foilU[-1][1])
    except:
        foilU[-1][1] = 0
    
    if foilU[-1][1] < minPrice:
        foilU[-1][1] = 0

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Ar+-t%3A\"basic+land\"").json())

foilR = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    foilR.append([response[:response.find("'lang'") - 3], response[response.find("'usd_foil'") + 13:response.find("'eur'") - 3]])

    try:
        foilR[-1][1] = float(foilR[-1][1])
    except:
        foilR[-1][1] = 0
    
    if foilR[-1][1] < minPrice:
        foilR[-1][1] = 0

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+r%3Am+-t%3A\"basic+land\"").json())

foilM = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    foilM.append([response[:response.find("'lang'") - 3], response[response.find("'usd_foil'") + 13:response.find("'eur'") - 3]])

    try:
        foilM[-1][1] = float(foilM[-1][1])
    except:
        foilM[-1][1] = 0
    
    if foilM[-1][1] < minPrice:
        foilM[-1][1] = 0

response = str(requests.get("https://api.scryfall.com/cards/search?q=s%3Aznr+is%3Abooster+t%3A\"basic+land\"+unique%3Aprints").json())

foilBasics = []

while response.find("'name'") != -1:
    response = response[response.find("'name'") + 9:]

    foilBasics.append([response[:response.find("'lang'") - 3], response[response.find("'usd_foil'") + 13:response.find("'eur'") - 3]])

    try:
        foilBasics[-1][1] = float(foilBasics[-1][1])
    except:
        foilBasics[-1][1] = 0
    
    if foilBasics[-1][1] < minPrice:
        foilBasics[-1][1] = 0

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

for index in range(len(foilC)):
    if foilC[index][0].find("//") != -1:
        foilC[index + 1] = "remove"
        foilC[index + 2] = "remove"

foilC = [item for item in foilC if item != "remove"]

for index in range(len(foilU)):
    if foilU[index][0].find("//") != -1:
        foilU[index + 1] = "remove"
        foilU[index + 2] = "remove"

foilU = [item for item in foilU if item != "remove"]

for index in range(len(foilR)):
    if foilR[index][0].find("//") != -1:
        foilR[index + 1] = "remove"
        foilR[index + 2] = "remove"

foilR = [item for item in foilR if item != "remove"]

for index in range(len(foilM)):
    if foilM[index][0].find("//") != -1:
        foilM[index + 1] = "remove"
        foilM[index + 2] = "remove"

foilM = [item for item in foilM if item != "remove"]

costs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for item in commons:
    costs[0] += item[1]
for item in uncommons:
    costs[1] += item[1]
for item in rares:
    costs[2] += item[1]
for item in mythics:
    costs[3] += item[1]
for item in basics:
    costs[4] += item[1]
for item in foilC:
    costs[5] += item[1]
for item in foilU:
    costs[6] += item[1]
for item in foilR:
    costs[7] += item[1]
for item in foilM:
    costs[8] += item[1]
for item in foilBasics:
    costs[9] += item[1]

for index in range(10):
    costs[index] = round(costs[index], 2)

ev = 0

ev += (484 / 45) * (costs[0] / len(commons))
ev += 3 * (costs[1] / len(uncommons))
ev += (6.4 / 7.4) * (costs[2] / len(rares))
ev += (1 / 7.4) * (costs[3] / len(mythics))
ev += costs[4] / len(basics)
ev += (121 / 720) * (costs[5] / len(foilC))
ev += (33 / 720) * (costs[5] / len(foilU))
ev += (11 / 720) * (6.4 / 7.4) * (costs[5] / len(foilR))
ev += (11 / 720) * (1 / 7.4) * (costs[5] / len(foilM))
ev += (11 / 720) * (costs[5] / len(foilBasics))

ev = round(ev, 2)

print("EV of Draft Booster: " + str(ev))
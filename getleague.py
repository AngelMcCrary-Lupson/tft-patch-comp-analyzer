from config import api_key
import json
import requests

print(api_key)
region = "na1"
country = "americas"
URL = f"https://{region}.api.riotgames.com/tft/league/v1/grandmaster?api_key={api_key}"

r = requests.get(URL)

data = r.json()

print(data["tier"])
# print(data["entries"])
summoners = {}
entries = data["entries"]

for entry in entries:

    name = entry["summonerName"]
    lp = entry["leaguePoints"]
    if lp > 800:
        summoners[name] = lp
        # print(name)

summonersPUUID = {}

for summoner in summoners:
    # print(summoner)
    puuidURL = f"https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summoner}?api_key={api_key}"
    re = requests.get(puuidURL)
    data2 = re.json()
    # print(data2["puuid"])
    summonersPUUID[summoner] = data2["puuid"]

# print(summonersPUUID)


# matchURL = f"https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuID}/ids?count=10&api_key{api_key}"
matchSet = {}
# print(type(matchSet))
matchSet = set()
# print(type(matchSet))

for summoner in summonersPUUID:
    puuid = summonersPUUID.get(summoner)
    # print(puuid)
    matchURL = f"https://{country}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?count=5&api_key={api_key}"
    ree = requests.get(matchURL)
    data3 = ree.json()
    # print(data3)
    matches = data3
    for id in matches:
        matchSet.add(id)
print(matchSet)

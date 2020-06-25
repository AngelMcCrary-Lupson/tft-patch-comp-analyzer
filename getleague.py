from config import api_key
import json
import requests
import declarecomp
import time

# print(api_key)
region = "na1"
country = "americas"
league = "challenger"
URL = f"https://{region}.api.riotgames.com/tft/league/v1/{league}?api_key={api_key}"
counts = 4
lp_param = 502
r = requests.get(URL)

data = r.json()

# print(data)
# print(data["entries"])
summoners = {}
entries = data["entries"]

for entry in entries:

    name = entry["summonerName"]
    lp = entry["leaguePoints"]
    if lp > lp_param:
        summoners[name] = lp
        # print(name)

summonersPUUID = {}

for summoner in summoners:
    # print(summoner)
    time.sleep(1)
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
    time.sleep(1)
    puuid = summonersPUUID.get(summoner)
    # print(puuid)
    matchURL = f"https://{country}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?count={counts}&api_key={api_key}"
    ree = requests.get(matchURL)
    data3 = ree.json()
    # print(data3)
    matches = data3
    for id in matches:
        matchSet.add(id)
# print(matchSet)

comp_counts_ranks = {
         "1" : {"Space Shrooms": 0,
            "4 Vanguards 4 Mystics": 0,
            "6 Cybers": 0,
            "Jinx Brawlers": 0,
            "6 Sorcs": 0,
            "6 BM Slowroll": 0,
            "6 Rebels": 0,
            "Mech Sorcs": 0,
            "Protectors": 0,
            "Comp Not Found": 0},
        "2" : {"Space Shrooms": 0,
            "4 Vanguards 4 Mystics": 0,
            "6 Cybers": 0,
            "Jinx Brawlers": 0,
            "6 Sorcs": 0,
            "6 BM Slowroll": 0,
            "6 Rebels": 0,
            "Mech Sorcs": 0,
            "Protectors": 0,
            "Comp Not Found": 0},
        "3" : {"Space Shrooms": 0,
            "4 Vanguards 4 Mystics": 0,
            "6 Cybers": 0,
            "Jinx Brawlers": 0,
            "6 Sorcs": 0,
            "6 BM Slowroll": 0,
            "6 Rebels": 0,
            "Mech Sorcs": 0,
            "Protectors": 0,
            "Comp Not Found": 0},
        "4" : {"Space Shrooms": 0,
            "4 Vanguards 4 Mystics": 0,
            "6 Cybers": 0,
            "Jinx Brawlers": 0,
            "6 Sorcs": 0,
            "6 BM Slowroll": 0,
            "6 Rebels": 0,
            "Mech Sorcs": 0,
            "Protectors": 0,
            "Comp Not Found": 0},
        None: 0
        }

for matchID in matchSet:
    time.sleep(1)
    matchInfoURL = f"https://{country}.api.riotgames.com/tft/match/v1/matches/{matchID}?api_key={api_key}"
    reee = requests.get(matchInfoURL)
    data4 = reee.json()
    # print(data4)
    # print(data4.keys())
    if "status" in data4.keys() and (data4["status"]["status_code"] == 404 or 429):
        break
    else:
        # print(data4)
        participants = data4["info"]["participants"]
        for participant in participants:
            # print(participant)

            comp = declarecomp.declare_comp(participant)


            if comp is None:
                prev_count = comp_counts_ranks[None]
                comp_counts_ranks[None] = prev_count + 1
            # elif "Comp Not Found" in comp:
            #     comp_not_found = comp[17:]
            #     print(comp_not_found)
            else:
                comp_composition = comp[2:]
                comp_rank = comp[:1]
                # print(comp_rank)
                # print(comp_composition)
                prev_count = comp_counts_ranks[comp_rank][comp_composition]
                comp_counts_ranks[comp_rank][comp_composition] = prev_count + 1
            # print(comp)

print(comp_counts_ranks)

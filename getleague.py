# from config import api_key     For debugging
import json
import requests
import declarecomp
import time
from datetime import datetime

def getleague(values):
    # run_now = datetime.now()   Debugging
    # dt_string = run_now.strftime("%d/%m/%Y %H:%M:%S")
    # print(f"Start: {dt_string}")

    api_key = values['-API-'].strip()
    filename = values['-FILESAVE-']
    region = values['-REGION-']
    league = values['-LEAGUE-'].lower()
    counts = int(values['-MATCHES-'])
    lp_param = int(values['-LPMIN-'])
    sleep_time = 1
    country = ""
    americas = {"BR1", "LA1", "LA2", "NA1", "OC1"}
    asia = {"JP1", "KR"}
    europe = {"EUN1", "EUW1", "RU", "TR1"}
    if region in americas:
        country = "americas"
    elif region in asia:
        country = "asia"
    elif region in europe:
        country = "europe"
    region = region.lower()

    URL = f"https://{region}.api.riotgames.com/tft/league/v1/{league}?api_key={api_key}"
    r = requests.get(URL)
    data = r.json()

    summoners = {}
    entries = data["entries"]

    for entry in entries:
        name = entry["summonerName"]
        lp = entry["leaguePoints"]
        if lp > lp_param:
            summoners[name] = lp

    summonersPUUID = {}

    for summoner in summoners:
        time.sleep(sleep_time)
        puuidURL = f"https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summoner}?api_key={api_key}"
        re = requests.get(puuidURL)
        data2 = re.json()
        summonersPUUID[summoner] = data2["puuid"]

    matchSet = {}
    matchSet = set()

    for summoner in summonersPUUID:
        time.sleep(sleep_time)
        puuid = summonersPUUID.get(summoner)
        matchURL = f"https://{country}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?count={counts}&api_key={api_key}"
        ree = requests.get(matchURL)
        data3 = ree.json()
        matches = data3
        for id in matches:
            matchSet.add(id)

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
        time.sleep(sleep_time)
        matchInfoURL = f"https://{country}.api.riotgames.com/tft/match/v1/matches/{matchID}?api_key={api_key}"
        reee = requests.get(matchInfoURL)
        data4 = reee.json()

        if "status" in data4.keys() and (data4["status"]["status_code"] == 404 or 429):
            break
        else:
            participants = data4["info"]["participants"]
            for participant in participants:
                comp = declarecomp.declare_comp(participant)
                if comp is None:
                    prev_count = comp_counts_ranks[None]
                    comp_counts_ranks[None] = prev_count + 1
                else:
                    comp_composition = comp[2:]
                    comp_rank = comp[:1]
                    prev_count = comp_counts_ranks[comp_rank][comp_composition]
                    comp_counts_ranks[comp_rank][comp_composition] = prev_count + 1

    with open(filename, 'w') as outfile:
        json.dump(comp_counts_ranks, outfile)

    # run_finished = datetime.now()     Debugging
    # dt_string_done = run_finished.strftime("%d/%m/%Y %H:%M:%S")
    # print(f"Finished: {dt_string_done}")

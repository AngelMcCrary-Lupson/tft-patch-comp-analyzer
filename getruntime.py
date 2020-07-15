import requests
import json
import math


def construct(values):
    region = values['-REGION-'].lower()
    league = values['-LEAGUE-'].lower()
    api_key = values['-API-']

    URL = f"https://{region}.api.riotgames.com/tft/league/v1/{league}?api_key={api_key}"
    r = requests.get(URL)
    data = r.json()

    if "status" in data.keys():
        print(data)
        return data["status"]
    else:
        lp_param = int(values['-LPMIN-'])
        matches = int(values['-MATCHES-'])
        summoners = {}
        entries = data["entries"]
        for entry in entries:
            name = entry["summonerName"]
            lp = entry["leaguePoints"]
            if lp > lp_param:
                summoners[name] = lp

        runtime = (len(summoners) * 2)
        runtime = runtime + (runtime * matches)
        # approx. runtime in seconds
        print(runtime)
        runtime_dict = {"runtime": int(runtime * 1.25)}
        return runtime_dict

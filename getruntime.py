import requests
import json


def construct(values):
    region = values[1].lower()
    league = values[0].lower()
    api_key = values[4]
    print(f"{region}, {league}, {api_key}")
    URL = f"https://{region}.api.riotgames.com/tft/league/v1/{league}?api_key={api_key}"
    # print(URL)
    r = requests.get(URL)
    data = r.json()
    # print(data)
    if "status" in data.keys():
        print(data)
        return data["status"]
    else:
        lp_param = int(values[2])
        matches = int(values[3])
        summoners = {}
        entries = data["entries"]

        for entry in entries:

            name = entry["summonerName"]
            lp = entry["leaguePoints"]
            if lp > lp_param:
                summoners[name] = lp

        print(len(summoners))

        runtime = (len(summoners) * 2 * matches)
        # approx. runtime in seconds
        print(runtime)
        return runtime

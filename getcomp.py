import json

def get_comp(data):
    # with open("dummydata9.json") as f:
    #     data = json.load(f)
    comp_data = data

    # def parseJSON(data):
    #     comp_data = data
    #
    # parseJSON(data)
    # print(comp_data)
    if comp_data["placement"] < 5:
        # print(data)
        player_comp = {}
        player_comp["placement"] = comp_data["placement"]
        player_comp["traits"] = []
        player_comp["units"] = []
        traits = comp_data["traits"]
        units = comp_data["units"]
        for trait in traits:
            player_trait = {}
            player_trait["name"] = trait["name"]
            player_trait['tier'] = trait["tier_current"]
            player_comp["traits"].append(player_trait)

        for unit in units:
            unit_id = unit["character_id"]
            player_comp["units"].append(unit_id)

        # return(player_comp)
        return(player_comp)
    return None

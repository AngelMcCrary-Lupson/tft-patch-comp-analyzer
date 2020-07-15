import json

def get_comp(data):
    # with open("file.json") as f:  For debugging to manually read a file
    #     data = json.load(f)
    comp_data = data

    if comp_data["placement"] < 5:
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

        return(player_comp)
    return None

import json
import getcomp

def declare_comp(data):
    player_data = data
    player_comp = getcomp.get_comp(data)
    if not player_comp is None:
        # print(player_comp)
        comp = return_comp(player_comp)
        return comp
    else:
        return None
# print(player_comp)

def is_space_shrooms(player_comp):
    # Vanguard Tier = 1, Teemo Exists
    is_space_shroom = False
    for trait in player_comp["traits"]:
        if "Vanguard" in trait["name"] and trait["tier"] == 1:
            is_space_shroom = True
            break

    if is_space_shrooms and "TFT3_Teemo" in player_comp["units"]:
        return True
        # return("Comp: Space Shrooms")
    return False
# Vanguard Tier = 2, Mystic Tier = 2

def is_four_vanguards_mystics(player_comp):
    is_four_vanguards = False
    is_four_mystics = False
    for trait in player_comp["traits"]:
        if "Vanguard" in trait["name"] and trait["tier"] == 2:
            is_four_vanguards = True
            break
    if is_four_vanguards:
        for trait in player_comp["traits"]:
            if "Set3_Mystic" in trait["name"] and trait["tier"] == 2:
                is_four_mystics = True
                return True
    return False
    # return("Comp: 4 Vanguards 4 Mystics")

# is_four_vanguards_mystics()

# 6 Cybers = 6 units w/ Cybernetic trait Tier = 2
def is_six_cybers(player_comp):
    is_six_cybers = False
    for trait in player_comp["traits"]:
        if "Cybernetic" in trait["name"] and trait["tier"] == 2:
            is_six_cybers = True
            return True
            break
    return False
# is_six_cybers()

# Jinx blaster brawlers = Jinx and brawler (tier = 1 or tier = 2) and others
def is_jinx_brawlers(player_comp):
    is_jinx_brawlers = False
    for trait in player_comp["traits"]:
        if "Set3_Brawler" in trait["name"] and (trait["tier"] == 2 or 1):
            is_jinx_brawlers = True
            break

    if is_jinx_brawlers and "TFT3_Jinx" in player_comp["units"]:
        return True
    return False
# is_jinx_brawlers()

# 6 sorcs = 6 sorcerer (tier = 3) and TFT3_Riven
def is_six_sorcs(player_comp):
    is_six_sorcs = False
    for trait in player_comp["traits"]:
        if "Set3_Sorcerer" in trait["name"] and trait["tier"] == 3:
            return True
    return False
# is_six_sorcs_riven()

# 6 Rebels = 6 rebels (tier = 2)
def is_six_rebels(player_comp):
    is_six_rebels = False
    for trait in player_comp["traits"]:
        if "Rebel" in trait["name"] and trait["tier"] == 2:
            is_six_rebels = True
            return True
    return False
# is_six_rebels()

# 6 BM slowroll = 6 blademaster (tier = 2)
def is_sixbm_slowroll(player_comp):
    is_sixbm_slowroll = False
    for trait in player_comp["traits"]:
        if "Set3_Blademaster" in trait["name"] and trait["tier"] == 2:
            is_sixbm_slowroll = True
            return True
    return False
# is_sixbm_slowroll()

# Mech Sorcs = Annie, Fizz, Rumble and sorcs
def is_mech_sorcs(player_comp):
    is_mech_sorcs = False
    for trait in player_comp["traits"]:
        if "MechPilot" in trait["name"] and trait["tier"] == 1:
            is_mech_sorcs = True
            return True
    return False
# is_mech_sorcs()

# Protector Infil = 4 Protectors (Tier = 2) w/ Fizz and Shaco**** sometimes plays snipers IDK FOR NOW
def is_protectors(player_comp):
    # is_protector_infil = False
    is_protectors = False
    for trait in player_comp["traits"]:
        if "Protector" in trait["name"] and (trait["tier"] == 2):
            is_protectors = True
            return True
    # if is_protectors:
    #     for trait in player_comp["traits"]:
    #         if "Infiltrator" in trait["name"] and (trait["tier"] == 1):
    #             is_protector_infil = True
    #             return True
    return False
# is_protector_infil();

# 6 Dark Stars = 6 Dark Star units
# def is_six_dark_stars 

# 6 Battlecast = 6 Battlecast units
# def is_six_bc

def return_comp(player_comp):
    placement = player_comp["placement"]
    if is_space_shrooms(player_comp):
        return f"{placement} Space Shrooms"
    elif is_four_vanguards_mystics(player_comp):
        return f"{placement} 4 Vanguards 4 Mystics"
    elif is_six_cybers(player_comp):
        return f"{placement} 6 Cybers"
    elif is_jinx_brawlers(player_comp):
        return f"{placement} Jinx Brawlers"
    elif is_mech_sorcs(player_comp):
        return f"{placement} Mech Sorcs"
    elif is_six_sorcs(player_comp):
        return f"{placement} 6 Sorcs"
    elif is_six_rebels(player_comp):
        return f"{placement} 6 Rebels"
    elif is_sixbm_slowroll(player_comp):
        return f"{placement} 6 BM Slowroll"
    elif is_protectors(player_comp):
        return f"{placement} Protectors"
    else:
        return f"{placement} Comp Not Found" #{player_comp}"

# print (declare_comp())

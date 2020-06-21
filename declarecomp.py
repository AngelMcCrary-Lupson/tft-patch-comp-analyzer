import json
import getcomp

player_comp = getcomp.get_comp()
print(player_comp)

def is_space_shrooms():
    # Vanguard Tier = 1, Teemo Exists
    is_space_shrooms = False
    for trait in player_comp["traits"]:
        if "Vanguard" in trait["name"] and trait["tier"] == 1:
            is_space_shrooms = True
            break

    if is_space_shrooms and "TFT3_Teemo" in player_comp["units"]:
        print("Space Shrooms")
        # return("Comp: Space Shrooms")

# Vanguard Tier = 2, Mystic Tier = 2
def is_four_vanguards_mystics():
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
                print("4 Vaungards 4 Mystics")
                break
    # return("Comp: 4 Vanguards 4 Mystics")

is_four_vanguards_mystics()

# 6 Cybers = 6 units w/ Cybernetic trait Tier = 2
def is_six_cybers():
    is_six_cybers = False
    for trait in player_comp["traits"]:
        if "Cybernetic" in trait["name"] and trait["tier"] == 2:
            is_six_cybers = True
            print("6 Cybers")
            break

# is_six_cybers()

# Jinx blaster brawlers = Jinx and brawler (tier = 1 or tier = 2) and others
def is_jinx_brawlers():
    is_jinx_brawlers = False
    for trait in player_comp["traits"]:
        if "Set3_Brawler" in trait["name"] and (trait["tier"] == 2 or 1):
            is_jinx_brawlers = True
            break

    if is_jinx_brawlers and "TFT3_Jinx" in player_comp["units"]:
        print("Jinx Brawlers")

# is_jinx_brawlers()

# 6 sorcs = 6 sorcerer (tier = 3) and TFT3_Riven
def is_six_sorcs_riven():
    is_six_sorcs_riven = False
    for trait in player_comp["traits"]:
        if "Set3_Sorcerer" in trait["name"] and trait["tier"] == 3:
            if "TFT3_Riven" in player_comp["units"]:
                if not "TFT3_Fizz" and "TFT_Rumble" in player_comp["units"]:
                    is_six_sorcs_riven = True
                    print("6 Sorcs & Riven")
                    break
# is_six_sorcs_riven()

# 6 Rebels = 6 rebels (tier = 2)
def is_six_rebels():
    is_six_rebels = False
    for trait in player_comp["traits"]:
        if "Rebel" in trait["name"] and trait["tier"] == 2:
            is_six_rebels = True
            print("Rebels")
            break
# is_six_rebels()

# 6 BM slowroll = 6 blademaster (tier = 2)
def is_sixbm_slowroll():
    is_sixbm_slowroll = False
    for trait in player_comp["traits"]:
        if "Set3_Blademaster" in trait["name"] and trait["tier"] == 2:
            is_sixbm_slowroll = True
            print("6BM Slowroll")
            break
# is_sixbm_slowroll()

# Mech Sorcs = Annie, Fizz, Rumble and sorcs
def is_mech_sorcs():
    is_mech_sorcs = False
    for trait in player_comp["traits"]:
        if "MechPilot" in trait["name"] and trait["tier"] == 1:
            is_mech_sorcs = True
            print("Mech Sorcs")
            break
# is_mech_sorcs()

# Protector Infil = 4 Protectors (Tier = 2) w/ Fizz and Shaco**** sometimes plays snipers IDK FOR NOW
def is_protector_infil():
    is_protector_infil = False
    is_protectors = False
    for trait in player_comp["traits"]:
        if "Protector" in trait["name"] and (trait["tier"] == 1 or 2):
            is_protectors = True
            break
    if is_protectors:
        for trait in player_comp["traits"]:
            if "Infiltrator" in trait["name"] and (trait["tier"] == 1):
                is_protector_infil = True
                print("Protector Infils")
                break
is_protector_infil();

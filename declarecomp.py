import json
import getcomp

player_comp = getcomp.get_comp()
print(player_comp)

def is_space_shrooms():
    # Vanguard Tier = 1, Teemo Exists
    is_space_shrooms = False
    for trait in player_comp["traits"]:
        if "Vanguard" in trait["name"] and trait["tier"] is 1:
            is_space_shrooms = True
            break

    if is_space_shrooms and "TFT3_Teemo" in player_comp["units"]:
        print("Space Shrooms")
        # return("Comp: Space Shrooms")

# Vanguard Tier = 2, Mystic Tier = 2
def is_four_vanguards():
    is_four_vanguards = False
    for trait in player_comp["traits"]:
        if "Vanguard" in trait["name"] and trait["tier"] is 2:
            if "Set3_Mystic" in trait["name"] and trait["tier"] is 2:
                is_four_vanguards = True
        else:
            break
    print("4 Vanguards 4 Mystics")
    # return("Comp: 4 Vanguards 4 Mystics")

is_four_vanguards()

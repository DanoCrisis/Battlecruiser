# The Battlecruiser stats; laid out as follows:

# 0: Name, 1: Core Level, 2: Power reserve, 3: Power per turn, 4: Hull integrity, 5: Max Shield Strength, 6: Current Shield Strength 7: Max Armour 8: Current Armour, 9: Max Actions Per Turn, 10: Current Actions

#                   0            1     2   3  4  5    6   7   8  9  10
battlecruiser = ["Dreadnought", 0.2, 100, 20, 1, 50, 50, 50, 50, 2, 2]

bc_primary_weapons_systems = ["Laser Beam M1", "No System", "No System"]

bc_sub_systems = []



# Weapons Systems

# 0: Damage, 1: Power Drain, 2: Ammo Loss, 3: Accuracy
primary_weapons_systems = {
    "Laser Beam M1" : [10, 5, 0, 0.8]

}



# Enemy Ships

# 0: Power reserve, 1: Power per turn, 2: Hull integrity, 3: Max Shield Strength, 4: Current Shield Strength 5: Max Armour 6: Current Armour, 7: Max Actions Per Turn, 8: Actions Left

#                   0    1  2   3   4   5  6   7  8
enemy_ships = {

    "Basic Drone" : [20, 5, 1, 20, 20, 10, 10, 1, 1]
}
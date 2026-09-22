# CTI 110
# P3T1 - Warmup with If free statements
# Castro-perez
# 9/22/26

# main() -- this is the program's starting point.
# You don't need to use it, but it's a very good idea.
def main():
    print("Hello and welcome the the dungeon")
    level = int(input("What level are you? "))
    if level >= 21:
        print("You can enter the dragon's spire dungeon.")
    else:
        print("Try leveling up first.")

    # Part 2 - List your potions
    print("Time to enter the dungeon.")
    potions = int(input("How many health potions did you bring? "))
    if potions == 0:
        print("It's dangerous to go alon without potions.")
    elif potions == 1:
        print(f"You have {potions} health potion.")
    elif potions >= 1:
        print(f"You have {potions} health potions.")
    else:
        print(f"HOW DID YOU GET {potions}!? that's less than 0")
    # Part 3 BOSS BATTLE!
    print ("you are facing the DELUXE OGRE MAGE")
    print ("This will be a hard fight")
    if level >= 25:
        if potions > 3:
            print("It takes 3 potions to get him to low health!")
            print("YOU ARE A HERO!!")
        else:
            print("You run out of healing before he's weakened.")
            print("Your Dead/Voce Morreu")
    else:
        print("His armor is too strong!")
        print("Your Dead/Voce Morreu")


# at the bottom -- start the program
main()

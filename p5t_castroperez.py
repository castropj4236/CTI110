#castroperezj
#10/27/2026
#PST: The Potion Pouch

import random

def drink_potions(hp_missing):
    
    #hp_missing = int(input("Enter HP missing: "))

    large = hp_missing // 25
    hp_missing = hp_missing % 25
    if large == 1:
        print(large, "Large Potion")
    elif large > 1:
        print(large, "Large Potions")

    small = hp_missing // 5
    hp_missing = hp_missing % 5
    if small == 1:
        print(small, "Small Potion")
    elif small > 1:
        print(small, "Small Potions")

    print("Still missing:", hp_missing, "HP")

def get_random_gold():
    gold = round(random.uniform(0.01, 100.00), 2)
    return gold

def main():
    #hp_missing = int(input("Enter HP missing: "))
    #drink_potions(hp_missing)
    max_hp = int(input("What is your max HP? "))
    hp = random.randint(1, max_hp)
    print(f"A goblin hits you. You have {hp} HP left.")
    hp_missing = max_hp - hp
    print(f"You are missing {hp_missing} HP.")

    gold = get_random_gold()
    print(f"You find {gold:.2f} gold in the chest.")
    drink_potions(hp_missing)

#Start the program
main()
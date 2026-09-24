# CTI 110
# P3LAB - Making Change
# castroperez
# 9/24/26
"""
# E1
hp =  int(input("How many hit points of damage (1-100): "))
print("You took ", hp, "DAMAGE!")

# Large potions heal 25
large = hp // 25
hp    = hp % 25

print("Drank ", large, "large potions.")
print("Damage remaining: ", hp)

# Small potions heal 5
small = hp // 5
hp    = hp % 5

print("Drank", small, "small potions.")
print("Damage remaining: ", hp)
"""
# E2
amount = float(input("Enter dollars and cents (ex: 0.00): "))
cents = round(amount * 100)
print("That's", cents, "cents")
dollars = cents // 100
cents   = cents % 100
if dollars == 0:
    pass
if dollars == 1:
    print("1 dollar")
if dollars > 1:
    print(dollars,"dollars")

quarters = cents // 25
cents    = cents % 25
if quarters == 0:
    pass
if quarters == 1:
    print("1 quarter")
if quarters > 1:
    print(quarters,"quarters")
    
dimes = cents // 10
cents = cents % 10
if dimes == 1:
    print("1 dime")
if dimes > 1:
    print(dimes,"dimes")
    
nickles = cents // 5
cents = cents % 5
if nickles == 1:
    print("1 nickle")
if nickles > 1:
    print(nickles,"nickles")
    
pennies = cents // 1
cents = cents % 1
if pennies == 1:
    print("1 penny")
if pennies > 1:
    print(pennies,"pennies")
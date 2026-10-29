# CTI 110
# P5LAB - Purchase and change
# castroperez
# 10/29/26
# Self checkout machine simulator. Makes change.

import random

def disperse_change(amount):
    print(f"Change is:${amount:.2f}")
    print()
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

def main():
    cost = 0.0
    amount_paid = 0.0
    change_owed = 0.0
    print("Welcome to the self-checkout sim.")
    cost =  round(random.uniform(0.01, 100.00),2)
    print(f"You owe: ${cost:.2f}")
    amount_paid = float(input("How much money do you put in the self checkout? $"))
    change_owed = amount_paid - cost
    print("Here is your change:")
    disperse_change(change_owed)

main()
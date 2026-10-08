# CTI 110
# P4LAB2 - loops
# Castro-Perez
# 10/8/26

"""
for number in (1,2,3,4):
    print(number)
for number in range (5):
    print(number)
for beer in range (99,0,-1):
    print(beer, "bottles of beer on the wall.")
print ("7's times tables:")
for mult in range(1,13):
    print (7*mult)
"""
again = "yes"
while again == "yes":

    multiplier = int(input("enter a number 0-12: "))
    while multiplier < 0 or multiplier > 12:
        print("That is invalid number.")
        multiplier = int(input("Enter a number 0-12: "))
    print("Multiplication Table")
    print("-"*20)
    for number in range(1,13):
        print(f"{multiplier} * {number} = {number * multiplier}")
    again = input("Run again? (yes/no) ")

print()
print("program ended code No. 009")
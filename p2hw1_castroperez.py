# CTI 110
# P2HW1 - Setup Only
# Talk about how to format the display

# Sample data - real program uses input()
budget = int(input("enter budget: "))

destination = input("enter your destination: ")

gas = int(input("enter that you can spend in gas: "))

hotel = int(input("enter that you spend the night: "))

food = int(input("enter the cost of the food and snacks: "))

expenses = gas+hotel+food

remaining = budget-expenses

print("<<<<<<<<<<Travel-Expenses>>>>>>>>>>")
print(f"{"Location:":<15} {destination:<15}")
print(f"{"Initial Budget:":<15} ${budget:<15.2f}")
print(f"{"Fuel:":<15} ${gas:<15.2f}")
print(f"{"Accomodation:":<15} ${gas:<15.2f}")
print(f"{"Food:":<15} ${food:<15.2f}")
print("<<<<<<<<<<Total Budget>>>>>>>>>>")
print(f"{"Remaining Balance for Budget:":<15} ${remaining:<15.2f}")

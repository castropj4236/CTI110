# CTI 110
# P1HW2
# Castro Perez, Jesus
# 9/10/26

# Ask user to enter their budget
budget = int(input("enter budget: "))

# Ask user to enter travel destination
destination = input("enter your destination: ")

# Ask user for amount they will spend on gas
gas = int(input("enter that you can spend in gas: "))

# Ask user for amount they will spend on accommodation
hotel = int(input("enter that you spend the night: "))

# Ask user for amount they will spend on food
food = int(input("enter the cost of the food and snacks: "))

# Add expenses
expenses = gas+hotel+food

# Subtract expenses from budget
remaining = budget-expenses

# Display results
print("<<<<<<<<<<Travel-Expenses>>>>>>>>>>")
print("Location: ",destination)
print("Initial Budget: ",budget)

print("Fuel: ",gas)
print("Accomodation: ",hotel)
print("Food: ",food)

print("Remaining Balance for Budget: ",remaining)
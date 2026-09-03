# CTI 110
# P1LAB2 - Selling Things
# castropj
# 9/3/26

# Fictional Store -- pick three things
# product_name, product_count, product_price

# Hardcoding sets values directly.
# product_name = "Television"
# product_count = 24
# product_price = 399.99

# Instead, we ask the user with input()
# INPUT
print("STORE STARTUP")
print("_" * 10) # ten _ in a row
product_name = input("Enter product name: ")
product_count = input("Enter product count: ")
product_price = input("Enter unit price: ")

# PROCESSING
product_count = int(product_count)
product_price = float(product_price)
total = product_count * product_price

# OUTPUT
print("CUSTOMER INTERFACE")
print("_" * 10) # ten _ in a row
print("Welcome to the", product_name, "store")
# For later -- f string with {variable:.2f} is the magic word to get 2 decimals
print(f"We have, {product_count}, {product_name}(s) at ${product_price:.2f},each")
print(f"Total is: ${total:.2f}.")


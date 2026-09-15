# CTI 110
# P2LAB1 - Radius
# castropj
# 9/15/26

PI = 3.14159

# Input -- get radius
radius = float(input("What is the radius of the circle? "))

# Calculation -- find diameter, circumference, and area
# diameter = 2r, circumference = 2pir, area = pi*r*r
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

# Output -- .1f, .2f, 3.f
print(f"The diameter is {diameter:.1f}.")
print(f"The circumference is {circumference:.2f}")
print(f"The area is {area:.3f}")
# CastroPerez_Jesus
# 10/06/2026
# P3HW2
# salary calculator

# request employee info
name = input("enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = 40 * rate
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    gross_pay = hours * rate

print(f"\nEmployee Name: {name}")


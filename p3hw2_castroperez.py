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
    regular_pay = hours * rate
    overtime_pay = 0
    overtime_hours = 0
    gross_pay = hours * rate

print(f"\nEmployee Name: {name}")
print(f"\nHours Worked: {hours}")
print(f"\nPayrate: {rate}")
print(f"\nOverTime: {overtime_hours}")
print(f"\nOverTime Pay: {overtime_pay}")
print(f"\nRegularHour Pay: {regular_pay}")
print(f"\nGross Pay: {gross_pay}")
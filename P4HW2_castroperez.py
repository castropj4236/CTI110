# CastroPerez_Jesus
# 10/22/2026
# P4HW2
# salary calculator

# request employee info
name = input("enter employee name or 'done' to finish: ")

overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    employee_count += 1
    hours = float(input("How many hours did " +name+ " work this week?"))
    rate = float(input("What is " +name+ "'s hourly pay rate?"))

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

    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

print(f"\nEmployee Name: {name}")
print(f"\nHours Worked: {hours}")
print(f"\nPayrate: {rate}")
print(f"\nOverTime: {overtime_hours}")
print(f"\nOverTime Pay: {overtime_pay}")
print(f"\nRegularHour Pay: {regular_pay}")
print(f"\nGross Pay: {gross_pay}")


name = input("enter employee name or 'done' to finish: ")

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular time: $", format(regularpay_total, ',.2f'))
print("Total amount paid for gross: $", format(grosspay_total, ',.2f'))
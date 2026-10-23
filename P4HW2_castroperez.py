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

while name != "Done":

    rate = float(input("What is " + name + "'s hourly pay rate? "))
    hours = float(input("How many hours did " + name + " work this week? "))

    if hours > 40:
        overtime_hours = hours - 40
        regular_pay = 40 * rate
        overtime_pay = overtime_hours * (rate * 1.5)
        gross_pay = regular_pay + overtime_pay
    else:
        regular_pay = hours * rate
        overtime_hours = 0
        overtime_pay = 0
        gross_pay = regular_pay

    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay
    employee_count += 1

    print("Employee Name:", name)
    print("Hours Worked:", hours)
    print("Pay Rate: $", format(rate, ".2f"), sep="")
    print("Overtime Hours:", overtime_hours)
    print("Overtime Pay: $", format(overtime_pay, ".2f"), sep="")
    print("Regular Pay: $", format(regular_pay, ".2f"), sep="")
    print("Gross Pay: $", format(gross_pay, ".2f"), sep="")
    print()

    name = input("Enter employee name or 'Done' to finish: ")

print()
print("Total number of employees entered:", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ",.2f"), sep="")
print("Total amount paid for regular time: $", format(regularpay_total, ",.2f"), sep="")
print("Total amount paid for gross: $", format(grosspay_total, ",.2f"), sep="")
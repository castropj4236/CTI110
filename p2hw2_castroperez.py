# CTI 110
# P2HW2 - just the setup

# This example only uses three numbers, the full uses six.
# get the grades
grade1 = float(input("Enter grade #1: "))
grade2 = float(input("Enter grade #2: "))
grade3 = float(input("Enter grade #3: "))
# put them all into a new list
grade_list = [grade1, grade2, grade3]

# Do some calculations -- minimum, maximum, and average
min_grade = min(grade_list)
max_grade = max(grade_list)
sum_grade = sum(grade_list)
length = len(grade_list)
average_grade = sum(grade_list) / len(grade_list)

# Reserves
print(f"{'Lowest_Grade:':<18}{min_grade}")
print(f"{'Average':<18}{average_grade:.2f}")
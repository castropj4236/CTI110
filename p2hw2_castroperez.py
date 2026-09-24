# CTI 110
# P2HW2 - just the setup

# This example only uses three numbers, the full uses six.
# get the grades
grade1 = float(input("Enter grade #1: "))
grade2 = float(input("Enter grade #2: "))
grade3 = float(input("Enter grade #3: "))
grade4 = float(input("Enter grade #4: "))
grade5 = float(input("Enter grade #5: "))
grade6 = float(input("Enter grade #6: "))
# put them all into a new list
grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]

# Do some calculations -- minimum, maximum, and average
min_grade = min(grade_list)
max_grade = max(grade_list)
sum_grade = sum(grade_list)
length = len(grade_list)
average_grade = sum(grade_list) / len(grade_list)

# Reserves
print("------------Results------------")
print(f"{'Lowest_Grade:':<18}{min_grade}")
print(f"{'Highest_Grade:':<18}{max_grade}")
print(f"{'Sum_of_Grade:':<18}{sum_grade}")
print(f"{'Average':<18}{average_grade:.2f}")
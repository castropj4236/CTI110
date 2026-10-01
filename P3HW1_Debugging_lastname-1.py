# Jesus Castro-Perez
# 9/29/2026
# P3HW1_Debugging
# Brief description of program

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
lowest_ = min(grades)
highest_ = max(grades)
sum_ = sum(grades)
length_ = len(grades)
average_ = sum(grades) / len(grades)

# determine letter grade for average
print("--------------Results--------------")
print(f"{'Lowest_Grade:':<18}{lowest_}")
print(f"{'Highest_Grade:':<18}{highest_}")
print(f"{'Sum_of_Grade:':<18}{sum_}")
print(f"{'Average':<18}{average_:.2f}")
print("-------------------------------------")

if average_ >= 90:
    letter_grade = "A"
elif average_ >= 80:
    letter_grade = "B"
elif average_ >= 70:
    letter_grade = "C"
elif average_ >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"{'Your grade is: ':<18}{letter_grade}")






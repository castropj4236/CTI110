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


if avg >= 90:
 
    print('Your grade is: A')
else:
if average > 80:
 print('Your grade is: B')
else:

else:
print('Your grade is: F') # TO DO: finish this






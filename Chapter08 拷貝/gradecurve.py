# L-8 MCS 260 : grading scale
"""
This program prompts the user to enter a number.
The corresponding letter grade is printed.
"""
DATA = input('Enter your number : ')
NUMBER = int(DATA)
if NUMBER >= 90:
    GRADE = 'A'
elif NUMBER >= 80:
    GRADE = 'B'
elif NUMBER >= 70:
    GRADE = 'C'
elif NUMBER >= 60:
    GRADE = 'D'
else:
    GRADE = 'F'
print('Your grade is ' + GRADE + '.')

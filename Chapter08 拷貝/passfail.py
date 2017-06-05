# L-8 MCS 260 : illustration of if else
"""
This program prompts the user to enter a number.
If the number entered is larger or equal than 80,
then the user is congratulated, else we are sorry.
"""
DATA = input('Enter your number : ')
NUMBER = int(DATA)
if NUMBER >= 80:
    print('Congratulations.  You passed!')
else:
    print('Sorry.  Please try again...')

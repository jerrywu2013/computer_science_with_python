# L-9 MCS 260 : alphatest.py
"""
We test if a given string is a number.
"""
DATA = input('Give a number : ')
SHOW = '\"' + DATA + '\"'
if DATA.isalpha():
    print(SHOW + ' is alphabetic ')
elif DATA.isdigit():
    print(SHOW + ' consist of digits only')
elif DATA.isalnum():
    print(SHOW + ' is alphanumeric ')
else:
    print(SHOW + ' fails all tests')

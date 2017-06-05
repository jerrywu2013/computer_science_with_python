# L-4 MCS 260 : yield and balance computation
"""
This program prompts the user for the following inputs:
(1) principal , (2) annual interest rate (percentage format),
(3) and number of years.  (1) and (2) are floats, (3) is integer.
The output of the program consists of
(1) the ending balance and (2) the yield of the investment.
"""
# welcome message, read input and convert to arithmetic types
print('computation of yield and balance')
DATA = input('Give the principal : ')
PRINCIPAL = float(DATA)
DATA = input('Give the annual interest rate : ')
INTEREST = float(DATA)
DATA = input('Give the number of years : ')
YEARS = int(DATA)
# confirm the user input using string concatenation
INVESTING = 'Investing ' + '$%.2f' % PRINCIPAL
RATE = ' at ' + '%.2f' % INTEREST + '%'
DURATION = ' for ' + '%d' % YEARS + ' years'
print(INVESTING + RATE + DURATION)
# calculate balance and yield (yield is a Python statement)
BALANCE = PRINCIPAL * (1.0 + INTEREST/100.0)**YEARS
YIELD = BALANCE - PRINCIPAL
# print the outcome, again using string concatenation
ENDBALANCE = '$%.2f' % BALANCE + ' as balance'
SHOWYIELD = '$%.2f' % YIELD + ' as yield'
print('gives ' + ENDBALANCE + ' and ' + SHOWYIELD + '.')

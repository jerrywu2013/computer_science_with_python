# L-11 MCS 260 : a while loop
"""
Shows annual growth of an investment.
The user enters principal, interest rate,
and the number of years.  After each year
the balance of the investment are shown.
"""
print('Calculation of the annual balance')
B = float(input('Give amount to invest : '))
R = float(input('Give annual interest rate : '))
N = int(input('Give number of years : '))
print('At year %d : Balance = $%.2f' % (0, B))
i = 1
while i <= N:
    B *= (1 + R/100)
    print('At year %d : Balance = $%.2f' % (i, B))
    i += 1

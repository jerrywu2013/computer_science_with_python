# L-11 MCS 260 : a for loop
"""
Shows annual growth of an investment.
The user enters principal, interest rate,
and the number of years.  After each year
the balance of the investment are shown.
"""
print('Calculation of the annual balance')
B = int(input('Give amount to invest : '))
R = float(input('Give annual interest rate : '))
N = int(input('Give number of years : '))
print('At year %d : Balance = $%.2f' % (0, B))
for i in range(1, N+1):
    B *= (1 + R/100)
    print('At year %d : Balance = $%.2f' % (i, B))

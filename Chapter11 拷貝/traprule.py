# L-11 MCS 260 : traprule
"""
Applies the trapezoidal rule to approximate Pi,
as a simple translation of a formula.
"""
from math import sqrt, pi

N = int(input('give the number of intervals : '))
S = 0
for i in range(0, N):
    x1 = float(i)/N
    fx1 = sqrt(1-x1*x1)
    x2 = float(i+1)/N
    fx2 = sqrt(1-x2*x2)
    base = x2 - x1
    height = (fx1 + fx2)/2
    S = S + base*height
APPROXIMATION = 4*S
ERROR = abs(APPROXIMATION - pi)
print('approximation for pi = %.14f' % APPROXIMATION)
print('error = %.3E' % ERROR)

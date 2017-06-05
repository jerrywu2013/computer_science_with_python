# L-12 MCS 260 : Monte Carlo for pi
"""
We count the number of samples (x, y)
that lie in the unit disk.
"""
from random import uniform as u

print('Monte Carlo simulation for Pi')
NBR = int(input('Give number of runs : '))
INDISK = 0
for i in range(NBR):
    (X, Y) = (u(-1, 1), u(-1, 1))
    if X**2 + Y**2 <= 1:
        INDISK = INDISK + 1
print('After %d runs : %f' % (NBR, 4*INDISK/NBR))

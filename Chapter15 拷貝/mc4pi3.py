# L-15 MCS 260 : mc4pi3
"""
Illustration of lambda forms in
a Monte Carlo method for Pi.
"""
import random
N = int(input('Give number of samples : '))
X = [random.uniform(0, 1) for i in range(N)]
Y = [random.uniform(0, 1) for i in range(N)]
Z = [(X[k], Y[k]) for k in range(N)]
T = lambda x_y: x_y[0]**2 + x_y[1]**2 <= 1
R = [T(z) for z in Z]
P = 4.0*sum(R)/len(R)
print('estimate for Pi : %f' % P)

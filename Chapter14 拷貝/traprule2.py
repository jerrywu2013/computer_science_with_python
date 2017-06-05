# L-14 MCS 260 : trapezoidal rule
"""
The trapezoidal rule approximates the
integral of a function f(x) over [a,b]
via (f(a) + f(b))*(b-a)/2
"""
def traprule(fun, start, stop):
    "trapezoidal rule for f(x) over [start, stop]"
    return (stop-start)*(fun(start) + fun(stop))/2

from math import exp
RESULT = 'integrating exp() over '
print(RESULT + '[a,b]')
A = float(input('give a : '))
B = float(input('give b : '))
APPROX = traprule(exp, A, B)
print(RESULT + '[%.1E, %.1E] : ' % (A, B))
print('the approximation : %.15E' % APPROX)
EXACT = exp(B) - exp(A)
print('  the exact value : %.15E' % EXACT)


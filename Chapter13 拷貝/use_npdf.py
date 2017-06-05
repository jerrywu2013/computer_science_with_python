# L-13 MCS 260 : a function
"""
Evaluate the probability density function
of a normal distribution.
"""

def npdf(arg, mean=0, sigma=1):
    """
    Normal probability density function
    with default values for the mean
    and the standard deviation.
    """
    import math
    result = math.exp(-(arg - mean)**2/(2*sigma**2))
    result = result/(sigma*math.sqrt(2*math.pi))
    return result

ARG = float(input('give x : '))
print('f(', ARG, ') = ', npdf(ARG))
MEAN = float(input('give mean : '))
SIGMA = float(input('give standard deviation : '))
print('for mu = ', MEAN, 'and sigma = ', SIGMA)
print('f(', ARG, ') = ', npdf(mean=MEAN, sigma=SIGMA, arg=ARG))

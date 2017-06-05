# L-13 MCS 260 : npdf
"""
Same name for function and module.
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

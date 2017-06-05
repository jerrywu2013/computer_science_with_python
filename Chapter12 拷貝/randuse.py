# L-12 MCS 260 : random numbers
"""
Illustration of using random numbers.
"""
import random         # use module random
random.seed(21342342) # get same sequence
print('uniformly distributed random numbers')
LOWER = float(input('give lower bound : '))
UPPER = float(input('give upper bound : '))
RND = random.uniform(LOWER, UPPER) # generate a number
print('a random number in [%.2f, %.2f] : %.15f' \
    % (LOWER, UPPER, RND))

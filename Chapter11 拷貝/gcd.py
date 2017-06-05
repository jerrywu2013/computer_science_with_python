# L-11 MCS 260 : loop for gcd
"""
Prints the greatest common divisor of two
user given positive numbers.
"""
print('The Greatest Common Divisor')
A = int(input('Give a : '))
B = int(input('Give b : '))
# save numbers for output later
OUTCOME = 'gcd(%d, %d) = ' % (A, B)
REST = A % B        # initialization
while REST != 0:
    (A, B) = (B, REST)
    REST = A % B
print(OUTCOME + '%d' % B)

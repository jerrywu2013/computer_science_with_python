# L-15 MCS 260 : apply
"""
apply() in a simple calculator
"""
from operator import add, sub, mul
OPS = { '+':add, '-':sub, '*': mul }
A = int(input('give first operand : '))
B = int(input('give second operand : '))
ACT = input('operator ? (+, -, *) ')
C = OPS[ACT](*(A, B))
print('%d %s %d = %d' % (A, ACT, B, C))

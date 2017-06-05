# L-10 MCS 260 : towers of Hanoi
"""
To illustrate the use of stacks we solve the
towers of Hanoi problem with three disks.
"""
print('Towers of Hanoi with 3 disks')
A = [1, 2, 3]
B = []
C = []
print('initially : A =', A, 'B =', B, 'C =', C)
B.insert(0, A.pop(0))
print('move 1 : A =', A, 'B =', B, 'C =', C)
C.insert(0, A.pop(0))
print('move 2 : A =', A, 'B =', B, 'C =', C)
C.insert(0, B.pop(0))
print('move 3 : A =', A, 'B =', B, 'C =', C)
B.insert(0, A.pop(0))
print('move 4 : A =', A, 'B =', B, 'C =', C)
A.insert(0, C.pop(0))
print('move 5 : A =', A, 'B =', B, 'C =', C)
B.insert(0, C.pop(0))
print('move 6 : A =', A, 'B =', B, 'C =', C)
B.insert(0, A.pop(0))
print('move 7 : A =', A, 'B =', B, 'C =', C)

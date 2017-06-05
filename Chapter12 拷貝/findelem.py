# L-12 MCS 260 : find element
"""
Illustration of a double for loop to find
an element in a two dimensional matrix.
"""
# first we make a random matrix
from random import randint
ROWS = int(input('give the number of rows : '))
COLS = int(input('give the number of columns : '))
MAT = []
for i in range(ROWS):
    MAT.append([randint(10, 99) for _ in range(COLS)])
print('random %d-by-%d matrix :' % (ROWS, COLS))
for row in MAT:
    print(row)
# then we ask for a number and search
NBR = int(input('give a number : '))
FOUND = False
for i in range(0, ROWS):
    for j in range(0, COLS):
        if MAT[i][j] == NBR:
            FOUND = True
            (ROW, COL) = (i, j)
            break
    if FOUND:
        break
# we report the result
if FOUND:
    print('found %d at [%d][%d]' % (NBR, ROW, COL))
else:
    print('%d does not occur in the matrix' % NBR)

# L-12 MCS 260 : binary expansion, version 1(b)
"""
Use of break for repeat until.
The script also shows how to avoid a line break
when printing the bits in the expansion.
"""
print('computing the binary expansion')
NBR = int(input('Give a number : '))
while True:
    (NBR, REST) = divmod(NBR, 2)
    print(REST, end=' ') # no line break
    if NBR == 0:
        break

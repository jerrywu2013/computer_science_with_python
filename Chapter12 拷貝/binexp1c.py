# L-12 MCS 260 : binary expansion
"""
A break only effects one loop.
"""
print('computing the binary expansion')
while True:
    NBR = int(input('Give a number (< 0 to exit) : '))
    if NBR < 0:
        break
    while True:
        (NBR, REST) = divmod(NBR, 2)
        print(REST)
        if NBR == 0:
            break

# L-12 MCS 260 : binary expansion
"""
This first version prints the bits
in the order as they are computed.
We use divmod(), an intrinsic operation
on numeric types.
"""
print('computing the binary expansion')
NBR = int(input('Give a number : '))
(NBR, REST) = divmod(NBR, 2)
print(REST)
while NBR > 0:
    (NBR, REST) = divmod(NBR, 2)
    print(REST)

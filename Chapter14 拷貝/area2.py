# L-14 MCS 260 : area2
"""
A rectangle is given by length and width,
for a square we only need one argument
to compute the area.
"""
def area(length, **width):
    "returns area of rectangle"
    if len(width) == 0:          # square
        return length**2
    else:                     # rectangle
        result = length
        for each in width:
            result *= width[each]
        return result

print('area of square or rectangle')
LEN = float(input('give length : '))
WID = float(input('give width : '))
if WID == 0:
    AREA = area(LEN)
else:
    AREA = area(LEN, width=WID)
print('the area is', AREA)

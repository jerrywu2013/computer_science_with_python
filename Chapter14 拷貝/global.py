# L-14 MCS 260 : global variables
"""
illustration of a global variable
"""
VALUE = 2014   # our global variable

def update(formalv):
    """
    shows value of formal v
    and prompts for new v
    """
    print('v = ', formalv)
    vraw = input('Give new value : ')
    newv = int(vraw)
    return newv

while True:
    VALUE = update(VALUE) # do not forget ()
    ANS = input('continue ? (y/n) ')
    if ANS != 'y':
        break

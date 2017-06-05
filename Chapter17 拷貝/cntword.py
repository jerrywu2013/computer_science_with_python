# L-17 MCS 260 : count words
"""
This program counts the number times
the sequence 'the' occurs in a text.
"""

def add_to_buffer(buf, let):
    """
    Adds let to a 3-letter buffer buf,
    on return is the updated buffer.
    """
    nbf = buf
    if len(buf) == 3:
        (nbf[0], nbf[1], nbf[2]) = (nbf[1], nbf[2], let)
    else:
        nbf.append(let)
    return nbf

SEARCH = ['t', 'h', 'e']
BUFF = []
NAME = input('give file name : ')
FILE = open(NAME, 'r')
COUNT = 0
while True:
    C = FILE.read(1)
    if C == '':
        break
    BUFF = add_to_buffer(BUFF, C)
    if BUFF == SEARCH:
        COUNT += 1
FILE.close()
print('#occurrences of the : %d' % COUNT)

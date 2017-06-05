# L-17 MCS 260 : replace word
"""
This program replaces each occurrence
of 'the' by 'one' in a text.
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
FILE = open(NAME, 'r+')
while True:
    C = FILE.read(1)
    if C == '':
        break
    BUFF = add_to_buffer(BUFF, C)
    if BUFF == SEARCH:
        CURSOR = FILE.tell()
        FILE.seek(-3, 1)
        FILE.write('one')
FILE.close()

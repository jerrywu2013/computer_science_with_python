# L-17 MCS 260 : scramvow.py
"""
This program scrambles vowels on a file.
"""
D = {'a':'e', 'e':'u', 'i':'o', 'o':'a', 'u':'i'}
print(list(D.keys()), '->', list(D.values()))
NAME = input('name of input file : ')
INFILE = open(NAME, 'r')
NAME = input('name of output file : ')
OUTFILE = open(NAME, 'w')
while True:
    C = INFILE.read(1)
    if C == '':
        break
    if C in D:
        OUTFILE.write(D[C])
    else:
        OUTFILE.write(C)
INFILE.close()
OUTFILE.close()

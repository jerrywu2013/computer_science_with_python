# L-17 MCS 260 : bkfrom2list
"""
Converts existing formats of books on file as

  1:1:Computer Science.  An Overview:
  0:2:Python Programming in Context:

into

  [True, 1, 'Computer Science.  An Overview']
  [False, 2, 'Python Programming in Context']
"""
INFILE = open('books', 'r')
OUTFILE = open('bookslists', 'w')
while True:
    S = INFILE.readline()
    if S == '':
        break
    L = S.split(':')
    R = [L[0] == '1', int(L[1]), L[2]]
    OUTFILE.write(str(R) + '\n')
INFILE.close()
OUTFILE.close()

# L-17 MCS 260 : bklist2dict
"""
Converts existing formats of books on file from

  [True, 1, 'Computer Science.  An Overview']
  [False, 2, 'Python Programming in Context']

 into

  {'available':True, 'key':1, 'title':'Computer Science.  An Overview'}
  {'available':False, 'key':2, 'title':'Python Programming in Context'}

"""
from ast import literal_eval
INFILE = open('bookslists', 'r')
OUTFILE = open('booksdicts', 'w')
while True:
    S = INFILE.readline()
    if S == '':
        break
    L = literal_eval(S)
    D = {'available':L[0], 'key':L[1], \
         'title':L[2]}
    OUTFILE.write(str(D) + '\n')
INFILE.close()
OUTFILE.close()

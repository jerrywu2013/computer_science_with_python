# L-15 MCS 260 : oracle.py
"""
With lambda forms we can make functions
that return functions.
"""
def make_oracle():
    "returns an oracle as a lambda form"
    numb = int(input('Give secret number : '))
    return lambda x: x == numb

ORACLE = make_oracle()
while True:
    DATA = input('Guess the secret : ')
    GUESS = int(DATA)
    if ORACLE(GUESS):
        break
    print('wrong, try again')
print('found the secret')

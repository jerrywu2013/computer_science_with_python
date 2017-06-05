# L-10 MCS 260 : write_values.py
"""
Input: a string of at most two words representing a number,
       separated by exactly one space.
Output: the corresponding numerical value of the words
        in the string.

This is the inverse of the Python script write_numbers
of the previous lecture,
except that it is limited to numbers up to 100.
"""
DIC = { \
    'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, \
    'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, \
    'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, \
    'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, \
    'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, \
    'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, \
    'ninety':90, 'hundred':100 \
}
WORDS = input('give a number in words : ')
OUTCOME = 'the value of ' + WORDS + ' is '
if WORDS in DIC:
    OUTCOME += str(DIC[WORDS])
else:
    SPLITTED = WORDS.split(' ')
    OUTCOME += str(DIC[SPLITTED[0]] + DIC[SPLITTED[1]])
print(OUTCOME)

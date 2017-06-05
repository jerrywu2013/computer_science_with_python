# L-10 MCS 260 : sortwords
"""
This program shows intrinsic operations
on strings and lists, to sort words,
given as a raw input string by the user.
"""
WORDS = input('Give words : ')
SPLITTED = WORDS.split()    # spaces separate the words
SPLITTED.sort()             # sort the list alphabetically
SORTED = ' '.join(SPLITTED) # join the sorted list
print('Sorted words :', SORTED)

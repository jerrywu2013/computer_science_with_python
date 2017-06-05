# L-8 MCS 260 : followup.py
"""
An illustration of a nested if-else statement
to handle followup questions in a dialogue.
"""
ANS = input('happy ? (y/n) ')
if ANS == 'n':
    ANS = input('bored ? (y/n) ')
    if ANS == 'y':
        print('class is soon over')
    else:
        print('but it is Friday')
else:
    print('keep up the good work')

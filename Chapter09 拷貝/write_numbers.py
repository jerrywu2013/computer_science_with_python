# L-9 MCS 260 : write_numbers.py
"""
When writing a check, the amount is spelled out in words.
The program below writes numbers strictly less than 1000 into words.
"""
DIC = { \
    0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', \
    5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', \
    10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', \
    14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', \
    18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', \
    40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', \
    90:'ninety', 100:'hundred' \
}
DATA = input('give a natural number : ')
NBR = int(DATA)
OUTCOME = '%d is ' % NBR
if NBR == 0:
    OUTCOME += DIC[NBR]
elif NBR >= 100:
    OUTCOME += DIC[NBR/100] + ' ' + DIC[100]
    NBR = NBR % 100
    if NBR != 0:
        OUTCOME += ' and '
if NBR > 0:                 # write zero only once
    if NBR <= 20:
        OUTCOME += DIC[NBR]
    else:
        REST = NBR % 10
        if REST == 0:
            OUTCOME += DIC[NBR]
        else:
            OUTCOME += DIC[NBR-REST] + ' ' + DIC[REST]
print(OUTCOME)

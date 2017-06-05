# L-14 MCS 260 : histograms
"""
A voting machine tallies votes.
We use two global variables in the main loop
as arguments in a sequence.
"""
TNO = 0   # tno counts no votes
TYES = 0  # tyes counts yes votes

def poll():
    "asks whether approve or not"
    print('Vote yes or no, 0 to stop')
    answer = input('approve ? (y/n) ')
    return answer

def update(tally, vote):
    "updates tally with vote"
    if vote == 'y':
        return (tally[0], tally[1]+1)
    elif vote == 'n':
        return (tally[0]+1, tally[1])

while True:
    VOTE = poll()
    if VOTE == '0':
        break
    (TNO, TYES) = update((TNO, TYES), VOTE)
print('Tally of votes :', (TNO, TYES))

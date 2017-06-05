# L-14 MCS 260 : histograms
"""
A voting machine tallies votes.
In this second version we use a list to
tally votes and use call by reference
in this way.
"""
TALLY = [0, 0] # TALLY[0] counts no votes
               # TALLY[1] counts yes votes
def poll():
    "asks whether approve or not"
    print('Vote yes or no, 0 to stop')
    answer = input('approve ? (y/n) ')
    return answer

def update(tally, vote):
    "updates tally with vote"
    if vote == 'y':
        tally[1] += 1
    elif vote == 'n':
        tally[0] += 1

while True:
    VOTE = poll()
    if VOTE == '0':
        break
    update(TALLY, VOTE)
print('Tally of votes :', TALLY)

# L-14 MCS 260 : histograms
"""
A voting machine tallies votes.
"""
TALLY = [0, 0] # TALLY[0] counts yes votes
               # TALLY[1] counts no votes
def poll():
    "asks whether approve or not"
    print('Vote yes or no, 0 to stop')
    answer = input('approve ? (y/n) ')
    return answer

def update(tally, vote):
    "updates tally with vote"
    newtally = tally
    if vote == 'y':
        newtally[0] += 1
    elif vote == 'n':
        newtally[1] += 1
    return newtally

while True:
    VOTE = poll()
    if VOTE == '0':
        break
    TALLY = update(TALLY, VOTE)
print('Tally of votes :', TALLY)

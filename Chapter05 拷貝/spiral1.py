# L-5 MCS 260 Fri 22 January 2016 : spiral1.py

"""
The instructions below illustrate some very basic turtle operations to
draw the start of a spiral on canvas, using primarily goto commands.
"""

from turtle import Turtle        # import the Turtle class
SAM = Turtle()                   # sam is the name of a Turtle object

SAM.up()                         # put the pen up
SAM.goto(0, 0)                   # goto center
SAM.down()                       # put the pen down
POS = SAM.pos()                  # get the current position
SAM.goto(POS[0], POS[1] - 10)    # go 10 pixels down
POS = SAM.pos()
SAM.goto(POS[0] - 10, POS[1])    # go 10 pixels to the left
POS = SAM.pos()
SAM.goto(POS[0], POS[1] + 20)    # go 20 pixels up
POS = SAM.pos()
SAM.goto(POS[0] + 20, POS[1])    # go 20 pixels to the right
POS = SAM.pos()
SAM.goto(POS[0], POS[1] - 30)    # go 30 pixels down
POS = SAM.pos()
SAM.goto(POS[0] - 30, POS[1])    # go 30 pixels to the left
POS = SAM.pos()
SAM.goto(POS[0], POS[1] + 40)    # go 40 pixels up
POS = SAM.pos()
SAM.goto(POS[0] + 40, POS[1])    # go 40 pixels to the right
ANS = input('hit enter to quit') # else window disappears

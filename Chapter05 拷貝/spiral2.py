# L-5 MCS 260 Fri 22 Jan 2016: spiral2.py

"""
The instructions below illustrate some very basic turtle operations to
draw the start of a spiral on canvas, without goto commands.
"""

from turtle import Turtle
LIZ = Turtle()
LIZ.down()                    # put the pen down
LIZ.right(90)                 # turn 90 degrees to the right
LIZ.forward(10)               # go forward by 10 pixels
LIZ.right(90)                 # turn 90 degrees to the right
LIZ.forward(10)               # go forward by 10 pixels
LIZ.right(90)                 # turn 90 degrees to the right
LIZ.forward(20)               # go forward by 20 pixels
LIZ.right(90)                 # turn 90 degrees to the right
LIZ.forward(20)               # go forward by 20 pixels
LIZ.right(90)                 # turn 90 degrees to the right
LIZ.forward(30)               # go forward by 30 pixels
LIZ.right(90)                 # turn 90 degrees to the right
LIZ.forward(30)               # go forward by 30 pixels
LIZ.right(90)                 # turn 90 degrees to the right
LIZ.forward(40)               # go forward by 40 pixels
LIZ.right(90)                 # turn 90 degrees to the right
LIZ.forward(40)               # go forward by 40 pixels
ANS = input('hit enter to exit')  # else window disappears

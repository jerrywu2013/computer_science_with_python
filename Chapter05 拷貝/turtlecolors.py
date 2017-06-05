# L50 MCS 260 Fri 22 Jan 2016 : turtlecolors

"""
The script below illustrates turtle geometry
and the (r, g, b) color triangle.
"""

from math import cos, sin, pi

from turtle import Turtle
from turtle import tracer

ANGLE = 2*pi/3 # angle to draw a triangle
BIGRAD = 200   # radius of the enscribed circle
CIRRAD = 80    # radius of the colored circles
# first we draw the triangle
TRIANGLE = Turtle()
TRIANGLE.up()
TRIANGLE.goto(BIGRAD, 0)
TRIANGLE.down()
TRIANGLE.goto(BIGRAD*cos(ANGLE), BIGRAD*sin(ANGLE))
TRIANGLE.goto(BIGRAD*cos(2*ANGLE), BIGRAD*sin(2*ANGLE))
TRIANGLE.goto(BIGRAD, 0)
ANS = input("hit enter to continue ...")
# at the corners we put primary rgb colored disks
tracer(False)
TRIANGLE.up()
TRIANGLE.goto(BIGRAD, -CIRRAD)
TRIANGLE.down()
TRIANGLE.begin_fill()
TRIANGLE.color((1.0, 0.0, 0.0), (1.0, 0.0, 0.0))
TRIANGLE.circle(CIRRAD)
TRIANGLE.end_fill()
TRIANGLE.up()
TRIANGLE.goto(BIGRAD*cos(ANGLE), BIGRAD*sin(ANGLE)-CIRRAD)
TRIANGLE.down()
TRIANGLE.begin_fill()
TRIANGLE.color((0.0, 1.0, 0.0), (0.0, 1.0, 0.0))
TRIANGLE.circle(CIRRAD)
TRIANGLE.end_fill()
TRIANGLE.up()
TRIANGLE.goto(BIGRAD*cos(2*ANGLE), BIGRAD*sin(2*ANGLE)-CIRRAD)
TRIANGLE.down()
TRIANGLE.begin_fill()
TRIANGLE.color((0.0, 0.0, 1.0), (0.0, 0.0, 1.0))
TRIANGLE.circle(CIRRAD)
TRIANGLE.end_fill()
ANS = input("hit enter to continue ...")
# then we draw the combinations at the edges
ANGLE2 = pi/3 # smaller angle for 6-gon
EDGE = 100    # to put circles on edges of triangle
RAD2 = 40     # radius of the secondary rgb colored disks
TRIANGLE.up()
TRIANGLE.goto(EDGE*cos(ANGLE2), EDGE*sin(ANGLE2)-RAD2)
TRIANGLE.down()
TRIANGLE.begin_fill()
TRIANGLE.color((1.0, 1.0, 0.0), (1.0, 1.0, 0.0))
TRIANGLE.circle(RAD2)
TRIANGLE.end_fill()
TRIANGLE.up()
TRIANGLE.goto(EDGE*cos(ANGLE+ANGLE2), EDGE*sin(ANGLE+ANGLE2)-RAD2)
TRIANGLE.down()
TRIANGLE.begin_fill()
TRIANGLE.color((0.0, 1.0, 1.0), (0.0, 1.0, 1.0))
TRIANGLE.circle(RAD2)
TRIANGLE.end_fill()
TRIANGLE.up()
TRIANGLE.goto(EDGE*cos(2*ANGLE+ANGLE2), EDGE*sin(2*ANGLE+ANGLE2)-RAD2)
TRIANGLE.down()
TRIANGLE.begin_fill()
TRIANGLE.color((1.0, 0.0, 1.0), (1.0, 0.0, 1.0))
TRIANGLE.circle(RAD2)
TRIANGLE.end_fill()
# to prevent the turtle window from disappearing
ANS = input('hit enter to exit ...')

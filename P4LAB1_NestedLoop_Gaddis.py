# CTI-110 
# P4LAB Nested Loop
# Shannon Gaddis
# March 25, 2018

import turtle
import random

# setup the window with a background colour
wn = turtle.Screen()
wn.setup(width=250, height=250) 

# assign a name to your turtle
t = turtle.Turtle()

colors = ["blue"]
t.pensize(4)            # increase pensize (takes integer)

def snowflake(size, pensize, x, y):
    t.penup()
    t.goto(x, y)
    t.forward(10*size)
    t.left(45)
    t.pendown()
    t.color((colors))

    for i in range(8):
        branch(size)
        t.left(45)

def branch(size):
    for i in range(3):
        for i in range(3):
            t.forward(10.0*size/3)
            t.backward(10.0*size/3)
            t.right(45)
        t.left(90)
        t.backward(10.0*size/3)
        t.left(45)
    t.right(90)
    t.forward(10.0*size)

snowflake(6, 4, 0, 0)

wn.exitonclick()

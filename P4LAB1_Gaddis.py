# P4LAB1
# Two Shapes
# Shannon Gaddis
# March 22, 2018

import turtle          
win = turtle.Screen()
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("turtle")


for i in range (3):
    t.forward(100)          
    t.left(120)            

t.penup()
t.forward(150)
t.pendown()

for s in range (4):
    t.pencolor("green")
    t.forward(85)
    t.left(90)
    
win.mainloop()             # Wait for user to close window

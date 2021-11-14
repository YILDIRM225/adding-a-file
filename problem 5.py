#conner martinez
#11/9/2021
#css 225
#problem 5: Use the following chunk of code as a base to produce the image shown below
import turtle

def drawsquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")
wn.exitonclick()
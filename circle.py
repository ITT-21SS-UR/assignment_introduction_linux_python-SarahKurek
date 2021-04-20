# Takes a radius (int) as commandline parameter. 
# Draws something resembling a circle with the given radius using the turtle module. 
# The turtle should alternatively move forward or turn left/right so that it stays at 
# about radius pixels from the center of the screen. 
# Experiment with varying turning angles and movement distances. 
# Do not use the circle() function - that would be too easy.

import turtle
import sys

def read_stdin():
    return sys.stdin



if __name__ == "__main__":
    # turtle.bgcolor("blue")
    # turtle.title("My little turtle program to draw a circle")
    s = turtle.getscreen()
    t = turtle.Turtle()
    t.right(90)
    t.goto(100,100)
    t.home()
    t.penup()
    t.pendown()

    print("Hello")

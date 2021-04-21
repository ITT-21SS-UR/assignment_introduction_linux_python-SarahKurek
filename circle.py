import turtle
import sys
import math

# Takes a radius (int) as commandline parameter.
# Draws something resembling a circle with the given radius using the turtle module.
# The turtle should alternatively move forward or turn left/right so that it stays at
# about radius pixels from the center of the screen.
# Experiment with varying turning angles and movement distances.
# Do not use the circle() function - that would be too easy.


def move_start(radius):
    my_turtle.penup()
    my_turtle.goto(turtle.Vec2D(0, radius))
    my_turtle.pendown()


def draw_circle(radius):
    my_turtle.begin_fill()

    for i in range(0, 360):
        my_turtle.left(1)
        my_turtle.forward(radius * math.pi / 180)
        i += 1

    my_turtle.end_fill()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Please enter exact one paramter!")

    if not sys.argv[1].isdigit():
        sys.exit("Please enter a digit!")

    turtle.bgcolor("orange")
    turtle.title("My little turtle program to draw a circle")
    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    my_turtle.pencolor("blue")
    my_turtle.fillcolor("blue")
    my_turtle.speed("fast")

    radius = int(sys.argv[1])

    move_start(radius)
    draw_circle(radius)

    turtle.done()

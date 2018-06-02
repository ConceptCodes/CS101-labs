# Import turtle graphics library
import turtle

#Import Random Libary
from random import *

# Function to draw a square about the current position
def drawSquareFromCenter(turtle, x):
    turtle.penup()
    turtle.forward(-x / 2)
    turtle.right(90)
    turtle.forward(x / 2)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.penup()
    turtle.forward(x / 2)
    turtle.left(90)
    turtle.forward(x / 2)
    turtle.right(90)

def repeat(turtle, size, count):
    for i in range(count):
        random_color(turtle)
        drawSquareFromCenter(turtle, size)
        turtle.fd(size)
    distance = count * size
    turtle.bk(distance)

def random_color(turtle):
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    turtle.pencolor((r, g, b))

def main():
    width = int(input("Enter your desired width: "))
    screen = turtle.Screen()
    screen.colormode(255)
    bob = turtle.Turtle(
    size =
    repeat(bob,size,width)
main()

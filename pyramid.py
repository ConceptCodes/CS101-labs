# Import turtle graphics library
import turtle

#Import Python Math Libary
from math import *
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

#TODO: Function to draw n squares in a row and go back to origin
def repeat(turtle, size, count):
    for i in range(count):
        random_color(turtle)
        drawSquareFromCenter(turtle, size)
        turtle.fd(size)
    distance = count*size
    turtle.bk(distance)

def random_color(turtle):
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    turtle.pencolor((r,g,b))

def main():
    bottom_row = int(input("Enter a number: "))
    screen = turtle.Screen()
    screen.colormode(255)
    box_size = 30
    bob = turtle.Turtle()
    bob.speed(8)
    
    for i in range(bottom_row):
        current_row = bottom_row - i
        repeat(bob,box_size,current_row)
        bob.lt(90)
        bob.fd(box_size)
        bob.rt(90)
        bob.fd(box_size/2)
        
main()

__author__ = 'dojo'

# Import turtle graphics library
import turtle

from math import *
from random import *

def random_color(turtle):
    screen = turtle.Screen()
    screen.colormode(255)
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    turtle.pencolor((r,g,b))

def drawConstellation(turtle, size, height,radius,star):
    drawStar(turtle,size,height)
    for i in range(star):
        distance = radius
        turtle.fd(distance)
        random_color(turtle)
        drawStar(turtle, size/2, height/2)
        turtle.bk(distance)
        turtle.rt(45)
        


def drawStar(turtle, size, height):
    drawSquareFromCenter(turtle, size)
    distance = size / 2
    turtle.bk(distance)
    turtle.lt(90)
    turtle.bk(distance)
    turtle.rt(90)
    for i in range(4):
        drawIsoTriangle(turtle, size, -height)
        turtle.fd(size)
        turtle.lt(90)
    turtle.fd(distance)
    turtle.lt(90)
    turtle.fd(distance)
    turtle.rt(90)


def drawIsoTriangle(turtle, base, height):
    side = sqrt((base / 2)**2 + height**2)
    angle = degrees(atan2(height, base / 2))
    turtle.pendown()
    turtle.forward(base)
    turtle.left(180 - angle)
    turtle.forward(side)
    turtle.left(angle * 2)
    turtle.forward(side)
    turtle.left(180 - angle)
    turtle.penup()


def drawSquareFromCenter(turtle, x):
    turtle.penup()
    turtle.forward(-x / 2)
    turtle.right(90)
    turtle.forward(x / 2)
    turtle.left(90)
    for i in range(4):
        turtle.pendown()
        turtle.forward(x)
        turtle.left(90)
    turtle.penup()
    turtle.forward(x / 2)
    turtle.left(90)
    turtle.forward(x / 2)
    turtle.right(90)
    
def main():
    bob = turtle.Turtle()
    drawConstellation(turtle,30,40)
    bob.speed(7)

    
main()

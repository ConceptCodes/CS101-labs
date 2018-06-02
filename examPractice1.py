import turtle
from math import *

def drawSquareFromCenter(turtle, x): 
    #making my variables
    move = x / 2

    turtle.penup()
    turtle.forward(-move)
    turtle.right(90)
    turtle.forward(move)
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
    turtle.forward(move)
    turtle.left(90)
    turtle.forward(move)
    turtle.right(90)

def main():
    # get user input
    #size1 = int(input('Enter size for square: '))

    size1 = 50

    # create turtle object
    bob = turtle.Turtle()

    #draw first square by rotating up
    bob.left(45)
    drawSquareFromCenter(bob,size1)

    #move in postion of second square
    bob.right(180)
    distance = size1/2
    bob.forward(distance)
    bob.left(90)
    bob.forward(size1)
    bob.left(90)
    bob.forward(distance)
    bob.right(90)
    
    #draw secong square
    drawSquareFromCenter(bob,size1)

    #go back to origin
    bob.right(90)
    bob.forward(distance)
    bob.right(90)
    bob.forward(size1+distance)
    bob.left(180)

    #go to third square
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)

    #draw third squarw
    drawSquareFromCenter(bob,size1)

    #go to origin
    bob.right(180)
    bob.forward(distance)
    bob.right(90)
    bob.backward(distance)

    #go to last square
    bob.forward(distance+size1)
    bob.right(90)
    bob.forward(distance)
    bob.right(90)

    #draw another square
    drawSquareFromCenter(bob,size1)

    #draw line through middle
    bob.forward(distance+size1)
    bob.left(90)
    bob.forward(distance)
    bob.left(135)
    bob.pendown()
    hypo = sqrt(size1**2 + size1**2)
    bob.forward(hypo*2)
    
    # go back to center
    bob.backward(hypo)

    #draw last square
    drawSquareFromCenter(bob,hypo*2)

main()

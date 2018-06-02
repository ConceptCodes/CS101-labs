# Import turtle graphics library
import turtle
# Import math functions
from math import *
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
# TODO: Right turn movement function
def moveToCenterRightTurn(turtle, x,):
   turtle.pu()
   turtle.fd(x/2)
   turtle.rt(270)
   turtle.fd(x/2)
   turtle.rt(90)
# TODO: Diagonal movement function
def moveToCenterDiagonal(turtle,x,y):
    # TODO: Complete program to call functions to draw pinwheel
    side_a = (x/2)-(y/2)
    side_o = (x/2)+(y/2)
    hyp = sqrt(side_a**2 + side_o**2)
    theta = degrees(cos(side_a/hyp))
    turtle.lt(theta)
    turtle.fd(hyp)
    turtle.rt(theta)
    turtle.rt(90)
def main():
    
    size1 = int(input('Enter size for first square: '))
    size2 = int(input('Enter size for first square: '))
    size3 = int(input('Enter size for first square: '))
    size4 = int(input('Enter size for first square: '))
    
    #Create Turtle Object
    bob = turtle.Turtle()
    
    # Draw first square
    moveToCenterRightTurn(bob,size1)
    drawSquareFromCenter(bob, size1)
    moveToCenterRightTurn(bob,-size1)  
    # Move towards the second sqaure
    bob.rt(90)
    moveToCenterRightTurn(bob,size2)
    # Draw second square
    drawSquareFromCenter(bob,size2)
    #move to third square
    bob.lt(180)
    moveToCenterDiagonal(bob,size2,size3)
    #draw the third sqaure
    drawSquareFromCenter(bob,size3)
    #move towards the last square
    moveToCenterDiagonal(bob,size3,size4)
    #draw the last square  
    drawSquareFromCenter(bob,size4)
main()
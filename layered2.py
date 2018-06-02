__author__ = 'conceptcodes'

import turtle
       
def drawSquareFromCenter(turtle,x):
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

def moveCursor(turtle,x):   
    turtle.left(90)
    turtle.forward(-x)
    turtle.right(90)

def main():
    #get user number
    user_number = int(input("Enter a number: "))
    
    #create turtle
    bob = turtle.Turtle()
    
    #draw first square
    drawSquareFromCenter(bob,user_number)
   
    #increase size
    new_size = user_number * 2
    
    #move cursor down
    moveCursor(bob,new_size - (user_number / 2))

    #draw second square
    drawSquareFromCenter(bob,new_size)

    #increase size
    new_size = user_number * 3

    #move cursor down
    moveCursor(bob, new_size - (user_number / 2))

    #draw third square
    drawSquareFromCenter(bob,new_size)

    #increase size
    new_size = user_number * 4

    #move cursor down
    moveCursor(bob, new_size - (user_number / 2))

    #draw last square
    drawSquareFromCenter(bob,new_size)

main()

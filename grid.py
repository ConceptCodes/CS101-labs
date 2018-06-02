# Import turtle graphics library
import turtle

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

def repeat(turtle,size,count):
    for i in range(count):
        drawSquareFromCenter(turtle,size)
        turtle.fd(size)
        

def main():
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
        
    bob = turtle.Turtle()
    bob.speed(8)
    size = 20
    for i in range(height):
        repeat(bob,size,width)
        bob.bk(width*size)
        bob.rt(90)
        bob.fd(size)
        bob.lt(90)

main()

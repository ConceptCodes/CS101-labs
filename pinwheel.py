import turtle

def drawSquareFromCenter(turtle,x):
    turtle.penup()
    turtle.forward(-x/2)
    turtle.right(90)
    turtle.forward(x/2)
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
    turtle.forward(x/2)
    turtle.left(20)
    turtle.forward(x/2)
    turtle.right(90)

def main():
    #create turtle
    bob = turtle.Turtle()
    #draw graphics
    drawSquareFromCenter(bob,200)

    #press any key to exit
    input()

main()
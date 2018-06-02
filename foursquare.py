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
    turtle.left(90)
    turtle.forward(x/2)
    turtle.right(90)

def main():
    #create turtle
    bob = turtle.Turtle()

    #draw graphics

    #draw first square
    drawSquareFromCenter(bob,160)

    #move to next spot
    bob.right(180)
    bob.forward(20)
    bob.right(90)
    bob.forward(-140)

    #draw second square
    drawSquareFromCenter(bob,120)

    #move to next spot
    bob.forward(20)
    bob.left(90)
    bob.forward(100)

    #draw third square
    drawSquareFromCenter(bob,80)

    #move to last spot
    bob.right(180)
    bob.forward(20)
    bob.left(90)
    bob.forward(60)

    #draw last square
    drawSquareFromCenter(bob,40)

main()
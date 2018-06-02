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

def firstSquare(turtle,x):
    move = x / 2
    turtle.penup()
    turtle.forward(move)
    turtle.left(90)
    turtle.forward(move)
    turtle.right(90)
    turtle.forward(move)
    turtle.left(90)
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


def backToOrigin(turtle,x):
    move = x/2
    turtle.forward(move)
    turtle.left(90)
    turtle.forward(move)

def back2origin(turtle,x):
    turtle.left(135)
    distance = sqrt(x/2*x/2 + x/2*x/2)
    turtle.forward(distance)
    turtle.right(135)
    
def moveToSecondSquare(turtle,x):
    turtle.left(45)
    hypotenuse = sqrt(x/2*x/2 + x/2*x/2)
    turtle.forward(hypotenuse)
    turtle.left(45)

def moveToThirdSquare(turtle,size):
    x,y = turtle.pos()
    destination = (x - (size / 2)), (y - (size / 2))
    turtle.setpos(destination)

def moveToLastSquare(turtle,x,y):
    delta_x = (y / 2) - (-x / 2)
    delta_y = (-y / 2) - (-x / 2)
    distance = sqrt(delta_x**2 + delta_y**2)
    angle = degrees(atan(int(((y/2)+(x/2))/(y/2))))
    turtle.left(angle)
    turtle.forward(distance)
    
def chooseIcon(dave,person):
    screen = turtle.Screen()
    if(person == "rick"):
        image = r"C:\Users\David Ojo\Desktop\Media\Python\CS101\rick.gif"
    if(person == "morty"):
        image = r"C:\Users\David Ojo\Desktop\Media\Python\CS101\morty.gif"
    if(person == "head"):
        image = r"C:\Users\David Ojo\Desktop\Media\Python\CS101\head.gif"
    if(person == "moonman"):
        image = r"C:\Users\David Ojo\Desktop\Media\Python\CS101\moonman.gif"
    screen.addshape(image)
    dave.shape(image)
    
def main():
    #use user input to get the values for the four squares
    size1 = int(input('Enter the number of the first square: '))
    size2 = int(input('Enter the number of the second square: '))
    size3 = int(input('Enter the number of the third square: '))
    size4 = int(input('Enter the number of the fourth square: '))
    
    #create turtle object
    dave = turtle.Turtle()
    dave.pencolor("green")
    dave.speed(4)
    
    ''' [draw graphics] '''

    #chooseIcon(dave, "rick")
    
    #use custom method to draw the first square by heading to the center
    firstSquare(dave,size1)

    #move back to the orgin by the reverse of what put me in the center
    backToOrigin(dave,size1)
    
    #chooseIcon(dave, "moonman")
    
    #move to second square by rotatinng 45 degrees and going the distance of the hypotenuse
    moveToSecondSquare(dave,size2)

    #draw square from center
    drawSquareFromCenter(dave,size2)

    #move back to center by fliping 180 and following the hypotenuse back up to the orgin
    back2origin(dave,size2)
   
    #chooseIcon(dave,"morty")

    #get current coordinates and set your destination to the center of the third square + curent location
    moveToThirdSquare(dave,size3)

    #draw square from center
    drawSquareFromCenter(dave,size3)
    
    #chooseIcon(dave, "head")

    #find the angle that lines up with center of last square and go the distance of the hypoteuse to get there
    moveToLastSquare(dave,size3,size4)

    #draw square from center
    drawSquareFromCenter(dave,size4)
    
main()

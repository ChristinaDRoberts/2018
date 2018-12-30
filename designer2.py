#Christina Roberts
#How to Code 2.0

from turtle import*
from random import randint

designer = Turtle()
designer.penup()
designer.goto(-330,330)

r,g,b, = 0,0,0,
colormode(255)

def choose_color():
    global r, g, b
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    designer.pencolor(r,g,b)
    designer.fillcolor(r,g,b)

    print("Color is: ", r, g, b)

def draw_square():
    designer.begin_fill()
    designer.pendown()                                                      
    for i in range(4):
        designer.forward(30)                                                                   
        designer.right(90)
    designer.penup()
    designer.end_fill()

    print("Sqaure Drawn")

def draw_one_row():
    for i in range(10):
        choose_color()
        draw_square()
        designer.forward(50)

def draw_pattern():
    for i in range(10):
        draw_one_row()
        designer.backward(500)
        designer.right(90)
        designer.forward(50)
        designer.left(90)

draw_pattern()
                     

                                                        

                        
        

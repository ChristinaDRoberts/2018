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

def draw_square(size):
    designer.begin_fill()
    designer.pendown()
    for i in range(4):
        designer.forward(size)
        designer.right(90)
    designer.penup()
    designer.end_fill()

    print("Sqaure Drawn")

def draw_one_row(number, size):
    for i in range(number):
        choose_color()
        draw_square(size)
        designer.forward(size)

def draw_pattern(number,size):
    for i in range(number):
        draw_one_row(number,size)
        designer.backward(size*number)
        designer.right(90)
        designer.forward(size)
        designer.left(90)

draw_pattern(10,25)


    


        

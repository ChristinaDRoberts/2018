#Christina Roberts
#How to code 2.0
from turtle import*

speed(0)
pencolor("pink")
bgcolor("black")

x = 0

penup()
lt(180)
fd(100)
rt(90)
pendown()

while x < 120:

    for i in range (6):
        fd(150)
        rt(62)

    rt(12.25)
    x = x+1

exitonclick()
        
    
    

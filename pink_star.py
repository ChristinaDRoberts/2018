#Christina Roberts
#How to Code 2.0

from turtle import*
#i tried import turtle and it gave me error for color not being
#defined. Look up how come import turtle wont work but from turtle imort* will

color("pink", "magenta")
begin_fill()
while True:
        backward(400)
        right(170)
        if abs(pos())<1:
            break
end_fill()
done()


from turtle import*
color("magenta", "pink")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()

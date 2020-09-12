from turtle import*
from random import randint

bgcolor('black')
x=1
speed(0)
shape('turtle')

while x < 600:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colormode(255)
    pencolor(r , g , b)
    forward(10 + x)
    right(98.99)
    x = x + 1

exitonclick()

# mainloop()
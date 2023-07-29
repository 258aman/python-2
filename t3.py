from turtle import *

pensize(2)
speed('fastest')
bgcolor('yellow')
pencolor('black')
for i in range(6):
    lt(60)
    fd(100)
    for i in range(6):
        lt(60)
        fd(50)
        fillcolor('red')
        begin_fill()
        for i in range(6):
            lt(60)
            fd(25)
        end_fill()
        circle(50, 360, 30)
hideturtle()
mainloop()
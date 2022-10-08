import  turtle

turtle.setup(600,600)
turtle.colormode(255)
turtle.bgcolor(50,0,70)

pen=turtle.Turtle()
pen.pencolor(255,255,0)
pen.pensize(2)
pen.speed(0)

angle=119
side=0
limit=600

def shape(angle,side,limit):
    reverseDirection=200
    pen.forward(side)

    if side% (reverseDirection*2)==0:
        angle=angle+2
        print(str(side))
    elif side%reverseDirection==0:
        angle=angle-2
        print(str(side))

    pen.right(angle)
    side=side+2
    if side<limit:
        shape(angle,side,limit)

shape(angle,side,limit)
turtle.mainloop()
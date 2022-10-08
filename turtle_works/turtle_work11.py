import turtle

turtle.setup(600,600)
turtle.bgcolor('black')

pen=turtle.Turtle()
pen.shape('turtle')
pen.pensize(1)
pen.color('cyan')
pen.speed(1)
pen.up()
pen.goto(30,120)
pen.down()
pen.hideturtle()

c=0
d=0

while True:
    turtle.tracer(6)
    for i in range(4):
        pen.forward(80)
        pen.right(90)
    pen.right(15)
    c+=1
    if c>=24+2:
        pen.forward(60)
        c=0
        d+=1
        if d>=24/2:
            break

turtle.mainloop()
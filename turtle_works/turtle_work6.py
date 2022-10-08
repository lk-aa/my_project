import turtle

turtle.setup(600,600)
turtle.bgcolor('black')
pen=turtle.Turtle()
pen.pensize(1)
pen.speed(0)
pen.hideturtle()
pen.color('deepskyblue','white')
#pen.begin_fill()
for i in range(150):
    pen.forward(i*6)
    pen.left(150)
#pen.end_fill()
turtle.mainloop()
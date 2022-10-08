import turtle

turtle.setup(600,600)
turtle.bgcolor('black')
pen=turtle.Turtle()
pen.pensize(1)
pen.speed(0)
pen.hideturtle()
pen.color('red','deepskyblue')
#pen.begin_fill()
for i in range(360):
    pen.forward(i)
    pen.left(100)
#pen.end_fill()
turtle.mainloop()
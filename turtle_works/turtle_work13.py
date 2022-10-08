import turtle
turtle.setup(600,600)
turtle.bgcolor('blue')
pen=turtle.Turtle()
pen.shape('turtle')
pen.pensize(3)
pen.color('red','yellow')
pen.speed(0)
pen.hideturtle()

pen.begin_fill()
for i in range(240):
    pen.forward(i)
    pen.right(59)
pen.end_fill()

turtle.mainloop()
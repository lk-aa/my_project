import turtle
turtle.setup(600,600)
turtle.bgcolor('slateblue')
pen=turtle.Turtle()
pen.pensize(1)
pen.speed(0)
pen.hideturtle()
pen.color('deepskyblue','white')
pen.begin_fill()
for i in range(240):
    pen.forward(i*2)
    pen.right(200)
pen.end_fill()
turtle.mainloop()
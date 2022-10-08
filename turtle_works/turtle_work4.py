import turtle
turtle.setup(600,600)
turtle.bgcolor('slateblue')

pen=turtle.Turtle()
pen.pensize(2)
pen.speed(0)
pen.color('white','deepskyblue')
pen.begin_fill()
for i in range(360):
    pen.forward(i)
    pen.right(77)
pen.end_fill()
turtle.mainloop()
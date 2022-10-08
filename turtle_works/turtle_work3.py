import turtle
turtle.setup(600,600)
turtle.bgcolor('black')

pen=turtle.Turtle()
pen.pensize(2)
pen.speed(0)
pen.color('salmon','deepskyblue')
for i in range(240):
    pen.forward(i*5)
    pen.right(89)
turtle.mainloop()
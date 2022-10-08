import turtle
turtle.setup(600,600)
turtle.bgcolor('black')
pen=turtle.Turtle()
pen.pensize(1)
pen.speed(0)
pen.hideturtle()
pen.color('limegreen','gold')
for i in range(200):
    pen.forward(i*1.5)
    pen.right(i)
turtle.mainloop()
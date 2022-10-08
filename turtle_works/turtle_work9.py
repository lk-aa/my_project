import turtle
turtle.setup(600,600)
turtle.bgcolor('black')
pen=turtle.Turtle()
pen.pensize(1)
pen.speed(0)
pen.hideturtle()
pen.color('white','gold')
for i in range(200):
    pen.forward(i)
    pen.right(i*90)
turtle.mainloop()

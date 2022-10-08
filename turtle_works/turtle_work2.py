import turtle
turtle.setup(600,600)
turtle.bgcolor('black')

turtle.pensize(2)
turtle.speed(0)
turtle.color('deepskyblue','salmon')
for i in range(240):
    turtle.forward(i*6)
    turtle.right(121)
turtle.mainloop()
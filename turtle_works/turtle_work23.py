import turtle
turtle.speed(0)
turtle.ht()

#画花秆
turtle.goto(0,-200)

#画右边的叶子
turtle.goto(0,-150)
turtle.setheading(20)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.right(30)
turtle.circle(120,60)
turtle.left(120)
turtle.circle(120,60)
turtle.end_fill()

#画左边的叶子
turtle.goto(0,-130)
turtle.setheading(-200)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.right(30)
turtle.circle(120,60)
turtle.left(120)
turtle.circle(120,60)
turtle.end_fill()


# 画花瓣
turtle.goto(0,20)
turtle.setheading(0)
turtle.fillcolor('yellow')
for r in range(20,361,20):
    turtle.begin_fill()
    turtle.circle(40,20)
    turtle.right(120)
    turtle.circle(120,60)
    turtle.left(120)
    turtle.circle(120,60)
    turtle.setheading(r)
    turtle.end_fill()

# 画花瓣中心的花盘
turtle.goto(0,0)
turtle.fillcolor('orange')
turtle.setheading(0)
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

turtle.mainloop()

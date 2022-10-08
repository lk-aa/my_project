import turtle as t
import math

# 画面的布局
t.screensize(1000, 1000, 'white')
t.title("龙猫")
t.hideturtle()
t.speed(5)
# t.begin_fill()
# t.fillcolor("red")


# 头上的右半圆
t.penup()
t.goto(0, 250)
t.pendown()
t.pensize(5)
t.color('black')
t.circle(-250, 25)

# 右耳朵
t.left(90)
t.forward(20)
t.circle(-100, 50)
t.right(90)
t.circle(-100, 50)
t.right(10)
t.forward(20)
t.left(108)

# 头上的右半圆
t.penup()
t.goto(0, 250)
t.pendown()
t.left(25)
t.circle(-250, -25)

# 左耳朵
t.left(75)
t.forward(20)
t.circle(100, 50)
t.left(90)
t.circle(100, 50)
t.left(10)
t.forward(20)

# 左半脸
t.right(55)
t.circle(200, 45)

# 左半身和右半身
t.right(40)
t.circle(186, 220)

# 右半脸
t.right(27)
t.circle(205, 43)

# t.end_fill()
t.right(32)
t.penup()

t.pensize(3)
# 两个眼睛
t.goto(115, 125)
t.pendown()
t.circle(40)

t.penup()
t.goto(-35, 125)
t.pendown()
t.circle(40)

t.begin_fill()
t.fillcolor("black")
t.penup()
t.goto(100, 135)
t.pendown()
t.circle(15)
t.end_fill()

t.begin_fill()
t.fillcolor("black")
t.penup()
t.goto(-50, 135)
t.pendown()
t.circle(15)
t.end_fill()

t.begin_fill()
t.fillcolor("white")
t.penup()
t.goto(100, 135)
t.pendown()
t.circle(5)
t.end_fill()

t.begin_fill()
t.fillcolor("white")
t.penup()
t.goto(-50, 135)
t.pendown()
t.circle(5)
t.end_fill()

# 鼻子
t.begin_fill()
t.fillcolor("grey")
t.penup()
t.goto(-30, 85)
t.pendown()
t.right(65)
t.circle(-80, 50)
t.right(130)
t.circle(-80, 50)
t.end_fill()

# 嘴巴
t.pensize(4)
t.penup()
t.goto(-12, 45)
t.pendown()
t.right(130)
t.circle(-40, 50)

# 肚子

t.pensize(5)
t.color("grey")
t.penup()
t.goto(-175, -40)
t.pendown()
t.left(50)
t.circle(-350, 8)
t.color("white")
t.circle(-350, 10.5)
t.color("grey")
t.circle(-350, 24.5)
t.color("white")
t.circle(-350, 10.5)
t.color("grey")
t.circle(-350, 7.5)

# 左手臂
t.pensize(5)
t.color("green")
t.penup()
t.goto(-135, -10)
t.pendown()
t.right(40)
t.circle(130, 35)
t.circle(20, 120)
t.left(10)
t.circle(130, 35)

# 右手臂
t.penup()
t.goto(90, -5)
t.pendown()
t.left(100)
t.circle(130, 30)
t.circle(20, 120)
t.left(10)
t.circle(130, 35)

# 右胡子
t.pensize(2)
t.color("black")
t.penup()
t.goto(140, 80)
t.pendown()
t.right(35)
t.circle(-200, 30)
t.penup()
t.goto(145, 70)
t.pendown()
t.circle(-150, 30)

# 左胡子
t.penup()
t.goto(-140, 80)
t.pendown()
t.left(190)
t.circle(200, 30)
t.penup()
t.goto(-145, 70)
t.pendown()
t.circle(150, 30)

# 衣服口袋
t.penup()
t.goto(-6, -130)
t.color('red', 'pink')
t.pensize(2)
t.pendown()
t.setheading(150)
t.begin_fill()
t.fd(10)
t.circle(15 * -3.745, 45)
t.circle(15 * -1.431, 165)
t.left(120)
t.circle(15 * -1.431, 165)
t.circle(15 * -3.745, 45)
t.fd(15)
t.end_fill()

# 耳朵的装饰
t.penup()
t.goto(110, 220)
t.begin_fill()
t.setheading(270)
for i in range(4):
    t.pendown()
    t.circle(15, 180)
    t.penup()
    t.setheading(i * 90)
t.end_fill()
t.penup()
t.goto(117, 235)
t.pencolor("yellow")
t.pensize(2)
t.pendown()
t.begin_fill()
t.fillcolor("yellow")
t.circle(7)
t.end_fill()

t.done()

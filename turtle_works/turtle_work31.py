# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:03:32 2022
@author: Margaret Wong
"""

import turtle as t
import random

t.setup(800, 600)
t.colormode(255)
t.bgcolor('lavender')
t.speed(0)
colorlist = ['silver', 'lightgoldenrodyellow', 'floralwhite',
             'slategrey', 'lightsteelblue', 'pink']
colorback = ['lavender', 'lightsteelblue']
randomColor = ['pink', 'lavender', 'lightsteelblue', 'silver',
               'lightgoldenrodyellow', 'floralwhite', 'slategrey']
angle = 60


# 画大星星
def drawFiveStar(x, y, angle, step, color):
    t.penup()
    t.goto(x, y)
    t.left(angle)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for x in range(5):
        t.forward(step)
        t.right(144)
    t.end_fill()


for i in range(50):
    step = random.randint(20, 40)
    x = random.randint(-400, 400)
    y = random.randint(0, 300)
    angle = random.randint(0, 36) * 10
    color = random.choice(colorlist)
    drawFiveStar(x, y, angle, step, color)
t.up()
t.goto(0, 0)
t.pendown()
# 画小星星
for j in range(200):
    back1 = random.choice(colorback)
    t.bgcolor(back1)
    temp1 = random.choice(colorlist)
    t.fillcolor(temp1)
    t.color(temp1)
    t.begin_fill()
    temp2 = random.randint(5, 15)
    li2 = [5, 7, 9]
    temp3 = random.choice(li2)
    for i in range(temp3):
        t.forward(temp2)
        t.left(180 - 180 / temp3)
    t.end_fill()
    t.hideturtle()
    t.penup()
    for k in range(2):
        t.left(random.randint(10, 120))
        t.forward(random.randint(10, 50))
t.up()
t.goto(0, 0)
t.pendown()
t.color('purple')
t.goto(0, 0)
t.down()
t.bgcolor('black')
# 画黑洞
for i in range(600):
    t.color(randomColor[i % 6])
    t.fd(i)
    t.rt(angle + 1)
t.penup()
t.color('white')
t.goto(0, 0)
t.down()
t.done()
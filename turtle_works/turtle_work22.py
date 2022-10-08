#粉红爱心
'''
from turtle import *
color('red', 'pink')
begin_fill()
left(135)
fd(100)
right(180)
circle(50, -180)
left(90)
circle(50, -180)
right(180)
fd(100)
end_fill()
hideturtle()
done()     '''

#红色五角星
'''from turtle import *
setup(400,400)
penup()
goto(-100,50)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(200)
    right(144)
end_fill()
hideturtle()
done()'''

#正方形螺旋线
'''
import turtle
n = 10
for i in range(1,10,1):
    for j in [90,180,-90,0]:
        turtle.seth (j)
        turtle.fd(n)
        n += 5       '''

#城市剪影
'''
import turtle
turtle.setup(800,300)
turtle.penup()
turtle.fd(-350)
turtle.pendown()
def DrawLine(size):
    for angle in [0,90,-90,-90,90]:
        turtle.left(angle)
        turtle.fd(size)
for i in [20,30,40,50,40,30,20]:
    DrawLine(i)
turtle.hideturtle()
turtle.done()     '''

#四阶同心圆
'''
import turtle as t
def DrawCctCircle(n):
    t.penup()
    t.goto(0,-n)
    t.pendown()
    t.circle(n,360)
for i in range(20,100,20):
    DrawCctCircle(i)
t.hideturtle()
t.done()     '''

#钢琴键
'''
import turtle as t
t.setup(500,300)
t.penup()
t.goto(-180,-50)   #将画笔移动到绝对位置(–180,–50)处
t.pendown()    #画笔落下
def Drawrect():
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.left(90)
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.penup()
    t.left(90)
    t.fd(42)
    t.pendown()
for i in range(7):
    Drawrect()
t.penup()
t.goto(-150,0)
t.pendown
def DrawRectBlack():
    t.color('black')
    t.begin_fill()
    t.fd(30)
    t.left(90)
    t.fd(70)
    t.left(90)
    t.fd(30)
    t.left(90)
    t.fd(70)
    t.end_fill()
    t.penup()
    t.left(90)
    t.fd(40)
    t.pendown()
DrawRectBlack()
DrawRectBlack()
t.penup()
t.fd(48)
t.pendown()
DrawRectBlack()
DrawRectBlack()
DrawRectBlack()
t.hideturtle()
t.done()   '''

#叠加等边三角形
'''
import turtle
turtle.pensize(2)    # 设置画笔宽度为2像素
turtle.color('red')
turtle.fd(160)   # 向小海龟当前行进方向前进160像素
turtle.seth(120)
turtle.fd(160)
turtle.seth(-120)
turtle.fd(160)
turtle.penup()
turtle.seth(0)
turtle.fd(80)
turtle.pendown()
turtle.seth(60)
turtle.fd(80)
turtle.seth(180)
turtle.fd(80)
turtle.seth(-60)
turtle.fd(80)
turtle.hideturtle()
turtle.done()   '''

#金色三角形
'''
import turtle as t
t.colormode(255)
t.color(255,215,0)    #设置颜色取值为金色（255,215,0）
t.begin_fill()
for x in range(0,8):      #绘制8条线
    t.forward(200)
    t.left(225)
t.end_fill()
t.hideturtle()
t.done()   '''

#五种多边形
'''
from turtle import *
for i in range(5):
    penup()    #画笔抬起
    goto(-200+100*i,-50)
    pendown()
    circle(40,steps=3+i)    #画某个形状
done()    '''

#绘制树形图
'''
import turtle as t
def tree(length,level):    #树的层次
    if level <= 0:
        return
    t.forward(length)    #前进方向画 length距离
    t.left(45)
    tree(0.6*length,level-1)
    t.right(90)
    tree(0.6*length,level-1)
    t.left(45)
    t.backward(length)
    return
t.pensize(3)
t.color('green')
t.left(90)
tree(100,6)  '''

#花形图
'''
import turtle
for i in range(4):
    turtle.right(90)
    turtle.circle(30,180)   '''

#星形图
'''
import turtle
for i in range(4):
    turtle.circle(-90,90)
    turtle.right(180)
'''

#类斯诺克图
'''
import turtle
#绘制边长为20的圆形
def drawCircle():
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.fd(40)

#绘制n层的如题干中描述的图形
def drawRowCircle(n):
    for j  in range(n,1,-1):
        for i in range(j):
            drawCircle()
        turtle.fd(-j*40-20)
        turtle.right(90)
        turtle.fd(40)
        turtle.left(90)
        turtle.fd(40)
    drawCircle()

#调用函数绘制图形    
drawRowCircle(5)
turtle.hideturtle()
turtle.done()
'''

#领结
'''
from turtle import *
pensize(6)
penup()
goto(-100,-50)
pendown()
fillcolor('red')
begin_fill()
goto(-100,50)
goto(100,-50)
goto(100,50)
goto(-100,-50)
penup()
goto(-10,0)
pendown()
right(90)
circle(10,360)
end_fill()
hideturtle()
done()
'''

#三菱
'''
import turtle

def Draw():
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.left(120)
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.end_fill()

for i in range(3):
    Draw()
turtle.hideturtle()
turtle.done()
'''
#螺旋状正方形
'''
import turtle
d = 0
k = 1
for j in range(10):
   for i in range(4):
        turtle.seth(d)
        d += 91
        turtle.fd(k)
        k += 4
turtle.done()
'''

#嵌套五边形
'''
import turtle
edge=5
d = 0
k = 1
for j in range(10):
    for i in range(edge):
       turtle.fd(k)
       d += 360/edge
       turtle.seth(d)
       k += 3
turtle.done() '''

#八卦图
'''
import turtle as t
t.circle(100)
t.circle(50,180)
t.circle(-50,180)
t.penup()
t.goto(0,140)
t.pendown()
t.circle(10)
t.penup()
t.goto(0,40)
t.pendown()
t.circle(10)
t.done()
'''

#同心圆
import turtle as t


def DrawCctCircle(n):
    t.penup()
    t.goto(0, -n)
    t.pendown()
    t.circle(n)


for i in range(20, 80, 20):
    DrawCctCircle(i)
t.done()





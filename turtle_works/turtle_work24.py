import turtle


# 参数x,y必须要有，这是事件传过来的坐标
# 根据y坐标调整背景颜色y坐标范围（0-255）
def change(x, y):
    rc = int(r.ycor())
    gc = int(g.ycor())
    bc = int(b.ycor())
    turtle.bgcolor(rc, gc, bc)


# 为了保证海龟移动范围，在调节条内，固定x坐标
def rmove(x, y):
    if 0 <= y <= 255:
        r.goto(-200, y)


def gmove(x, y):
    if 0 <= y <= 255:
        g.goto(0, y)


def bmove(x, y):
    if 0 <= y <= 255:
        b.goto(200, y)


# 设置颜色模式取值范围0-255，方便后续设置背景色
turtle.colormode(255)
# 设置海龟图标为logo模式，头部朝上也就是北
turtle.mode("logo")
# 设置海龟调整尺寸模式为user方便后续改变海龟形状
turtle.resizemode(rmode="user")
# 隐藏默认的海龟图标，否则屏幕上会出现四个海龟
turtle.hideturtle()
# 初始化背景颜色
turtle.bgcolor(255 // 2, 255 // 2, 255 // 2)

# 红色海龟对象
r = turtle.Turtle()
# 设置颜色，填充色，尺寸
r.pen(pencolor="red", fillcolor='red', pensize=5, )
# 设置海龟显示形状为海龟图形
r.shape(name="turtle")
# 设置海龟大小
r.turtlesize(3, 3)
# 移动至指定位置
r.penup()
r.goto(-200, 0)
r.pendown()
r.fd(255)
r.bk(255 / 2)
# 绑定海龟拖动事件
r.ondrag(rmove)
# 绑定左键松开后事件
r.onrelease(change)

# 以下是另外两个对象
g = turtle.Turtle()
g.pen(pencolor="green", fillcolor='green', pensize=5, )
g.shape(name="turtle")
g.turtlesize(3, 3)
g.pendown()
g.fd(255)
g.bk(255 / 2)
g.pendown()
g.ondrag(gmove)
g.onrelease(change)

b = turtle.Turtle()
b.pen(pencolor="black", fillcolor='black', pensize=5, )
b.shape(name="turtle")
b.turtlesize(3, 3)
b.penup()
b.goto(200, 0)
b.pendown()
b.fd(255)
b.bk(255 / 2)
b.ondrag(bmove)
b.onrelease(change)

turtle.done()


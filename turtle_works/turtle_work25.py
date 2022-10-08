import turtle


# 帮助我们画出一个按钮
def rbutton(x, y, width=100, height=40, text=""):
    myturtle.color('red', 'black')
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.pendown()
    myturtle.begin_fill()
    for i in range(2):
        myturtle.fd(width)
        myturtle.right(90)
        myturtle.fd(height)
        myturtle.right(90)
    myturtle.end_fill()
    myturtle.penup()
    myturtle.goto(x + 20, (y + y - height) // 2)
    myturtle.pendown()
    myturtle.write(text, align="left", font=('Arial', 8, 'bold'))
    myturtle.penup()
    myturtle.home()
    myturtle.pendown()
    return [(x, x + width), (y - height, y)]


# 绑定画板事件设置画笔尺寸函数
def setpensize(x, y):
    if xrange[0] < x < xrange[1] and yrange[0] < y < yrange[1]:
        size = screen.numinput("画笔尺寸", "请输入画笔尺寸", default=3, minval=3, maxval=15)
        myturtle.pensize(size)
    # 设置完成必须再次把焦点转移到画板，否则按键事件无法触发
    screen.listen()


# 绑定画板按键事件，撤销画笔操作
def cancel():
    myturtle.undo()


# 为了方便大家区分，画笔对象和画板对象，我们分别新建一个画笔和画板对象
# 画板对象
screen = turtle.Screen()
# 画笔对象
myturtle = turtle.Turtle()
# 设置窗口尺寸
screen.setup(800, 600)
# 设置窗口标题
screen.title("简陋的调色板")
# 为了方便设置，设置颜色模式
turtle.colormode(cmode=255)
# 绑定空格键按下事件
screen.onkey(cancel, key='space')
# 按键事件必须开启该监听函数
screen.listen()
# 画出的按钮返回坐标范围
xrange, yrange = rbutton(-350, 250, text="画笔尺寸")
# 利用坐标范围触发画板事件，设置画笔尺寸
screen.onscreenclick(setpensize)
# 设置画笔拖动事件为goto,拖动画笔自动画线
myturtle.ondrag(myturtle.goto)
screen.mainloop()

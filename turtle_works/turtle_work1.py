from turtle import *

setup(600,600,0,190)
bgcolor('blue')

pensize(5)
shape('turtle')
turtlesize(0.5,0.5,2)
speed(5)

color('orangered','gold')
for i in range(56):
    forward(i*10)
    right(90)

mainloop()
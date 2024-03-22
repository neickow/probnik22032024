from turtle import *
tracer(50)
screensize(3000, 3000)
down()
left(90)
n=25
# шаблон выше
x=0
y=0
for i in range(10):
    x+=4
    y+=3
    goto(x*n, y*n)
    x += -4
    y += 10
    goto(x*n , y*n)
    x += 18
    y += -12
    goto(x*n , y*n)
    x += -24
    y += -12
    goto(x*n , y*n)
# шаблон ниже
up()
color('red')
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*n, y*n)
        dot(3)
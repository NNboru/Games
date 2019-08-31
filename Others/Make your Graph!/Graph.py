from time import *
from turtle import *
from math import *
setworldcoordinates(-20,-14,20,14)
shape('turtle')
y1='rohan'
speed(0)
delay(0)
title(y1)
bgcolor('yellow')
setup(1300,800,0,0)
pu()
sety(32)
pd()
rt(90)

for i in range(32):
    dot(5)
    write(str(int(ycor())),align='right',font=('arial',6,''))
    fd(2)
pu()
goto(-44,0)
pd()
lt(90)

for i in range(44):
    dot(5)
    write(str(int(xcor())),align='center',font=('arial',7,''))
    fd(2)
pu()
goto(-44,0)
pd()
pencolor('brown')
width(0)
x= -44.0
j=0
n=0
for i in range(1060):
    try:
        if abs(x)<1:
            x=x+0.01
        else:
            x+=0.1
        a=4    
        y= 5*sin(10*x)
        if abs(y)<200:
            seth(towards(x,y))
            goto(x,y)
            if j==1:
                j=0
                pd()
        else:
            j=1
            pu()
    except (SyntaxError,TypeError):
        print ('Please enter correct syntax.')
        n=1
        bye()
        break
    except :
        pu()
        j=1
if n==0:
    delay(100)
    speed(1)
    lt(16*360)
    
    

from turtle import *
i=9
delay(0)
wd=window_width()
ht=window_height()
setworldcoordinates(-wd,-ht,wd,ht)
setup(1000,680)
title('ROHAN Graphics')
shape('square')
shapesize(1,1,4)
color('grey')
bgcolor('white')
speed(0)
l=['blue','yellow','orange','pink','green','maroon','brown','violet','grey','magenta','white','black','purple','red']
def q(x,y):
    pu()
    goto(x,y)
    pd()
def Clear():
    clear()
def rubber():
    pencolor('white')
    width(5)
def pen():
    color('grey')
    width(5)
def ChangeColor():
    global i
    i=i+1
    if i==14:
        i=0
    color(l[i])
def WidthInc():
    width(width()+1)
def WidthDec():
    width(width()-1)
def disable():
    pu()
def enable():
    pd()
def ChangeColor2():
    global i
    i=i-1
    if i==-1:
        i=13
    color(l[i])
def Fill():
    fill((not fill()))
def Undo():
    undo()
def zoom():
    global wd
    global ht
    setworldcoordinates(-wd-wd/10,-ht-ht/10,wd+wd/10,ht+ht/10)
    wd=wd+wd/10
    ht=ht+ht/10
def zoomOut():
    global wd
    global ht
    setworldcoordinates(-wd+wd/10,-ht+ht/10,wd-wd/10,ht-ht/100)
    wd=wd-wd/10
    ht=ht-ht/10
def backFill():
    bgcolor(l[i])
ondrag(goto)
onscreenclick(q)
onkey(ChangeColor,'Right')
onkey(rubber,'r')
onkey(pen,'p')
onkey(WidthInc,'Up')
onkey(WidthDec,'Down')
onkey(disable,'n')
onkey(enable,'y')
onkey(ChangeColor2,'Left')
onkey(Fill,'f')
onkey(Clear,'c')
onkey(Undo,'u')
onkey(zoom,'z')
onkey(zoomOut,'x')
onkey(backFill,'b')
width(5)
listen()
while 1:
    lt(0)


from math import *                                         					#importing required modules.
from string import *
from re import *
from random import *
from turtle import *
from winsound import Beep
from time import *
def star():
    addshape('star',((6.00,0.00), (1.15,-3.53), (3.00,2.18), (4.85,-3.53), (-0.00,-0.00), (6.00,0.00)))
                                                        						#checking if it is new player.

o=0
while 1<2:          
    name=raw_input('Enter your name : ')
    name=name.strip()
    for i in punctuation :
        if (i in name) or (20<len(name)) or (len(name)<2):
            print('please enter valid name.')
            break            
    else:
        break        

name=name.lower()
q=open('./sn.txt')
q1=q.read()
q.close()
q2=q1.splitlines()
ind= -1
for ii in q2:
    ind=ind+1
    i10=ii.split(':')[0]
    if i10==name:
        naam=0
        naam1=0
        i10=ii.split(':')[1]
        break
else:
    naam=1
    naam1=1
                                                                            					#Introduction to new player.
star()
title('Snake')
delay(0)
speed(0)

if naam==1:
    bgcolor('magenta')
    ht()
    pu()
    sety(200)
    color('purple')
    write(('Snake'+'\n\n\n\n\n'),align='center',font=('forte',70,'bold italic underline'))
    sleep(0.5)
    write(('Welcome - '+name.title()),align='center',font=('forte',30,'underline'))
    sleep(0.5)
    color('darkblue')
    sety(-200)  
    write(('Hope that you would\n like this game!'),align='center',font=('forte',30))
    sleep(5)
    clear() 
    write(('keys -- '+ '\n'*7),align='center',font=('ravie',30,'bold underline'))
    write(('KeyUp  -  Move Up'+ '\n'*8),align='center',font=('arial',20))
    write(('KeyDown  -  Move Down'+ '\n'*7),align='center',font=('arial',20))
    write(('KeyLeft  -  Move Left'+ '\n'*6),align='center',font=('arial',20))
    write(('KeyRight  -  Move Right'+ '\n'*5),align='center',font=('arial',20))
    write(('LeftClick  -  Left Turn'+ '\n'*3),align='center',font=('arial',20))
    write(('RightClick  -  Right Turn'+ '\n'*2),align='center',font=('arial',20))
    write(('s  -  Left Turn'+ '\n'),align='center',font=('arial',20))
    write(('d  -  Right Turn'),align='center',font=('arial',20))
    sety(ycor()-50)
    shape('square')
    shapesize(2)
    color('red')
    delay(4)
    v=1
    def rn(x,y):
        global v
        v=0
    onscreenclick(rn)
    for i in range(3600):
        if v==1:
            lt(1)
    del rn,v,q
    clearscreen()
o=0
strg=''
j1=0

                                                                  		      #level 3
def l2():    
    global j1
    global strg
    setup(choice(range(640,1250)),choice(range(620,720)))
    q=0
    a=0

    i1=0
    i2=0
    i3=0
    d=0
    u=0
    f=0
    z=0
    b=0
    e=0
    n=0
    m=1    
    k=5
    g=0 
    c=0.1
    e1=time()+250
    delay(0)
    ht()
    bgcolor('magenta')
    r=Turtle()
    s=Turtle()
    P=Turtle()    
    p=Turtle()
    P.shape('turtle')
    speed(10)
    r.speed(0)
    p.speed(0)
    s.speed(0)
    p.ht()
    P.ht()
    s.shape('triangle')
    s.pu()
    s.ht()
    r.width(10)
    r.pu()
    r.color('brown')
    r.ht()
    r.sety(50)
    r.width(15)
    r.write('Level 3',align='center',font=('forte',150,'underline'))
    sleep(1.5)
    r.sety(0)
    r.width(10)
    r.clear()
    r.color('yellow')
    r.write('Ready',align='center',font=('forte',50))
    sleep(0.8)
    r.clear()
    r.write('Set',align='center',font=('forte',70))
    sleep(0.8)
    r.clear()

    r.write('Go...',align='center',font=('forte',100))
    sleep(0.8)
    r.clear()
    h=window_height()-80
    w=window_width()-25
    r.goto(w/2,-h/2)
    r.fillcolor('red')
    r.fill(True)
    r.sety(-r.ycor())
    r.setx(-r.xcor())
    r.sety(-r.ycor())
    r.setx(-r.xcor())
    r.fill(False)
    r.shape('turtle')
    l=['blue','yellow','orange','pink','green','maroon','brown','black','grey','magenta','white','purple']
    r.lt(90)
    r.shapesize(4)
    r.color('green')
    color('lightblue')
    p.pu()
    p.sety(h/2+5)
    p.setx(-w/2+5)
    p.width(2)
    p3=p.clone()
    p3.write('Level 3',font=('arial',22))
    p.setx(0)
    p.width(10)
    t=s.clone()
    p1=p.clone()
    p1.setx(w/2-80)
    p2=p.clone()
    p2.setx(w/2-200)
    p2.color('red')
    p2.width(15)
    t.ht()
    t.shapesize(2)
    s.st()
    r.st()
    st()
    r.ht()
    t.shape('turtle')
    shape('turtle')
    pu()
    stamp()
    for i in range(30):
        stamp()
                                                        		  				# Defining snake movements.
    def u(x,y): 
        global v
        v=0

    def f0():
        lt(90)
        tilt(-90)
    def f00():
        rt(90)
        tilt(90)
    def f(x,y):
        lt(90)
        tilt(-90)
    def z(x,y):
        rt(90)
        tilt(90)
    def f1(x,y):
        lt(180)
        tilt(-90)
    def f2():
        global strg
        strg=strg+'r'
    def f3():
        global strg
        strg=strg+'o'
    def f4():
        global strg
        strg=strg+'h'
    def f5():
        global strg
        strg=strg+'a'
    def f6():
        global strg
        strg=strg+'n'
    def f7():
        seth(90)
        settiltangle(-90)
    def f8():
        seth(270)
        settiltangle(90)
    def f9():
        seth(180)
        settiltangle(180)
    def f10():
        seth(0)
        settiltangle(0)
    def f11():
        global q
        if q==0:
            q=1
        else:
            q=0            
    def f12():
        global strg

        strg=''
    def f13():
        seth(towards(s.pos()))
                                            						#Binding of above functions to keys.
    
    onscreenclick(f)
    onscreenclick(z,3)
    P.onclick(u)    
    onkey(f0,'s')
    onkey(f00,'d')
    onclick(f1,2)
    onkey(f2,'r')
    onkey(f3,'o')
    onkey(f4,'h')
    onkey(f5,'a')
    onkey(f6,'n')
    onkey(f7,'Up')
    onkey(f8,'Down')
    onkey(f9,'Left')
    onkey(f10,'Right')
    onkey(f11,'space')
    onkey(f12,'e')
    onkey(f13,'t')
    listen()    
   
                                                    							 #Main working loop
    while 1<2:
        m=m+1
        x=choice(range(20-w/2,w/2-20,20))
        y=choice(range(20-h/2,h/2-10,20))
        s.color(choice(l))
        s.st()
        s.goto(x,y)
        if d==0:
            g=g+1       
        if g==6:
            d=1
            g=0
            i2=0
            t.color(choice(l))
            a=choice(range(40-w/2,w/2-40,20))
            b=choice(range(40-h/2,h/2-40,20))
            t.goto(a,b)
            t.st()
            e=time()+6       
        while 2<3:
            p1.clear()
            if e1-time() <10:
                p1.color('red')
                p1.width(20)
            p1.write(round(e1-time(),1),align='left',font=('arial',20))
            
            if strg=='rohan':
                j1=j1+1000
                p.undo()
                p.write(j1,align='left',font=('arial',20))
                strg=''
            if q==0:
                tilt(choice(range(-180,180,2)))
                i1=i1+1
                if i1==15:
                    color(choice(l))
                    i1=0
                s.fd(m*1.7)
                if i1<8:
                    s.lt(choice(range(30)))
                else:
                    s.rt(choice(range(30)))
                fd(20)
                shape('turtle')
                bk(20)
                stamp()
                fd(20)
                shape('circle')
                clearstamps(1)
            sleep(c)
            if g==0:
                p2.clear()
                p2.write(round(e-time(),2),align='left',font=('arial',20))
                t.fd(m/2.0)
                if i1<8:
                    t.lt(choice(range(30)))
                else:
                    t.rt(choice(range(30)))
                if time()>e:
                    p2.clear()
                    t.ht()
                    d=0
                    g=1
                elif ((t.xcor()-30)< xcor()< (t.xcor()+30)) and ((t.ycor()-30)< ycor()< (t.ycor()+30)) and i2==0:
                    p2.clear()
                    t.ht()
                    shapesize(2)
                    stamp()
                    shapesize(1)
                    fd(20)
                    d=0
                    j1=j1+k*int(round((e-time())))
                    p.undo()
                    p.write(j1,align='left',font=('arial',20))
                    i2=1
                    g=1
        
            if ((s.xcor()-20)< xcor()< (s.xcor()+20)) and ((s.ycor()-20)< ycor()< (s.ycor()+20)) :
                s.ht()              
                stamp()
                j1=j1+k
                k=k+10
                p.undo()
                p.write(j1,align='left',font=('arial',20))
                if m>15:
                    p3.clear()
                    color('blue')
                    clear()
                    r.clear()       
                    bgcolor('yellow')      
                    home()
                    ht()
                    t.ht()
                    r.ht()
                    p.clear()
                    p1.clear()
                    write('level-3  Complete\n\n\n\n',align='center',font=('forte',40,'underline'))
                    sleep(0.5)
                    i3=int(round(e1-time()))*4
                    j1=j1+i3
                    write(('Time Bonus :  '+str(i3)+'.'+'\n\n'),align='center',font=('forte',30))
                    sleep(0.2)
                    write(('Level Score :  '+str(j1)+'.' +'\n'),align='center',font=('forte',30))
                    sleep(2)
                    clear()
                    write('\n\n\n')
                    bgcolor('magenta')
                    for i in range(10,30):
                        color(('#12'+str(i)+'56789'))
                        if i==29:
                                color('darkgreen')
                        write(('Congratulations.\n\n'),align='center',font=('forte',i+40))
                        sleep(0.05)
                        if i<29:
                                 undo()                   
                    sleep(0.2)
                    write(('You have completed all the levels.'),align='center',font=('forte',40))
                    sleep(5)
                    clear()
                    write(('You Win the Game!'),align='center',font=('forte',i+40))
                    n=1                    
                break
            
            if abs(t.xcor())>=w/2-20:
                if t.xcor()<0:
                    t.setx(-t.xcor()-20)

                else:
                    t.setx(-t.xcor()+20)            
            if abs(t.ycor())>=h/2-20:
                if t.ycor()<0:
                    t.sety(-t.ycor()-20)
                else:
                    t.sety(-t.ycor()+20)
            
            if abs(s.xcor())>=w/2-20:
                if s.xcor()<0:
                    s.setx(-s.xcor()-20)
                else:
                    s.setx(-s.xcor()+20)            
            if abs(s.ycor())>=h/2-20:
                if s.ycor()<0:
                    s.sety(-s.ycor()-20)
                else:
                    s.sety(-s.ycor()+20)

            if abs(xcor())>=w/2-20:
                if xcor()<0:
                    setx(-xcor()-20)
                else:
                    setx(-xcor()+20)            
            if abs(ycor())>=h/2-20:
                if ycor()<0:
                    sety(-ycor()-20)
                else:
                    sety(-ycor()+20) 
            if (e1<time() and n!=1) or strg=='han':
                p3.clear()
                p1.clear()
                color('orange')
                for i in range(20,60,4):
                    dot(i)
                clear()
                p2.clear()
                r.clear()
                p.clear()
                bgcolor('brown')      
                home()
                t.ht()
                ht()
                r.ht()
                p.ht()
                s.ht()
                write('oops!  Time Up!!',align='center',font=('forte',50))
                sleep(2)
                clear()
                color('red')

                write('GAME OVER',align='center',font=('forte',70))
                n=1
                break
            
            if d==1:
                t.rt(10)
        if n==1:
            break
   
                                                        		     #Level-1
def l1():
    global v
    global q
    global o
    global j2
    global strg
    v=1
    a=0
    q=0
    d=0
    f=0
    z=0
    b=0
    e=0
    n=0
    m=1    
    j2=0
    k=5
    g=0
    delay(0)
    bgcolor('blue')
    r=Turtle()
    s=Turtle()
    P=Turtle()
    P.shape('turtle')
    p=Turtle()
    r.speed(0)
    p.ht()
    P.ht()
    s.shape('triangle')
    s.pu()
    s.ht()
    r.width(10)
    r.pu()
    r.color('brown')
    r.ht()
    r.sety(50)
    r.width(15)
    r.write('Level 1',align='center',font=('forte',150,'underline'))
    sleep(1.5)

    r.sety(0)
    r.width(10)
    r.clear()
    r.color('yellow')
    r.write('Ready',align='center',font=('forte',50))
    sleep(0.8)
    r.clear()
    r.write('Set',align='center',font=('forte',70))
    sleep(0.8)
    r.clear()
    r.write('Go...',align='center',font=('forte',100))
    sleep(0.8)
    r.clear()
    h=window_height()-80
    w=window_width()-25
    r.goto(w/2,-h/2)
    r.pd()
    r.st()
    r.fillcolor('#500100101')
    r.fill(True)
    r.sety(-r.ycor())
    r.setx(-r.xcor())
    r.sety(-r.ycor())
    r.setx(-r.xcor())
    r.pu()
    r.fill(False)
    r.shape('turtle')
    l=['blue','yellow','orange','pink','red','green','maroon','brown','black','grey','magenta','white']
    r.lt(90)
    r.shapesize(4)
    r.color('green')
    color('orange')
    p.pu()
    p.sety(h/2+5)
    p.setx(-w/2+5)
    p.width(2)
    p3=p.clone()
    p3.write('Level 1',font=('arial',22))
    p.setx(0)
    p.width(1) 
    p.width(10)
    t=s.clone()
    p1=p.clone()
    p1.setx(w/2-30)
    t.ht()
    t.shapesize(2)
    r.ht()
    s.st()
    s.speed(0)
    t.shape('square')

    shape('circle')
    pu()
    stamp()
    stamp()
    strg=''
                                                              						 # Defining snake movements.
    def u(x,y):
        global v
        v=0
    def f0():
        lt(90)
    def f00():
        rt(90)
    def f(x,y):
        lt(90)
    def z(x,y):
        rt(90)
    def f1(x,y):
        lt(180)
    def f2():
        global strg
        strg=strg+'r'
    def f3():
        global strg
        strg=strg+'o'
    def f4():
        global strg
        strg=strg+'h'
    def f5():
        global strg
        strg=strg+'a'
    def f6():
        global strg
        strg=strg+'n'
    def f7():
        seth(90)
        if o==1:
            settiltangle(-90)
    def f8():
        seth(270)
        if o==1:
            settiltangle(90)
    def f9():
        seth(180)
        if o==1:
            settiltangle(180)
    def f10():
        seth(0)
        if o==1:
            settiltangle(0)

    def f11():
        global q
        if q==0:
            q=1
        else:
            q=0            
    def f12():
        global strg
        strg=''
    def f13():
        seth(towards(x,y))
    def f14():
        clearscreen()
        l2()
                                                						#Binding of above functions to keys.
    onscreenclick(f)
    onscreenclick(z,3)
    P.onclick(u)    
    onkey(f0,'s')
    onkey(f00,'d')
    onclick(f1,2)
    onkey(f2,'r')
    onkey(f3,'o')
    onkey(f4,'h')
    onkey(f5,'a')
    onkey(f6,'n')
    onkey(f7,'Up')
    onkey(f8,'Down')
    onkey(f9,'Left')
    onkey(f10,'Right')
    onkey(f11,'space')
    onkey(f12,'e')
    onkey(f13,'t')
    onkey(f14,'3')
    listen()
   
                                                        							 #Main working loop
    while 1<2:       
        x=choice(range(25-w/2,w/2-25,10))
        y=choice(range(20-h/2,h/2-10,20))
        s.color(choice(l))
        s.st()
        s.goto(x,y)
        if d==0:
            g=g+1       
        if g==7:
            d=1
            g=0
            t.color(choice(l))
            a=choice(range(40-w/2,w/2-40,10))

            b=choice(range(35-h/2,h/2-25,20))
            t.goto(a,b)
            t.st()
            e=time()+6
        listen()        
        while 2<3:            
            if strg=='rohan':
                j2=j2+1000
                p.undo()
                p.write(j2,align='left',font=('arial',20))
                strg=''
            if q==0:
                fd(20)
                stamp()
                clearstamps(1)
            sleep(0.2)
            if g==0:
                p1.clear()
                p1.write(round(e-time(),2),align='left',font=('arial',20))
                if time()>e:
                    p1.clear()
                    t.ht()
                    d=0
                    g=1
                elif ((a-30)< xcor()< (a+30)) and ((b-30)< ycor()< (b+30)):
                    t.ht()
                    d=0
                    j2=j2+k*int(round((e-time())))
                    p1.clear()
                    p.clear()
                    p.write(j2,align='left',font=('arial',20))
                    g=1
        
            if ((x-20)< xcor()<(x+20)) and ((y-20)< ycor()< (y+20)) :
                s.ht()
                stamp()
                m=m+1
                j2=j2+k
                p.clear()
                p.write(j2,align='left',font=('arial',20))
                if m>=10:
                    p3.clear()
                    color('blue')
                    speed(0)
                    clear()
                    r.clear()       
                    bgcolor('yellow')      
                    home()
                    ht()
                    r.ht()

                    p.clear()
                    write('level-1 Complete\n',align='center',font=('forte',40))
                    sleep(0.5)
                    write(('Your Score is '+str(j2)+'.'),align='center',font=('forte',30))                    
                    sleep(2)
                    clear()
                    n=1
                    o=1
                break
            
            if abs(xcor())>=w/2-15 or abs(ycor())>=h/2-10:
                p3.clear()
                t.ht()
                ht()
                s.ht()
                color('red')
                for i in range(20,60,4):
                    dot(i)
                p1.clear()
                clear()
                r.clear()
                p.clear()
                home()
                bgcolor('brown')                                      
                write('GAME OVER',align='center',font=('forte',70))                
                n=1
                    
                P.st()
                P.pu()
                P.rt(90)
                P.fd(50)
                P.color('blue')
                P.write(('Total score is '+str(j2)+'.'),align='center',font=('forte',30))
                P.fd(50)
                P.write('Play again! ',align='center',font=('forte',30))   
                P.seth(0)
                P.fd(115)
                P.seth(90)
                P.fd(20)  
                P.color('green')
                delay(10)
                for i in range (360):
                        if v==1:
                            P.lt(1)
                for i in range (360):
                        if v==1:
                           P.rt(1)
                if v==1:
                        exit ()
                else:

                        clearscreen()            
                break
            s.lt(10)
            if d==1:
                t.rt(10)
        if n==1:
            break


                                                                    		      #level 2
while 1<2:
    while o==0:  
        l1()      						# - Starting excution of function - l1 containing Level 1.
    v=1
    a=0
    q=0
    d=0
    f=0
    z=0
    b=0
    e=0
    n=0
    m=1    
    j=0
    j1=0
    k=5
    g=0 
    c=0.2
    delay(0)
    bgcolor('blue')
    r=Turtle()
    s=Turtle()
    P=Turtle()
    P.shape('turtle')
    p=Turtle()
    r.speed(0)
    p.ht()
    P.ht()
    s.shape('star')
    s.shapesize(2)
    s.pu()
    s.ht()
    r.width(10)
    r.pu()
    r.color('brown')
    r.ht()
    r.sety(50)

    r.width(15)
    r.write('Level 2',align='center',font=('forte',150))

    sleep(1.5)
    r.sety(0)
    r.width(10)
    r.clear()
    r.color('yellow')  
    r.write('Ready',align='center',font=('forte',50))
    sleep(0.8)
    r.clear()
    r.write('Set',align='center',font=('forte',70))
    sleep(0.8)
    r.clear()
    r.write('Go...',align='center',font=('forte',100))
    sleep(0.8)
    r.clear()
    h=window_height()-80
    w=window_width()-25
    r.goto(w/2,-h/2)
    r.pd()
    r.st()
    r.fillcolor('#500100101')
    r.fill(True)
    r.sety(-r.ycor())
    r.setx(-r.xcor())
    r.sety(-r.ycor())
    r.setx(-r.xcor())
    r.pu()
    r.fill(False)
    r.shape('turtle')
    l=['blue','yellow','orange','pink','red','green','maroon','brown','black','grey','magenta','white']
    r.lt(90)
    r.shapesize(4)
    r.color('green')
    color('orange')
    p.pu()
    p.sety(h/2+5)
    p.setx(-w/2+5)
    p.width(2)
    p3=p.clone()
    p3.write('Level 2',font=('arial',22))
    p.setx(0)
    p.width(1) 
    p.width(10)
    t=s.clone()
    p1=p.clone()
    p1.setx(w/2-30)
    t.ht()
    t.shapesize(2)
    s.st()
    r.ht()
    s.speed(0)

    t.shape('turtle')
    shape('turtle')
    pu()
    stamp()
    for i in range(10):
        stamp()
                                                        						# Defining snake movements.
    def u(x,y):
        global v
        v=0
    def f0():
        lt(90)
    def f00():
        rt(90)
    def f(x,y):
        lt(90)
    def z(x,y):
        rt(90)
    def f1(x,y):
        lt(180)
    def f2():
        global strg
        strg=strg+'r'
    def f3():
        global strg
        strg=strg+'o'
    def f4():
        global strg
        strg=strg+'h'
    def f5():
        global strg
        strg=strg+'a'
    def f6():
        global strg
        strg=strg+'n'
    def f7():
        seth(90)
    def f8():
        seth(270)
    def f9():
        seth(180)
    def f10():
        seth(0)
    def f11():
        global q
        if q==0:
            q=1
        else:
            q=0            
    def f12():

        global strg
        strg=''
    def f13():
        seth(towards(x,y))
    def f14():
        clearscreen()
        l2()
                                           						 #Binding of above functions to keys.
    onscreenclick(f)
    onscreenclick(z,3)
    P.onclick(u)    
    onkey(f0,'s')
    onkey(f00,'d')
    onclick(f1,2)
    onkey(f2,'r')
    onkey(f3,'o')
    onkey(f4,'h')
    onkey(f5,'a')
    onkey(f6,'n')
    onkey(f7,'Up')
    onkey(f8,'Down')
    onkey(f9,'Left')
    onkey(f10,'Right')
    onkey(f11,'space')
    onkey(f12,'e')
    onkey(f13,'t')
    onkey(f14,'3')
    listen()
   
                                                    							#Main working loop
    while 1<2:       
        x=choice(range(25-w/2,w/2-25,10))
        y=choice(range(20-h/2,h/2-10,20))
        s.color(choice(l))
        s.st()
        s.goto(x,y)
        if d==0:
            g=g+1       
        if g==6:
            d=1
            g=0
            t.color(choice(l))
            a=choice(range(40-w/2,w/2-40,10))
            b=choice(range(35-h/2,h/2-25,20))
            t.goto(a,b)
            t.st()
            e=time()+6       
        while 2<3:            
            if strg=='rohan':
                j=j+1000

                p.undo()
                p.write(j,align='left',font=('arial',20))
                strg=''
            if q==0:
                fd(20)
                stamp()
                clearstamps(1)
            sleep(c)
            if g==0:
                p1.clear()
                p1.write(round(e-time(),2),align='left',font=('arial',20))
                if time()>e:
                    p1.clear()
                    t.ht()
                    d=0
                    g=1
                elif ((a-30)< xcor()< (a+30)) and ((b-30)< ycor()< (b+30)):
                    t.ht()
                    d=0
                    j=j+k*int(round((e-time())))
                    p1.clear()
                    p.clear()
                    p.write(j,align='left',font=('arial',20))
                    g=1
        
            if ((x-20)< xcor()< (x+20)) and ((y-20)< ycor()< (y+20)) :
                s.ht()
                stamp()
                m=m+1               
                if m==4:
                    if c<=0.02:
                        c=c-0.004
                        k=k+40
                    elif c<=0.04:                    
                        c=c-0.01
                        k=k+20
                    else:
                        c=c-0.054
                        k=k+10
                    m=0
                j=j+k
                p.clear()
                p.write(j,align='left',font=('arial',20))
                if c<=0.015:
                    p1.clear()
                    p3.clear()
                    color('blue')
                    speed(0)
                    clear()
                    r.clear()       

                    bgcolor('yellow')      
                    home()
                    ht()
                    r.ht()
                    t.ht()
                    p.clear()
                    write('level-2 Complete\n\n',align='center',font=('forte',40))
                    sleep(0.5)
                    write(('Level Score is '+str(j)+'. \n'),align='center',font=('forte',30))
                    sleep(2)
                    write(('Total Score is '+str(j+j2)+'.'),align='center',font=('forte',30))
                    sleep(2)
                    clear()
                    l2()           					# - Starting excution of function - l2 containing Level 3.
                    n=1
                break
            
            if abs(xcor())>=w/2-15 or abs(ycor())>=h/2-10:
                p3.clear()
                p1.clear()
                t.ht()
                ht()
                s.ht()
                color('red')
                for i in range(20,60,4):
                    dot(i)
                clear()
                r.clear()
                p.clear()
                home()
                bgcolor('brown')                                      
                write('GAME OVER',align='center',font=('forte',70))                
                n=1
                break
            s.lt(10)
            if d==1:
                t.rt(10)
        if n==1:
            break
                        					#To display score and to ask if the player wants to play again.
    h=window_height()-40
    w=window_width()-40
    r.shapesize(0.5)
    r.goto(w/2,-h/2)
    r.seth(90)
    r.speed(5)
    shape('star')
    shapesize(1)
    goto(-w/2,h/2)
    seth(270)

    speed(5)
    P.st()
    P.pu()
    P.rt(90)
    P.fd(50)
    P.color('blue')
    j3=j+j1+j2
    P.write(('Total score is '+str(j3)+'.'),align='center',font=('forte',30))
							# Comparision with previous score for old player.
    if naam==0:      					
        P.fd(50)
        if int(i10)<j3:  
            P.write(('You have made a New Highscore!'),align='center',font=('forte',30))
            q2[ind] = (name + ':' + str(j3))
            q3='\n'.join(q2)+'\n'
            q1=open('./sn.txt','w')
            q1.write(q3)
            q1.close()
            i10=str(j3)
        else:
            P.write(('you have scored '+str(int(i10)-j3)+' points less than previous - ' + i10 +'.') , align = 'center',                          font = ('forte',20))
        fd(50)

    if naam == 1:   								# Saving score of new player.
        q=open('./sn.txt','a')
        q.write((name + ':' + str(j3) +'\n'))
        naam=0
        i10=str(j3)
        q.close()

    P.fd(50)
    P.write('Play again! ',align='center',font=('forte',30))    
    P.seth(0)
    P.fd(115)
    P.seth(90)
    P.fd(20)  
    P.color('green')
    delay(2)
    i3=0
    for i in range (360):
        if v==1:
            r.fd(20)
            fd(20)
            if abs(r.xcor())>=w/2 or abs(r.ycor())>=h/2:
                delay(1)
                r.lt(90)
                delay(2)
            if abs(xcor())>=w/2 or abs(ycor())>=h/2:
                delay(1)

                lt(90)
                delay(2)
            r.stamp()
            stamp()
            P.lt(1)
            i3=i3+1
            if i3>h/20 or i3>w/20:
                clearstamps(1)
                r.clearstamps(1)
    i3=0
    for i in range (360):
        if v==1:
            i3=i3+1
            r.speed(0)
            r.fd(20)
            if abs(r.xcor())>=w/2 or abs(r.ycor())>=h/2:
                r.lt(90)
            r.stamp()
            P.rt(1)
            if i3%2==0:
                fd(20)
                clearstamps(3)
            if abs(xcor())>=w/2 or abs(ycor())>=h/2:
                speed(0)
                lt(90)
                speed(8)
            if i3<h/20:
                stamp()  
              
    if v==1:
        break
    else:
        o=0
        clearscreen()


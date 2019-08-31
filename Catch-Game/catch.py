import pygame as p
from pygame.locals import *
from sys import exit
from random import choice,randrange,random,sample
from  pygame.math import Vector2
from math import cos,sin
from time import time,sleep

w,h=1366,768
colors=[(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,255,255),(255,0,255),(128,128,128),(128,0,0),(128,128,0),(0,128,0),(128,0,128),(0,128,128),(0,0,128)]
p.init()

clock=p.time.Clock()
r=20
timepassed=0
food=[]
hunter=[]
T=t=time()
wait=0
score=0
generate=8.
pause=0

def ready():
    font1.set_underline(1)
    sur.blit(font1.render("!! CATCHER !!",True,(100,0,0)),(w/4-50,10))
    font1.set_underline(0)
    sur.blit(font.render("ESCAPE : QUIT",True,(100,100,0)),(100,600))
    sur.blit(font.render("CATCH GREENS.",True,(0,255,0)),(100,300))
    sur.blit(font.render("AVOID REDS.",True,(255,0,0)),(100,400))
    p.display.update()
    sur.fill((0,0,255))
    a=1
    while a:
        for e in p.event.get():
            if e.type==2:
                a=0
                if e.key==27:
                    p.quit()
                    exit()
            if e.type==5:
                a=0
    sur.blit(font1.render("! READY !",True,(100,0,0)),(w/3-50,h/3+50))
    p.display.update()
    p.time.delay(500)
    sur.blit(image,(0,0))
    sur.blit(font1.render("!! ------- GO ------- !!",True,(100,0,0)),(w/4-100,h/3+50))
    p.display.update()
    p.time.delay(500)
    
class Obj:
    def __init__(s,centerx,centery,color,angle,speed,random):
        s.color,s.angle,s.speed=color,angle,speed
        s.v =Vector2(cos(angle),sin(angle))
        s.v1=Vector2(centerx,centery)
        s.random=random
        
    def draw(s):
        p.draw.circle(sur,s.color,(int(s.v1.x),int(s.v1.y)),r)        
        v1=s.v1+s.v*r
        p.draw.circle(sur,s.color,(int(v1.x),int(v1.y)),r/3)

    def update(s,t):
        s.v1=s.v1+ s.v*s.speed*t
        s.draw()
        

    def change_angle(s,pos,sign):
        if s.random:            
            ang=choice((-1,1))
        else:
            v1=Vector2(pos[0]-s.v1.x,pos[1]-s.v1.y)
            ang=s.v.angle_to(sign*v1)           
        if ang>0:
            s.v=s.v.rotate(choice(range(-5,20)))
        else:
            s.v=s.v.rotate(choice(range(-20,5)))
    
    def collide(s,pos):
        if s.v1.distance_to(pos)<1.2*r:
            return True
        else:
            return False
        
sur=p.display.set_mode((w,h),FULLSCREEN)
image=p.transform.scale(p.image.load(str(choice(range(1,9)))+'.png'),(w,h)).convert()
sur.fill((0,0,255))

font=p.font.SysFont('forte',60)
font1=p.font.SysFont('hobostdopentype',120)

so1=p.mixer.Sound('back.wav')
so1.set_volume(0.4)
so2=p.mixer.Sound('tu.wav')
so3=p.mixer.Sound('out.wav')
so4=p.mixer.Sound('win.wav')
so4.set_volume(0.2)
ready()
p.mouse.set_visible(0)
so1.play(-1)
while 1:      
    for e in p.event.get():
        if e.type==2:
            if e.key==27:
                font1=p.font.SysFont('hobostdopentype',200)
                font1.set_bold(1)
                font1.set_italic(1)
                a=0
                for i in xrange(15):                   
                        for e in p.event.get():
                            if e.type==5 or e.type==2:
                                a=1
                        if a:
                            break
                        sur.fill(choice(colors))
                        sur.blit(font1.render("! THANKS !",True,(100,0,0)),(40,10))
                        sur.blit(font1.render("!    FOR    !",True,(0,100,0)),(40,h/2-100))
                        sur.blit(font1.render("! PLAYING !",True,(0,0,100)),(30,h-220))
                        p.display.update()
                        sleep(0.2)
                p.quit()
                exit()
            if e.key==98:
                image=p.transform.scale(p.image.load(str(choice(range(1,9)))+'.png'),(w,h)).convert()
            if e.key==99:
                if hunter!=[]:
                    hunter.pop()
            if e.key==32:
                pause = not pause
                if pause:
                    p.mixer.pause()
                else:
                    p.mixer.unpause()
                    
    if not pause:
        sur.blit(image,(0,0))
                
    pos=p.mouse.get_pos()        
    p.draw.circle(sur,(0,255,0),pos,r)   #draw mouse
    p.draw.circle(sur,(255,0,0),pos,int(r*0.6))
    p.draw.circle(sur,(0,0,255),pos,int(r*0.2))
    
 
    if not pause:
        t1=time()
        if t1>t+wait:
            wait=choice(range(1,10))/generate
            t=t1
            if random()>0.2:
                food.append(Obj(randrange(w/5,w-w/5),randrange(h/5,h-h/5),(0,255,0),randrange(-180,180),randrange(250,350),False))
            else:
                if choice((1,0)):
                    hunter.append(Obj(randrange(-2*r,w+2*r),choice((-2*r,h+2*r)),(255,0,0),randrange(-180,180),randrange(250,350),choice((1,1,1,1,False))))
                else:
                    hunter.append(Obj(choice((-2*r,w+2*r)),randrange(-2*r,h+2*r),(255,0,0),randrange(-180,180),randrange(250,350),choice((1,1,1,1,False))))
    
        for fo in food:
            fo.update(timepassed)
            fo.change_angle(pos,-1)
            if fo.collide(pos):
                so2.play()
                score+=1
                food.remove(fo)
            if  not(-100<fo.v1.x<w+100 and -100<fo.v1.y<h+100):
                food.remove(fo)
        for hu in hunter:
            hu.update(timepassed)
            hu.change_angle(pos,1)
            if hu.random:
                if not (-8*r<hu.v1.x<w+8*r and -8*r<hu.v1.y<h+8*r):
                    angle_v=Vector2(w/2,h/2)-hu.v1
                    hu.v=angle_v.normalize()
            if hu.collide(pos):
                p.display.update()
                so1.stop()
                so3.play()
                sleep(1)

                open('h.txt','a')
                hsfile=open('h.txt','r')
                highscore=hsfile.read()
                if highscore=='':
                    showhs=0
                    hsfile=open('h.txt','w')
                    hsfile.write(str(int(score*2+t1-T)))
                else:
                    showhs=1
                    highscore=int(highscore)                   
                if score*2+t1-T > highscore:
                    so4.play()
                    str1='NEW HIGHSCORE : '
                    str2='PREVIOUS SCORE : '
                    hsfile=open('h.txt','w')
                    hsfile.write(str(int(score*2+t1-T)))
                else:
                    str1="YOUR SCORE : "
                    str2="HIGHSCORE   : "
                
                p.mouse.set_visible(1)
                p.mouse.set_cursor(*p.cursors.diamond)
                col=sample(colors,4)
                sur.fill(col[0])
                font1.set_bold(1)
                sur.blit(font1.render("  GAME OVER ! ",True,col[1]),(w/8,20))
                font1.set_bold(0)
                c=col[2]
                sur.blit(font1.render("CAUGHT : "+str(score),True,c),(50,160))
                sur.blit(font1.render("TIME      : "+str(int(t1-T)),True,c),(50,280))
                sur.blit(font1.render(str1+str(int(score*2+t1-T)),True,c),(50,400))
                if showhs:
                    sur.blit(font1.render(str2+str(int(highscore)),True,c),(50,520))
                re=font.render(" RESTART ",True,c)
                ex=font.render(" EXIT ",True,c)
                re1=p.draw.rect(sur,(30,40,50),(w/8,660,re.get_width(),re.get_height()))
                ex1=p.draw.rect(sur,(30,40,50),(w/8+re.get_width()+100,660,ex.get_width(),ex.get_height()))
                sur.blit(re,(w/8,660))
                sur.blit(ex,(w/8+re.get_width()+100,660))
                sur.blit(font.render("NN",True,col[3]),(w-110,h-font.get_height()))
                p.display.update()
                a=1
                a1=0
                a2=0
                while a:
                    for e in p.event.get():
                        if e.type==2:
                            if e.key==27:
                                a1=1
                            if e.key==32:
                                a2=1
                        if e.type==5 or a1 or a2:
                            if re1.collidepoint(p.mouse.get_pos()) or a2:
                                a=0
                                food=[]
                                hunter=[]
                                T=time()
                                score=0
                                sur.fill((0,0,255))
                                ready()
                                p.mouse.set_visible(0)
                                so1.play(-1)
                            if ex1.collidepoint(p.mouse.get_pos()) or a1:
                                font1=p.font.SysFont('hobostdopentype',200)
                                font1.set_bold(1)
                                font1.set_italic(1)
                                a2=0
                                for i in range(15):
                                    for e in p.event.get():
                                        if e.type==5 or e.type==2:
                                            a2=1
                                    if a2:
                                        break
                                    sur.fill(choice(colors))
                                    sur.blit(font1.render("! THANKS !",True,(100,0,0)),(40,10))
                                    sur.blit(font1.render("!    FOR    !",True,(0,100,0)),(40,h/2-100))
                                    sur.blit(font1.render("! PLAYING !",True,(0,0,100)),(30,h-220))
                                    p.display.update()
                                    sleep(0.2)
                                p.quit()
                                exit()
        
    text=font1.render(str(score)+"   "+str(int(t1-T)),True,(100,0,200))
    sur.blit(text,(int(0.7*w),20))
    
    timepassed=clock.tick(120)/1000.
    p.display.update()

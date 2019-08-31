import pygame as p
from pygame.locals import *
from sys import exit

p.init()
sur=p.display.set_mode((1366,768),FULLSCREEN)

sur.fill((255,255,0))

while 1:
    for e in p.event.get():
        pass
    key=p.key.get_pressed()
    mou=p.mouse.get_pressed()
    
    if key[27]:
        p.quit()
        exit()

    if key[32]:
        sur.fill((255,255,0))

    if mou[0]:
        if not down:
            sur1=sur.copy()
            start=p.mouse.get_pos()
            down=1
        else:
            if draw:
                sur.blit(sur1,(0,0))
            draw=1
            end=p.mouse.get_pos()
            p.draw.line(sur,(0,255,255),start,end,5)
    else:
        draw=down=0
                
    p.display.update()






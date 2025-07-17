import pygame
import sys
import math
import random 
pygame.init()
screen=pygame.display.set_mode((288,512))
player=pygame.Rect((50,216),(32,32))
playerimage=pygame.Surface((32,32))
points=0
realpoint=0
myfont = pygame.font.SysFont('Comic Sans MS', 30)


toppipe_y=random.randint(0,300)
bottompipe_y=362-toppipe_y
toppipe=pygame.Rect((288,0),(40,toppipe_y))
bottompipe=pygame.Rect((288,512-bottompipe_y),(40,bottompipe_y))
pointbox=pygame.Rect((288,0),(1,512))
overtext=pygame.Rect((15,200),(250,80))
gameover=pygame.image.load('gameover.png')
gameover=pygame.transform.scale(gameover,(250,80))
topimage=pygame.Surface((40,toppipe_y))
bottomimage=pygame.Surface((40,bottompipe_y))
bottomimage.fill((0,200,0))
topimage.fill((0,200,0))


clock=pygame.time.Clock()
bird=pygame.image.load('bird.png')
bird=pygame.transform.scale(bird,(32,32))
#real gravity
#g=9.8
#game gravity
g=14
dt=0.1
v=0
while True:
    clock.tick(30)
    screen.fill((135,206,235))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                #normal jump
                #v=-13
                #game jump
                v=-17
    toppipe.move_ip(-5,0)
    bottompipe.move_ip(-5,0)
    pointbox.move_ip(-5,0)
    if toppipe.x<-50:
        toppipe_y=random.randint(0,300)
        bottompipe_y=362-toppipe_y
        toppipe=pygame.Rect((288,0),(40,toppipe_y))
        bottompipe=pygame.Rect((288,512-bottompipe_y),(40,bottompipe_y))
        pointbox=pygame.Rect((288,0),(1,512))
        topimage=pygame.Surface((40,toppipe_y))
        bottomimage=pygame.Surface((40,bottompipe_y))
        bottomimage.fill((0,200,0))
        topimage.fill((0,200,0))
    if player.colliderect(pointbox):
        points=points+1
    realpoint=round(points/6)
    textsurface = myfont.render(str(realpoint), False, (255, 50, 30))
    screen.blit(textsurface,(0,0))
    if player.colliderect(toppipe) or player.colliderect(bottompipe) or player.y>480 or player.y<0:
        print("GAME OVER!")
        bird=pygame.transform.scale(bird,(90,90))
        screen.blit(bird,(110, 166))
        screen.blit(gameover,overtext)
        pygame.display.update()
        quit()
    v=v+g*dt
    player.move_ip(0,v)
    #print(v)

    screen.blit(topimage,toppipe)
    screen.blit(bottomimage,bottompipe)
    screen.blit(bird,player.topleft)
    pygame.display.update()

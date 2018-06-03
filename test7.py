#coding=uft-8
import pygame


pygame.init()

X_SCREENSIZE=800
Y_SCREENSIZE=600
Tick = 60

ourScreen=pygame.display.set_mode((X_SCREENSIZE, Y_SCREENSIZE))
pygame.display.set_caption("파이게임")
finish = False;
color3=(0,0,0)

img = pygame.image.load("zzang.png")

def myimg(x, y):
    ourScreen.blit(img, (x, y))

x=X_SCREENSIZE*0.5
y=Y_SCREENSIZE*0.5

#clock = pygame.time.Clock()

while not finish:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            finish = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE : finish = True
            elif e.key == pygame.K_UP   : y-=Tick
            elif e.key == pygame.K_DOWN : y+=Tick
            elif e.key == pygame.K_LEFT : x-=Tick
            elif e.key == pygame.K_RIGHT: x+=Tick
        
        if y < 0: y=0
        if y > Y_SCREENSIZE: y=Y_SCREENSIZE
        if x < 0: x=0
        if x > X_SCREENSIZE: x=X_SCREENSIZE

        ourScreen.fill(color3)
        myimg(x, y)
   
        
        pygame.display.update()

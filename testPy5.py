import pygame


pygame.init()

X_SCREENSIZE=400
Y_SCREENSIZE=300
X_RECTSIZE=60
Y_RECTSIZE=60
Tick = 60

ourScreen=pygame.display.set_mode((X_SCREENSIZE, Y_SCREENSIZE))
pygame.display.set_caption("파이게임")
finish = False;


color1 = (0,0,255)
color2 = (255,0,0)
color3 = (0,0,0)
color = color1

# 좌표 
x=30
y=30

# 초당 프레임 
#clock = pygame.time.Clock()

while not finish:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            finish = True
            
        #pygame.draw.rect(ourScreen, (0, 0, 255), pygame.Rect(100,100,60,60))
        
        #if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
        #    if color==color1:
        #       color=color2
        #    else: color=color1    
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE: finish = True
            if e.key == pygame.K_UP :     y-=Tick
            elif e.key == pygame.K_DOWN : y+=Tick
            elif e.key == pygame.K_LEFT : x-=Tick
            elif e.key == pygame.K_RIGHT: x+=Tick
        
        if y < 0: y=0
        if y > Y_SCREENSIZE: y=Y_SCREENSIZE
        if x < 0: x=0
        if x > X_SCREENSIZE: x=X_SCREENSIZE
                
        #if color==color1:color=color2
        #else: color=color1
        
        ourScreen.fill(color3)
        
        pygame.draw.rect(ourScreen, color, pygame.Rect(x,y,X_RECTSIZE,Y_RECTSIZE))
        
        
        pygame.display.update()
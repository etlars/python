import pygame


pygame.init()

ourScreen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("파이게임")
finish = False;


color1 = (0,0,255)
color2 = (255,0,0)
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
            if e.key == pygame.K_UP :     y-=3
            elif e.key == pygame.K_DOWN : y+=3
            elif e.key == pygame.K_LEFT : x-=3
            elif e.key == pygame.K_RIGHT: x+=3
        
        if color==color1:color=color2
        else: color=color1
        
        #ourScreen.fill(color3)
        
        pygame.draw.rect(ourScreen, color, pygame.Rect(x,y,60,60))
        
        
        pygame.display.update()
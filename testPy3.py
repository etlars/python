import pygame


pygame.init()

ourScreen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("파이게임")
finish = False;

color1 = (0,0,255)
color2 = (255,0,0)
color = color1

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
            
        #pygame.draw.rect(ourScreen, (0, 0, 255), pygame.Rect(100,100,60,60))
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if color==color1:
               color=color2
            else: color=color1
        pygame.draw.rect(ourScreen, color, pygame.Rect(100,100,60,60))
        
        
        pygame.display.update()
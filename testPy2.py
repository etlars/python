import pygame


pygame.init()

ourScreen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("파이게임")
finish = False;

color = (0,0,255)

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
            
        pygame.draw.rect(ourScreen, color, pygame.Rect(100,100,60,60))
        
        
        pygame.display.update()
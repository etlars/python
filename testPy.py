import pygame
pygame.init()

ourScreen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("PYGAME")
finish = False;

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
            
        pygame.display.update()

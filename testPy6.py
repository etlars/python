import pygame


pygame.init()

X_SCREENSIZE=800
Y_SCREENSIZE=600

ourScreen=pygame.display.set_mode((X_SCREENSIZE, Y_SCREENSIZE))
pygame.display.set_caption("파이게임")
finish = False;
color3=(0,0,0)

img = pygame.image.load("zzang.png")
def myimg(x, y):
    ourScreen.blit(img, (x, y))
# 좌표 
x=X_SCREENSIZE*0.5
y=Y_SCREENSIZE*0.5

# 초당 프레임 
#clock = pygame.time.Clock()

while not finish:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            finish = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE: finish = True

        ourScreen.fill(color3)
        myimg(x, y)
   
        
        pygame.display.update()
import pygame

pygame.init()

scr = pygame.display.set_mode((800,600))
icon = pygame.image.load('spa.png')
icn = pygame.image.load('spa.png')
bullet = pygame.image.load('bullet.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("Test Game")

x = 370
y = 400
x1 = 370
y1 = 400
def player():
    scr.blit(icn,(x,y))


def bullet():
    y1 = 400.0
    while True:
        scr.blit(bullet,(x1,y1))
        y1 += 1
        

ru = True
r = 200
g = 0
b = 0
while ru:
    scr.fill((r, g, b))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ru = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x1 += 5
                x += 5
            if event.key == pygame.K_LEFT:
                x -= 5
                x1 -= 5
            if event.key == pygame.K_UP:
                bullet()
                
            
    player()
    pygame.display.update()

import pygame 

pygame.init()

pygame.display.set_caption("OK")
screen = pygame.display.set_mode((300,300))
screen.fill("white")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen
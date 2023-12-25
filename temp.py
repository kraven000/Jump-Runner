# import pygame
# pygame.init()

# screen = pygame.display.set_mode((760,428))
# clock = pygame.time.Clock()

# ground = pygame.image.load("ground.png").convert_alpha()
# ground_rect = ground.get_rect(topright=(760,300))
# sky = pygame.image.load("sky.png").convert_alpha()
# sky_rect = sky.get_rect(topright=(760,-105))

# lufy = pygame.image.load("lufy.png").convert_alpha()
# lufy_rect = lufy.get_rect(midright=(60,250))
# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             exit()

#     screen.blit(sky,sky_rect)
#     screen.blit(ground,ground_rect)
#     screen.blit(lufy,lufy_rect)
#     # print(ground_rect.x)
#     print(sky_rect.x)
#     ground_rect.x += 1
#     if ground_rect.x>-200:
#         ground_rect.x = -324
#     sky_rect.x += 2
#     if sky_rect.x>30:
#         sky_rect.x = -34

#     pygame.display.update()
#     clock.tick(40)




from time import sleep
def count_down():
    interval = 1
    count = 0
    time = 60
    while True:
        count += 1
        if count == (time*interval):
            interval += 1
            print(count)
        sleep(1)

count_down()
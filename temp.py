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




# from time import sleep
# def count_down():
#     interval = 1
#     count = 0
#     time = 60
#     while True:
#         count += 1
#         if count == (time*interval):
#             interval += 1
#             print(count)
#         sleep(1)

# count_down()

# from playsound import playsound
# while True:
#     playsound("background_music.mp3")


import pygame

pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Simple Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()
while run:
    # pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
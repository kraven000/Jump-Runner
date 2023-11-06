import pygame

pygame.init()
# Setting up Screen, fps and Title
screen = pygame.display.set_mode((760,428))
clock = pygame.time.Clock()
pygame.display.set_caption("Jump Runner")

# Making Image Surfaces,text:- 

# Static motion Image
sky_surface = pygame.image.load("sky.png").convert_alpha()
ground_surface = pygame.image.load("ground.png").convert_alpha()

#Dynamic motion Image
enemy_surface = pygame.image.load("zombie.png")
enemy_rec = enemy_surface.get_rect(midbottom=(700,345))
character_surface = pygame.image.load("lufy.png")
character_rec = character_surface.get_rect(midbottom=(12,340))

#Text
text = pygame.font.Font("ArchitectsDaughter-Regular.ttf",40)
game_surface = text.render("Jump!!",True,"Black")  

score = 0
gravity = 12
condition = True
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if condition:
            if character_rec.bottom==340:
                if event.type==pygame.KEYUP or event.type==pygame.K_SPACE:
                    gravity = -20
        else:        
            if event.key==pygame.K_SPACE:
                condition = True
                score = 0
                enemy_rec.x=700

    if condition: 
        score += 1       
        #Static 
        screen.blit(sky_surface,(-30,-80))
        screen.blit(ground_surface,(0,320))

        #Dynamic
        score_card = text.render(F"SCORE:-{score}",True,"Black")
        screen.blit(score_card,(500,30))
        screen.blit(enemy_surface,enemy_rec)
        enemy_rec.x -= 3.5
        if enemy_rec.x<=0:
            enemy_rec.x = 700
        
        gravity += 1
        character_rec.y += gravity

        character_rec.x += 3.5
        if character_rec.x>=720:
            character_rec.x = 12
        if character_rec.bottom>=340:
            character_rec.bottom = 340
        screen.blit(character_surface,character_rec)

        screen.blit(game_surface,(100,30))
        if enemy_rec.colliderect(character_rec):
            condition = False
    else:
        screen.fill("Yellow")
        game_over = text.render("GAME OVER!!!",True,"Red")
        game_over1 = text.render("PRESS SPACE TO RESTART THE GAME",True,"Red")
        screen.blit(game_over,(0,0))
        screen.blit(game_over1,(0,100))

    pygame.display.update()
    clock.tick(60)
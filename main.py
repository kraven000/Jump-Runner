import pygame
from tkinter import Tk,PhotoImage,Label,Button

def about():
    read = None
    with open("about.txt") as f:
        read = f.read()
    root = Tk()
    root.minsize(300,200)
    root.maxsize(300,200)
    Label(root,text=str(read),font="Aerial 16 bold").grid(row=0,column=0)
    root.mainloop()
    

def highscore():
    score = None
    with open("highscore.txt") as f:
        score = f.read()
    root = Tk()
    root.minsize(100,200)
    root.maxsize(100,200)
    Label(root,text=str(score),font="Aerial 30 bold").place(x=50,y=85)
    
    root.mainloop()
    

def game():
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
                if event.type==pygame.QUIT:
                    exit()        
                if event.type==pygame.KEYUP:
                    condition = True
                    score = 0
                    enemy_rec.x=700
                    character_rec.x = 12

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
                ini_score = None
                with open("Highscore.txt","r") as f:
                    ini_score = f.read()
                if int(score)>int(ini_score):
                    with open("Highscore.txt","w") as f:
                        f.write(str(score))
                condition = False
        else:
            screen.fill("Yellow")
            game_over = text.render("GAME OVER!!!",True,"Red")
            game_over1 = text.render("PRESS KEYUP TO RESTART THE GAME",True,"Red")
            game_over2 = text.render(f"SCORE:- {score}",True,"Red")
            screen.blit(game_over,(0,0))
            screen.blit(game_over1,(0,100))
            screen.blit(game_over2,(0,200))
        pygame.display.update()
        clock.tick(60)


def start():
    root = Tk()
    root.geometry("760x428")
    background_image = PhotoImage(file="Background.png")
    Label(root,image=background_image).pack()
    Button(root,text="START",command=game).place(relheight=0.12,relwidth=0.15,x=345,y=25)
    Button(root,text="ABOUT",command=about).place(relheight=0.12,relwidth=0.15,x=345,y=125)
    Button(root,text="HIGHSCORE",command=highscore).place(relheight=0.12,relwidth=0.15,x=345,y=225)
    Button(root,text="EXIT",command=exit).place(relheight=0.12,relwidth=0.15,x=345,y=325)
    root.mainloop()

if __name__ == "__main__":
    start()
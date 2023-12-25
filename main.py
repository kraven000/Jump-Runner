# The code you provided is a Python script that implements a simple game called "Jump Runner" using
# the Pygame library and the Tkinter library for the GUI.
from os import system
from multiprocessing import Process
from time import sleep

try:
    import pygame
    from tkinter import Tk,PhotoImage,Label,Button
    from playsound import playsound
    
    
    def countdown():
        interval = 1
        count = 0
        time = 60
        while True:
            count += 1
            if count == (time*interval):
                interval += 1
                print(count)
            sleep(1)

    def about():
        read = None
        with open("about.txt") as f:
            read = f.read()
        root = Tk()
        root.title("Jump Runner")
        root.minsize(400,180)
        root.maxsize(400,180)
        Label(root,text=str(read),font="Helvetica 16 bold",bg="black",fg="white",relief="sunken",border=6,borderwidth=6).grid(row=0,column=0)
        root.mainloop()
        

    def highscore():
        score = None
        with open("highscore.txt") as f:
            score = str(f.read())
        root = Tk()
        root.title("Jump Runner")
        root.minsize(200,100)
        root.maxsize(200,100)
        
        Label(root,text=str(score),font="Roman 24 bold",fg="white",bg="black",relief="groove",border=10,borderwidth=10).place(x=0,y=0,relheight=1,relwidth=1)
        root.mainloop()
        
        
    def game():
        pygame.init()
        # Setting up Screen, fps and Title
        screen = pygame.display.set_mode((760,428))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Jump Runner")

        # Making Image Surfaces,text:- 
        sky_surface = pygame.image.load("sky.png").convert_alpha()
        sky_rec = sky_surface.get_rect(midbottom=(380,340))
        ground_surface = pygame.image.load("ground.png").convert_alpha()
        ground_rec = ground_surface.get_rect(midright=(760,420))

        enemy_surface = pygame.image.load("zombie.png")
        enemy_rec = enemy_surface.get_rect(midbottom=(700,345))
        character_surface = pygame.image.load("lufy.png")
        character_rec = character_surface.get_rect(midbottom=(12,340))

        #Text
        text = pygame.font.Font("ArchitectsDaughter-Regular.ttf",40)
        game_surface = text.render("Jump!!",True,"Black")  

        # Sound
        jump = pygame.mixer.Sound("jump.mp3")
        kill = pygame.mixer.Sound("kill.mp3")
        background_music = pygame.mixer.Sound("background_music.mp3")
        
        # Intervals
        interval = 0

        score = 0
        gravity = 12
        condition = True
        enemy_speed = 4.0
        
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    # exit()
                if condition:
                    if character_rec.bottom==340:
                        if event.type==pygame.KEYUP or event.type==pygame.K_SPACE:
                            score += 2
                            gravity = -20
                            jump.play()
                else:   
                    if event.type==pygame.QUIT:
                        exit()        
                    if event.type==pygame.KEYUP:
                            condition = True
                            enemy_speed = 4.0
                            score = 0
                            enemy_rec.x=700
                            character_rec.x = 12

            if condition:
                # background_music.play()
                interval += 1
                #Static 
                screen.blit(sky_surface,sky_rec)
                
                screen.blit(ground_surface,ground_rec)
                #Dynamic
                score_card = text.render(F"SCORE:-{score}",True,"Black")
                screen.blit(score_card,(500,30))
                screen.blit(enemy_surface,enemy_rec)
                
                # Enemy speed
                enemy_rec.x -= enemy_speed
                if score>=60:
                    if score%60==0:
                        enemy_speed += 0.5

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
                    kill.play()
                    condition = False
                    ini_score = None
                    with open("highscore.txt","r") as f:
                        ini_score = f.read()
                    if int(score)>int(ini_score):
                        with open("highscore.txt","w") as f:
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
        root.minsize(760,428)
        root.maxsize(760,428)
        root.title("Jump Runner")
        background_image = PhotoImage(file="Background.png")
        Label(root,image=background_image).pack()
        Button(root,text="START",command=game).place(relheight=0.12,relwidth=0.15,x=345,y=25)
        Button(root,text="ABOUT",command=about).place(relheight=0.12,relwidth=0.15,x=345,y=125)
        Button(root,text="HIGHSCORE",command=highscore).place(relheight=0.12,relwidth=0.15,x=345,y=225)
        Button(root,text="EXIT",command=exit).place(relheight=0.12,relwidth=0.15,x=345,y=325)
        root.mainloop()

except Exception as e:
    system("pip3 install -r requirement.txt")
    print()
    print()
    print()
    print("Rerun your Program\nIf you still encounter this error reinstall python and than try")

if __name__ == "__main__":
    start()
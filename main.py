# The code you provided is a Python script that implements a simple game called "Jump Runner" using
# the Pygame library and the Tkinter library for the GUI.
try:
    import pygame
    from tkinter import Tk,PhotoImage,Label,Button,messagebox
    from os import system


    def about():
        '''Making a About window. If the user press ABout Button. It will show About sections or Credits.'''
        
        read = None
        with open("about.txt") as f:
            read = f.read()
        root = Tk()
        root.title("Jump Runner")
        root.minsize(750,410)
        root.maxsize(750,410)
        Label(root,text=str(read),font="Helvetica 16 bold",bg="black",fg="white",relief="sunken",border=6,borderwidth=6).grid(row=0,column=0)
        root.mainloop()

    def music():
        '''It is function which will control Music if User press music button.'''
        
        with open("configuration.txt","r") as f:
            previous_conf = f.readlines()
            if previous_conf[1].strip("\n")=="yes":
                resp = messagebox.askyesno(title="MUSIC",message="DO YOU WANT TO SWITCH OFF THE MUSIC?")
                if resp == True:
                    # previous_conf = f.readlines()
                    previous_conf[1] = "no\n"
                    with open("configuration.txt","w") as f:
                        f.writelines(previous_conf)
                        
            elif previous_conf[1].strip("\n")=="no":
                resp = messagebox.askyesno(title="MUSIC",message="DO YOU WANT TO SWITCH ON THE MUSIC?")
                if resp == True:
                    # previous_conf = f.readlines()
                    previous_conf[1] = "yes\n"
                    with open("configuration.txt","w") as f:
                        f.writelines(previous_conf)
                        
            del previous_conf


    def sound():
        '''It is function which will control Sound if User press Sound button.'''
        
        with open("configuration.txt","r") as f:
            previous_conf = f.readlines()
            if previous_conf[2].strip("\n")=="yes":
                resp = messagebox.askyesno(title="SOUND",message="DO YOU WANT TO SWITCH OFF THE SOUND?")
                if resp == True:
                    # previous_conf = f.readlines()
                    previous_conf[2] = "no\n"
                    with open("configuration.txt","w") as f:
                        f.writelines(previous_conf)
                        
            elif previous_conf[2].strip("\n")=="no":
                resp = messagebox.askyesno(title="MUSIC",message="DO YOU WANT TO SWITCH ON THE SOUND?")
                if resp == True:
                    # previous_conf = f.readlines()
                    previous_conf[2] = "yes\n"
                    with open("configuration.txt","w") as f:
                        f.writelines(previous_conf)
                        
            del previous_conf


    def highscore():
        '''Making a Highscore window. If user press Highscore button, the highscore will be shown.'''
        
        score = None
        with open("configuration.txt","r") as f:
            score = str(f.readlines()[0].strip("\n"))
        root = Tk()
        root.title("Jump Runner")
        root.minsize(200,100)
        root.maxsize(200,100)
        
        Label(root,text=score,font="Roman 24 bold",fg="white",bg="black",relief="groove",border=10,borderwidth=10).place(x=0,y=0,relheight=1,relwidth=1)
        root.mainloop()


    def game():
        '''It is main function where the game logic is written and it will execute the function if the user press start'''
        
        pygame.init()
        # Setting up Screen, fps and Title
        screen = pygame.display.set_mode((760,428))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Jump Runner")
        
        # Background Music and Sound Effects
        pygame.mixer.music.load("background.mp3")
        pygame.mixer.music.set_volume(10)
        
        jump = pygame.mixer.Sound("jump.mp3")
        kill = pygame.mixer.Sound("kill.mp3")
        
        # Checking if music should be played or not
        with open("configuration.txt","r") as f:
            if f.readlines()[1].strip("\n")=="yes":
                pygame.mixer.music.play(-1)
                
        
        # Making Image Surfaces,text:- 
        # Background
        background = pygame.image.load("combined.png").convert_alpha()
        background_rect = background.get_rect(midbottom=(380,530))
        
        # Game Characters
        enemy_surface = pygame.image.load("zombie.png")
        enemy_rec = enemy_surface.get_rect(midbottom=(700,345))
        character_surface = pygame.image.load("character.png")
        character_rec = character_surface.get_rect(midbottom=(12,340))
        
        #Text
        text = pygame.font.Font("ArchitectsDaughter-Regular.ttf",40)
        game_surface = text.render("Jump!!",True,"Black")  
        
        # Miscellaneous
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
                            # Tracking Score
                            score += 2
                            
                            # Tracking Gravity and jump sound
                            gravity = -20
                            
                            # Checking if jump sound should be played
                            with open("configuration.txt","r") as f:
                                if f.readlines()[2].strip("\n")=="yes":
                                    jump.play()
                else:
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        # exit()        
                    if event.type==pygame.KEYUP:
                            # Making Condition's Default if user restart the game
                            condition = True
                            enemy_speed = 4.0
                            score = 0
                            enemy_rec.x=700
                            character_rec.x = 12

            if condition:
                #Static 
                screen.blit(background,background_rect)
                
                #Dynamic
                score_card = text.render(F"SCORE:-{score}",True,"Black")
                screen.blit(score_card,(500,30))
                
                # Showing Enemy & tracking speed
                screen.blit(enemy_surface,enemy_rec)
                enemy_rec.x -= enemy_speed
                
                # It will Gradually Increase Speed Of Characters 
                if score%4==0 and score!=0:
                    enemy_speed += (1/1000000000)
                
                # Setting Enemy Position to default
                if enemy_rec.x<=0:
                    enemy_rec.x = 700
                
                # Showing Character & Tracking Speed,Jumps
                gravity += 1
                character_rec.y += gravity
                character_rec.x += 3.5
                
                # Setting Character position to default
                if character_rec.x>=720:
                    character_rec.x = 12
                if character_rec.bottom>=340:
                    character_rec.bottom = 340
                screen.blit(character_surface,character_rec)

                # Showing Text
                screen.blit(game_surface,(100,30))
                
                # Checking Collison between two characters
                if enemy_rec.colliderect(character_rec):
                    # checking if kill sound should be played or not
                    with open("configuration.txt","r") as f:
                        if f.readlines()[2].strip("\n")=="yes":
                            kill.play()
                    
                    # To stop the game
                    condition = False
                    
                    # Two check Highscores
                    with open("configuration.txt","r") as f:
                        previous_conf = list(map(lambda x:x.strip("\n"),f.readlines()))
                        
                        ini_score = previous_conf[0]
                        
                        if int(score)>int(ini_score):
                            previous_conf[0] = str(score)
                            with open("configuration.txt","w") as f:
                                previous_conf = list(map(lambda x:x+"\n",previous_conf))
                                f.writelines(previous_conf)
                            del previous_conf
                        
                        condition = False
            else:
                # Making Game Over screen
                screen.fill("Yellow")
                game_over = text.render("GAME OVER!!!",True,"Red")
                game_over1 = text.render("PRESS KEYUP TO RESTART THE GAME",True,"Red")
                game_over2 = text.render(f"SCORE:- {score}",True,"Red")
                screen.blit(game_over,(0,0))
                screen.blit(game_over1,(0,100))
                screen.blit(game_over2,(0,200))
            
            pygame.display.update()
            clock.tick(60)


    def game_start():
        '''It is the starting Interface of program, where all buttons will be shown.'''
        
        root = Tk()
        root.minsize(749,419)
        root.maxsize(749,419)
        root.title("Jump Runner")
        
        # Setting Up Background Image
        background_image = PhotoImage(file="background.png")
        Label(root,image=background_image).place(x=0,y=0)
        
        # Button for Music
        music_image = PhotoImage(file="music_image.png")
        Button(root,image=music_image,command=music).place(height=60,width=60,x=0,y=359)
        
        # Button for Sound
        sound_image = PhotoImage(file="sound_image.png")
        Button(root,image=sound_image,command=sound).place(height=60,width=60,x=70,y=359)

        # Button for Start
        Button(root,text="START",command=game).place(relheight=0.12,relwidth=0.15,x=345,y=25)
        
        # Button for About
        Button(root,text="ABOUT",command=about).place(relheight=0.12,relwidth=0.15,x=345,y=125)
        
        # Button for Highscore
        Button(root,text="HIGHSCORE",command=highscore).place(relheight=0.12,relwidth=0.15,x=345,y=225)
        
        # Button for Exit
        Button(root,text="EXIT",command=exit).place(relheight=0.12,relwidth=0.15,x=345,y=325)
        
        root.mainloop()


except Exception as e:
    system("pip3 install -r requirement.txt")
    print()
    print()
    print()
    print("Rerun your Program\nIf you still encounter this error reinstall python and than try")


if __name__ == "__main__":
    game_start()
    
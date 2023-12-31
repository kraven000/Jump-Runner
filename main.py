# The code you provided is a Python script that implements a simple game called "Jump Runner" using
# the Pygame library and the Tkinter library for the GUI.

try:
    import pygame
    from tkinter import Tk,PhotoImage,Label,Button,messagebox,Scrollbar,Listbox,Frame
    from os import system 
    from math import ceil
    from sys import platform
    

    def read_write_file(file,mode,text=None):
        if mode=="r":
            with open(file,mode) as f:
                return f.readlines()
        elif (mode=="w" or mode=="a") and text!=None:
            with open(file,mode) as f:
                f.writelines(text)
        elif text==None:
            raise TypeError("If you open file in 'w' or 'a'. please specify text." )
    
    
    def reset_your_highscore():
        '''It is function which will reset your highscore if User press reset your highscore button.'''
        
        reset_highscore = read_write_file("configuration.txt","r")
        reset_highscore[0] = "0\n"
        
        read_write_file("configuration.txt","w",reset_highscore)
        
        exit()


    def about():
        '''Making a About window. If the user press ABout Button. It will show About sections or Credits.'''
        
        root = Tk()
        # Setting Up Geometry and Title
        root.title("Jump Runner")
        root.minsize(800,400)
        root.maxsize(800,400)
        
        # Setting Up ScrollBar 
        scrollbar = Scrollbar(root)
        scrollbar.pack(side="right", fill="y")
        
        # Setting Up Widget
        listbox = Listbox(root,height=400,width=640,font="Harrington 12 bold",bg="black",fg="wheat",yscrollcommand = scrollbar.set)
        
        read = list(map(lambda x:x.strip("\n"),read_write_file("about.txt",mode="r")))
        
        for i in read:
            listbox.insert("end",i)
        
        # Packing and configuring the widget and scrollbar
        listbox.pack(fill="both")
        scrollbar.config(command=listbox.yview)
        
        root.mainloop()
    
    
    def music():
        '''It is function which will control Music if User press music button.'''
    
        file_txt = read_write_file("configuration.txt","r")
        if file_txt[1]=="yes\n":
            resp = messagebox.askyesno(title="MUSIC",message="DO YOU WANT TO SWITCH OFF THE MUSIC?")
            if resp==True:
                file_txt[1] = "no\n"
                read_write_file("configuration.txt","w",file_txt)
                del resp
        
        elif file_txt[1]=="no\n":
            resp = messagebox.askyesno(title="MUSIC",message="DO YOU WANT TO SWITCH ON THE MUSIC?")
            if resp==True:
                file_txt[1] = "yes\n"
                read_write_file("configuration.txt","w",file_txt)
                del resp
        del file_txt


    def sound():
        '''It is function which will control Sound if User press Sound button.'''
        
        file_txt = read_write_file("configuration.txt","r")
        if file_txt[2]=="yes\n":
            resp = messagebox.askyesno(title="SOUND",message="DO YOU WANT TO SWITCH OFF THE SOUND?")
            if resp==True:
                file_txt[2] = "no\n"
                read_write_file("configuration.txt","w",file_txt)
                del resp
        
        elif file_txt[2]=="no\n":
            resp = messagebox.askyesno(title="SOUND",message="DO YOU WANT TO SWITCH ON THE SOUND?")
            if resp==True:
                file_txt[2] = "yes\n"
                read_write_file("configuration.txt","w",file_txt)
                del resp
        del file_txt


    def highscore():
        '''Making a Highscore window. If user press Highscore button, the highscore will be shown.'''
        
        # GETTING YOUR HIGHSCORE THROUGH CONFIGURATION.TXT
        score = read_write_file("configuration.txt","r")[0].strip("\n")
        
        # SETTING UP GEOMETRY AND TITLE
        root = Tk()
        root.title("Jump Runner")
        root.minsize(230,130)
        root.maxsize(230,130)
        
        scrollbar = Scrollbar(root)
        scrollbar.place(x=0,y=200,relheight=0.7,relwidth=0.7)
        
        l = Listbox(root, font="Roman 20 bold",bg="black",fg="white",xscrollcommand=scrollbar.set)
        
        l.insert("end",score)
        l.pack(fill="both")
        
        Button(root, text="RESET YOUR HIGHSCORE", bg="light sky blue", fg="black", relief="sunken", borderwidth=3,command=reset_your_highscore).place(x=10, y=60)
        
        scrollbar.config(command=l.xview)
        
        root.quit()
        root.mainloop()


    def game():
        '''It is main function where the game logic is written and it will execute the function/game if the user press start'''
        
        pygame.init()
        
        # Setting up Screen, fps and Title
        screen = pygame.display.set_mode((800,500))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Jump Runner")
        
        # Background Music and Sound Effects
        pygame.mixer.music.load("background.mp3")
        pygame.mixer.music.set_volume(10)
        
        jump = pygame.mixer.Sound("jump.mp3")
        kill = pygame.mixer.Sound("kill.mp3")
        
        # Checking if music should be played or not
        file_txt = read_write_file("configuration.txt","r")
        if file_txt[1]=="yes\n":
            pygame.mixer.music.play(-1)
                
        
        # Making Image Surfaces,text:- 
        # Background
        background = pygame.image.load("combined.png").convert_alpha()
        background_rect = background.get_rect(topleft=(0,-225))
        
        # Game Characters
        enemy_surface = pygame.image.load("zombie.png")
        enemy_rec = enemy_surface.get_rect(midbottom=(790,400))
        character_surface = pygame.image.load("character.png")
        character_rec = character_surface.get_rect(topleft=(10,600))
        
        # Text
        text = pygame.font.Font("ArchitectsDaughter-Regular.ttf",40)
        game_surface = text.render("Jump!!",True,"Black")  
        
        # Miscellaneous
        score = 0
        gravity = 13
        condition = True
        enemy_speed = 4.0
        game_start_stop = True
        
        # This line is to move your background
        tiles = ceil(800/background.get_width())+1
        move = 0
        
        while game_start_stop:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_start_stop = False
                    
                if condition:
                    if character_rec.bottom==400:
                        if event.type==pygame.KEYUP or event.type==pygame.K_SPACE:
                            # Tracking Score
                            score += 2
                            
                            # Tracking Gravity and jump sound
                            gravity = -20
                            
                            # Checking if jump sound should be played
                            
                            if file_txt[2]=="yes\n":
                                jump.play()
                else:
                    if event.type==pygame.QUIT:
                        game_start_stop = False

                    if event.type==pygame.KEYUP:
                            # Making Condition's Default if user restart the game
                            condition = True
                            enemy_speed = 4.0
                            score = 0
                            enemy_rec.x=800
                            character_rec.x = 12

            if condition:
                # Making Background Move
                for i in range(0,tiles):
                    screen.blit(background,(i*background.get_width()+move,-225))
                
                move -= 3.5
                if abs(move)>=background_rect.width:
                    move = 0
                
                #Showing Score Card
                score_card = text.render(F"SCORE:-{score}",True,"Black")
                screen.blit(score_card,(500,30))
                
                # Showing Enemy & tracking speed
                screen.blit(enemy_surface,enemy_rec)
                enemy_rec.x -= enemy_speed
                
                # It will Gradually Increase Speed Of Characters 
                if score%4==0 and score!=0:
                    enemy_speed += (1/1000)
                
                # Setting Enemy Position to default
                if enemy_rec.x<=5:
                    enemy_rec.x = 800
                
                # Showing Character & Tracking Speed,Jumps
                gravity += 1
                character_rec.y += gravity
                character_rec.x += 3.5
                
                # Setting Character position to default
                if character_rec.x>=795:
                    character_rec.x = 10
                if character_rec.bottom>=400:
                    character_rec.bottom = 400
                
                screen.blit(character_surface,character_rec)
                
                # Showing Text
                screen.blit(game_surface,(100,30))
                
                # Checking Collison between two characters
                if enemy_rec.colliderect(character_rec):
                    # To stop the game
                    condition = False
                    
                    # checking if kill sound should be played or not
                    if file_txt[2]=="yes\n":
                        kill.play()

                    # Two check Highscores
                    ini_score = file_txt[0]
                    
                    if int(score)>int(ini_score):
                        file_txt[0] = str(score)+"\n"
                        
                        read_write_file("configuration.txt","w",file_txt)
                    
            else:
                # Making Game Over screen
                screen.fill("Yellow")
                
                # Message to write Game Over
                game_over = text.render("GAME OVER!!!",True,"Red")
                
                # Message of Instruction how to restart the game
                game_over1 = text.render("PRESS KEYUP TO RESTART THE GAME",True,"Red")
                
                # Message to show the score you jump
                game_over2 = text.render(f"SCORE:- {score}",True,"Red")
                
                # Showing It in Screen
                screen.blit(game_over,(0,0))
                screen.blit(game_over1,(0,100))
                screen.blit(game_over2,(0,200))
            
            pygame.display.update()
            clock.tick(60)
        pygame.quit()

    def game_start():
        '''It is the starting Interface of program, where all buttons will be shown.'''
        
        root = Tk()
        
        # Setting Up Tittle, Geometry and Icon
        root.minsize(749,419)
        root.maxsize(749,419)
        root.title("Jump Runner")
        root.iconphoto(False,PhotoImage(file="icon.png"))
        
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
        Button(root,text="START",relief="sunken",borderwidth=6,command=game).place(relheight=0.12,relwidth=0.15,x=345,y=25)
        
        # Button for About
        Button(root,text="ABOUT",relief="sunken",borderwidth=6,command=about).place(relheight=0.12,relwidth=0.15,x=345,y=125)
        
        # Button for Highscore
        Button(root,text="HIGHSCORE",relief="sunken",borderwidth=6,command=highscore).place(relheight=0.12,relwidth=0.15,x=345,y=225)
        
        # Button for Exit
        Button(root,text="EXIT",relief="sunken",borderwidth=6,command=exit).place(relheight=0.12,relwidth=0.15,x=345,y=325)
        
        root.mainloop()

except Exception as e:
    if platform=="linux":
        system("pip3 install -r requirement.txt")
    else:
        system("pip install -r requirements.txt")
    print()
    print()
    print("Rerun your Program\nIf you still encounter this error reinstall python and than try")


if __name__ == "__main__":
    game_start()
    
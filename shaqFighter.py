#Andy Tian and Dennis Dolinskiy
#5/22/2019
#shaqFighter.py
#1 on 1 fighter program created for our final project

#importing libraries
import pygame
import math

#Creating Pygame Window
pygame.init()
WIDTH=800
HEIGHT=600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

#Implementing clock and some variables
clock=pygame.time.Clock()
inPlay=True
mainMenu=True
game=True
gameScreen=False
settings=False
instructions=False
volume=0.5

#Color declaration
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(46, 209, 103)
YELLOW=(248, 255, 48)
RED=(255, 0, 21)

#Add background Music

#Function for loading images and lists for animations
def load(image):
    picture=pygame.image.load(image)
    return picture

#loading all images and lists for animations
rightAnimation=[load('0.png'),load('1.png'),load('2.png'),load('3.png'),load('4.png'),load('5.png')]
leftAnimation=[load('6.png') ,load('7.png'),load('8.png'),load('9.png')]
jumpAnimation=[load('10.png'),load('11.png'),load('12.png'),load('13.png'),load('14.png'),load('15.png'),load('16.png')]
idleAnimation=[load('48.png'),load('49.png'),load('50.png'),load('51.png'),load('52.png'),load('53.png'),load('54.png'),load('55.png')]
punchAnimation=[load('17.png'),load('18.png'),load('19.png')]
shieldAnimation=[load('25.png'),load('26.png'),load('27.png'),load('28.png')]
dunkAnimation=[load('29.png'),load('30.png'),load('31.png'),load('32.png'),load('33.png'),load('34.png'),load('35.png'),load('36.png')]
kickAnimation=[load('20.png'),load('21.png'),load('22.png'),load('23.png'),load('24.png')]
deathAnimation=[load('37.png'),load('38.png'),load('39.png'),load('40.png'),load('41.png'),load('42.png')]
victoryAnimation=[load('43.png'),load('44.png'),load('45.png'),load('46.png'),load('47.png')]
idleAnimation1=[load('Kaori/3.png'),load('Kaori/2.png'),load('Kaori/1.png'),load('Kaori/0.png')]
rightAnimation1=[load('Kaori/9.png'),load('Kaori/8.png'),load('Kaori/7.png'),load('Kaori/6.png'),load('Kaori/5.png'),load('Kaori/4.png')]
leftAnimation1=[load('Kaori/17.png'),load('Kaori/16.png'),load('Kaori/15.png'),load('Kaori/14.png'),load('Kaori/13.png'),load('Kaori/12.png'),load('Kaori/11.png'),load('Kaori/10.png')]
deathAnimation1=[load('Kaori/39.png'),load('Kaori/40.png'),load('Kaori/41.png'),load('Kaori/42.png'),load('Kaori/43.png'),load('Kaori/44.png')]
kickAnimation1=[load('Kaori/28.png'),load('Kaori/27.png'),load('Kaori/26.png'),load('Kaori/25.png')]
shieldAnimation1=[load('Kaori/36.png'),load('Kaori/37.png'),load('Kaori/38.png')]
punchAnimation1=[load('Kaori/35.png'),load('Kaori/34.png'),load('Kaori/33.png')]
tornadoAnimation=[load('Kaori/29.png'),load('Kaori/30.png'),load('Kaori/31.png'),load('Kaori/32.png')]
victoryAnimation1=[load('Kaori/45.png'),load('Kaori/46.png'),load('Kaori/47.png'),load('Kaori/48.png'),load('Kaori/49.png'),load('Kaori/50.png'),load('Kaori/51.png'),load('Kaori/52.png')]
jumpAnimation1=[load('Kaori/18.png'),load('Kaori/19.png'),load('Kaori/20.png'),load('Kaori/21.png'),load('Kaori/22.png'),load('Kaori/23.png'),load('Kaori/24.png')]
background=load('background.png')
mainScreen=load('mainMenu.png')
instructionScreen=load('instructions.png')
kaoriWin=load('kaoriWin.png')
volumeSettings=load('volume.png')
shaqWin=load('shaqWin.png')

#Start of Game screen
while game:
    
    #Main Menu page music
    if mainMenu==True:
        pygame.mixer.music.load("bgMusic.mp3")
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        
    #While the main menu is being displayed
    while mainMenu:
        
        #Setting volume each time
        pygame.mixer.music.set_volume(volume)
        gameWindow.blit(mainScreen,(0,0))
        
        #Keydown events for main menu
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    mainMenu=False
                    settings=False
                    gameScreen=False
                    inPlay=False
                    instructions=False
                    game=False
        pygame.event.get()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_p]:
            gameScreen=True
            inPlay=True
            mainMenu=False
            instructions=False
        elif keys[pygame.K_n]:
            settings=True
            gameScreen=False
            inPlay=False
            mainMenu=False
            instructions=False
        if keys[pygame.K_i]:
            instructions=True
            mainMenu=False
            inPlay=False
            settings=False
        pygame.display.update()
        
    #instructions page
    while instructions:
        gameWindow.fill((255,255,255))
        gameWindow.blit(instructionScreen,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    instructions=False
                    mainMenu=True
        pygame.display.update()
        
    #settings page
    while settings:
        gameWindow.blit(volumeSettings,(0,0)) 
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    settings=False
                    mainMenu=True
                if event.key==pygame.K_EQUALS:
                    volume+=0.1
                    if volume>1:
                        volume=1
                if event.key==pygame.K_MINUS:
                    volume-=0.1
                    if volume<0.1:
                        volume=0.1
                        
        #updating volume
        pygame.mixer.music.set_volume(volume)
        pygame.display.update()
        
    #Play music when it's gamescreen           
    if gameScreen:
        pygame.mixer.music.load("gameMusic.mp3")
        pygame.mixer.music.set_volume(volume-0.4)
        pygame.mixer.music.play(-1)
        
    #When it's on the gamescreen
    while gameScreen:
        
        #Implementing all variables (and re-declaring after restarting game)
        
        idle=True
        idle1=True
        jump=False
        jump1=False
        left=False
        left1=False
        right=False
        right1=False
        punch=False
        punch1=False
        shield=False
        shield1=False
        dunk=False
        tornado=False
        kick=False
        kick1=False
        death=False
        death1=False
        first=True
        first1=True
        victory=False
        victory1=False
        jumpCount=0
        jumpCount1=0
        flyingCount=10
        flyingCount1=10
        leftCount=0
        leftCount1=0
        rightCount=0
        rightCount1=0
        idleCount=0
        idleCount1=0
        punchCount=1
        punchCount1=1
        shieldCount=0
        shieldCount1=0
        dunkCount=1
        tornadoCount=0
        kickCount=0
        kickCount1=0
        deathCount=0
        deathCount1=0
        victoryCount=0
        victoryCount1=0
        healthPlayer=200
        healthPlayer1=600
        pygame.display.update()
        
        #Class of player1
        class Player(pygame.sprite.Sprite):
            def __init__(player):
                pygame.sprite.Sprite.__init__(player)
                player.image=load('0.png')
                player.rect=player.image.get_rect()
                player.rect.center=(100,HEIGHT/2)
                player.vel=0
                player.onGround=False
                
            #Updating player and commencing all animations (Global variables to use them)
            def update(player):
                global rightCount
                global leftCount
                global jumpCount
                global idleCount
                global punchCount
                global shieldCount
                global flyingCount
                global dunkCount
                global kickCount
                global deathCount
                global jump
                global punch
                global dunk
                global kick
                global victoryCount
                global healthPlayer
                
                #Casting animations
                if idle:
                    player.image=idleAnimation[idleCount//10]
                    if idleCount>=79:
                        idleCount=0
                    idleCount+=1
                if left and not dunk:
                    player.image=leftAnimation[leftCount//6]
                    if leftCount>=23:
                        leftCount=0
                    leftCount+=1
                if right and not dunk:
                    player.image=rightAnimation[rightCount//6]
                    if rightCount>=29:
                        rightCount=0
                    rightCount+=1
                if jump:
                    player.image=jumpAnimation[jumpCount//6]
                    if jumpCount>=41:
                        jumpCount=0
                    jumpCount+=1
                    if flyingCount>=-10:
                        neg=1
                        if flyingCount<0:
                            neg=-1
                        player.rect.y-= (flyingCount**2)*0.2*neg
                        flyingCount-=1
                    if player.rect.y==269:
                        jump=False
                        flyingCount=10
                        player.rect.y=277

                if punch:
                    player.image=punchAnimation[punchCount//5]
                    if punchCount>=14:
                        punchCount=0
                        punch=False
                    punchCount+=1
                if shield:
                    player.rect.y=287
                    player.image=shieldAnimation[shieldCount//4]
                    if shieldCount>=15:
                        shieldCount=0
                    shieldCount+=1
                if dunk:
                    player.image=dunkAnimation[dunkCount//6]
                    if player.rect.x<785:
                        player.rect.x+=2
                    if dunkCount>=47:
                        dunkCount=0
                        dunk=False
                    dunkCount+=1
                if kick:
                    player.image=kickAnimation[kickCount//5]
                    if kickCount>=24:
                        kickCount=0
                        kick=False
                    kickCount+=1
                if death:
                    player.image=deathAnimation[deathCount//5]
                    if deathCount>=29:
                        deathCount=29
                    if deathCount<29:
                        deathCount+=1
                    if player.rect.y<320:
                        player.rect.y+=1
                    else:
                        player.rect.y=320
                if victory:
                    player.image=victoryAnimation[victoryCount//5]
                    if victoryCount>=24:
                        victoryCount=0
                    victoryCount+=1
                    
                #Collision variables
                rect1=player1.image.get_rect()
                coordinates1=player1.rect[0:2]+rect1[2:4]
                collision1=pygame.Rect(coordinates1)
                
                #Check collision
                if (collision1).colliderect(player.rect) and punch1==True and shield==False:
                    healthPlayer-=2
                if (collision1).colliderect(player.rect) and punch1==True and shield==True:
                    healthPlayer-=1
                if (collision1).colliderect(player.rect) and kick1==True and shield==False:
                    healthPlayer-=2
                if (collision1).colliderect(player.rect) and kick1==True and shield==True:
                    healthPlayer-=1
                if (collision1).colliderect(player.rect) and tornado==True and shield==False:
                    healthPlayer-=1
                if (collision1).colliderect(player.rect) and tornado==True and shield==True:
                    healthPlayer-=1
                    
        #Player2 class
        class player1(pygame.sprite.Sprite):
            def __init__(player1):
                pygame.sprite.Sprite.__init__(player1)
                player1.image=load('Kaori/3.png')
                player1.rect=player1.image.get_rect()
                player1.rect.center=(700,HEIGHT/2+3)
                
            #Player2 update, animations etc. (Globaling the variables so you can use them in the counts)
            def update(player1):
                global rightCount1
                global leftCount1
                global jumpCount1
                global idleCount1
                global punchCount1
                global shieldCount1
                global flyingCount1
                global dunkCount1
                global kickCount1
                global jump1
                global punch1
                global kick1
                global healthPlayer1
                global deathCount1
                global tornadoCount
                global victoryCount1
                
                #Casting all animations
                if idle1:
                    player1.image=idleAnimation1[idleCount1//6]
                    if idleCount1>=23:
                        idleCount1=0
                    idleCount1+=1
                if right1:
                    player1.image=rightAnimation1[rightCount1//6]
                    if rightCount1>=35:
                        rightCount1=0
                    rightCount1+=1
                if left1:
                    player1.image=leftAnimation1[leftCount1//6]
                    if leftCount1>=47:
                        leftCount1=0
                    leftCount1+=1
                if jump1:
                    player1.image=jumpAnimation1[jumpCount1//6]
                    if jumpCount1>=41:
                      jumpCount1=0
                    jumpCount1+=1
                    if flyingCount1>=-10:
                        neg1=1
                        if flyingCount1<0:
                            neg1=-1
                        player1.rect.y-= (flyingCount1**2)*0.2*neg1
                        flyingCount1-=1
                        if player1.rect.y==276:
                            flyingCount1=10
                            jump1=False
                            player1.rect.y=284
                if death1:
                    player1.image=deathAnimation1[deathCount1//5]
                    if deathCount1>=29:
                        deathCount1=29
                    if deathCount1<29:
                        deathCount1+=1
                    if player1.rect.y<320:
                        player1.rect.y+=1
                    else:
                        player1.rect.y=320
                if shield1:
                    player1.image=shieldAnimation1[shieldCount1//6]
                    if shieldCount1>=17:
                        shieldCount1=0
                    shieldCount1+=1
                if punch1:
                    player1.image=punchAnimation1[punchCount1//8]
                    if punchCount1>=23:
                        punchCount1=0
                        punch1=False
                    punchCount1+=1
                if kick1:
                    player1.image=kickAnimation1[kickCount1//6]
                    if kickCount1>=23:
                        kickCount1=0
                        kick1=False
                    kickCount1+=1
                if victory1:
                    player1.image=victoryAnimation1[victoryCount1//6]
                    if victoryCount1>=47:
                        victoryCount1=0
                    victoryCount1+=1
                if tornado:
                    player1.image=tornadoAnimation[tornadoCount//6]
                    if tornadoCount>=23:
                        tornadoCount=0
                    tornadoCount+=1
                    if left1:
                        player1.rect.x+=4
                    if right1:
                        player1.rect.x-=2
                        
                #Collision variables
                rect=player.image.get_rect()
                coordinates=player.rect[0:2]+rect[2:4]
                collision=pygame.Rect(coordinates)
                
                #Check collision (attack animations)
                if (collision).colliderect(player1.rect) and punch==True and shield1==False:
                    healthPlayer1+=2
                if (collision).colliderect(player1.rect) and punch==True and shield1==True:
                    healthPlayer1+=1
                if(collision).colliderect(player1.rect) and dunk==True and shield1==False:
                    healthPlayer1+=2
                if (collision).colliderect(player1.rect) and dunk==True and shield1==True:
                    healthPlayer1+=1
                if(collision).colliderect(player1.rect) and kick==True and shield1==False:
                    healthPlayer1+=2
                if (collision).colliderect(player1.rect) and kick==True and shield1==True:
                    healthPlayer1+=1
                    
        #Class of health bar of player1
        class Health(pygame.sprite.Sprite):
            def __init__(health):
                pygame.sprite.Sprite.__init__(health)
                health.image=pygame.Surface((200,15))
                health.image.fill(GREEN)
                health.rect=health.image.get_rect()
                health.rect.center=(healthPlayer1,50)
            def update(health):
                global death1
                global healthPlayer1
                global first
                global death
                if death==False and death1==False:
                    health.rect.x=healthPlayer1
                #If player1 is dead
                if death==False and death1==False:
                    if healthPlayer1>800:
                        if first:
                            player1.rect.y=280
                        death1=True
                        jump=False
                        right=False
                        left=False
                        shield=False
                        dunk=False
                        first=False
                        death=False
                        healthPlayer1=801
                #Updating health
                if death==False and death1==False:
                    health.image=pygame.Surface((healthPlayer1,25))
                
                #Colors of the health bar depending on what health they have
                if healthPlayer1<700:
                    health.image.fill((GREEN))
                if healthPlayer1>=700 and healthPlayer1<=750:
                    health.image.fill(YELLOW)
                if healthPlayer1>=750:
                    health.image.fill(RED)
                    
        #Health of player 2
        class Health1(pygame.sprite.Sprite):
            def __init__(health1):
                pygame.sprite.Sprite.__init__(health1)
                health1.image=pygame.Surface((healthPlayer,25))
                health1.rect=health1.image.get_rect()
                health1.rect.center=(100,50)
            def update(health1):
                global healthPlayer
                global first1
                global death
                global death1
                
                #When the player dies
                if death==False and death1==False:
                    if healthPlayer<0:
                        if first1:
                            player.rect.y=280
                        healthPlayer=0
                        first1=False
                        death=True
                        right1=False
                        left1=False
                        shield1=False
                        punch1=False
                        kick1=False
                        tornado=False

                #updating health
                if death==False and death1==False:
                    health1.image=pygame.Surface((healthPlayer,25))
                
                #color of health bars
                if healthPlayer>100:
                    health1.image.fill(GREEN)
                if healthPlayer>50 and healthPlayer<=100:
                    health1.image.fill(YELLOW)
                if healthPlayer<=50:
                    health1.image.fill(RED)
            
        #adding all the sprites to a spritegroup      
        all_sprites=pygame.sprite.Group()
        player=Player()
        health=Health()
        player1=player1()
        health1=Health1()
        all_sprites.add(player)
        all_sprites.add(health)
        all_sprites.add(player1)
        all_sprites.add(health1)
        
        #When in the game
        while inPlay:
            pygame.event.get()
            keys=pygame.key.get_pressed()
            clock.tick(50)
            
            #Detecting all keydown events
            if death==False and death1==False:
                if left==False and right==False and jump==False and shield==False and dunk==False and victory==False:
                    idle=True
                else:
                    idle=False
                if keys[pygame.K_LEFT] and shield==False and death==False and dunk==False and player.rect.x>0:
                    player.rect.x-=2
                    left=True
                else:
                    left=False
                if keys[pygame.K_RIGHT]and shield==False and dunk==False and death==False and player.rect.x<780:
                        player.rect.x +=5
                        right=True
                else:
                    right=False
                if keys[pygame.K_DOWN] and punch==False and kick==False and jump==False and death==False:
                    shield=True
                else:
                    shield=False
                if shield==False and jump==False and death==False:
                    player.rect.y=277
                if keys[pygame.K_UP] and shield==False and death==False:
                    jump=True
                if right1==False and jump1==False and left1==False and tornado==False and victory1==False and death1==False:
                    idle1=True
                else:
                    idle1=False
                if keys[pygame.K_d] and player1.rect.x<770 and shield1==False:
                    player1.rect.x+=2
                    right1=True
                else:
                    right1=False
                if keys[pygame.K_a] and player1.rect.x>0 and shield1==False:
                    player1.rect.x-=5
                    left1=True
                else:
                    left1=False
                if keys[pygame.K_w] and shield1==False and death==False:
                    jump1=True
                if keys[pygame.K_s] and jump1==False and death==False:
                    shield1=True
                else:
                    shield1=False
                if keys[pygame.K_e] and shield1==False and jump1==False and death1==False and victory1==False:
                    tornado=True
                else:
                    tornado=False
                if keys[pygame.K_COMMA] and kick==False and shield==False and dunk==False:
                    punch=True
                if keys[pygame.K_SLASH] and punch==False and shield==False and dunk==False:
                    kick=True
                if keys[pygame.K_LSHIFT] and kick1==False and shield1==False and tornado==False:
                    punch1=True
                if keys[pygame.K_LCTRL] and punch1==False and shield1==False and tornado==False:
                    kick1=True
                if keys[pygame.K_m]:
                    gameScreen=False
                    inPlay=False
                    mainMenu=True
                if keys[pygame.K_SEMICOLON] and shield==False and jump==False:
                    dunk=True   
            if keys[pygame.K_m]:
                gameScreen=False
                inPlay=False
                mainMenu=True
                
            #updating sprites and printing background
            all_sprites.update()    
            gameWindow.blit(background,(0,0))
            all_sprites.draw(gameWindow)
            
            #Check if anyone wins, and prompts to leave to main menu
            if death1==True:
                victory=True
                tornado=False
                death=False
                gameWindow.blit(shaqWin,(300,75))
            if death==True:
                victory1=True
                death1=False
                tornado=False
                gameWindow.blit(kaoriWin,(300,75))
                
            #Update pygame display
            pygame.display.update()
            
#quit the program after user quits
pygame.quit()

import pygame
import time
import random

pygame.init()

white = (255,255,255)
black=(0,0,0)
green = (0,155,0)
red = (255,0,0)

display_width = 800
display_height = 600
pygame.display.set_caption('Slither')
icon =pygame.image.load('apple.png')
pygame.display.set_icon(icon)
AppleThickness = 30
FPS = 15
block_size = 20
direction = 'right'
smallfont = pygame.font.SysFont('comicsansms',25)
medfont = pygame.font.SysFont('comicsansms',50)
largefont = pygame.font.SysFont('comicsansms',80)
clock = pygame.time.Clock()
def pause():
    paused=True
    message_to_screen('PAUSED',black,-100,'large')
    message_to_screen('Press C to  continue q to quit',black,25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)
        clock.tick(5)
def score(score):
    text = smallfont.render('SCORE: '+str(score),True,black)
    gameDisplay.blit(text,[0,0])
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen('Welcome to SLITHER',green,-90,'large')
        message_to_screen('The objective is to eat red apples',black,-30)
        message_to_screen('The more apples you eat the longer you get',black,10)
        message_to_screen('If you run into yourself you lose',black,50)

        message_to_screen('Press c to play ,q to quit ,p to pause',black,180)
        pygame.display.update()
        clock.tick(15)

        
def text_objects(text,color,size):
    if size == 'small':
        textSurface = smallfont.render(text, True,color)
    elif size == 'medium':
        textSurface = medfont.render(text, True,color)
    elif size == 'large':
        textSurface = largefont.render(text, True,color)
   
    return textSurface,textSurface.get_rect()
def randAppleGen():
    randAppleX = round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0
    return randAppleX,randAppleY

                
def message_to_screen(msg,color,y_displace=0,size='small'):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)

    
gameDisplay = pygame.display.set_mode((display_width,display_height))

img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png')
def snake(block_size,snakeList):
    if direction == 'right':
        head = pygame.transform.rotate(img,270)
    if direction == 'left':
        head = pygame.transform.rotate(img,90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img,180)
    gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])
    
#pygame.display.flip()
#pygame.display.update()

def gameLoop():
    global direction
    direction= 'right'
    lead_x=display_width/2
    lead_y=display_height/2

    gameExit= False
    gameOver= False

    randAppleX,randAppleY = randAppleGen()
    lead_x_change = 10
    lead_y_change = 0
    
    snakeList = []
    snakeLength = 1
    
    while not gameExit:
        if gameOver == True:
            
            message_to_screen("Game Over",red,y_displace=-50,size='large')
            message_to_screen("Press c to play again and q to quit",black,y_displace=50,size='medium')
            pygame.display.update()
            
            
        while gameOver==True:
            #gameDisplay.fill(white)
          
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_q:
                        
                        gameExit = True
                        gameOver = False
                
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit= True
                gameOver = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = 'right'
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = 'up'
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = 'down'
                elif event.key==pygame.K_p:
                    pause()
                    

        if lead_x <= 0 or lead_x >= display_width or lead_y >= display_height or lead_y <= 0:
                gameOver = True
        """if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0 --> to move only till key is pressed """ 

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)

        
        #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
            
        
        snake(block_size,snakeList)
        score(snakeLength-1)
        
       #gameDisplay.fill(red,[200,200,50,50])
        
        pygame.display.update()
        

##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
##                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
##                snakeLength+=1
                
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x+block_size>randAppleX and lead_x + block_size<randAppleX +AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength+=1
                

            elif lead_y+block_size>randAppleY and lead_x + block_size<randAppleY +AppleThickness:             
                randAppleX,randAppleY = randAppleGen()
                snakeLength+=1
                            
        clock.tick(FPS)
                
    pygame.quit()
    quit()
game_intro()
gameLoop()


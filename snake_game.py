
# Importing and Initializing

import pygame 
import random
pygame.init()
pygame.mixer.init()


# Game variables

screenW=700
screenH=400
exitgame=False

# Window initialization

gameWindow=pygame.display.set_mode((screenW,screenH))
pygame.display.set_caption("Snake Game")
clock=pygame.time.Clock()

def textRender(text,color,x,y,text_size):
     font=pygame.font.SysFont(None,text_size)
     screenText=font.render(text,True,color)
     gameWindow.blit(screenText,(x,y))

def welcome():
    global exitgame
    global gameover
    pygame.mixer.music.load('welcome.mp3')
    pygame.mixer.music.play(-1)
    while not exitgame:
        
        gameover=False
        
        welcomeImg = pygame.image.load("snake.jpg")
        welcomeImg = pygame.transform.scale(welcomeImg, (700,400))
        gameWindow.blit(welcomeImg,(0,0))
        textRender("Snake",(255,255,255),260,30,45)
        textRender("by",(255,255,255),350,60,25)
        textRender("Mrpnh",(255,0,0),370,80,45)
        textRender("Press Space To Start",(255,255,0),260,125,22)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exitgame=True
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    gameLoop()
                    pygame.mixer.music.load('welcome.mp3')
                    pygame.mixer.music.play(-1)

        
        
        pygame.display.update()


def gameLoop():
    global exitgame
    gameOver=False
    snakeVelX=0
    snakeVelY=0
    snakex=45
    snakeY=55
    snakeSize=8
    initialVel=5
    moveX=1
    moveY=1
    foodX=random.randint(50,650)
    foodY=random.randint(50,350)
    score=0
    snake_list=[]
    snake_len=1

    while not gameOver:
       for event in pygame.event.get():
          if event.type==pygame.QUIT:
              gameOver=True
        
          if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_LEFT and moveX==1:
                   snakeVelX-=initialVel
                   snakeVelY=0
                   moveX=0
                   moveY=1
               if event.key==pygame.K_RIGHT and moveX==1:
                   snakeVelX+=initialVel
                   snakeVelY=0
                   moveX=0
                   moveY=1
               if event.key==pygame.K_UP and moveY==1:
                   snakeVelY-=initialVel
                   snakeVelX=0
                   moveY=0
                   moveX=1
               if event.key==pygame.K_DOWN and moveY==1:
                   snakeVelY+=initialVel
                   snakeVelX=0
                   moveY=0
                   moveX=1
       snakex+=snakeVelX
       snakeY+=snakeVelY

       pygame.Surface.fill(gameWindow,(255,255,255))
    
       if score%80==0 and score!=0:
              pygame.draw.circle(gameWindow,(255,0,0), (foodX,foodY),7,7)
       else:
              pygame.draw.circle(gameWindow,(255,0,0), (foodX,foodY),4,4)

       if abs(snakex-foodX)<8 and abs(snakeY-foodY)<8:
            pygame.mixer.music.load('eat.mp3')
            pygame.mixer.music.play()
            if score%80==0 and score!=0:
                  score+=50
            else:
                  score+=10
            foodX=random.randint(50,650)
            foodY=random.randint(50,350)
            snake_len+=3
    
       head=[]
       head.append(snakex)
       head.append(snakeY)
       snake_list.append(head)
    
       if len(snake_list)>snake_len:
              del snake_list[0]
    
       if head in snake_list[:-1]:
              pygame.mixer.music.stop()
              gameOver=True

       for x,y in snake_list:
              pygame.draw.rect(gameWindow,(0,0,0),(x,y,snakeSize,snakeSize))

       textRender("Score: "+str(score),(255,0,0),600,20,25)
     

       if snakex-5<0 or snakex+11>screenW or snakeY-5<0 or snakeY+11>screenH:
            pygame.mixer.music.stop()
            gameOver=True
       pygame.display.update()
       clock.tick(30)


if __name__ == '__main__':
     welcome()
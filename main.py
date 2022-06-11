import pygame
import time
import numpy as np

def verif():
    for i in range(0,3):
        if (a[i,0]==a[i,1]) and (a[i,2]==a[i,1]) and (a[i,1]!=-1):
            return a[i,1]
    for j in range(0,3):
        if (a[0,j]==a[2,j]) and (a[2,j]==a[1,j]) and (a[1,j]!=-1):
            return a[1,j]
    if (a[0,0] == a[1,1] == a[2,2] and a[0,0]!=-1)or (a[0,2]==a[1,1]==a[2,0]):
        return a[1,1]
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf,TextRect = text_objects(text,largeText)
    TextRect.center = (250,450)
    gameDisplay.blit(TextSurf,TextRect)



def text_objects(text,font):
    textSurface=font.render(text,True,red)
    return textSurface,textSurface.get_rect()

def milieu(x1,x2,y1,y2):
    v=(x1+x2)//2
    w=(y1+y2)//2
    return v , w

def drawO():
    pygame.draw.circle(gameDisplay,black,(v,w),40)
    pygame.draw.circle(gameDisplay,white,(v,w),30)

def drawX():
    pygame.draw.line(gameDisplay,red,(v,w),(v+30,w+30),5)
    pygame.draw.line(gameDisplay,red,(v,w),(v-30,w-30),5)
    pygame.draw.line(gameDisplay,red,(v,w),(v-30,w+30),5)
    pygame.draw.line(gameDisplay,red,(v,w),(v+30,w-30),5)

def debut():
    global elyeswin
    global changer
    global compteur
    compteur=0
    gameDisplay.fill(white)
    pygame.draw.line(gameDisplay,red,(200, 80),(200, 380),5)
    pygame.draw.line(gameDisplay,red,(300, 80),(300, 380),5)
    pygame.draw.line(gameDisplay,red,(105, 167),(405, 167),5)
    pygame.draw.line(gameDisplay,red,(105, 266),(405, 266),5)
    elyeswin=0
    changer=1
    for i in range(0,3):
        for j in range(0,3):
            a[i,j]=-1

def winner():
    global elyeswin
    if verif()==1:
        message_display("X win !")
        elyeswin=1
        
    elif verif()==0:
        message_display("O win !")
        elyeswin=1
    else:
        if compteur==9:
            message_display("Draw Ooo")

elyeswin=0      
changer=1
v=0
w=0
a=np.ones((3,3))
a=a*(-1)
pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
gameDisplay = pygame.display.set_mode((500, 500))
debut()


    

pygame.display.set_caption('TicTacToe made by Elyes K')


while True:
    keys = pygame.key.get_pressed()
    x=pygame.mouse.get_pos()[0]
    y=pygame.mouse.get_pos()[1]
    winner()     
        
    if keys[pygame.K_F1]:
        exit()
    
    if keys[pygame.K_r]:
        debut()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.MOUSEBUTTONUP:
            compteur+=1
            if changer==1:
                if (x>=104 and x<=196) and (y>=81 and y<=165) and (a[0,0]==-1) and (elyeswin==0):
                    v , w = milieu(104,196,81,165)
                    a[0,0]=1
                    drawX()
                    changer=0
                if (x>=200 and x<=300) and (y>=81 and y<=165) and (a[0,1]==-1) and (elyeswin==0):
                    v , w = milieu(200,300,81,165)
                    a[0,1]=1
                    drawX()
                    changer=0
                if (x>=300 and x<=400) and (y>=81 and y<=165) and (a[0,2]==-1) and (elyeswin==0):
                    v , w = milieu(300,400,81,165)
                    a[0,2]=1
                    drawX()
                    changer=0
                if (x>=104 and x<=200) and (y>=166 and y<=265) and (a[1,0]==-1) and (elyeswin==0):
                    v , w = milieu(104,200,166,265)
                    a[1,0]=1
                    drawX()
                    changer=0
                if (x>=200 and x<=300) and (y>=166 and y<=265) and (a[1,1]==-1) and (elyeswin==0):
                    v , w = milieu(200,300,166,265)
                    a[1,1]=1
                    drawX()
                    changer=0
                if (x>=300 and x<=405) and (y>=165 and y<=265) and (a[1,2]==-1) and (elyeswin==0):
                    v , w = milieu(300,405,165,265)
                    a[1,2]=1
                    drawX()
                    changer=0
                if (x>=106 and x<=200) and (y>=266 and y<=380) and (a[2,0]==-1) and (elyeswin==0):
                    v , w = milieu(106,200,266,380)
                    a[2,0]=1
                    drawX()
                    changer=0
                if (x>=200 and x<=300) and (y>=266 and y<=380) and (a[2,1]==-1) and (elyeswin==0):
                    v , w = milieu(200,300,266,380)
                    a[2,1]=1
                    drawX()
                    changer=0
                if (x>=300 and x<=404) and (y>=266 and y<=380) and (a[2,2]==-1) and (elyeswin==0):
                    v , w = milieu(300,404,266,380)
                    a[2,2]=1
                    drawX()
                    changer=0
            else:
                if (x>=104 and x<=196) and (y>=81 and y<=165) and (a[0,0]==-1) and (elyeswin==0):
                    v , w = milieu(104,196,81,165)
                    a[0,0]=0
                    drawO()
                    changer=1
                if (x>=200 and x<=300) and (y>=81 and y<=165) and (a[0,1]==-1) and (elyeswin==0):
                    v , w = milieu(200,300,81,165)
                    a[0,1]=0
                    drawO()
                    changer=1
                if (x>=300 and x<=400) and (y>=81 and y<=165) and (a[0,2]==-1) and (elyeswin==0):
                    v , w = milieu(300,400,81,165)
                    a[0,2]=0
                    drawO()
                    changer=1
                if (x>=104 and x<=200) and (y>=166 and y<=265) and (a[1,0]==-1) and (elyeswin==0):
                    v , w = milieu(104,200,166,265)
                    a[1,0]=0
                    drawO()
                    changer=1
                if (x>=200 and x<=300) and (y>=166 and y<=265) and (a[1,1]==-1) and (elyeswin==0):
                    v , w = milieu(200,300,166,265)
                    a[1,1]=0
                    drawO()
                    changer=1
                if (x>=300 and x<=405) and (y>=165 and y<=265) and (a[1,2]==-1) and (elyeswin==0):
                    v , w = milieu(300,405,165,265)
                    a[1,2]=0
                    drawO()
                    changer=1
                if (x>=106 and x<=200) and (y>=266 and y<=380) and (a[2,0]==-1) and (elyeswin==0):
                    v , w = milieu(106,200,266,380)
                    a[2,0]=0
                    drawO()
                    changer=1
                if (x>=200 and x<=300) and (y>=266 and y<=380) and (a[2,1]==-1) and (elyeswin==0):
                    v , w = milieu(200,300,266,380)
                    a[2,1]=0
                    drawO()
                    changer=1
                if (x>=300 and x<=404) and (y>=266 and y<=380) and (a[2,2]==-1) and (elyeswin==0):
                    v , w = milieu(300,404,266,380)
                    a[2,2]=0
                    drawO()
                    changer=1
    pygame.display.update()

#Name: Bashshar Bin Atif
#Date Stared: 10/21/2019
#Description: As a child, I used to live in a "Haunted House", or so I imagined to be. Using my vivid imagination (and probably not some super natural activities), I would see the curtains over lap forming a Y-shape with an illumanated triangle. This gave me an eriee vibe and scared me as I thought it was some type of monster. Furthermore, when our family used to go to Riyadh, I was terrified by the Kingdom Tower which was a giant 600M tall building with a (usually) purple triangle in the top center. As a child, I thought the "Triangle Monsters" had a giant cult, Kingdom Tower being the HQ. Now as I am older, I spend my weekend nights alone infront of the Lake or peering into closed, dark stores on Lakeshore Drive. The Manquins gave off the same eriee vibe and made me nostalgic of my past. With that, I present you the Honted Store, in front of the lake, with the evil "Triangle Monsters" as the Manaquins. They sense you through thier V shaped eyes and you cannot escape them as they hover fast. They are essentially futuristic ghosts. A.I. is the scariest thing I know so here you go!!!

#The building is based off a real one... so is the lake. ;)

import pygame
import random 
pygame.init()

#Colour Constants
SKY   =  (2,71,147)
LAKE  = (15,30,53)
BLUE1 = (67,125,255)
BLUE2 = (67,125,225)
BLUE3 = (67,125,200)
BLUE4 = (67,125,175)
BLUE5 = (67, 125, 150)
BLUE6 = (67,125, 100)
RED   = (255,0,0)
GRAY  = (174,160,142) 
GRAY2 = (224, 200, 132)
GRAY3 = (125, 108, 87)
WHITE = (255,255,255)
WHITE2= (237, 192, 135)
YELLOW= (255, 254, 176)
BROWN = (84, 61, 52)
GREEN = (70, 115, 74)
BLACK = (0,0,0)
GHOST1 = (61, 9, 59)
GHOST2 = (156, 40, 56)
TRUNK = (115, 108, 103)

#Random Integer Formulation
x_moon = random.randint(1,200) # this selects a random integer from 1 to 100 inclusive
y_moon = random.randint(1,200)  

x_ghost  = random.randint(250,500)
x_ghost3  = random.randint(250,500)
x_ghost1  = random.randint(250,500)

x_ghost2 = random.randint(350,550)
y_ghost2 = random.randint(50,150)

x_ghost4 = random.randint(50,200)
y_ghost4 = random.randint(200,500)

#Size of screen
SIZE = (600,600)
screen = pygame.display.set_mode(SIZE)
#Sky aka background
screen.fill(SKY)

#LAKE
def lake():
    pygame.draw.rect(screen, LAKE, pygame.Rect(0, 300, 600, 600), 0)
def sky(): 
    pygame.draw.rect(screen, BLUE1, pygame.Rect(0, 0, 600, 50), 0)  
    pygame.draw.rect(screen, BLUE2, pygame.Rect(0, 50, 600, 100), 0)  
    pygame.draw.rect(screen, BLUE3, pygame.Rect(0, 100, 600, 150), 0)  
    pygame.draw.rect(screen, BLUE4, pygame.Rect(0, 150, 600, 200), 0)  
    pygame.draw.rect(screen, BLUE5, pygame.Rect(0, 200, 600, 250), 0)      
    pygame.draw.rect(screen, BLUE6, pygame.Rect(0, 250, 600, 300), 0)          
 #The Horrified Moon    
def moon (x,y):
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(x, y, 50, 50 ))
    pygame.draw.ellipse(screen, BLACK, pygame. Rect( x+5, y+10, 10,10))
    pygame.draw.ellipse(screen, BLACK, pygame. Rect( x+30, y+10, 10,10))  
    pygame.draw.ellipse(screen, WHITE, pygame. Rect( x+32.5, y+12.5, 5,5))      
    pygame.draw.ellipse(screen, WHITE, pygame. Rect( x+7.5, y+12.5, 5,5))  
    pygame.draw.ellipse(screen, RED, pygame. Rect( x+10, y+25, 30,20))
#Board Walk
def board():
    pygame.draw.rect(screen, BROWN, pygame.Rect(0, 500, 600, 600), 0) 
#Constructing the Shop
def shop():   
    pygame.draw.ellipse(screen, GRAY3, pygame. Rect(250, 200, 100,100)) 
    pygame.draw.rect(screen, GRAY2, pygame.Rect(250, 250, 100, 50), 0)      
    pygame.draw.rect(screen, GRAY, pygame.Rect(250, 400, 250, 100), 0)
    pygame.draw.rect(screen, GRAY2, pygame.Rect(250, 300, 250, 100 ), 0)
    pygame.draw.line(screen, GRAY3, (240,300),(510,300),10)
    pygame.draw.line(screen, GRAY3, (240,250),(360,250),10)            
    pygame.draw.line(screen, WHITE2, (240,400),(510,400),10) 
    pygame.draw.line(screen, WHITE2, (300,200),(300,150),5)  
    pygame.draw.ellipse(screen, RED, pygame. Rect(295, 145, 10,10)) 
    pygame.draw.ellipse(screen, BLUE6, pygame. Rect(310, 260, 30,30)) 
    pygame.draw.ellipse(screen, BLUE6, pygame. Rect(260, 260, 30,30)) 
    pygame.draw.line(screen, GRAY3, (260,275),(289,275),5)   
    pygame.draw.line(screen, GRAY3, (310,275),(339,275),5)            
    pygame.draw.line(screen, GRAY3, (275,260),(275,289),5)
    pygame.draw.line(screen, GRAY3, (275,260),(275,289),5)            
    pygame.draw.line(screen, GRAY3, (325,260),(325,289),5)      
    
#The arch window (a mix of an ellipse and a rectangle)
def window (x):
    pygame.draw.ellipse(screen, LAKE, pygame. Rect(x+255, 310, 75,50))     
    pygame.draw.rect(screen, LAKE, pygame.Rect(x+255, 330, 75, 60 ), 0)   
    pygame.draw.line(screen, GRAY3, (x+255,330),(x+330,330),5)      
    pygame.draw.line(screen, GRAY3, (x+255,360),(x+330,360),5)   
    pygame.draw.line(screen, GRAY3, (x+292.5,310),(x+292.5,390),5)     

#The arch windows (on the first floor)
def window_1st_floor (x):
    pygame.draw.ellipse(screen, LAKE, pygame. Rect(x+255, 410, 75,50))     
    pygame.draw.rect(screen, LAKE, pygame.Rect(x+255, 430, 75, 60 ), 0)   
    pygame.draw.line(screen, GRAY3, (x+255,430),(x+330,430),5)      
    pygame.draw.line(screen, GRAY3, (x+255,460),(x+330,460),5)   
    pygame.draw.line(screen, GRAY3, (x+292.5,410),(x+292.5,490),5)   
#Smaller window on the right of the door
def mini_window ():
    pygame.draw.ellipse(screen, LAKE, pygame. Rect(465, 440, 30, 30)) 
    pygame.draw.line(screen, GRAY3, (464,455),(495,455),5)   
    pygame.draw.line(screen, GRAY3, (480,440),(480,470),5)     
#The door
def door (x):
    pygame.draw.ellipse(screen, WHITE2, pygame. Rect(x+255, 420, 75,70))     
    pygame.draw.rect(screen, BLACK, pygame.Rect(x+255, 440, 75, 60 ), 0)   
    pygame.draw.line(screen, GRAY3, (x+255,440),(x+330,440),5)      
    pygame.draw.line(screen, GRAY3, (x+292.5,440),(x+292.5,500),5)     
    pygame.draw.ellipse(screen, YELLOW, pygame. Rect(x+300, 470, 10,10)) 
    pygame.draw.ellipse(screen, YELLOW, pygame. Rect(x+275, 470, 10,10)) 

#Planks on the boardwalk
def lines(x):
    pygame.draw.line(screen, BLACK, (x,500),(x,600))  

#The lights
def light(x):
    pygame.draw.rect(screen, BLACK, pygame.Rect(x, 525, 50, 50),0)
    pygame.draw.rect(screen, TRUNK, pygame.Rect(x+20, 525-75, 10, 100),0)
    pygame.draw.ellipse(screen, YELLOW, pygame.Rect(x, 525-115, 50, 50 ))

#The bushed on the shop
def bush(x):
    pygame.draw.ellipse(screen, GREEN, pygame. Rect(x+260, 475, 30,30)) 

#The "Triangle Monsters"
def ghost(x,y):
    pygame.draw.polygon( screen , GHOST2 , [ (x+0,y+0)  , (x+20,y+0) , (x+10,y+20) ] )
    pygame.draw.polygon( screen , GHOST1, [ (x+5,y+20)  , (x+15,y+20) , (x+10,y+60) ] )
    pygame.draw.line(screen, BLACK, (x+5,y+5),(x+10,y+10))  
    pygame.draw.line(screen, BLACK, (x+15,y+5),(x+11,y+10))   

#A bigger variation of the "Triangle Monster"
def ghost2(x,y):
    
    pygame.draw.polygon( screen , GHOST2 , [ (x+0,y+0)  , (x+40,y+0) , (x+20,y+40) ] )
    pygame.draw.polygon( screen , GHOST1 , [ (x+10,y+40)  , (x+30,y+40) , (x+20,y+120) ] )
    pygame.draw.line(screen, BLACK, (x+10,y+10),(x+20,y+20))  
    pygame.draw.line(screen, BLACK, (x+30,y+10),(x+22,y+20))   
    
    
# Calling the functions 
sky()  
lake()
shop() 
board()
moon(x_moon,y_moon)
  
lines(10)
lines(20)
lines(30)
lines(40)
lines(50)
lines(60)
lines(70)
lines(80)
lines(90)
lines(100)
lines(110)
lines(120)
lines(130)
lines(140)
lines(150)
lines(160)
lines(170)
lines(180)
lines(190)
lines(200)
lines(210)
lines(220)
lines(230)
lines(240)
lines(250)
lines(260)
lines(270)
lines(280)
lines(290)
lines(300)
lines(310)
lines(320)
lines(330)
lines(340)
lines(350)
lines(360)
lines(370)
lines(380)
lines(390)
lines(400)
lines(410)
lines(420)
lines(430)
lines(440)
lines(450)
lines(460)
lines(470)
lines(480)
lines(490)
lines(500)
lines(510)
lines(520)
lines(530)
lines(540)
lines(550)
lines(560)
lines(570)
lines(580)
lines(590)
lines(600)

light (50)
light (175)
light (525)
window (0)
window (80)
window (160)
window_1st_floor (0)
window_1st_floor (50)
pygame.draw.line(screen, GRAY3, (317.5,415),(317.5,480),5)   #Adding an extra beam between the two windows.
mini_window()
door (132.5)
ghost (x_ghost,240)
ghost (x_ghost1,330)
ghost (x_ghost3,440)
ghost2 (x_ghost2, y_ghost2)
ghost2 (x_ghost4, y_ghost4)
bush (-20)
bush (0)
bush (20)
bush (40)
bush (60)
bush (80)
bush (100)
bush (200)
bush (220)

pygame.display.flip() 
pygame.wait
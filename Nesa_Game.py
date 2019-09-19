# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:36:50 2019

@author: epras
"""
#Importing Libraries
import pygame
import time
import random
import csv

#Initializing Pygame
pygame.init()

#Game Display height and width
display_width = 600
display_height = 500

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisp = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Pray for Nesamani")
clock = pygame.time.Clock()
#crashed = False
nesaw = 115
hamw = 50
hamh = 85

nesaimg = pygame.image.load('nesa1.png')
hamimg = pygame.image.load('ham.png')
roww = []

#Importing images
def nesa(x,y):
    gameDisp.blit(nesaimg, (x,y))

#For Messages
def text_objects(text,font):
    TextSurface = font.render(text,True,white)
    return TextSurface, TextSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',75)
    Textsurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisp.blit(Textsurf,TextRect)
    pygame.display.update()
    

#Hammer
def hammer(hamx, hamy):
    gameDisp.blit(hamimg, (hamx,hamy))

#Score
def suthi(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Suthiyal: "+str(count),True, white)
    gameDisp.blit(text,(0,0))
    
#MAIN GAME LOOP
def game_loop():
    x = (display_width*0.45)
    y = (display_height*0.75)
    loop_num = 0
    
    ll = 0;rr = 0 #Counting Left/Right Press
    ham_startx = random.randrange(150, (display_width-160))
    ham_starty = -600
    ham_speed = 8       #To change the hammer speed
    x_change = 0
    crashed = False
    suthiyal = 0

    while not crashed:
        loop_num += 1 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            #print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ll = 1
                    x_change = -8   #Move 8 Pixels in Left direction
                elif event.key == pygame.K_RIGHT:
                    rr = 1
                    x_change += 8   #Move 8 Pixels in Right direction
            if event.type == pygame.KEYUP:   
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    ll = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 0
                    rr = 0
        #To Stay in boundary
        if x > 8 and x < display_width-100:
            #print(x)
            x_change = x_change
        elif x<8:
            #print('ee',x)
            x = 8
        elif x > display_width-100:
            x = display_width-150
        x += x_change
        #print(x)
        gameDisp.fill(black)
        
        hammer(ham_startx,ham_starty)
        ham_starty += ham_speed
        nesa(x,y)  
        
        if ham_starty > display_height:
            ham_starty = 0-250
            ham_startx = random.randrange(0,display_width)
            suthiyal += 1
            #ham_speed += 0.25
        suthi(suthiyal)
        #high_score = get_high_score()
        current_score = suthiyal
        #print(high_score)
        print(current_score)
        if y < ham_starty + hamh:
            #print("ss")
            
            #GameOver Condition
            if x+15 > ham_startx and x+15 < ham_startx + hamw or x+15 + nesaw > ham_startx and x+15 + nesaw < ham_startx + nesaw:
                global cur_score
                cur_score = suthiyal
                message_display("AYIOOO..")
                crashed = True
        
        #Lists
        if ll == 1: o1,o2,o3 = [1,0,0]
        elif rr == 1: o1,o2,o3 = [0,0,1]
        else:o1,o2,o3 = [0,1,0]
        row =[x, x-ham_startx,x-300, ham_startx, ham_starty, o1,o2,o3]
        print(row)
        if loop_num % 5 == 0:
            roww.append(row)   #roww contains lists of lists of all the required data
        
        pygame.display.update()
        clock.tick(60)    
        
game_loop()

#FIELDS
fields = ['NESAX','NesaX-hamstartx','NesaX-300','Ham_StartX','Ham_StartY','K_Left','Center','K_Right']
filename = "scores34.csv"

###Writing in CSV  
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(roww)

pygame.quit()


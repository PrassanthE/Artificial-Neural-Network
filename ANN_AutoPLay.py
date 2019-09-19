# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:07:09 2019

@author: epras
"""
#Importing libraries
import pygame
import time
import random
import numpy as np
import pandas as pd
import csv

#Initializing Pygame
pygame.init()

#Game Window width and height
display_width = 600
display_height = 500

#Colours in RGB format
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisp = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Pray for Nesamani")
clock = pygame.time.Clock()

#Image width and height
nesaw = 115
hamw = 50
hamh = 85

#Load Images
nesaimg = pygame.image.load('nesa1.png')
hamimg = pygame.image.load('ham.png')
roww = []

#Load Image
def nesa(x,y):
    gameDisp.blit(nesaimg, (x,y))

def text_objects(text,font):
    TextSurface = font.render(text,True,white)
    return TextSurface, TextSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',75)
    Textsurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisp.blit(Textsurf,TextRect)
    pygame.display.update()

#Importing the training model
from keras.models import load_model
#model = pygam2.return_model()
model = load_model('epagent3')  # For Training the model check pygame4 file

#To predict the values
def epagent(a):
    d = model.predict(np.array(a))[0]
    d = d.tolist()
    print(d)
    if d.index(max(d)) == 0:
        return [-8,[1,0,0]]         #If the first value is high move left
    elif d.index(max(d)) == 2:      #If the third value is high move right
        return [8,[0,0,1]]
    else:return [0,[0,1,0]]

#Display Hammer
def hammer(hamx, hamy):
    gameDisp.blit(hamimg, (hamx,hamy))

#Counting Scores
def suthi(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Suthiyal: "+str(count),True, white)
    gameDisp.blit(text,(0,0))
    
#MAIN GAME LOOP
def game_loop():
    x = (display_width*0.45)
    y = (display_height*0.75)
    loop_num = 0
    ham_startx = random.randrange(150, (display_width-160)) 
    ham_starty = -600 #Initial Y starting point
    ham_speed = 16 #Speed of the hammer
    x_change = 0
    crashed = False
    suthiyal = 0 #For Score

    while not crashed:
        loop_num += 1 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            #print(event)
        
        #Sending this values to the training model to predict the data
        e = [[x,x-ham_startx,x-300, ham_startx, ham_starty]] 
        
        #e = [[x,400-x,ham_startx,ham_starty]]
            #x_change = epagent(d)
        
        
        if x > 8 and x < display_width-100:
            print(x)
            ddd = epagent(e)
            x_change = ddd[0]
            #Append values to roww for every 5 execution of if loop
            if loop_num % 5 == 0:
                row =[x,x-ham_startx,x-300, ham_startx, ham_starty,ddd[1][0],ddd[1][1],ddd[1][2]]
                roww.append(row)
        elif x<8:
            print('ee',x)           #Condition to stay in boundary
            x = 20
        elif x >display_width-100:
            print("ff",x)
            x = display_width-150
        x += x_change
        
        gameDisp.fill(black)    #Game BGM colour
        
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
        #print(current_score)
        if y < ham_starty + hamh:
            #print("ss")
            #Game Over condition
            if x+15 > ham_startx and x+15 < ham_startx + hamw or x+15 + nesaw > ham_startx and x+15 + nesaw < ham_startx + nesaw:
                global cur_score
                cur_score = suthiyal
                message_display("AYIOOO..")
                crashed = True
        pygame.display.update()
        clock.tick(60)    
        
game_loop()

fields = ['NESM','X-HamX','NesaX-400','Ham_StartX','Ham_StartY','K_Left','K_Center','K_Right']
filename = "scores72.csv"  #To get the training data and store it in a CSV file
  
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(roww)
      
pygame.quit()


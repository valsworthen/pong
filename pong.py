# -*- coding: utf-8 -*-
"""
Pong game created with Pygame as an exercice

Contains 3 files: pong.py, classes.py, constantes.py
"""

import pygame
from pygame.locals import *
from constantes import *

from classes import *
import numpy as np

pygame.init()

#opening of the pygame window (square)
fenetre = pygame.display.set_mode((width_window, height_window))
clock=pygame.time.Clock()

pygame.key.set_repeat(10, 1)


while 1:
    clock.tick(60)
    game = 0
    speed_x = 0
    speed_y = 0
    ball_speed = [speed_x,speed_y]
    
      
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            
        if event.type == KEYDOWN:
            #set ball's speed
            speed_x = np.random.uniform(2,4)
            
            speed_y = np.sqrt(speed_norm - speed_x**2)
            ball_speed = [speed_x,speed_y]
            print(ball_speed)
            game = 1 #start game
            
    
    #Display player's bar at initial position
    player = Player()
    player.draw_bar(fenetre)
    
    #Display ball
    ball = Ball(ball_speed)
    ball.draw_ball(fenetre)
    
    pygame.display.flip()
    
    '''GAME LOOP'''
    while game:
        #INPUT
        #automatic movement
        ball.move(player)
               
        pygame.time.delay(5)
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            #UPDATE GAME        
            #move player's bar
            #with mouse
            '''if event.type == MOUSEMOTION:
                if event.rel[1] < 0:
                    player.move('up')
                elif event.rel[1] > 0:
                    player.move('down')'''
	        #with keyboard
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player.move('up')
                elif event.key == K_DOWN:
                    player.move('down')
                
        #RENDER GAME
        #display object at their new positions
        fenetre.fill(BLACK)    
        ball.draw_ball(fenetre)        
        player.draw_bar(fenetre)
        pygame.display.flip()
        
        #losing the game
        if ball.ball.left < 0:
            game = 0
            fenetre.fill(BLACK) 
            pygame.display.flip()
            

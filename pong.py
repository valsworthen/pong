# -*- coding: utf-8 -*-
"""
Pong game created with Pygame as an exercice

Contains 3 files: pong.py, classes.py, constantes.py
"""

try:
    import pygame
except ImportError:
    print('This game require pygame to work!')
    #import pip
    #pip.main(['install', '--user', 'pygame'])
    #import pygame

from pygame.locals import *
from constantes import *

from classes import *
import numpy as np

pygame.init()

#opening of the pygame window (square)
fenetre = pygame.display.set_mode((width_window, height_window))
clock=pygame.time.Clock()

pygame.key.set_repeat(10, 1)

solo = True #MULTIPLAYER ACTIVATED


while 1:
    clock.tick(fps)
    game = 0
    speed_x = 0
    speed_y = 0
    ball_speed = [speed_x,speed_y]


    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()

        if event.type == KEYDOWN:
            #set ball's speed
            if solo:
                sign = 1
            else:
                sign = np.random.choice([-1,1])
            speed_x = sign * np.random.uniform(min_speed_x,max_speed_x)

            speed_y = np.sqrt(speed_norm - speed_x**2)
            ball_speed = [speed_x,speed_y]
            #print(ball_speed)
            game = 1 #start game


    #Display player's bar at initial position
    player1 = Player(x1,y1,width,height)
    player1.draw_bar(fenetre)
    if not solo:
        player2 = Player(x2,y2,width,height)
        player2.draw_bar(fenetre)

    #Display ball
    ball = Ball(speed_x, speed_y)
    ball.draw_ball(fenetre)

    pygame.display.flip()

    '''GAME LOOP'''
    while game:
        #INPUT
        #automatic movement
        ball.check_collision_player1(player1)
        if not solo:
            ball.check_collision_player2(player2)
        ball.move(player1)
        ball.check_collision_window(solo)

        pygame.time.delay(refresh)

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
            pressed_keys = pygame.key.get_pressed()
            if not solo:
                if pressed_keys[K_UP]:
                    player2.move('up')
                elif pressed_keys[K_DOWN]:
                    player2.move('down')

            if pressed_keys[K_z]:
                player1.move('up')
            elif pressed_keys[K_s]:
                player1.move('down')

        #RENDER GAME
        #display object at their new positions
        fenetre.fill(BLACK)
        ball.draw_ball(fenetre)
        player1.draw_bar(fenetre)
        if not solo:
            player2.draw_bar(fenetre)
        pygame.display.flip()

        #losing the game
        if ball.left < 0 or (not solo and ball.right > width_window):
            print('GAME LOST')
            game = 0
            fenetre.fill(BLACK)
            pygame.display.flip()

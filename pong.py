# -*- coding: utf-8 -*-
"""
Pong game created with Pygame as an exercice

Contains 3 files: pong.py, classes.py, constantes.py
"""

try:
    import pygame
except ImportError:
    print('This game require pygame to work!')

from pygame.locals import *
from constantes import *

from classes import *
import numpy as np

pygame.init()

#opening of the pygame window (square)
fenetre = pygame.display.set_mode((width_window, height_window))
myfont = pygame.font.SysFont("monospace", 15)
score_font = pygame.font.SysFont("arial", 100)
clock=pygame.time.Clock()

pygame.key.set_repeat(10, 1)

solo = True #SOLOPLAYER ACTIVATED
welcome = 1
new_game = 0
new_round = 0

def display_score(score_1, score_2):
    label = score_font.render(str(score_1), 1, (255,255,0))
    score_width, score_height = label.get_rect().width, label.get_rect().height
    fenetre.blit(label, (width_window / 3 - score_width / 2,
                    (height_window - score_height) / 2))
    label = score_font.render(str(score_2), 1, (255,255,0))
    fenetre.blit(label, (2*width_window / 3 - score_width / 2,
                    (height_window - score_height) / 2))

def init_new_round():
    fenetre.fill(BLACK)
    pygame.display.flip()
    return 0, 1

def init_new_game():
    new_game = 1 #start new game
    welcome = 0
    fenetre.fill(BLACK)
    return 0, 1

while 1:
    """Home screen"""
    while welcome:
        welcome_screen = pygame.image.load(welcome_img).convert()
        fenetre.blit(welcome_screen, (0,0))
        pygame.display.flip()

        clock.tick(fps)
        #if key is pressed --> quit welcome screen
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_F1:
                    solo = True
                    welcome, new_game = init_new_game()
                elif event.key == K_F2:
                    solo = False
                    welcome, new_game = init_new_game()

    """Initialize new game"""
    while new_game:
        new_game_screen = pygame.image.load(new_game_img).convert()
        fenetre.blit(new_game_screen, (0,0))
        display_score(score_1, score_2)
        pygame.display.flip()
        #Display player's bar at initial position
        player1 = Player(x1,y1,width,height)
        player1.draw_bar(fenetre)
        if not solo:
            player2 = Player(x2,y2,width,height)
            player2.draw_bar(fenetre)

        #Display ball
        ball = Ball(0, 0)
        ball.draw_ball(fenetre)
        speed_x = 0
        speed_y = 0

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
            #Start round
            if event.type == KEYDOWN and event.key == K_p:
                if solo:
                    sign = 1
                else:
                    sign = np.random.choice([-1,1])
                speed_x = sign * np.random.uniform(min_speed_x,max_speed_x)

                speed_y = np.sqrt(speed_norm - speed_x**2)
                ball.speed_x = speed_x
                ball.speed_y = speed_y

                new_game = 0
                new_round = 1
                fenetre.fill(BLACK)

    '''GAME LOOP'''
    while new_round:
        #automatic movement
        ball.check_collision_player1(player1)
        if not solo:
            ball.check_collision_player2(player2)
        ball.move(player1)
        ball.check_collision_window(solo)

        pygame.time.delay(refresh)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()

            #UPDATE GAME
            #move player's bar
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
        display_score(score_1, score_2)
        ball.draw_ball(fenetre)
        player1.draw_bar(fenetre)
        if not solo:
            player2.draw_bar(fenetre)
        pygame.display.flip()

        #losing the game
        if ball.left < 0:
            score_2 += 1
            new_round, new_game = init_new_round()
        if not solo and ball.right > width_window:
            score_1 += 1
            new_round, new_game = init_new_round()

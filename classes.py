# -*- coding: utf-8 -*-
"""
This file implements the main classes of the Pong game, that is the Player and the Ball.
"""
from constantes import *
import pygame
from pygame.locals import *


#Define a player's bar
class Player(pygame.Rect):
    def __init__(self):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    #display player's bar
    def draw_bar(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

    #update the position of player's bar
    def move(self, direction):
        if direction == 'up' and self.y >2:
            self.y -= 3
        if direction == 'down' and (self.y+self.height) < (height_window-2):
            self.y += 3

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#Define the ball
class Ball:
    def __init__(self, speed_x, speed_y):
        self.size = ball_size
        self.x = ball_x
        self.y = ball_y
        self.ball = pygame.Rect(self.x, self.y, self.size, self.size)

        self.speed_x = speed_x
        self.speed_y = speed_y

    #display ball
    def draw_ball(self, screen):
        pygame.draw.rect(screen, WHITE, self.ball)

    #automatic movement
    def move(self, player):
        #check if the ball collides with the paddle, then move it
        self.check_collision_player(player)
        self.ball.x += self.speed_x
        self.ball.y += self.speed_y

    def check_collision_window(self):
        #collision  with the window
        #bounce back horizontally and vertically when the ball collides the window
        if self.ball.right > width_window:
            self.speed_x = - self.speed_x
        if self.ball.top < 0 or self.ball.bottom > height_window:
            self.speed_y = - self.speed_y

    def check_collision_player(self, player):
        #collision with the player
        if self.ball.colliderect(player.rect):
            self.speed_x = - self.speed_x
            self.ball.x = player.rect.right + 4
            #if ball hits the top of the paddle, then move it downwards
            if self.ball.centery > player.rect.centery:
                self.speed_y = - abs(self.speed_y)
            #if ball hits the bottom of the paddle, then move it upwards
            else:
                self.speed_y = abs(self.speed_y)

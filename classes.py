# -*- coding: utf-8 -*-
"""
This file implements the main classes of the Pong game, that is the Player and the Ball. 
"""
from constantes import *
import pygame
from pygame.locals import *


#Define a player's bar
class Player:
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
    def __init__(self, ball_speed):
        self.size = ball_size
        self.x = ball_x
        self.y = ball_y
        self.ball = pygame.Rect(self.x, self.y, self.size, self.size)
        
        self.speed = ball_speed
        
    #display ball
    def draw_ball(self, screen):
        pygame.draw.rect(screen, WHITE, self.ball)
        
    #automatic movement
    def move(self, player):
        self.ball = self.ball.move(self.speed)
        
        #collision  with the window
        #bounce back horizontally and vertically when the ball collides the window
        if self.ball.right > width_window:
            self.speed[0] = - self.speed[0]
        if self.ball.top < 0 or self.ball.bottom > height_window:
            self.speed[1] = - self.speed[1]
            
        #collision with the player
        if self.ball.colliderect(player.rect):
            self.speed[0] = - self.speed[0]
            
            """This part needs fixing"""
            """
            if self.ball.y > player.x:
                self.speed[1] = - self.speed[1] #incorrect
            else:    
                self.speed[0] = - self.speed[0]
            """
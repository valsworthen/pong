# -*- coding: utf-8 -*-
"""
This file implements the main classes of the Pong game, that is the Player and the Ball.
"""
from constantes import *
import pygame
from pygame.locals import *


#Define a player's bar
class Player(pygame.Rect):
    def __init__(self,x,y,width,height):
        Rect.__init__(self, x, y, width, height)


    #display player's bar
    def draw_bar(self, screen):
        pygame.draw.rect(screen, WHITE, self)

    #update the position of player's bar
    def move(self, direction):
        if direction == 'up' and self.y >2:
            self.y -= player_speed
        if direction == 'down' and (self.y+self.height) < (height_window-2):
            self.y += player_speed

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#Define the ball
class Ball(pygame.Rect):
    def __init__(self, speed_x, speed_y):
        Rect.__init__(self, ball_x, ball_y, ball_size, ball_size)

        self.speed_x = speed_x
        self.speed_y = speed_y

    #display ball
    def draw_ball(self, screen):
        pygame.draw.rect(screen, WHITE, self)

    #automatic movement
    def move(self, player):
        #check if the ball collides with the paddle, then move it
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision_window(self, solo):
        #collision  with the window
        #bounce back horizontally and vertically when the ball collides the window
        if solo:
            if self.right > width_window:
                self.speed_x = - self.speed_x
        if self.top < 0 or self.bottom > height_window:
            self.speed_y = - self.speed_y

    def check_collision_player1(self, player):
        #collision with the player
        if self.colliderect(player):
            #check if collision occurred on the top or bottom extremity of the player
            #pb still happens when corner of the ball hits corner of the player
            if (player.collidepoint(self.topleft) or player.collidepoint(self.topright)) and not player.collidepoint(self.bottomleft):
                    self.y = player.bottom + 4
                    self.speed_y = - self.speed_y
            elif (player.collidepoint(self.bottomleft) or player.collidepoint(self.bottomright)) and not player.collidepoint(self.topleft):
                    self.y = player.top - 4
                    self.speed_y = - self.speed_y
            else: #it happened on the right side
                self.speed_x = - self.speed_x
                self.x = player.right + 4
                #if ball hits the bottom of the paddle, then move it downwards
                if self.centery > player.centery + player.height/4:
                    self.speed_y = abs(self.speed_y)
                #if ball hits the top of the paddle, then move it upwards
                elif self.centery < player.centery - player.height/4:
                    self.speed_y = - abs(self.speed_y)

    def check_collision_player2(self, player):
        #collision with the player
        if self.colliderect(player):
            #check if collision occurred on the top or bottom extremity of the player
            #pb still happens when corner of the ball hits corner of the player
            if (player.collidepoint(self.topleft) or player.collidepoint(self.topright)) and not player.collidepoint(self.bottomright):
                    self.y = player.bottom + 4 #collided from bottom
                    self.speed_y = - self.speed_y
            elif (player.collidepoint(self.bottomleft) or player.collidepoint(self.bottomright)) and not player.collidepoint(self.topright):
                    self.y = player.top - 4 #collided from top
                    self.speed_y = - self.speed_y
            else: #it happened on the right side
                self.speed_x = - self.speed_x
                self.right = player.left - 4
                #if ball hits the bottom of the paddle, then move it downwards
                if self.centery > player.centery + player.height/4:
                    self.speed_y = abs(self.speed_y)
                #if ball hits the top of the paddle, then move it upwards
                elif self.centery < player.centery - player.height/4:
                    self.speed_y = - abs(self.speed_y)

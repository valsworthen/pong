# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:28:29 2017

@author: vguiguet
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
        
    #Affiche le rectangle joueur
    def draw_bar(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
    
    #Actualise les coordonnées du rectangle représentant le joueur = DEPLACEMENT    
    def move(self, direction):
        if direction == 'up' and self.y >2:
            self.y -= 3
        if direction == 'down' and (self.y+self.height) < (height_window-2):
            self.y += 3
                    
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        
class Ball:
    def __init__(self, ball_speed):
        self.size = ball_size
        self.x = ball_x
        self.y = ball_y
        self.ball = pygame.Rect(self.x, self.y, self.size, self.size)
        
        self.speed = ball_speed
        
    #Affiche la balle
    def draw_ball(self, screen):
        pygame.draw.rect(screen, WHITE, self.ball)
        
    #Mouvement auto
    def move(self, player):
        self.ball = self.ball.move(self.speed)
        
        #Collision avec le bord
        if self.ball.right > width_window:
            self.speed[0] = - self.speed[0]
        if self.ball.top < 0 or self.ball.bottom > height_window:
            self.speed[1] = - self.speed[1]
            
        #Collision avec player
        """Rajouter des conditions pour le cas de la collision vers le bas"""
        if self.ball.colliderect(player.rect):
            if self.ball.y > player.x:
                self.speed[1] = - self.speed[1] #incorrect
            else:    
                self.speed[0] = - self.speed[0]
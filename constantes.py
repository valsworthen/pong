# -*- coding: utf-8 -*-
"""
This file contains the main constants used in the Pong game
"""

#window's parameters
width_window = 1024
height_window = 640
BLACK = (0,0,0)
refresh = 5
fps = 60


#Player's parameters
width = 30
height = 130
x1 = 5
y1 = height_window / 2 - height / 2
x2 = width_window - width - 5
y2 = y1
player_speed = 5
WHITE = (255, 255, 255)

#Ball's parameters
ball_size = 20
ball_x = width_window / 2 - ball_size / 2
ball_y = height_window / 2 - ball_size / 2

speed_norm = 20
min_speed_x = 2
max_speed_x = 4

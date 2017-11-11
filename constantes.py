# -*- coding: utf-8 -*-
"""
This file contains the main constants used in the Pong game
"""

#window's parameters
width_window = 640
height_window = 480
BLACK = (0,0,0)
refresh = 5
fps = 60


#Player's parameters
width = 30
height = 100
x = width
y = height_window / 2 - height / 2
WHITE = (255, 255, 255)

#Ball's parameters
ball_size = 20
ball_x = width_window / 2 - ball_size / 2
ball_y = height_window / 2 - ball_size / 2

speed_norm = 20
min_speed_x = 2
max_speed_x = 4

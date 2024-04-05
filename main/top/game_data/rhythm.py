'''
OK SO I CHALLENGED VINCENT TO MAKE A RYTHM GAME AND NEED TO MAKE IT BEFORE END OF WEEKEND TUESDAY
THE START DAY IS 4/5/24, FINISH BY FOLLOWING TUSSDAY

Goal:
    -So, here is what I intend to do. I am going to draw a rectangle on the bottom, visible.
    I am going to divide the top if the screen into an even amount, likely 8ths. 
    Squares will be drawn into one of these 8 positions. When they reach the bottom rectangle,
    you have to press the appropriate key.
        - keys can be (normal home typing pos): 
            - left: A, S, D, F
            - right: J, K, L, :
    Once you do, the cube will change color indicating it has been activated. 
    Once the cube is off of the screen, if it is activated, it will add to your score.
    It will also increase a streak. If it is not activated, it will reset your streak 
    and your score will go down.
    Music will be played in the background and somehow synced with these notes.
    
    GOALS:
        - fullscreen appliance, game built for 1080x1920 or whatever that resolution is
        - Get a good bakcground image
        - Get audio working and a map working
        - Get all required pygame things
        - Minimum delay for running as fast as possible (to not accidentally miss keys)
            - efficient cond statements    

    PYGAME NECESSARY:
        - delay:
            pygame.time.delay(10)

        - checking for events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                running = False

        - getting device inputs:
            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pressed()

        - rect with example inputs (must be one line in code):
            player = pygame.draw.rect(
                window, 
                color, 
                (
                    x 
                    y, 
                    width, 
                    height
                )
            )
            
    TODO:
        - NEED TO FIND OUT HOW TO MAP MUSIC INTO GAME, PREFERABLY FINAL PRODUCT IS A LIST
        - FIND OUT HOW TO PRELOAD AUDIO
        - COPY OVER CONCEPTS FROM FLAPPY BIRD
        - MAKE DYNAMIC CUBE GENERATION (2D array with a bool saying to generate a cube,
            and where to draw it (top left coord))
'''

# pip import for libraries
import pip
pip.main(['install', 'pygame'])
print('--------------------------')

# other imports
import pygame
from pygame.locals import *
import random
import time
import timeit
import os
import threading

## pygame essentials
pygame.init()
# dimensions of screen
W, H = pygame.display.Info().current_w, pygame.display.Info().current_h

# establishing window
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("thing!")

#######################################################################################

### CONSTANTS

## screen
WIDTH = W # width of screen
HEIGHT = H # height of screen
ACTIVE_WIDTH = 1920 # width where game will be displayed
ACTIVE_HEIGHT = 1080 # height where game will be displayed

## a crapton of colors (thank you ChatGPT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

## active keys to register
REGISTER = ['a', 's', 'd', 'f', 'j', 'k', 'l', ';']

#######################################################################################

### PRELOADING

## img
bg_img = ''

## font
font_1 = ''

## audio file
file_1 = ''

#######################################################################################

pygame.draw.rect(window, RED, (0,  0, WIDTH, HEIGHT))
pygame.draw.rect(window, BLUE, (0, 0, ACTIVE_WIDTH, ACTIVE_HEIGHT))
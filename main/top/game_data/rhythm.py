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
import json

### pygame 
## pygame
pygame.init()
# W, H = pygame.display.Info().current_w, pygame.display.Info().current_h

#######################################################################################

### CONSTANTS

## screen
WIDTH = 1920 
HEIGHT = 1080

## a crapton of colors (thank you ChatGPT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

## active keys to register
REGISTER = ['a', 's', 'd', 'f', 'j', 'k', 'l', ';']
#EXITS = [[K_LCTRL, K_c], [K_LCTRL, K_w], [K_ESCAPE]]

#######################################################################################

### PRELOADING

# establishing window 
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("thing!")

#######################################################################################

### classes

class Zone:
    def __init__(self):
        #vals to change
        self.move_up = 150
        
        # math (local)
        extra = HEIGHT - self.move_up
        gap = HEIGHT - extra

        # pos
        self.x = 0
        self.y = HEIGHT - self.move_up

        # size
        self.width = WIDTH
        self.height = gap
    
    def draw(self):
        self.zone_rect = pygame.draw.rect(window, RED, (self.x, self.y, self.width, self.height))

class Notes:
    def __init__(self):
        self.points = []
        self.num_cubes = 4
        self.cube_width = 50  # Adjust this as needed

        # Calculate the gap between each cube
        self.gap = (WIDTH - (self.num_cubes * self.cube_width)) / (self.num_cubes + 1)

        # Calculate the x-coordinate for each cube
        for i in range(self.num_cubes):
            self.cube_x = (i + 1) * self.gap + i * self.cube_width
            self.points.append(self.cube_x)

    def draw(self, trust=False, x_val=0, i=[], toggle=False):
        global running
        if trust == False:
            for i in self.points:
                pygame.draw.rect(window, GREEN, (i, 0, 50, 50))
        
        elif trust == True:
            loop = True
            while loop:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                
                if toggle == False:
                    m = pygame.mixer
                    m.init()
                    m.music.load('main/top/game_data/rush.mp3') #vscode path
                    m.music.set_volume(0.75)
                
                window.fill(BLACK)
                pygame.draw.rect(window, YELLOW, (x_val, 0, 50, 50))
                print(f'sleeping for {i[2]}s,', f'{round(1000 * i[2])}ms')
                pygame.time.delay(round(1000 * i[2]))
                pygame.display.update()
                if toggle == False:
                    m.music.play()
                    delay = 1.485
                    delay_ms = int(1000 * delay)
                    pygame.time.delay(delay_ms)
                loop = False

            toggle = True
            return toggle

    def iter(self):
        '''notes
        4: bit delayed, random notes that do not exist
        3: way more synced, with delay = 1.485
        2: 
        '''

        f = open("main\\top\game_data\\audio-out\('vocals', 2).json", 'r')
        thing = json.load(f)
        f.close()

        val = 0
        toggle = False
        print('--------------------------')
        for i in thing:
            if i[0] == 'end':
                pass

            else:
                # for i2 in i:
                #     #print(random.randint(1, 4), i2)
                #     notes.draw(trust=True, x_val=random.randint(1, 4))
                toggle = self.draw(trust=True, x_val=self.points[val], i=i, toggle=toggle)
                if val == 0:
                    val = 1
                elif val == 1:
                    val = 2
                elif val == 2:
                    val = 3
                elif val == 3:
                    val = 0
        print('Playback mapping finished.')
                
#######################################################################################

### INITIALIZE VARIABLES

#######################################################################################
## set up the zone for registering keys
zone = Zone()
notes = Notes()
notes.iter()

running = True
#running = False
y = 0

while running:
    # delay
    pygame.time.delay(10)

    # checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # gathering input data
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # exits if
    keys = pygame.key.get_pressed()
    if keys[K_LCTRL]:
        if keys[K_c]:
            running = False
        elif keys[K_w]:
            running = False
    if keys[K_ESCAPE]:
        running = False

    window.fill(BLACK)


    zone.draw()
    #notes.draw()
    down = pygame.draw.rect(window, BLUE, (0, y, WIDTH, 50))
    y += 2.5

    if zone.zone_rect.colliderect(down):
        if keys[K_w]:
            exit()

    pygame.display.update()
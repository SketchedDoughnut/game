'''
OK SO I CHALLENGED VINCENT TO MAKE A RHYTHM GAME AND NEED TO MAKE IT BEFORE END OF WEEKEND TUESDAY
THE START DAY IS 4/5/24, FINISH BY FOLLOWING TUESDAY

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

## file name
FILE_NAME = 'rhythm.py'
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
class Data_format:
    def __init__(self):
        self.window = None
        self.color =  None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        
class Data:
    def __init__(self):
        self.active_cubes = []
        
    def iter(self):
        ## chat gpt
        while True:
            new_list = []
            for cubex in self.active_cubes:
                #cubex.y = cubex.y + 2.5 * (delta_time)
                #cubex.y = cubex.y + 100 * delta_time
                cubex.y += 0.01
                if cubex.y < HEIGHT:
                    new_list.append(cubex)  # Keep the cube in the list
            self.active_cubes = new_list
            print(len(self.active_cubes))
            #time.sleep(1)
        # Remove cubes that have moved off the screen
        #self.active_cubes = [cubex for cubex in self.active_cubes if cubex.y < HEIGHT]

    def add_to_active(self, obj):
        self.active_cubes.append(obj)

class Profiles:

    def __init__(self):
        
        ## class obj
        self.data = Data()
        ## constants
        self.CUBE_HEIGHT = 10
        self.CUBE_WIDTH = 100

        ## load Whats the Rush by Jesse Woods
        self.p1 = pygame.mixer
        self.p1.init()

        ## load Stayed Gone (Lute and Lillith version)
        self.p2 = pygame.mixer
        self.p2.init()
        # self.p2.music.load('main\\top\\game_data\\songs\\stayed_gone(lute_and_lilith).mp3')
        # self.p2.music.set_volume(0.75)

        ## load Stayed Gone
        self.p3 = pygame.mixer
        self.p3.init()

    def Whats_the_Rush(self): # FUNCTION IS OUT OF DATE
        f = open("main\\top\game_data\\audio-out\('vocals', 3).json", 'r') 
        vocal_track = json.load(f)
        f.close()
        f = open('main\\top\game_data\maps\stayed_gone\\vocal_tracks.json', 'r')
        tracks_pos = json.load(f)
        f.close()

        val = 0
        toggle = False
        obj = Data_format()
        print('--------------------------')
        print('Profile: "Whats the Rush?" by Jesse Woods')
        print('--------------------------')
        for times, tracks in zip(vocal_track, tracks_pos):
            if times[0] == 'end':
                pass
            else:
                #x_val = notes.notes_pos[val]
                x_val = notes.notes_pos[tracks]
                #loop = True
                #while loop:f
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            #running = False
                            break

                main_delay_ms = int(round(times[2], 3) * 1000)
                if toggle == True:
                    print(f'sleeping for {round(times[2], 3)}s,', f'{main_delay_ms}ms')
                    pygame.time.delay(main_delay_ms)
                    #window.fill(BLACK)
                    #pygame.draw.rect(window, YELLOW, (x_val, 0, self.CUBE_WIDTH, self.CUBE_HEIGHT))
                    obj.window = window
                    obj.color = YELLOW
                    obj.x = x_val
                    obj.y = 0
                    obj.width = self.CUBE_WIDTH
                    obj.height = self.CUBE_HEIGHT
                    # obj = [window, YELLOW, x_val, 0, self.CUBE_WIDTH, self.CUBE_HEIGHT]
                    self.data.add_to_active(obj)

                    pygame.display.update()
                if toggle == False:
                    self.p1.music.load('main/top/game_data/songs/rush.mp3') #vscode path
                    self.p1.music.set_volume(0.75)
                    self.p1.music.play()
                    #start_delay = 1.485 # how long lyrics take to start - how long it takes square to travel down screen
                    error = 0.05
                    start_delay = 1.85 - error
                    start_delay_ms = int(1000 * start_delay)
                    #pygame.time.delay(start_delay_ms)
                    print(f'start delaying by {start_delay}s, {start_delay_ms}ms')
                    for i in range(1000, start_delay_ms, 1000):
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               #running = False
                               break
                       #window.fill(BLACK)
                       pygame.time.delay(1000)
                       pygame.display.update()
                    toggle = True

                #loop = False
                # if val == notes.num_cubes - 1:
                #     val = 0
                # else:
                #     val += 1

    def Stayed_Gone(self):
        f = open("main\\top\game_data\\audio-out\('vocals', 7).json", 'r') 
        vocal_track = json.load(f)
        f.close()
        f = open("main\\top\game_data\\audio-out\('vocals', 7).json", 'r')
        tracks_pos = json.load(f)
        f.close()
        val = 0
        toggle = False
        obj = Data_format()
        print('--------------------------')
        print('Profile: "Stayed Gone" by Andrew Underberg, Sam Haft, Christian Borle, Amir Talai, and Joel Perez')
        print('--------------------------')
        for times, tracks in zip(vocal_track, tracks_pos):
            if times[0] == 'end':
                pass
            else:
                x_val = notes.notes_pos[val]
                #x_val = notes.notes_pos[tracks]
                #loop = True
                #while loop:f
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            #running = False
                            break

                main_delay_ms = int(round(times[2], 3) * 1000)
                if toggle == True:
                    print(f'sleeping for {round(times[2], 3)}s,', f'{main_delay_ms}ms')
                    pygame.time.delay(main_delay_ms)
                    #window.fill(BLACK)
                    #pygame.draw.rect(window, YELLOW, (x_val, 0, self.CUBE_WIDTH, self.CUBE_HEIGHT))
                    obj.window = window
                    obj.color = YELLOW
                    obj.x = x_val
                    obj.y = 0
                    obj.width = self.CUBE_WIDTH
                    obj.height = self.CUBE_HEIGHT
                    # obj = [window, YELLOW, x_val, 0, self.CUBE_WIDTH, self.CUBE_HEIGHT]
                    self.data.add_to_active(obj)

                    pygame.display.update()
                if toggle == False:
                    self.p3.music.load('main/top/game_data/songs/stayed_gone.mp3')
                    self.p3.music.set_volume(0.50)
                    self.p3.music.play()
                    #start_delay = 20.775 # how long lyrics take to start - how long it takes square to travel down screen
                    start_delay = 20.275
                    start_delay_ms = int(1000 * start_delay)
                    #pygame.time.delay(start_delay_ms)
                    print(f'start delaying by {start_delay}s, {start_delay_ms}ms')
                    for i in range(1000, start_delay_ms, 1000):
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               #running = False
                               break
                       #window.fill(BLACK)
                       pygame.time.delay(1000)
                       pygame.display.update()
                    toggle = True

                #loop = False
                if val == notes.num_cubes - 1:
                    val = 0
                else:
                    val += 1
        print('Playback done.')

class Notes:
    def __init__(self):
        # profiles class
        self.profiles = Profiles()

        self.notes_pos = []
        self.num_cubes = 6
        self.cube_width = self.profiles.CUBE_WIDTH  # Adjust this as needed

        # Calculate the gap between each cube
        self.gap = (WIDTH - (self.num_cubes * self.cube_width)) / (self.num_cubes + 1)

        # Calculate the x-coordinate for each cube
        for i in range(self.num_cubes):
            self.cube_x = (i + 1) * self.gap + i * self.cube_width
            self.notes_pos.append(self.cube_x)


    # def draw(self, trust=False, x_val=0, i=[], toggle=False):
    #     global running
    #     if trust == False:
    #         for i in self.notes_pos:
    #             pygame.draw.rect(window, GREEN, (i, 0, 50, 50))
        
    #     elif trust == True:
    #         loop = True
    #         while loop:
    #             for event in pygame.event.get():
    #                     if event.type == pygame.QUIT:
    #                         running = False
                
    #             if toggle == False:
    #                 m = pygame.mixer
    #                 m.init()
    #                 m.music.load('main/top/game_data/rush.mp3') #vscode path
    #                 m.music.set_volume(0.75)
                
    #             window.fill(BLACK)
    #             pygame.draw.rect(window, YELLOW, (x_val, 0, 50, 50))
    #             delay_ms = round(1000 * i[2])
    #             print(f'sleeping for {i[2]}s,', f'{delay_ms}ms')
    #             pygame.time.delay(delay_ms)
    #             pygame.display.update()
    #             if toggle == False:
    #                 m.music.play()
    #                 delay = 1.485
    #                 delay_ms = int(1000 * delay)
    #                 pygame.time.delay(delay_ms)
    #             loop = False

    #         toggle = True
    #         return toggle

    # def iter(self):
    #     '''notes
    #     5: honestly my inputs just sucked
    #     4: bit delayed, random notes that do not exist
    #     3: way more synced, with delay = 1.485
    #     2: basically the same to 3, with delay = 1.485
    #     1: similar to 2/3 but more delayed, with delay = 1.485
    #     '''

    #     f = open("main\\top\game_data\\audio-out\('vocals', 3).json", 'r')
    #     thing = json.load(f)
    #     f.close()

    #     val = 0
    #     toggle = False
    #     print('--------------------------')
    #     for i in thing:
    #         if i[0] == 'end':
    #             pass

    #         else:
    #             # for i2 in i:
    #             #     #print(random.randint(1, 4), i2)
    #             #     notes.draw(trust=True, x_val=random.randint(1, 4))
    #             toggle = self.draw(trust=True, x_val=self.notes_pos[val], i=i, toggle=toggle)
    #             if val == 0:
    #                 val = 1
    #             elif val == 1:
    #                 val = 2
    #             elif val == 2:
    #                 val = 3
    #             elif val == 3:
    #                 val = 0

    #     print('--------------------------')
    #     print('Playback mapping finished')
    #     print('--------------------------')
                
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
#######################################################################################

### INITIALIZE VARIABLES

'''
- so first we add the new cube as an object with object.data being all drawing data into a list, called active_notes
- then in the main game loop we will draw each cube in said active list, using object.data
- then we will run the function that will iterate through that list and change object.data.y by the speed it goes down screen
- then we will check for the zone and the right keys being pressed, the right key is linked in object.data.key
- then we will see if it is off the screen, then find index, then remove it from list
- then we will do point eval
'''
#######################################################################################
## set up the zone for registering keys
zone = Zone()
notes = Notes()
#notes.iter()
#notes.profiles.Whats_the_Rush()
#notes.profiles.Stayed_Gone()

music_thread = threading.Thread(target=lambda:notes.profiles.Stayed_Gone())
#music_thread = threading.Thread(target=lambda:notes.profiles.Whats_the_Rush())
music_thread.start()

iter_thread = threading.Thread(target=lambda:notes.profiles.data.iter())
#iter_thread.start()

delay = 10
start = time.time()

prev_time = time.time()
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  # Adjust 60 to your desired FPS
    # delay
    #pygame.time.delay(delay)

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

    #notes.draw()
    # down = pygame.draw.rect(window, BLUE, (0, y, WIDTH, 50))
    # y += speed

    # if zone.zone_rect.colliderect(down):
    #     if keys[K_w]:
    #         exit()
    
    # if down.y > HEIGHT:
    #     end = time.time()
    #     dif = end - start
    #     print(f'Time to go down screen: {round(dif, 2)}s and {1000 * round(dif, 3)}ms at a speed of {speed}, with delay of {delay}')
    #     running = False

    # for i in active:
    #     pygame.draw.rect(i[0], i[1], (i[2], i[3], i[4], i[5]))

    window.fill(BLACK)
    #zone.draw()
    for obj in notes.profiles.data.active_cubes:
        pygame.draw.rect(obj.window, obj.color, (obj.x, obj.y, obj.width, obj.height))
        #iter_thread = threading.Thread(target=lambda:notes.profiles.data.iter())
        #iter_thread.start()
    current_time = time.time()
    delta_time = current_time - prev_time
    prev_time = current_time
    
    delta_time = clock.get_time() / 1000

    #notes.profiles.data.iter()
    pygame.display.update()
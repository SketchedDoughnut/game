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

## environment, vscode (False), run (True)
ENV = False

## active keys to register
#REGISTER = ['a', 's', 'd', 'f', 'j', 'k', 'l', ';']
REGISTER = [[0, K_s], [1, K_d], [2, K_f], [3, K_j], [4, K_k], [5, K_l]]
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
        new_list = []
        for cubex in self.active_cubes:
            cubex.y += 1

            if cubex.y < HEIGHT:
                new_list.append(cubex)
        self.active_cubes = new_list

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

        ## set up music player
        self.player = pygame.mixer
        self.player.init()

    def secondary(self, right_time_track_list, right_track_list):
        print('Secondary music thread started.')
        #print('--------------------------')
        
        ## vars
        # toggle when first starting, starts music and built-in delay
        starting_toggle = False
        
        # main iter loop
        for times_right, track_right in zip(right_time_track_list, right_track_list):
            if times_right[0] == 'end':
                pass
            else:
                main_delay = round(times_right[0], 3)
                main_delay_ms = int(main_delay * 1000)
                if starting_toggle == True:
                    if paused == True:
                        while paused == True:
                            pass
                    elif paused == False:
                        time.sleep(main_delay)
                        x_val = notes.notes_pos[track_right]
                        obj = Data_format()
                        obj.window = window
                        obj.color = RED
                        obj.x = x_val
                        obj.y = 0
                        obj.width = self.CUBE_WIDTH
                        obj.height = self.CUBE_HEIGHT
                        self.data.add_to_active(obj)
                if starting_toggle == False:
                    start_delay = 20.275 - 2.50 # secondary delay for ('timings_1_3-5')
                    start_delay_ms = int(1000 * start_delay)
                    time.sleep(start_delay)
                    starting_toggle = True
        print('Second playback done.')


    def Whats_the_Rush(self): # still needs to be made
        '''
        print('--------------------------')
        print('Profile: "Whats the Rush?" by Jesse Woods')
        print('--------------------------')
        delay: 1.85
        '''

    def Stayed_Gone(self):
        print('--------------------------')
        print('Main music thread started.')
        #filename = os.path.join(wDir, 'setup/analyze.py')
        ## preload files
        # paths
        # get path to working directory
        # https://stackoverflow.com/questions/21957131/python-not-finding-file-in-the-same-directory
        wDir = os.path.dirname(os.path.abspath(__file__))
        if ENV:
            left_timing_path = os.path.join(wDir, "maps\\stayed_gone\\timings_3_0-2.json")
            left_track_path = os.path.join(wDir, "maps\\stayed_gone\\tracks_3_0-2.json")
            right_timing_path = os.path.join(wDir, "maps\\stayed_gone\\timings_1_3-5.json")
            right_track_path = os.path.join(wDir, "maps\\stayed_gone\\tracks_1_3-5.json")
            music_path = os.path.join(wDir, "songs\\stayed_gone.mp3")
        elif not ENV:
            left_timing_path = "main\\top\\game_data\\src\\rhythm\\maps\\stayed_gone\\timings_3_0-2.json"
            left_track_path = "main\\top\\game_data\\src\\rhythm\\maps\\stayed_gone\\tracks_3_0-2.json"
            right_timing_path = "main\\top\\game_data\\src\\rhythm\\maps\\stayed_gone\\timings_1_3-5.json"
            right_track_path = "main\\top\\game_data\\src\\rhythm\\maps\\stayed_gone\\tracks_1_3-5.json"
            music_path = "main\\top\\game_data\\src\\rhythm\\songs\\stayed_gone.mp3"
        # load left time track
        print('Loading left timing track...')
        f = open(left_timing_path, 'r')
        left_time_track_list = json.load(f)
        f.close()
        # load left position track
        print('Loading left position track...')
        f = open(left_track_path, 'r')
        left_track_list = json.load(f)
        f.close()
        print('Loading right timing track...')
        f = open(right_timing_path, 'r')
        right_time_track_list = json.load(f)
        f.close()
        print('Loading right posiition track...')
        f = open(right_track_path, 'r')
        right_track_list = json.load(f)
        f.close()
        #thread object
        secondary_thread = threading.Thread(target=lambda:self.secondary(right_time_track_list, right_track_list))
        secondary_thread.start()
        
        ## vars
        # toggle when first starting, starts music and built-in delay
        starting_toggle = False
        print('--------------------------')
        print('Profile: "Stayed Gone" by Andrew Underberg, Sam Haft, Christian Borle, Amir Talai, and Joel Perez')
        print('--------------------------')
        # main iter loop
        for times_left, track_left in zip(left_time_track_list, left_track_list):
            if times_left[0] == 'end':
                pass
            else:
                main_delay = round(times_left[0], 3)
                main_delay_ms = int(main_delay * 1000)
                if starting_toggle == True:
                    if paused == True:
                        while paused == True:
                            pass
                    elif paused == False:
                        time.sleep(main_delay)
                        x_val = notes.notes_pos[track_left]
                        obj = Data_format()
                        obj.window = window
                        obj.color = BLUE
                        obj.x = x_val
                        obj.y = 0
                        obj.width = self.CUBE_WIDTH
                        obj.height = self.CUBE_HEIGHT
                        self.data.add_to_active(obj)
                if starting_toggle == False:
                    self.player.music.load(music_path)
                    self.player.music.set_volume(0.50)
                    #self.player.music.set_volume(0.00)
                    self.player.music.play()
                    #start_delay = 20.775 # how long lyrics take to start - how long it takes square to travel down screen
                    # 20.275 - travel time
                    #start_delay = 20.275 - 2.75 # delay for timings_0-2.json
                    #start_delay = 20.275 - 2.25 # delay for ('vox vocals 1', 8).json
                    #start_delay = 20.275 - 2.70 # delay for ('vox vocals 1', 8).json
                    #start_delay = 20.275 - 2.70 # delay for timings_2_0-2
                    start_delay = 20.275 - 2.65 # delay for timings_3_0-2
                    start_delay_ms = int(1000 * start_delay)
                    print('Starting playback.')
                    print(f'- start delaying by {start_delay}s, {start_delay_ms}ms')
                    time.sleep(start_delay)
                    starting_toggle = True
        print('Main playback done.')


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


class Points:
    def __init__(self):
        self.total_points = 0
        self.streak = 0
    
    def reset_streak(self):
        self.streak = 0
    
    def point_up(self):
        self.total_points += 1
        self.streak += 1
    
    def point_down(self):
        self.total_points -= 1

                
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
        self.zone_rect = pygame.draw.rect(window, YELLOW, (self.x, self.y, self.width, self.height))


#######################################################################################
## set up class objects
zone = Zone()
notes = Notes()
points = Points()

# start music thread with chosen profile
music_thread = threading.Thread(target=lambda:notes.profiles.Stayed_Gone(), daemon=True)
music_thread.start()

# set up clock (not used)
clock = pygame.time.Clock()

# load booleans
pressed1 = False
pressed2 = False
space_pressed = False
paused = False
running = True
while running:
    # set fps to 60
    # clock.tick(60)
    # delay
    pygame.time.delay(1)

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
            #music_thread.join()
            running = False
        elif keys[K_w]:
            #music_thread.join()
            running = False
    if keys[K_ESCAPE]:
        #music_thread.join()
        running = False
    
    # pause if
    # if keys[K_SPACE]:
    #     if space_pressed == False:
    #         if paused == False:
    #             paused = True
    #             notes.profiles.player.music.pause()
    #         elif paused == True:
    #             paused = False
    #             notes.profiles.player.music.unpause()
    #         space_pressed = True
    # if not keys[K_SPACE]:
    #     space_pressed = False

    ## draws
    window.fill(BLACK)
    # draws the input zone at bottom
    zone.draw()
    # iterates through list of notes
    for obj in notes.profiles.data.active_cubes:
        active_note = pygame.draw.rect(obj.window, obj.color, (obj.x, obj.y, obj.width, obj.height))
        #https://stackoverflow.com/questions/49954039/how-do-you-create-rect-variables-in-pygame-without-drawing-them
        #pygame.Rect(obj.x, obj.y, obj.width, obj.height)
        
        # only do if not paused
        if paused == False:
            # gets collumn of notes
            index = notes.notes_pos.index(obj.x)
            for i in REGISTER:
                active_num1 = REGISTER.index(i)
                if index == REGISTER[active_num1][0]:
                    active_key = REGISTER[active_num1][1]
                    break
                
            # check if note is outside of screen, reset streak and delete if it is - NOT WORKING
            if active_note.y > HEIGHT:
                points.reset_streak()

            # checks if note is within zone
            if active_note.colliderect(zone.zone_rect):
                # checks if the right key is pressed, if so remove note from list and increase points by 1
                if keys[active_key]:
                    #if pressed1 == False: #############
                    notes.profiles.data.active_cubes.remove(obj)
                    points.point_up()
                        #pressed1 = True ################

                #elif not keys[active_key]: ###########
                    #pressed1 = False ############

            # system for preventing spam inputs & deducting points for false inputs, currently not plausible until future development
            # else:
            #     for i in REGISTER:
            #         active_num2 = REGISTER.index(i)
            #         if keys[REGISTER[active_num2][1]]:
            #             if pressed2 == False:
            #                 points.point_down()
            #                 pressed2 = True

            #         elif not keys[REGISTER[active_num2][1]]:
            #             pressed2 = False

    if paused == False:
        # moves notes down
        notes.profiles.data.iter()
    pygame.display.update()

'''
text = font.render(str(level), True, white, None) # text, some bool(?), text color, bg color
text_rect = text.get_rect()
text_rect.center = (25, 30) # some positioning
window.blit(text, text_rect)
'''

pygame.quit()
music_thread.join(timeout=0)
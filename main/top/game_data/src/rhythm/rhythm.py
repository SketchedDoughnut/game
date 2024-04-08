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
        
        ## load files
        print('--------------------------')
        print('Loading "Stayed Gone" files...')
        #f = open("main\\top\game_data\src\\rhythm\setup\\audio-out\('testing2_1-2', 18).json", 'r') # the long ones
        f = open("main\\top\game_data\src\\rhythm\maps\stayed_gone\('timings_1_0-2', 8).json", 'r')
        self.times_left_list = json.load(f)
        f.close()
        #f = open("main\\top\game_data\src\\rhythm\setup\\audio-out\('testing2_1-2', 18).json", 'r')
        #self.times_right_list = json.load(f)
        #f.close()
        #f = open("main\\top\game_data\src\\rhythm\setup\\nums\gen_left.json", 'r') # the long ones
        f = open("main\\top\game_data\src\\rhythm\maps\stayed_gone\\tracks_1_0-2.json", 'r')
        self.track_left_list = json.load(f)
        f.close()
        #f = open("main\\top\game_data\src\\rhythm\setup\\nums\gen_right.json", 'r')
        #self.track_right_list = json.load(f)
        #f.close()


    def Whats_the_Rush(self): # still needs to be made
        '''
        print('--------------------------')
        print('Profile: "Whats the Rush?" by Jesse Woods')
        print('--------------------------')
        delay: 1.85
        '''

    def Stayed_Gone(self):
        val = 0
        toggle = False
        obj = Data_format()
        print('--------------------------')
        print('Profile: "Stayed Gone" by Andrew Underberg, Sam Haft, Christian Borle, Amir Talai, and Joel Perez')
        print('--------------------------')
        # loading all the files (god help me)
        #for times_left, times_right, track_left, track_right in zip(self.times_left_list, self.times_right_list, self.track_left_list, self.track_right_list):
        for times_left, track_left in zip(self.times_left_list, self.track_left_list):
            if times_left[0] == 'end':
                pass
            else:
                #x_val = notes.notes_pos[val]
                #loop = True
                #while loop:f
                # for event in pygame.event.get():
                #         if event.type == pygame.QUIT:
                #             #running = False
                #             break

                main_delay = round(times_left[0], 3)
                main_delay_ms = int(main_delay * 1000)
                if toggle == True:
                    #print(f'sleeping for {round(times[2], 3)}s,', f'{main_delay_ms}ms') #####################################################
                    #pygame.time.delay(main_delay_ms)
                    time.sleep(main_delay)
                    #window.fill(BLACK)
                    #pygame.draw.rect(window, YELLOW, (x_val, 0, self.CUBE_WIDTH, self.CUBE_HEIGHT))
                    #if times_left[1]:
                    x_val = notes.notes_pos[track_left]
                    obj = Data_format()
                    obj.window = window
                    obj.color = BLUE
                    obj.x = x_val
                    obj.y = 0
                    obj.width = self.CUBE_WIDTH
                    obj.height = self.CUBE_HEIGHT
                    # obj = [window, YELLOW, x_val, 0, self.CUBE_WIDTH, self.CUBE_HEIGHT]
                    self.data.add_to_active(obj)
                    # if times_right[1]:
                    #     x_val = notes.notes_pos[track_right]
                    #     obj = Data_format()
                    #     obj.window = window
                    #     obj.color = BLUE
                    #     obj.x = x_val
                    #     obj.y = 0
                    #     obj.width = self.CUBE_WIDTH
                    #     obj.height = self.CUBE_HEIGHT
                    #     # obj = [window, YELLOW, x_val, 0, self.CUBE_WIDTH, self.CUBE_HEIGHT]
                    #     self.data.add_to_active(obj)

                    #pygame.display.update()
                if toggle == False:
                    self.p3.music.load('main\\top\game_data\src\\rhythm\songs\stayed_gone.mp3')
                    self.p3.music.set_volume(0.50)
                    #self.p3.music.set_volume(0.00)
                    self.p3.music.play()
                    #start_delay = 20.775 # how long lyrics take to start - how long it takes square to travel down screen
                    # 20.275 - travel time
                    #start_delay = 20.275 - 2.75 # delay for timings_0-2.json
                    #start_delay = 20.275 - 2.25 # delay for ('vox vocals 1', 8).json
                    start_delay = 20.275 - 2.70 # delay for ('vox vocals 1', 8).json
                    start_delay_ms = int(1000 * start_delay)
                    #pygame.time.delay(start_delay_ms)
                    print('Starting playback.')
                    print(f'- start delaying by {start_delay}s, {start_delay_ms}ms')
                    time.sleep(start_delay)
                    # for i in range(1000, start_delay_ms, 1000):
                    #    for event in pygame.event.get():
                    #        if event.type == pygame.QUIT:
                    #            #running = False
                    #            break
                    #    #window.fill(BLACK)
                    #    #pygame.time.delay(1000)
                    #    #time.sleep(1)
                    #    pygame.display.update()
                    toggle = True

                #loop = False
                # if val == notes.num_cubes - 1:
                #     val = 0
                # else:
                #     val += 1
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
        self.zone_rect = pygame.draw.rect(window, RED, (self.x, self.y, self.width, self.height))


class Draw:
    def __init__(self):
        for obj in notes.profiles.data.active_cubes:
            pygame.draw.rect(obj.window, obj.color, (obj.x, obj.y, obj.width, obj.height))
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
## set up class objects
zone = Zone()
notes = Notes()
points = Points()

# start music thread with chosen profile
music_thread = threading.Thread(target=lambda:notes.profiles.Stayed_Gone(), daemon=True)
#music_thread = threading.Thread(target=lambda:notes.profiles.Whats_the_Rush())
music_thread.start()

pressed1 = False
pressed2 = False
clock = pygame.time.Clock()
running = True
while running:
    # set fps to 60
    #clock.tick(60)
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

    ## draws
    window.fill(BLACK)
    # draws the input zone at bottom
    zone.draw()
    # iterates through list of notes
    for obj in notes.profiles.data.active_cubes:
        active_note = pygame.draw.rect(obj.window, obj.color, (obj.x, obj.y, obj.width, obj.height))
        #https://stackoverflow.com/questions/49954039/how-do-you-create-rect-variables-in-pygame-without-drawing-them
        #pygame.Rect(obj.x, obj.y, obj.width, obj.height)

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
            
    # moves notes down
    notes.profiles.data.iter()
    #print('total points:', points.total_points, 'total streak:', points.streak)
    pygame.display.update()

print('''
text = font.render(str(level), True, white, None) # text, some bool(?), text color, bg color
text_rect = text.get_rect()
text_rect.center = (25, 30) # some positioning
window.blit(text, text_rect)
''')

pygame.quit()
music_thread.join(timeout=0)
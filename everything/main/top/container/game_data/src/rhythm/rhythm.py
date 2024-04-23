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
# import pip
# pip.main(['install', 'pygame'])
# print('--------------------------')

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
# https://stackoverflow.com/questions/5814125/how-to-designate-where-pygame-creates-the-game-window
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
# W, H = pygame.display.Info().current_w, pygame.display.Info().current_h

#######################################################################################

### CONSTANTS

## file name
FILE_NAME = 'rhythm.py'
## screen
# WIDTH = 1920 
# HEIGHT = 1080
pygame.init()
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

'''
Everything that is dependent on screen dimensions:
- bottom zone
- notes width (height?)
- time delay to handle how much to delay songs / notes for travel from top to bottom of screen
'''
## a crapton of colors (thank you ChatGPT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

## environment, vscode (False), run (True)
ENV = True

## active keys to register
#REGISTER = ['a', 's', 'd', 'f', 'j', 'k', 'l', ';']
REGISTER = [[0, K_s], [1, K_d], [2, K_f], [3, K_j], [4, K_k], [5, K_l]]
DISPLAY_REGISTER = [[0, 'S'], [1, 'D'], [2, 'F'], [3, 'J'], [4, 'K'], [5, 'L']]
#EXITS = [[K_LCTRL, K_c], [K_LCTRL, K_w], [K_ESCAPE]]

#######################################################################################

### PRELOADING

# establishing window 
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption("thing!")

#######################################################################################

### functions

## func var
paused = False
# pausing?
def pause_game():
    while paused:
        pass

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
    '''
    SONGS
    - Boggle by Mega Mango
    - Loser, Baby (as per request) from Hazbin Hotel
    - Everybody Wants to Rule the World (tears for fears)
    '''
    
    def __init__(self):
        
        ## class obj
        self.data = Data()

        ## constants
        self.CUBE_HEIGHT = (10 / 1080) * HEIGHT
        self.CUBE_WIDTH = (100 / 1920) * WIDTH

        ## set up music player
        self.player = pygame.mixer
        self.player.init()


    def music_delay(self, time_amount, path):
        time.sleep(time_amount)
        print('Music delay over, starting song.')
        self.player.music.load(path)
        self.player.music.set_volume(0.50)
        #self.player.music.set_volume(0.00)
        self.player.music.play()

    def secondary(self, right_time_track_list, right_track_list, color):
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
                        print('Secondary sleep over, starting notes.')
                        x_val = notes.notes_pos[track_right]
                        obj = Data_format()
                        obj.window = window
                        obj.color = color
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


    def Whats_the_Rush(self):
        print('--------------------------')
        print('Main music thread started.')
        ## preload files
        # get path to working directory
        # https://stackoverflow.com/questions/21957131/python-not-finding-file-in-the-same-directory
        wDir = os.path.dirname(os.path.abspath(__file__))
        if ENV:
            left_timing_path = os.path.join(wDir, "maps\\rush\\timings_1_0-5.json")
            left_track_path = os.path.join(wDir, "maps\\rush\\tracks_1_0-5.json")
            music_path = os.path.join(wDir, "songs\\rush.mp3")
        elif not ENV:
            left_timing_path = "main\\top\\game_data\\src\\rhythm\\maps\\rush\\timings_1_0-5.json"
            left_track_path = "main\\top\\game_data\\src\\rhythm\\maps\\rush\\tracks_1_0-5.json"
            music_path = "main\\top\\game_data\\src\\rhythm\\songs\\rush.mp3"
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
        
        ## vars
        # toggle when first starting, starts music and built-in delay
        starting_toggle = False
        second_toggle = False
        print('--------------------------')
        print('Profile: "Whats the Rush?" by Jesse Woods')
        print('--------------------------')
        # main iter loop
        for times_left, track_left in zip(left_time_track_list, left_track_list):
            if times_left[0] == 'end':
                pass
            else:
                main_delay = round(times_left[0], 3)
                main_delay_ms = int(main_delay * 1000)
                if starting_toggle == True:
                    
                    if paused:
                        while paused:
                            print('player paused')

                    if second_toggle == False:
                        print('- music delay thread started.')
                        threading.Thread(target=lambda:self.music_delay(0.95, music_path)).start()
                        second_toggle = True

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
                    # how long lyrics take to start - how long it takes square to travel down screen
                    #start_delay = 1.85 - 2.65 # delay for timings 1_0-5
                    start_delay = 0
                    start_delay_ms = int(1000 * start_delay)
                    print('Starting playback.')
                    print(f'- start delaying by {start_delay}s, {start_delay_ms}ms')
                    time.sleep(start_delay)
                    print('Main start delay over, starting notes')
                    starting_toggle = True
        print('Main playback done.')

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
        secondary_thread = threading.Thread(target=lambda:self.secondary(right_time_track_list, right_track_list, RED))
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

    def Rule_The_World(self):
        print('--------------------------')
        print('Main music thread started.')
        #filename = os.path.join(wDir, 'setup/analyze.py')
        ## preload files
        # paths
        # get path to working directory
        # https://stackoverflow.com/questions/21957131/python-not-finding-file-in-the-same-directory
        wDir = os.path.dirname(os.path.abspath(__file__))
        if ENV:
            left_timing_path = os.path.join(wDir, "maps\\rule_the_world\\timings_1_0-5.json")
            left_track_path = os.path.join(wDir, "maps\\rule_the_world\\tracks_1_0-5.json")
            music_path = os.path.join(wDir, "songs\\rule_the_world.mp3")
        elif not ENV:
            left_timing_path = "main\\top\\game_data\\src\\rhythm\\maps\\rule_the_world\\timings_1_0-5.json"
            left_track_path = "main\\top\\game_data\\src\\rhythm\\maps\\rule_the_world\\tracks_1_0-5.json"
            music_path = "main\\top\\game_data\\src\\rhythm\\songs\\rule_the_world.mp3"
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
        
        ## vars
        # toggle when first starting, starts music and built-in delay
        starting_toggle = False
        print('--------------------------')
        print('Profile: "Everybody Wants To Rule The World" by Tears for Fears')
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
                    start_delay = 63.5 - 2.65 # delay for timings_1_0-5
                    start_delay_ms = int(1000 * start_delay)
                    print('Starting playback.')
                    print(f'- start delaying by {start_delay}s, {start_delay_ms}ms')
                    time.sleep(start_delay)
                    print('Main start delay over, starting notes')
                    starting_toggle = True
        print('Main playback done.')

    def Boggle(self):
        print('--------------------------')
        print('Main music thread started.')
        #filename = os.path.join(wDir, 'setup/analyze.py')
        ## preload files
        # paths
        # get path to working directory
        # https://stackoverflow.com/questions/21957131/python-not-finding-file-in-the-same-directory
        wDir = os.path.dirname(os.path.abspath(__file__))
        if ENV:
            left_timing_path = os.path.join(wDir, "maps\\boggle\\timings_1_0-5.json")
            left_track_path = os.path.join(wDir, "maps\\boggle\\tracks_1_0-5.json")
            music_path = os.path.join(wDir, "songs\\boggle.mp3")
        elif not ENV:
            left_timing_path = "main\\top\\game_data\\src\\rhythm\\maps\\boggle\\timings_1_0-5.json"
            left_track_path = "main\\top\\game_data\\src\\rhythm\\maps\\boggle\\tracks_1_0-5.json"
            music_path = "main\\top\\game_data\\src\\rhythm\\songs\\boggle.mp3"
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
        
        ## vars
        # toggle when first starting, starts music and built-in delay
        starting_toggle = False
        print('--------------------------')
        print('Profile: "Boggle" by Mega Mango')
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
                    start_delay = 29 - 2.65 # delay for timings_1_0-5 ################################################
                    start_delay_ms = int(1000 * start_delay)
                    print('Starting playback.')
                    print(f'- start delaying by {start_delay}s, {start_delay_ms}ms')
                    time.sleep(start_delay)
                    print('Main start delay over, starting notes')
                    starting_toggle = True
        print('Main playback done.')

    def prof_setup(self):
        # song lists
        self.song_dict = {
            "Stayed Gone": threading.Thread(target=lambda:self.Stayed_Gone(), daemon=True), # Stayed Gone
            "Whats the Rush?": threading.Thread(target=lambda:self.Whats_the_Rush(), daemon=True), # Whats the Rush
            "Everybody Wants To Rule The World": threading.Thread(target=lambda:self.Rule_The_World(), daemon=True), # Everybody Wants to Rule the World
            "Boggle": threading.Thread(target=lambda:self.Boggle(), daemon=True) # Boggle
        }


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


class Draw:
    def __init__(self):
        self.draw_list = []
        self.text_list = []

    def draw(self):
        for obj in self.draw_list:
            pygame.draw.rect(obj.window, obj.color, (obj.x, obj.y, obj.width, obj.height))
        for obj in self.text_list:
            window.blit(obj[0], obj[1])


# class Text: #########################################################################################################
#     def __init__(self):
#         self.num_divs = 6
#         self.div_width = WIDTH / self.num_divs # for the new letter gen system
#         self.divs_pos = []

#         # Calculate the gap between each cube
#         self.gap = (WIDTH - (self.num_divs * self.div_width)) / (self.num_divs + 1)
    
#     def append(self):
#         list_out = []
#         self.move_up = 100
#         font = pygame.font.Font('freesansbold.ttf', round(36 * 1.5))
#         for i in range(self.num_divs):
#             active_letter = DISPLAY_REGISTER[i][1]
#             text = font.render(str(active_letter), True, BLACK, None) # text, some bool(?), text color, bg color
#             self.cube_x = (i + 1) * self.gap + i * self.div_width
#             self.height = HEIGHT - (HEIGHT - self.move_up)

#             # obj format
#             self.obj = Data_format()
#             #self.obj.window = window
#             #self.obj.color = BLACK
#             self.obj.x = self.cube_x + 200
#             self.obj.y = HEIGHT - self.move_up
#             self.obj.width = self.div_width
#             self.obj.height = self.height
#             self.obj = pygame.Rect(self.obj.x, self.obj.y, self.obj.width, self.obj.height)
#             list_out.append([text, self.obj])
            
#         return list_out


class Div:
    def __init__(self):
        # class object
        self.draw = Draw()
        #self.text = Text() #########################################################################################################
        self.divs_pos = []
        self.num_divs = 5
        self.div_width = 10  # Adjust this as needed

        # Calculate the gap between each cube
        self.gap = (WIDTH - (self.num_divs * self.div_width)) / (self.num_divs + 1)

    def append(self):
        for i in range(self.num_divs):
            self.move_up = 150

            self.cube_x = (i + 1) * self.gap + i * self.div_width
            
            self.height = HEIGHT - (HEIGHT - self.move_up)

            self.obj = Data_format()
            self.obj.window = window
            self.obj.color = BLACK
            self.obj.x = self.cube_x
            self.obj.y = HEIGHT - self.move_up
            self.obj.width = self.div_width
            self.obj.height = self.height
            #print('Adding dividers to background draw list...')
            #self.draw.draw_list.append(self.obj)

    def dump_text(self, list_in):
        self.draw.text_list = list_in
        


class Zone:
    def __init__(self):
        # class objects
        self.div = Div()

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
        self.height = (gap / 1080) * HEIGHT

    def append(self):
        # set up draw object
        self.obj = Data_format()
        self.obj.window = window
        self.obj.color = YELLOW
        self.obj.x = self.x
        self.obj.y = self.y
        self.obj.width = self.width
        self.obj.height = self.height
        #print('Adding zone to bg draw list...')
        self.div.draw.draw_list.append(self.obj)
    
    def draw(self):
        #self.div.draw.draw_list.append(self.obj)
        #self.zone_rect = pygame.draw.rect(window, YELLOW, (self.x, self.y, self.width, self.height))
        self.zone_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def handler(self):
        self.append()   
        self.draw()
        self.div.append()
        #self.div.dump_text(self.div.text.append()) #########################################################################################################


#######################################################################################
## set up class objects
zone = Zone()
zone.handler()
notes = Notes()
points = Points()

## NEW ADDITION - before loading song profile, allow them to select
# run display menu
import tools.song_select as ss
chosen_song = ss.display_loop()

# restart vars
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("thing!")

# get dict entry
notes.profiles.prof_setup()
ct = notes.profiles.song_dict[chosen_song] # ct = chosen thread
ct.start()

## OLD SYSTEM
# start music thread with chosen profile
#music_thread = threading.Thread(target=lambda:notes.profiles.Whats_the_Rush(), daemon=True)
#music_thread = threading.Thread(target=lambda:notes.profiles.Stayed_Gone(), daemon=True)
#music_thread.start()

# set up clock (not used)
clock = pygame.time.Clock()

# load booleans
pressed1 = False
pressed2 = False
space_pressed = False
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
    if keys[K_LCTRL]:
        if keys[K_c]:
            #music_thread.join()
            print('--------------------------')
            print('ctrl + c')
            running = False
        elif keys[K_w]:
            #music_thread.join()
            print('--------------------------')
            print('ctrl + w')
            running = False
    if keys[K_ESCAPE]:
        #music_thread.join()
        print('--------------------------')
        print('escape')
        running = False
    
    # pause if
    # if keys[K_SPACE]:
    #     if space_pressed == False:
    #         if paused == False:
    #             paused = True
    #             print('music paused')
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
    #zone.draw()
    zone.div.draw.draw()
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
        #print('iter')
        notes.profiles.data.iter()
    pygame.display.update()

'''
text = font.render(str(level), True, white, None) # text, some bool(?), text color, bg color
text_rect = text.get_rect()
text_rect.center = (25, 30) # some positioning
window.blit(text, text_rect)
'''

pygame.quit()
ct.join(timeout=0)

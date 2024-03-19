# imports
import pygame
from pygame.locals import *
import random
import time

# init
pygame.init()

# dimensions of screen
w, h = pygame.display.Info().current_w, pygame.display.Info().current_h

# window settings
window = pygame.display.set_mode((w, h))
pygame.display.set_caption("thing!")


###################################################


# cube
class Cube:
    def __init__(self):

        # positionhttps://youtu.be/Ir5u9L4VZOo?list=PL3tRBEVW0hiDR4Q_ELqHvxcDqd4uvzbeO&t=110

        self.x = 500
        self.y = h / 2

        # sizing
        self.width = 40
        self.height = 40

        # motion
        self.yv = 0
        self.moving = False

        # environment
        self.grav = 0.5
        self.jump = -7.5

    ## functions aided by friend
    
    # pick color
    def pick_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 

    # generate gravity on cube
    def gravity(self):
        self.yv += self.grav
    
    # update cubes location
    def update_location(self):
        self.y += self.yv 

    # make cube jump
    def jumping(self):
        self.yv = self.jump


###################################################
        

# wall
class Walls:
    def __init__(self):

        # position
        self.x = w
        self.gap = 6
        #self.gap = 10

        # sizing
        self.width = 100
        self.height = 550  
        #self.height = 1100


    def b_vertical(self):
        #self.y = h
        #self.y -= h / random.randint(1, 10)
        ####### attempt changes below  
        self.b_pos = h / 2
        self.y = random.randint(self.b_pos + self.b_pos / 2, h)
        

    def t_vertical(self):
        #self.y = h
        #self.y = 0.025 * (h / 10)
        ####### attempt changes below 
        self.t_pos = h / 2
        self.y = random.randint(0 + self.t_pos / 2, self.t_pos)
        self.y += self.gap - self.height

    # movement
    def move_wall(self):
        self.x -= 5

    # pick color
    def pick_color(self):
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) 

    
###################################################
# initialize cube
cube = Cube()
cube.pick_color()

# initialize walls
wall_1 = Walls()
wall_1.pick_color()
wall_1.b_vertical()

wall_2 = Walls()
wall_2.pick_color()
wall_2.t_vertical()

# leveling
level = 0

# data list
data_list = []
###################################################

def data(param=0):
#     print(f"""DATA:
#     - WALL 1 (bottom):
#         - gap: {wall_1.gap}
#         - width: {wall_1.width}
#         - height: {wall_1.height}
#         - b_pos: {wall_1.b_pos}
#             - y: {wall_1.y}
#             - color: {wall_1.color}
    
#     - WALL 2 (top):
#         - gap: {wall_2.gap}
#         - width: {wall_2.width}
#         - height: {wall_2.height}
#         - t_pos: {wall_2.t_pos}
#             - y: {wall_2.y}
#             - color: {wall_2.color}

# Walls distance: {(wall_1.y - wall_2.height)}
# ----------------------------------------""")
    temp = 0
    temp2 = 0
    #print(data_list)
    data_list.append(wall_1.y - wall_2.height)
    for i in data_list:
        temp += i 
    temp2 = temp / len(data_list)
    print('----------------------------------------')
    print(f'Walls distance: {(wall_1.y - wall_2.height)}')
    print(f'Avg: {temp2}')
    print(f'Avg (r->2): {round(temp2, 2)}')
    print(f'Total tests: {len(data_list)}/{param}')
    
    return len(data_list)
###################################################

def bounds():
    global running
    if cube.y >= h:
        print('out of bounds: down')
        running = False

    elif cube.y <= 0:
        print('out of bounds: top')
        running = False

'''
- CUBE
        - height: {cube.height}
        - width: {cube.width}
        - jump: {cube.jump}
        - grav: {cube.grav}
        - color: {cube.color}
        - moving: {cube.moving}
'''

###################################################
def config():
    global wall_1
    global wall_2

    counter = 1
    data_list = []

    print('Analyzing screen values...')
    while counter < param:

        wall_1 = Walls()
        wall_1.pick_color()
        wall_1.b_vertical()

        wall_2 = Walls()
        wall_2.pick_color()
        wall_2.t_vertical()
        
        counter += 1
        data_list.append(wall_1.y - wall_2.height)
        print(f'Test: {counter}/{param}')
    
    total = 0
    avg = 0

    for i in data_list:
        total += i 
    avg = total / len(data_list)
    print('----------------------------------------')
    print('Tests complete. Data:')
    print(f'    - Walls distance: {(wall_1.y - wall_2.height)}')
    print(f'    - Avg: {avg}')
    print(f'    - Avg (r->2): {round(avg, 2)}')
    print(f'    - Total tests: {len(data_list)}')
    print('----------------------------------------')

# psuedo for testing
def psuedo():
    param = int(input('Input max test value: '))
    while True:
        global wall_1
        global wall_2

        wall_1 = Walls()
        wall_1.pick_color()
        wall_1.b_vertical()

        wall_2 = Walls()
        wall_2.pick_color()
        wall_2.t_vertical()
        
        if data(param) == param:
            print(f'{param} tests done; cancelling.')
            exit()

# testing
param = 2500
psuedo()
config()

# simulate an environment without pygame visuals

def sim():
    while True:

# main loop
#running = True
running = False
while running:

    # timer for delay
    pygame.time.delay(10)

    # checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

    # check all keys here
    keys = pygame.key.get_pressed()
    if keys[K_LCTRL]: 
        if keys[K_w]:
            print('ctrl + w')
            running = False

    if cube.moving == True:
        cube.gravity()

    if keys[K_SPACE]:
        if cube.moving == False:
            print('starting wall generation, wall movement, cube movement')
        cube.moving = True

    if keys[K_x]:
        cube.moving = False

    if keys[K_SPACE]:
        if cube.moving == True:
            cube.jumping()

    # functions
    if cube.moving == True:
        cube.update_location()


    #cube.pick_color()

    if wall_1.x < (-5 + (-1 * wall_1.width)) and wall_2.x < (-5 - (1 * wall_2.width)):
        print('generating new walls')
        wall_1 = Walls()
        wall_1.pick_color()
        wall_1.b_vertical()

        wall_2 = Walls()
        wall_2.pick_color()
        wall_2.t_vertical()
        #data()  

        level += 1
        print(f'level up: {level}')
    
    if cube.moving == True:
        wall_1.move_wall()
        wall_2.move_wall()
        bounds() 

    # make rect and update display
    window.fill((0, 0, 0))
    player = pygame.draw.rect(window, cube.color, (cube.x, cube.y, cube.width, cube.height))   
    wall_r1 = pygame.draw.rect(window, wall_1.color, (wall_1.x, wall_1.y, wall_1.width, wall_1.height))     
    wall_r2 = pygame.draw.rect(window, wall_2.color, (wall_2.x, wall_2.y, wall_2.width, wall_2.height))    

    # https://www.youtube.com/watch?v=BHr9jxKithk 
    if player.colliderect(wall_r1): 
        print('wall impact: bottom')
        running = False

    elif player.colliderect(wall_r2): 
        print('wall impact: top') 
        running = False

    pygame.display.update() 

# quit if exit loop
pygame.quit()

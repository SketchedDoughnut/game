# imports
import pygame
from pygame.locals import *
import random

# init
pygame.init()

# dimensions of screen
w, h = pygame.display.Info().current_w, pygame.display.Info().current_h

# window settings
window = pygame.display.set_mode((w, h))
pygame.display.set_caption("thing!")

# cube data
class Cube:
    def __init__(self):

        # position
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
    
cube = Cube()

class Walls:
    def __init__(self):

        # position
        self.x = w

        # sizing
        self.width = 100
        self.height = 550

    def b_vertical(self):
        #self.y = h
        #self.y -= h / random.randint(1, 10)
        ####### attempt changes below
        div = h/10
        self.y = -= h / random.randint(4, 5)

    def t_vertical(self):
        #self.y = h
        #self.y = 0.025 * (h / 10)
        ####### attempt changes below 
        div = h/10
        frac = random.randint(1, 2)
        frac /= 2
        self.y = add * div

    # movement
    def move_wall(self):
        self.x -= 5

    # pick color
    def pick_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 

wall_1 = Walls()
wall_1.pick_color()
wall_1.b_vertical()

wall_2 = Walls()
wall_2.pick_color()
wall_2.t_vertical()

def bounds():
    global running
    if cube.y >= h:
        running = False

    elif cube.y <= 0:
        running = False

# main loop
running = True
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
            running = False

    if cube.moving == True:
        cube.gravity()

    if keys[K_SPACE]:
        if cube.moving ==  False:
            print('starting wall generation, wall movement, cube movement')
        cube.moving = True
        if cube.moving == True:
            cube.jumping()

    # functions
    if cube.moving == True:
        cube.update_location()

    #cube.pick_color()

    if wall_1.x < -5 and wall_2.x < -5:
        print('generating new walls')
        wall_1 = Walls()
        wall_1.pick_color()
        wall_1.b_vertical()
        wall_2 = Walls()
        wall_2.pick_color()
        wall_2.t_vertical()
    
    if cube.moving == True:
        wall_1.move_wall()
        wall_2.move_wall()

    if cube.moving == True:
        bounds() 

    # make rect and update display
    window.fill((0, 0, 0))
    player = pygame.draw.rect(window, cube.color, (cube.x, cube.y, cube.width, cube.height))   
    wall_r1 = pygame.draw.rect(window, wall_1.color, (wall_1.x, wall_1.y, wall_1.width, wall_1.height))     
    wall_r2 = pygame.draw.rect(window, wall_2.color, (wall_2.x, wall_2.y, wall_2.width, wall_2.height))    

    # https://www.youtube.com/watch?v=BHr9jxKithk 
    if player.colliderect(wall_r1) or player.colliderect(wall_r2): 
        print('wall impact')
        running = False

    pygame.display.update() 

# quit if exit loop
pygame.quit()

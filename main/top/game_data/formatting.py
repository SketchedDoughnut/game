import time
import os
import pygame
from pygame.locals import *

pygame.init()
WIDTH = 1000
HEIGHT = 1000

##################################################

start = time.time()
end = 0

space = False
time_list = []
goal = input('file name (.txt:) ')

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("thing!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_s]:
        running = True
        break

# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/
m = pygame.mixer
m.init()
m.music.load('main/top/game_data/rush.mp3')
m.music.set_volume(0.25)
m.music.play()

while running:
    # delay
    pygame.time.delay(1)

    # checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # gathering input data
    keys = pygame.key.get_pressed()

    if keys[K_x]:
        print('dumping...')
        f = open(f'main/top/game_data/{goal}.txt', 'w')
        f.write(time_list)
        f.close()
        running = False

    if keys[K_SPACE]:
        if space == False:
            end = round(time.time(), 2)
            dif = round(end - start, 2)
            start = end
            time_list.append([end, start, dif])
            space = True
            print(f"""
start: {start}
end: {end}
dif: {dif}""")
    
    elif not keys[K_SPACE]:
        space = False

    # exits
    if keys[K_LCTRL]:
        if keys[K_c]:
            running = False
        elif keys[K_w]:
            running = False
    if keys[K_ESCAPE]:
        running = False
        
    pygame.display.update()
import time
import os
import pygame
from pygame.locals import *
import json

f = open('main/top/game_data/count/count.json', 'r')
num = json.load(f)
f.close()

pygame.init()
WIDTH = 1000
HEIGHT = 1000

##################################################

start = time.time()
end = 0

space = False
time_list = [['end', 'start', 'dif']]
print('-----------------------------------------')
goal = input('file name (.json): '), num
print('Proceed, S to start.')
print('-----------------------------------------')

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
# https://open.spotify.com/track/75eo472nc6DIqpwlVOA91B?si=77a2e07864e5445a
#m.music.load('main/top/game_data/songs/rush.mp3') #vscode path

# https://open.spotify.com/track/5rmNtZHtAHHbuzFFQ1c4Nd?si=d2f8eefe411c4b49
#m.music.load('main\\top\\game_data\\songs\\stayed_gone(lute_and_lilith).mp3') #vscode path

# https://open.spotify.com/track/4Po97bPnn3ISdEkuJBMt2f?si=6a51325cff4a49e2
m.music.load('main/top/game_data/songs/stayed_gone.mp3') #vscode path


m.music.set_volume(0.75)
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
        f = open(f'main/top/game_data/audio-out/{goal}.json', 'w')
        json.dump(time_list, f)
        f.close()

        print('iterating num...')
        num += 1
        f = open(f'main/top/game_data/count/count.json', 'w')
        json.dump(num, f)
        f.close()
        
        print('Done. Exiting')
        running = False

    if keys[K_SPACE]:
        if space == False:
            end = (time.time())
            dif = (end - start)
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
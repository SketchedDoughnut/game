import pygame
from pygame.locals import *
import json
import os
import requests
import time
import threading

'''
POSSIBLE SOURCES

https://stackoverflow.com/questions/60716016/how-to-get-the-latest-release-version-in-github-only-use-python-requests
https://gist.github.com/pdashford/2e4bcd4fc2343e2fd03efe4da17f577d
https://gist.github.com/jwodder/c0ad1a5a0b6fda18c15dbdb405e1e549
'''

'''
IDEAS

- make a way to create releases that are announcements that can be displayed in game
    - the name "!announce" will trigger it(?)
- create urgency indicators that will demand an update
- make a seperate branch / release tag for game_data and make it wipe and re-install it, KEEP IT SEPERATE FROM ACTUAL DATA (only re-install games)
- check installer version and warn if its out of date
- add a choices function that gets choices with two buttons, you can input: x, y, width, height
'''
# pygame
pygame.init()
WIDTH = 1920
HEIGHT = 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN  = (0, 255, 0)
text_msg = 'Checking for updates...'
_cancel = False
exit = False
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("thing!")

def check_version():
    # globals
    global exit
    global text_msg

    # release destination, working directory, loading version
    dest = 'https://api.github.com/repos/SketchedDoughnut/development/releases/latest' # link format: https://api.github.com/repos/{owner}/{repo}/releases/latest
    wDir = os.path.dirname(os.path.abspath(__file__))
    response = requests.get(dest)
    # print(response.json()["name"])

    # print
    print('----------------------------')

    # check if version file exists (how to handle if not?)
    if os.path.exists(os.path.join(wDir, 'version.json')):
        print('File found: Comparing versions...')

        # loads version
        f = open(f'{wDir}/version.json', 'r')
        version = json.load(f)
        f.close()

        # seeing if there is a difference
        if str(version) != response.json()["name"]:
            print('Name decrepancy: Prompting for update...')

        elif str(version) == response.json()["name"]:
            print('No decrepancy: Exiting...')
            text_msg = 'No updates found.'
            time.sleep(2)
            exit = True


def cancel(mode=0):
    global exit
    global text_msg
    global _cancel
    global check
    if mode == 0:
        _cancel = True
        text_msg = 'Are you sure you want to cancel?'
    if mode == 1:
        _cancel = False
        text_msg = 'Exiting...'
        check.join()
        time.sleep(3)
        exit = True
    if mode == 2:
        _cancel = False
        try:
            idk.join()
        except:
            print('no thread error')
        check = threading.Thread(target=lambda:check_version(), daemon=True)
        check.start()



print('----------------------------')
print('NOTE: THIS UPDATE AGENT IS CURRENTLY DEPRECIATED. WHY? I AM LAZY.')
check = threading.Thread(target=lambda:check_version(), daemon=True)
check.start()

while not exit:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # exits if
    if keys[K_LCTRL]:
            if keys[K_c]:
                cancel(0)
            elif keys[K_w]:
                cancel(0)
    if keys[K_ESCAPE]:
        cancel(0)

    window.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', round(36 * 1.5))
    text = font.render(text_msg, True, WHITE, None) # text, some bool(?), text color, bg color
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    window.blit(text, text_rect)

    if _cancel:
        width = (500)
        height = (HEIGHT / 15)
        x = (WIDTH / 2) - (width / 2)
        y = 3 * (HEIGHT / 5)
        cancel_zone = pygame.draw.rect(window, GREEN, (x, y, width, height))
        y = 4 * (HEIGHT / 5)
        stop = pygame.draw.rect(window, RED, (x, y, width, height))

        if cancel_zone.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                text_msg = 'Exiting...'
                idk = threading.Thread(target=lambda:cancel(1), daemon=True)
                idk.start()
        if stop.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                cancel(2)

    pygame.display.update()

'''
  font = pygame.font.Font('freesansbold.ttf', round(36 * 1.5))
  text = font.render(path_list[1][1], True, WHITE, None) # text, some bool(?), text color, bg color
  text_rect = text1.get_rect(center=(WIDTH / 2, HEIGHT / 4))
  window.blit(text1, text1_rect)
'''

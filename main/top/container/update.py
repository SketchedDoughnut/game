print('----------------------------')
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

'''
OUTLINE

- setup
- starts check for update as a thread
- pygame puts text (from global variable text_msg)
- if X on window, ctrl c, escape, ctrl w: run function as thread (w/ daemon) that loops, setting text_msg to: "Are you sure you want to cancel?", and set _cancel to true
    - if no, set _cancel to False, and join the above function thread
    - if yes, set exit to True, join all threads, have exit code outside of the loop
'''
# pygame
pygame.init()

WIDTH = 300
HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN  = (0, 255, 0)

text_msg = 'Checking for updates...'

_cancel = False
do_exit = False
confirm = False

top_wDir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'setup/data.json')
wDir = os.path.dirname(os.path.abspath(__file__))
################################################################################################

# runs as a thread, checks version while pygame cheeks drawing
def check_version():
    # globals
    global do_exit, text_msg, confirm, _cancel

    # release destination, working directory, loading version
    dest = 'https://api.github.com/repos/SketchedDoughnut/development/releases/latest' # link format: https://api.github.com/repos/{owner}/{repo}/releases/latest
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
            global WIDTH
            global HEIGHT
            do_exit = True
            confirm = False
            WIDTH = pygame.display.Info().current_w
            HEIGHT = pygame.display.Info().current_y
            text_msg = 'Do you want to update?'
            _cancel = True


        elif str(version) == response.json()["name"]:
            print('No decrepancy: exiting...')
            text_msg = 'No updates found.'
            time.sleep(0.5)
            do_exit = True
            confirm = True

# the buttons it draws (yes or no)
def buttons(yes_list, no_list):
    yes_zone = pygame.Rect(yes_list[0], yes_list[1], yes_list[2], yes_list[3])
    no_zone = pygame.Rect(no_list[0], no_list[1], no_list[2], no_list[3])
    return [[GREEN, yes_zone], [RED, no_zone]]

def exit_handler():
    global do_exit, confirm
    time.sleep(3)
    do_exit = True
    confirm = True

def yes_confirm():
    # objective is to reach back up to data.json and change update and bounds
    pass

def no_confirm():
    global _cancel, do_exit, confirm
    cancel = False
    time.sleep(2)
    do_exit = True
    confirm = True
################################################################################################

print('----------------------------')
print('NOTE: THIS UPDATE AGENT IS CURRENTLY DEPRECIATED. WHY? I AM LAZY.')

# button data
width = (250)
height = (HEIGHT / 15)
x = (WIDTH / 2) - (width / 2)
y = 2 * (HEIGHT / 4)
yes = [x, y, width, height] # green
y = 3 * (HEIGHT / 4)
no = [x, y, width, height] # red
objects = buttons(yes, no)
yes_zone = objects[0][1]
no_zone = objects[1][1]

# thread objects
check = threading.Thread(target=lambda:check_version(), daemon=True)
exit_thread = threading.Thread(target=lambda:exit_handler())

# start threads
check.start()

while True:
    do_exit = False
    confirm = False
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("thing!")

    while not do_exit:
        pygame.time.delay(1)

        # if close window, prompt for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                text_msg = 'Exiting...'
                exit_thread.start()

        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        window.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', round(24))
        text = font.render(text_msg, True, WHITE, None) # text, some bool(?), text color, bg color
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        window.blit(text, text_rect)

        if _cancel:
            yes = pygame.draw.rect(window, objects[0][0], (yes_zone))
            no = pygame.draw.rect(window, objects[1][0], (no_zone))
            if yes.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    try:
                        run_no.join()
                    except:
                        pass
                    run_yes = threading.Thread(target=lambda:yes_confirm(), daemon=True)
                    run_yes.start()
            if no.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    try:
                        run_yes.join()
                    except:
                        pass
                    run_no = threading.Thread(target=lambda:no_confirm(), daemon=True)
                    run_no.start()

        pygame.display.update()

    pygame.quit()
    if confirm:
        break

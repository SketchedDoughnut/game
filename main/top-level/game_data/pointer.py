# imports
import pygame
from pygame.locals import *
import random
import time
import os
import threading

# https://youtu.be/YbouZ2X8fGk

# init
pygame.init()

# dimensions of screen
w, h = pygame.display.Info().current_w, pygame.display.Info().current_h

# window settings
#window = pygame.display.set_mode((w, h))
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("thing!")

def mouse_collisions():
    pos = pygame.mouse.get_pos()

    if pos[0] < 50 and pos[0] > -1 and pos[1] < 50 and pos[1] > -1:
        window.fill((0, 255, 0))
    
    elif pos[0] > 350 and pos[0] < 400 and pos[1] < 50 and pos[1] > -1:
        window.fill((0, 0, 255))

    elif pos[0] > 175 and pos[0] < 225 and pos[1] > 175 and pos[1] < 225:
        window.fill((255, 0, 0))

    else:
        window.fill((0, 0, 0))

def drag():
    pos = pygame.mouse.get_pos()
    drag = 0.001

    #m_zone = pygame.draw.rect(window, (255, 0, 0), (175, 175, 50, 50))
    #if not m_zone.collidepoint((pos[0], pos[1])):

    if pos[0] > 225:
        print(pos, 'x out right')
        pygame.mouse.set_pos((pos[0] - drag, pos[1]))

    if pos[1] > 225:
        print(pos, 'y out bottom')
        pygame.mouse.set_pos((pos[0], pos[1] - drag))

    if pos[0] < 175:
        print(pos, 'x out left')
        pygame.mouse.set_pos((pos[0] + drag, pos[1]))

    if pos[1] < 175:
        print(pos, 'y out top')
 
    #else:
    #    print('colliding')

mc = (255, 255, 255)
sm = 0
clicked = False

def change_color():
    global mc
    global sm
    if m_zone.collidepoint(pos):
        window.fill((255, 0, 0))
    elif tl_zone.collidepoint(pos):
        window.fill((0, 255, 0))
    elif tr_zone.collidepoint(pos):
        window.fill((0, 0, 255))
    elif mode.collidepoint(pos):
        if mc == (255, 255, 255):
            mc = (127.5, 127.5, 127.5)
            sm = 1
        elif mc == (127.5, 127.5, 127.5):
            mc = (255, 255, 255)
            sm = 0

pygame.mouse.set_pos((200, 200))
# main loop
running = True
while running:
    # timer for delay
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LCTRL]:
        if keys[K_w]:
            running = False
        elif keys[K_c]:
            running = False

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        try:
            change_color()
        except Exception as e:
            print('rect not yet made:', e)

    ### code goes here
    pos = pygame.mouse.get_pos()
    #print(pos)

    if sm == 1:
        mouse_collisions()
    #drag()
    tl_zone = pygame.draw.rect(window, (0, 255, 0), (0, 0, 50, 50))
    tr_zone = pygame.draw.rect(window, (0, 0, 255), (350, 0, 50, 50))
    m_zone = pygame.draw.rect(window, (255, 0, 0), (175, 175, 50, 50))
    mode = pygame.draw.rect(window, mc, (0, 350, 400, 400))
    ### code ends here

    pygame.display.update()

# quit if exit loop
pygame.quit()
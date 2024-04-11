# the coding gods have screwed me over and I need to redesign this program

# imports
import pygame
from pygame.locals import *
import timeit
import time
import os

pygame.init()

WIDTH = 1920
HEIGHT = 1080

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("thing!")

wDir = os.path.dirname(os.path.abspath(__file__))
path_list = []
path_list.append(os.path.join(wDir, 'src/flappy/flappy.py'))
path_list.append(os.path.join(wDir, 'src/rhythm/rhythm.py'))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Format:
  def __init__(self):
    self.x = None
    self.y = None
    self.width = None
    self.height = None

draw_var = Format()

running = True
while running: 

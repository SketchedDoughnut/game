'''
This is the system responsible for checking for updates, and initiating them.
It has its own pygame interface and whatnot, and is rather simple.
The nature of this file (and any others equipped with a crash handler) is that the
entirety of the code is inside of a try, except. So, if it breaks, the crash handler
can log that to a file then exit smoothly.
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# the coding gods have screwed me over and I need to redesign this program
########################################################################

# this is the main try/except used
try:
  
  # builtin modules
  import os
  import subprocess
  import sys
  import random

  # file imports
  import index_elevator as elevator

  # establish the working directory for later use
  WDIR = os.path.dirname(os.path.abspath(__file__))

  # this is the list of paths for any setup files to be called on
  # each module is in a different file to have it be its own independent system
  # this makes it a bit reliable, because if one system fails the whole thing
  # won't explode :D
  setup_path_list = [
     [os.path.join(WDIR, 'imports.py'), 'Imports agent'],
     [os.path.join(WDIR, 'update.py'), 'Update agent']
  ]

  # this is a list of all of the current games available
  path_list = [
     [os.path.join(WDIR, 'game_data/src/flappy/flappy.py'), 'Flappy bird'],
     [os.path.join(WDIR, 'game_data/src/rhythm/rhythm.py'), 'Rhythm'],
     [os.path.join(WDIR, 'game_data/src/conways-game/main.py'), 'Conways Game Of Life']
  ]

  # here we call on a file to test imports
  # and make sure all dependencies exist
  print(f'Running {setup_path_list[0][1]}...')
  print('----------------------------')
  subprocess.run(f'python "{r'{path}'.format(path=setup_path_list[0][0])}"')
  print('----------------------------')

  # once all of the imports has been tested, the file will likely crash
  # this is because upon initialization of the python IDE the modules do not exist
  # so it needs to restart before it can load these modules
  try:
    import pygame
    from pygame.locals import *
    # import timeit
    # import time
    import json
  except:
     print('Some dependencies do not exist. The program must restart')
     input('Enter anything to exit: ')
     sys.exit()

  # some initial function calls are done here
  # such as running pygame.init
  # it doesn't really matter when it is called,
  # so it is called here-
  pygame.init()

  # set up a majority of the constants (such as colors)
  # or pygame dimensions, or whatnot
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLUE = (0, 0, 255)
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  WIDTH = pygame.display.Info().current_w # 1920
  HEIGHT = pygame.display.Info().current_h # 1080

  # this is the class responsible for building the screen elements
  # it can divide the screen into sections, make rectangles that format themselves,
  # and assign text labels
  # it dynamically scales based on the length of the path_list
  class Format:
    def __init__(self, div_amount: list | int = None): 
       self.builds = [] # each of the created rectangles
       self.section_pos = [] # the positions of each section
       self.text_draw_queue = [] # each of the text to draw 
       self.draw_queue = [] # general queue to draw things

       if div_amount != None: 
          if type(div_amount) == list: self.num_sections = len(div_amount)
          elif type(div_amount) == int: self.num_sections = div_amount
          elif div_amount == None: self.num_sections = None

    # this function is responsible for creating a simple object
    # that has an x, y, width, and height
    def construct(self):
       self.x = None
       self.y = None
       self.width = None
       self.height = None

    # this class is responsible for dividing up the screen
    # it finds out how many sections it needs to divide it into
    def div(self):

      # the amount of sections
      # self.num_sections = len(path_list)
      section_width = HEIGHT / self.num_sections

      # Calculate the gap between each cube
      section_gap = (HEIGHT - (self.num_sections * section_width)) / (self.num_sections + 1)

      # I am not entirely sure what this is supposed to do
      # but according to previous comments:
      # "# Calculate the x-coordinate for each cube"
      for i in range(self.num_sections):
          cube_y = round((i + 1) * section_gap + i * section_width)
          self.section_pos.append(cube_y)

    # this function is responsible for making the rectangle zones
    # that people click on to do stuff
    def build_rect(self):
      for coord in self.section_pos:
        new_rect = pygame.Rect(
           left=0, 
           top=coord, 
           width=WIDTH, 
           height=round(HEIGHT / self.num_sections))
        self.builds.append(new_rect)

    # this function is responsible for creating the text labels
    # for each of the rectangles
    # it might as well be black magic for me
    def assemble_text(self):

      # if the init for pygame has not been ran yet,
      # this will run the pygames init
      if not pygame.font.get_init(): pygame.font.init()

      # establish the font that will be used
      font = pygame.font.Font('freesansbold.ttf', round(36 * 1.5))

      # for each path data in the path_list
      for data in path_list:
            
            # get the text data and render it using the font
            rendered_text = font.render(str(data[1]), True, WHITE, None)

            # establish the center via the x axis and y axis
            x_center = WIDTH / 2
            y_center = (path_list.index(data) + 0.5) * (HEIGHT / self.num_sections)

            # create the rectangle for the text to be cast on, and append it
            # into the queue to display text (used by pygame loop)
            text_rect = text.get_rect(center=(x_center, y_center))
            self.text_draw_queue.append([rendered_text, text_rect])
    
    # this functions job is to assemble an object 
    # that has data, and put it into a list
    # not sure why but eh, its fine 
    def assemble(self):
      for pos in self.section_pos:
        obj = Format().construct()
        obj.x = 0
        obj.y = pos
        obj.width = WIDTH
        obj.height = round(HEIGHT / self.num_sections)
        self.draw_queue.append(obj)

    # this is called on to execute everything else
    # cleanly :D
    def handler(self):
      self.div()
      self.assemble()
      self.assemble_text()
      self.build_rect()

  

  # here we call on the other setup file,
  # which checks for updates
  # it has its own pygame system and open its own window
  print('----------------------------')
  print(f'Running {setup_path_list[1][1]}...')
  subprocess.run(f'python "{r'{path}'.format(path=setup_path_list[1][0])}"')

  # after the update file has been run, this runs
  # if you do confirm you want to update (and restart), 
  # the update.py file will exit. However, that won't exit this
  # file. So this file checks for a value stored by update.json.
  # If the value is true, it will exit from here too which will
  # properly exit the whole thing.
  f = open(f'{WDIR}/state.json', 'r')
  update_state = bool(json.load(f))
  f.close()
  if update_state: sys.exit()

  # we call on the formatting agent, and 
  # start the whole process of dividing up the screen
  setup = Format()
  setup.handler()

  # this file is designed to direct into other games
  # if you are put into those games and exit, you get
  # led back to this file. So due to that, it needs
  # to do certain setup things over and over again
  # each time you return to this file. That is what
  # setup_bool is for. As for select, when you select a game,
  # select indicates that to prevent other actions from happening
  # beyond that point
  setup_bool = False
  select = False

  # yeah.
  path = elevator.Elevator.elevated_universe
  f = open(f'{path}/index/content_url.txt', 'w')
  f.write("gay")
  f.close()

  # this is the main loop that repeats indefinitely
  # unless you exit
  while True:

    # if the program has not done setup yet
    # do it
    if not setup_bool:

      # reset variables
      select = False 
      mouse_pressed = False
      s_pressed = False
      r_pressed = False
      color_list = []

      # for each rectangle zone to draw,
      # assign a random R, G, and B value to it
      # so the colors are random every time
      # makes some cool combinations :D
      # but can be an eyesore at times
      # afterwards, the colors chosen are printed
      # and also further instructions are printed
      for i in setup.draw_queue:
        color_list.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
      print('----------------------------')
      print('Colors:', color_list)
      # print('S to export colors (game_data/ignore/colors.json)')
      print('S to save colors ((install)/universe/index/colors.json)')
      print('R to refresh colors.')

      # reset the pygame.init() (just in case!)
      # and create a new window
      pygame.init()
      WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
      pygame.display.set_caption("thing!")

      # set setup_bool to true
      # now that it is true, this will not run again
      # until it gets set to false
      setup_bool = True

    # ???
    pygame.time.delay(1)

    # for each pygame event, if they want to quit then
    # break out of the loop
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              break
      
    # find out what keys have been pressed
    # and find out where the mouse currently is
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # if any of these keys are pressed,
    # exit the program
    if keys[K_LCTRL]: # if left ctrl + c or w pressed
          if keys[K_c]: break
          elif keys[K_w]: break
    if keys[K_ESCAPE]: break # if escape pressed
    
    # if the key S is pressed and has is not already pressed,
    # use the elevated path and store the new color value
    # in the colors.json file. If the file does not exist, 
    # make a new one first then store the data
    if keys[K_s]:
      if s_pressed == False:
        # f = open(os.path.join(WDIR, 'game_data/ignore/colors.json'), 'r')
        access_path = path + '/index/colors.json'

        # try to open the file
        # will error if file does not exist
        try:

          # try to load the current colors stored
          f = open(access_path, 'r')
          color_load = list(json.load(f))
          f.close()
          color_load.append(color_list)

        # if the file does not exist,
        # the color_load is set to the only colors
        # we currently have
        except FileNotFoundError: 
          color_load = [color_list]

        # open the file, write the new saved colors
        # to the file
        # s_pressed is set to true so this doesn't run again
        f = open(access_path, 'w')
        json.dump(color_load, f)
        f.close()
        # print('- dumped colors into game_data/ignore/colors.json')
        print(f'- dumped colors into {access_path}')
        s_pressed = True

    # if the key S is not pressed, set s_pressed to false
    # this is so that we can check for the event again :D
    elif not keys[K_s]:
      s_pressed = False

    # if the key R is pressed,
    # it has similar behaviors to the above code with s_pressed
    # but instead it applies to r_pressed
    # Anyways, this cycles 3 new colors and stores them in color_list
    if keys[K_r]:
      if r_pressed == False:
          color_list = []
          for i in setup.draw_queue:
            color_list.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
          print('- refreshed colors')
          r_pressed = True
    elif not keys[K_r]:
      r_pressed = False
    


    # iterate over the current color and the current object to draw
    # and draw them onto the window
    for current_obj, current_color in zip(setup.draw_queue, color_list):
      bound = pygame.draw.rect(WINDOW, current_color, (current_obj.x, current_obj.y, current_obj.width, current_obj.height))

      # if the mouse coordinate is colliding with a zone
      # and the person is clicking their mouse
      # set select to true, and find out what they clicked on
      # by saving the index of current_obj in setup.draw_queue
      if bound.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
          selected_index = setup.draw_queue.index(current_obj)
          select = True

    # iterate over all of the text things
    # and blit them onto the window
    for text in setup.text_draw_queue:
      WINDOW.blit(text[0], text[1])
    
    # finally, update the screen
    pygame.display.update()

    # if they did select something, end the pygame window
    if select:
      pygame.quit()
      print('----------------------------')
      running = path_list[selected_index][1]
      print(f'Running {running}...')
      c3 = r'{path}'.format(path=path_list[selected_index][0])
      # os.system(f'python {path_list[num][0]}')
      # os.system(c3)
      subprocess.run(f'python "{c3}"')
      setup_bool = False


  print('----------------------------')
  print('Exiting...')

except Exception as e:
  import os
  import traceback
  import index_crash_handler
  index_crash_handler.Crash_handler(
      error = traceback.format_exc()
  )
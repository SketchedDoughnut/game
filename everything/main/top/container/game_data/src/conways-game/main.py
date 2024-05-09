import pygame
import rendering
import time

# my files
import eval

pygame.init()
WINDOW = pygame.display.set_mode((600,400), pygame.RESIZABLE)
pygame.display.set_caption('Conways Game Of Life')
renderer = rendering.BoardRenderer()

renderer.cellSize = 50
renderer.borderSize = 3
renderer.FPS = 30
renderer.onColor = (97, 26, 122) # not final colors
renderer.offColor = (36, 25, 42)
renderer.backgroundColor = (8,0,12)

# my additions
width = 100
height = 100
board_gen = eval.GenerateBoard(width, height)
generationTickRate = 5
lastTime = time.perf_counter()
tickTimer = 0


renderer.camera.x = board_gen.width / 2 * renderer.cellSize
renderer.camera.y = board_gen.height / 2 * renderer.cellSize

leftMouseButtonDown = False
rightMouseButtonDown = False
paintMode = True
panning = False
lastMousePosition = (0,0)

# pausing 
paused = True
start_menu = True
space_pressed = False
running = True

import start_screen
SS = start_screen.StartScreen(WINDOW)
while running:

    SCREENWIDTH = pygame.display.Info().current_w

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('window quit')
            running = False
        
        elif event.type == pygame.WINDOWRESIZED:
            SS = start_screen.StartScreen(WINDOW)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # originally elif
            if not panning:
                clickedCellLocation = renderer.camera.screenToWorldPoint(event.pos)
                clickedCellLocation = (round(clickedCellLocation[1] / renderer.cellSize),round(clickedCellLocation[0] / renderer.cellSize))
                if clickedCellLocation[0] < board_gen.width and clickedCellLocation[0] >= 0 and clickedCellLocation[1] < board_gen.width and clickedCellLocation[1] >= 0:
                    board_gen.set_state(clickedCellLocation)
            leftMouseButtonDown = False
            panning = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            leftMouseButtonDown = True
            lastMousePosition = (event.pos[0],event.pos[1])
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            rightMouseButtonDown = True
            clickedCellLocation = renderer.camera.screenToWorldPoint(event.pos)
            clickedCellLocation = (round(clickedCellLocation[1] / renderer.cellSize),round(clickedCellLocation[0] / renderer.cellSize))
            paintMode = not board_gen.get_state(clickedCellLocation)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            rightMouseButtonDown = False

        elif event.type == pygame.MOUSEMOTION:
            if leftMouseButtonDown:
                panning = True
                widthScale = pygame.display.get_window_size()[0] / SCREENWIDTH
                worldStart = renderer.camera.screenToWorldPoint(lastMousePosition)
                worldChange = renderer.camera.screenToWorldPoint((event.pos[0],event.pos[1]))
                worldChange = ((worldChange[0] - worldStart[0]) / widthScale, (worldChange[1] - worldStart[1]) / widthScale)
                renderer.camera.x -= worldChange[0] * widthScale
                renderer.camera.y -= worldChange[1] * widthScale
                lastMousePosition = event.pos
            elif rightMouseButtonDown:
                clickedCellLocation = renderer.camera.screenToWorldPoint(event.pos)
                clickedCellLocation = (round(clickedCellLocation[1] / renderer.cellSize),round(clickedCellLocation[0] / renderer.cellSize))
                if clickedCellLocation[0] < board_gen.width and clickedCellLocation[0] > 0 and clickedCellLocation[1] < board_gen.width and clickedCellLocation[1] > 0:
                    board_gen.board[clickedCellLocation[0]][clickedCellLocation[1]] = paintMode

        elif event.type == pygame.MOUSEWHEEL:
            renderer.camera.z = renderer.camera.z * (0.9 ** event.y)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start_menu == True:
                    start_menu = False
                else:
                    paused = not paused
                    print('space:', paused, '->', not paused)
            elif event.key == pygame.K_r:
                board_gen = eval.GenerateBoard(width, height)
            elif event.key == pygame.K_ESCAPE:
                print('menu invoked')
                paused = True
                start_menu = True
            
    deltaTime = time.perf_counter() - lastTime
    lastTime = time.perf_counter()
    tickTimer += deltaTime
    current_board = board_gen.get_current_board()
    if tickTimer > 1 / generationTickRate:
        tickTimer = 0
        if paused == False:
            new_board = board_gen.gen_new_board()
    renderer.tick(WINDOW, current_board)
    if start_menu == True:
        start_menu = SS.draw()
    if tickTimer > 1 / generationTickRate:
        if paused == False:
            current_board = new_board
    pygame.display.update()
    # import os
    # import webbrowser
    # filename = 'file:///'+os.getcwd()+'/' + 'test.html'
    # webbrowser.open_new_tab(filename) 
    # break
pygame.quit()
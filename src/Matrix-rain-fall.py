from random import randint
import pygame
from pygame.locals import *
import Data
import time

SQ_SIZE =  16 
MAX_FPS = 15
IMAGES = {}

'''
Initialize global directory of images
'''
def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK']
    for piece in pieces:
        IMAGES[piece] = pygame.image.load("../images/" + piece +".png")

'''
Main -- Handle user input and update graphics
'''
def main():
    WIDTH, HEIGHT = 1200, 800
    pygame.init()

    screen = pygame.display.set_mode(( WIDTH, HEIGHT ), pygame.RESIZABLE) #, pygame.NOFRAME)
    clock = pygame.time.Clock()

    pygame.display.set_caption('Matrix Rain Fall')
    screen.fill(pygame.Color('black'))
    state = Data.State()

    loadImages()
    
    notNow = int(time.time())

    mainLoop = True
    while mainLoop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(state.dictionary, "\n")
                #print((HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE))
                #state.addDrop(WIDTH / SQ_SIZE, (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE))
            elif event.type == pygame.VIDEORESIZE:
                screen.fill(pygame.Color('black'))
                HEIGHT = screen.get_height()
                WIDTH = screen.get_width()
        
        now = int(time.time()*10 % 60)
        if now != notNow:
            state.update((HEIGHT / SQ_SIZE / 2))    
            
            state.addDrop(WIDTH / SQ_SIZE, (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE))
            state.addDrop(WIDTH / SQ_SIZE, (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE))
        
        notNow = int(time.time()*10 % 60)


        drawState(screen, state)
        clock.tick(MAX_FPS)
        pygame.display.flip()

 
'''
Responsible for all graphics within a current game state
'''   
def drawState(screen, state): #, state):
    HEIGHT = screen.get_height()
    WIDTH = screen.get_width()

    left = (WIDTH / SQ_SIZE / 2) - (WIDTH / SQ_SIZE)
    right = (WIDTH / SQ_SIZE / 2 )
    top = (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE)
    bottom = (HEIGHT / SQ_SIZE / 2)

    for r in range( int(top) -1, int(bottom) +1):
        for c in range( int(left) -1, int(right) +1):

            padding = 0.5
            squareOuter = pygame.Rect(
                (right+c)*SQ_SIZE + padding, 
                (bottom+r)*SQ_SIZE + padding, 
                SQ_SIZE - 2*padding, 
                SQ_SIZE - 2*padding)
            squareOuter2 = pygame.Rect(
                (right+c)*SQ_SIZE, 
                (bottom+r)*SQ_SIZE, 
                SQ_SIZE+1, 
                SQ_SIZE)

            randy = randint(0, 5)

            if (randy == 0):
                img = IMAGES['wR']
            elif (randy == 1):
                img = IMAGES['wN']
            elif (randy == 2):
                img = IMAGES['wB']
            elif (randy == 3):
                img = IMAGES['wQ']
            elif (randy == 4):
                img = IMAGES['wQ']
            elif (randy == 5):
                img = IMAGES['wP']

            pawn = pygame.transform.scale(img, (18,18))

            if (r,c) in state.dictionary:
                screen.fill((0,0,0), squareOuter2)
                if state.dictionary[(r,c)]== (1, 255):
                    fill(pawn, pygame.Color(255, 255, 255))
                elif state.dictionary[(r,c)][0]== 1:
                    fill(pawn, pygame.Color(0, state.dictionary[(r,c)][1] // 2, 0))
                screen.blit(pawn, squareOuter)

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))
            

main()
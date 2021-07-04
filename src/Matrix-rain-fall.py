from random import randint
import pygame
from pygame.locals import *
import Data
import time

SQ_SIZE =  16 
MAX_FPS = 15
IMAGES = {}

# Initialize global directory of images
def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK']
    for i in range(0, 5):
        IMAGES[i] = pygame.image.load("../images/" + pieces[i] +".png")

# Main -- Handle user input and update graphics
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

    dropQuantity = 0
    mainLoop = True
    while mainLoop:

        # Event Handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(len(state.dictionary), "\n")
                #state.dictionary.clear()
                #print((HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE))
                #state.addDrop(WIDTH / SQ_SIZE, (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE))
            elif event.type == pygame.VIDEORESIZE:
                HEIGHT = screen.get_height()
                WIDTH = screen.get_width()
        
        # Update-ticker
        now = int(time.time()*10 % 60)
        if now != notNow:
            # Update Drops
            state.update((HEIGHT / SQ_SIZE / 2))    
            
            # Add Drop
            if(dropQuantity % 2 == 0):
                state.addDrop(WIDTH / SQ_SIZE, (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE))
            dropQuantity += 1
        notNow = now

        # Draw State
        drawState(screen, state)
        clock.tick(MAX_FPS)
        pygame.display.flip()


 
# Responsible for all graphics within a current game state
def drawState(screen, state): #, state):
    HEIGHT = screen.get_height()
    WIDTH = screen.get_width()

    left = (WIDTH / SQ_SIZE / 2) - (WIDTH / SQ_SIZE)
    right = (WIDTH / SQ_SIZE / 2 )
    top = (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE)
    bottom = (HEIGHT / SQ_SIZE / 2)

    for r in range( int(top) -1, int(bottom) +1):
        for c in range( int(left) -1, int(right) +1):

            if (r,c) in state.dictionary:

                squareOuter = pygame.Rect(
                    (right+c)*SQ_SIZE, 
                    (bottom+r)*SQ_SIZE, 
                    SQ_SIZE+1, 
                    SQ_SIZE)
                screen.fill((0,0,0), squareOuter)

                piece = state.dictionary[(r,c)]
                pieceImg = IMAGES[piece[0]]
                pieceColor = (255, 255, 255) if piece[1] == 255 else (0, piece[1] // 2, 0)

                pawn = pygame.transform.scale(pieceImg, (SQ_SIZE,SQ_SIZE))
                fill(pawn, pygame.Color(pieceColor))
                screen.blit(pawn, squareOuter)

def fill(surface, color):
    # Fill all pixels of the surface with color, preserve transparency.
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))
            

main()

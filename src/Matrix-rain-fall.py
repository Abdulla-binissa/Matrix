import pygame
from pygame.locals import *
import Data

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

    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                mainLoop = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = (location[0] - WIDTH / 2) // SQ_SIZE 
                row = (location[1] - HEIGHT / 2) // SQ_SIZE 
                cellSelected = (row, col)

                state.cellClicked(cellSelected)

            elif event.type == pygame.VIDEORESIZE:
                screen.fill(pygame.Color('black'))
                HEIGHT = screen.get_height()
                WIDTH = screen.get_width()
                
        drawState(screen, state)
        clock.tick(MAX_FPS)
        pygame.display.flip()

 
'''
Responsible for all graphics within a current game state
'''   
def drawState(screen, state):
    HEIGHT = screen.get_height()
    WIDTH = screen.get_width()

    left = (WIDTH / SQ_SIZE / 2) - (WIDTH / SQ_SIZE)
    right = (WIDTH / SQ_SIZE / 2 )
    top = (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE)
    bottom = (HEIGHT / SQ_SIZE / 2)

    for r in range( int(top) -1, int(bottom) +1):
        for c in range( int(left) -1, int(right) +1):

            padding, margin = 0.5, 4
            squareOuter = pygame.Rect(
                (right+c)*SQ_SIZE + padding, 
                (bottom+r)*SQ_SIZE + padding, 
                SQ_SIZE - 2*padding, 
                SQ_SIZE - 2*padding)
            squareInner = pygame.Rect(
                (right+c)*SQ_SIZE + padding + margin, 
                (bottom+r)*SQ_SIZE + padding + margin, 
                SQ_SIZE - 2*padding - 2*margin, 
                SQ_SIZE - 2*padding - 2*margin)
            color = state.getCellValue((r,c))

            #pygame.draw.rect(screen, getSquareColor(color), squareOuter)
            #pygame.draw.rect(screen, pygame.Color( "black"), squareInner)
            
            pawn = pygame.transform.scale(IMAGES['wR'], (18,18))
            #fill(pawn, pygame.Color(10, 80, 10))
            fill(pawn, pygame.Color(0, 255, 0))
            screen.blit(pawn, squareOuter)

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

'''
Returns color based on value
'''
def getSquareColor(value):
    return pygame.Color(200, 200, 200)
        
                

main()
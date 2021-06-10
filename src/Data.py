import random
from random import randint

class State():

    def __init__(self):
        self.dictionary = {} #{(row, col): (pieceIMG, brightness)}

    def addDrop(self, width, top):
        screenTop = top - 1
        screenLeft = -width // 2
        screenRight = width // 2
        column = random.randint(screenLeft, screenRight)

        self.dictionary[screenTop, column] = (1, 255)
    
    def update(self, screenBottom):
        temp = dict(self.dictionary) #.copy()
        tailSize = 5

        for cellPos in self.dictionary.keys():
            cellIMG = self.dictionary[cellPos][0]
            cellOpacity = self.dictionary[cellPos][1]
            
            #Update Cell
            opacity = cellOpacity - tailSize if cellOpacity >= tailSize else 0
            cellIMG = cellIMG if randint(0, opacity**2) <= 10000 else randint(0,4)
            temp[cellPos] = (cellIMG, opacity) 
            
            # Add white to next bottom
            if cellPos[0] <= screenBottom:
                temp[(cellPos[0] + 1, cellPos[1])] = (randint(0,4), 255)  
            # Deleting cells
            if cellOpacity < tailSize:
                #del temp[cellPos]
                temp.pop(cellPos)
        
        self.dictionary = temp

        
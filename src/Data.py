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
        tailSize = 10
        keys = self.dictionary.keys()

        for cellPos in list(reversed(keys)):
            cellIMG = self.dictionary[cellPos][0]
            cellOpacity = self.dictionary[cellPos][1]
            
            #Update Cell
            opacity = cellOpacity - tailSize if cellOpacity >= tailSize else 0
            cellIMG = cellIMG if randint(0, (opacity//20)**2) <= 1 else randint(0,4)
            self.dictionary[cellPos] = (cellIMG, opacity) 
            
            # Add white to next bottom
            if cellPos[0] <= screenBottom:
                nextCell = (cellPos[0] + 1, cellPos[1])
                if nextCell not in self.dictionary: 
                    self.dictionary[nextCell] = (randint(0,4), 255)  
                
            # Deleting cells
            if cellOpacity < tailSize:
                #del temp[cellPos]
                self.dictionary.pop(cellPos)

        
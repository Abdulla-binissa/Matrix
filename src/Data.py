import random

class State():

    def __init__(self):
        self.dictionary = {(0,0): (1, 255)} #{(row, col): (value?, brightness)}


    def addDrop(self, width, top):
        screenTop = top - 1
        screenMin = -width // 2
        screenMax = width // 2
        column = random.randint(screenMin, screenMax)

        self.dictionary[screenTop, column] = (1, 255)
    
    def update(self, screenBottom):
        temp = dict(self.dictionary) #.copy()
        tailSize = 5

        for cellPos in self.dictionary.keys():
            cellValue = (self.dictionary[cellPos][0], self.dictionary[cellPos][1])
            #Lower oppacity
            temp[cellPos] = (cellValue[0], cellValue[1] - tailSize) if (cellValue[1] >= tailSize) else (cellValue[0], 0) 
            # Add white to next bottom
            if cellPos[0] <= screenBottom:
                temp[(cellPos[0] + 1, cellPos[1])] = (1, 255)  
            # Deleting cells
            if cellValue[1] < tailSize:
                #del temp[cellPos]
                temp.pop(cellPos)
        
        self.dictionary = temp

        
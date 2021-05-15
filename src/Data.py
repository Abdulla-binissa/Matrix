import random

class State():

    def __init__(self):
        self.dictionary = {(0,0): (1, 255)}


    def addDrop(self, width, top):
        screenTop = top - 1
        screenMin = -width // 2
        screenMax = width // 2
        column = random.randint(screenMin, screenMax)

        self.dictionary[screenTop, column] = (1, 255)

        print(self.dictionary)


    def update(self, screenBottom):
        temp = self.dictionary.copy()
        
        for cellPos in self.dictionary.keys():
            cellValue = (self.dictionary[cellPos][0], self.dictionary[cellPos][1])
            
            #if cellValue[1] <= 0:
               #del temp[cellPos]
                #print("pop")

            if cellValue[1] >= 20:
                temp[cellPos] =  (cellValue[0], cellValue[1] - 20) #Lower oppacity
            else: 
                temp[cellPos] =  (cellValue[0], 0) 
            
            if cellPos[0] <= screenBottom:
                temp[(cellPos[0] + 1, cellPos[1])] = (1, 255)  # Add white to next bottom
            
        
        self.dictionary = temp.copy()

        
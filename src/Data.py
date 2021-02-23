import random

class State():

    def __init__(self):

        self.dictionary = {(0,0): 1}

    def cellClicked(self, cellSelected):
        step = 1
        if cellSelected in self.dictionary.keys():
            value = self.dictionary.get(cellSelected)
            value += step
            if value >= 12: 
                value = 0
            self.dictionary[cellSelected] = round(value, 1)
        else: 
            self.dictionary[cellSelected] = round(step, 1)

    def getCellValue(self, cellSelected):
        if not cellSelected in self.dictionary.keys():
            return 0
        return self.dictionary.get(cellSelected)

    def add(self, centerCell):
        amount = 10
        x = centerCell[0]
        y = centerCell[1]

        for i in range(1, amount):
            for j in range(i + 1):
                x1 = x - i + j
                y1 = y - j
                self.cellClicked( (x1, y1) )

                x2 = x + i - j
                y2 = y + j
                self.cellClicked( (x2, y2) )

            for j in range(1, i):
                x1 = x - j
                y1 = y + i - j
                self.cellClicked( (x1, y1) )

                x2 = x + j
                y2 = y - i + j
                self.cellClicked( (x2, y2) )

    def add2(self, centerCell):
        amount = 10
        x = centerCell[0]
        y = centerCell[1]

        startCell = (x-1, y) # Cell directly above
        checkCell = startCell
        closestCell = startCell

    def add3(self, centerCell):
        amount = 20 * self.dictionary.get(centerCell)
        x = centerCell[0]
        y = centerCell[1]

        ## Step1: Get list of surrounding cells (empty)
            # Iterate with golden angle (137.5) around center cell to get surrounding cells until cells starts to repeat

        ## Step2: Find closest cell within list
            # Break ties with whichever is first in list (should be in order of the 137.5 angle)

        ## Done!







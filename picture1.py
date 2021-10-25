
FILL = 1
EMPTY = 2
BLANK = 0

#rowClues = [ [1],[3],[3],[5],[6],[9],[10],[7,2],[6,1],[7],[7,1],[1,8],[11],[9],[1,3]]

#colClues = [[1],[3],[3,2],[4,4], [6,3],[7,5],[2,12],[11],[9],[9],[8],[5],[1,1],[2,1],[2]]


colClues = [[1], [2], [6], [9], [1,6], [5], [5], [4], [3], [4]]
rowClues = [[2], [1,1], [4], [2,1], [3,1], [8], [8], [7], [5], [3]]

gridSize = 10
grid = []

class Cell:
    def __init__(self,x,y):
        self.state = BLANK
        self.xPos = x
        self.yPos = y
        self.complete = False


for x in range (gridSize):
    for y in range(gridSize):
        cell = Cell(x,y)
        grid.append(cell)

allSolved = True
for cell in grid:
    if cell.complete == False:
        allSolved = True
        rClue = rowClues[cell.xPos]
        cClue = colClues[cell.yPos]

        # Deal with single clues first
        if len(rClue) == 1:
            clue = rClue[0]
            if clue == 6:
                if cell.yPos >= clue - 1 or cell.yPos <= clue + 1:
                    cell.state = FILL
                    cell.complete = True
            if clue == 7:
                if cell.yPos >= clue - 2 or cell.yPos <= clue + 2:
                    cell.state = FILL
                    cell.complete = True
            if clue == 8:
                if cell.yPos >= clue - 3 or cell.yPos <= clue + 3:
                    cell.state = FILL
                    cell.complete = True
            if clue == 9:
                if cell.yPos >= clue - 4 or cell.yPos <= clue + 4:
                    cell.state = FILL
                    cell.complete = True
            if clue == 10:
                if cell.yPos >= clue - 5 or cell.yPos <= clue + 5:
                    cell.state = FILL
                    cell.complete = True



fillChars = {0: ".", 1:"@", 2:"X"}

for j in range(gridSize):
    column = []
    for i in range(gridSize):
        column.append(0)
    grid.append(column)


def printGrid():
    print("---------------")

    for y in range(gridSize):
        for x in range(gridSize):
            print(fillChars[grid[x][y]], end="")
        print()
    print("---------------")



def fillInAddsUpToGrid(clueNumber, clue):
    print("Filling adds up to Grid")
    pos = 1
    for i in clue:
        for j in range(i):
            fillCells(pos, pos,clueNumber, clueNumber,FILL)
            pos += 1
        if pos < gridSize:
            fillCells(pos, pos, clueNumber, clueNumber, EMPTY)

def fillInAddsUpToGridCols(clueNumber, clue):
    print("Filling adds up to Grid Cols")
    pos = 1
    for i in clue:
        for j in range(i):
            fillCells(clueNumber, clueNumber,pos,pos,FILL)
            pos += 1
        if pos < gridSize:
            fillCells(clueNumber, clueNumber,pos,pos, EMPTY)

def fillCells(startX, endX, startY, endY, fillChar):
    x = startX - 1
    while x < endX:
        y = startY - 1
        while y < endY:
            grid[x][y] = fillChar
            y += 1
        x += 1


def checkRows():
    clueNumber = 0
    for clue in rowClues:
        print(clue)

        # The easiest are 0 and gridSize
        if len(clue) == 1:
            if clue[0] == gridSize:
                fillCells(1, gridSize, clueNumber, clueNumber, FILL)
            if clue[0] == 0:
                fillCells(1, gridSize, clueNumber, clueNumber,EMPTY)

            # Do the large numbers
            if clue[0] == 8:
                fillCells(8,8,clueNumber, clueNumber, FILL)
            elif clue[0] == 9:
                fillCells(7,9,clueNumber, clueNumber, FILL)
            elif clue[0] == 10:
                fillCells(6,10,clueNumber, clueNumber, FILL)
            elif clue[0] == 11:
                fillCells(5,11,clueNumber, clueNumber, FILL)
            elif clue[0] == 12:
                fillCells(4,12,clueNumber, clueNumber, FILL)
            elif clue[0] == 13:
                fillCells(3,13,clueNumber, clueNumber, FILL)
            elif clue[0] == 14:
                fillCells(2,14,clueNumber, clueNumber, FILL)


        else:
            #  Now look at rows adding up to gridSize
            addsUpToGrid = 0
            for i in clue:
                addsUpToGrid += i
            addsUpToGrid += (len(clue) - 1)

            if addsUpToGrid == gridSize:
                fillInAddsUpToGrid(clueNumber, clue)

        # Look at next clue
        clueNumber += 1

def checkColumns():
    clueNumber = 0
    for clue in colClues:
        print(clue)

        # The easiest are 0 and gridSize
        if len(clue) == 1:
            if clue[0] == gridSize:
                fillCells(clueNumber,clueNumber, 1, gridSize, FILL)
            if clue[0] == 0:
                fillCells(clueNumber, clueNumber,1,gridSize,EMPTY)

            # Do the large numbers
            if clue[0] == 8:
                fillCells(clueNumber, clueNumber,8,8, FILL)
            elif clue[0] == 9:
                fillCells(clueNumber, clueNumber,7,9, FILL)
            elif clue[0] == 10:
                fillCells(clueNumber, clueNumber,6,10, FILL)
            elif clue[0] == 11:
                fillCells(clueNumber, clueNumber,5,11, FILL)
            elif clue[0] == 12:
                fillCells(clueNumber, clueNumber,4,12, FILL)
            elif clue[0] == 13:
                fillCells(clueNumber, clueNumber,3,13, FILL)
            elif clue[0] == 14:
                fillCells(clueNumber, clueNumber,2,14, FILL)


        else:
            #  Now look at rows adding up to gridSize
            addsUpToGrid = 0
            for i in clue:
                addsUpToGrid += i
            addsUpToGrid += (len(clue) - 1)
            if addsUpToGrid == gridSize:
                fillInAddsUpToGridCols(clueNumber, clue)

        # Look at next clue
        clueNumber += 1

checkRows()
checkColumns()
printGrid()




FILL = 1
EMPTY = 2
BLANK = 0

#rowClues = [ [1],[3],[3],[5],[6],[9],[10],[7,2],[6,1],[7],[7,1],[1,8],[11],[9],[1,3]]

#colClues = [[1],[3],[3,2],[4,4], [6,3],[7,5],[2,12],[11],[9],[9],[8],[5],[1,1],[2,1],[2]]


rowClues = [[1], [2], [1,6], [9], [6], [5], [5], [4], [3], [4]]
colClues = [[2], [1,1], [4], [2,1], [3,1], [8], [8], [7], [5], [3]]

class Cell:
    def __init__(self,x,y):
        self.state = BLANK
        self.xPos = x
        self.yPos = y
        self.complete = False

class Grid:
    def __init__(self, size):
        self.grid = []
        self.gridSize = size
        self.grid = [[0 for x in range(self.gridSize)] for y in range(self.gridSize)]

    def setValue(self,x,y,value):
        self.grid[x][y] = value

    def setLine(self,startX, startY, endX, endY, value):

        y = startY
        while y <= endY:
            x = startX
            while x <= endX:
                self.setValue(x,y,value)
                x += 1
            y += 1

    def get(self,x,y):
        return self.grid[x][y]

    def print(self):
        print("---------------")
        for y in range(self.gridSize):
            for x in range(self.gridSize):
                if self.grid[x][y] == 0:
                    print(".", end="")
                if self.grid[x][y] == 1:
                    print("#", end="")
                if self.grid[x][y] == 2:
                    print("X", end="")
            print()

        print("---------------")

    def findFilledInCellRow(self,row):
        for i in range(grid.gridSize):
            if self.grid[i][row] == 1:
                return (i)
        return (0)



grid = Grid(10)
grid.print()

# Now fill in the first clues with the big numbers
row = 0
for clue in rowClues:

    # Deal with single clues first
    if len(clue) == 1:
        hint = clue[0]
        if hint > (grid.gridSize/2):
            checkDiff = hint - (grid.gridSize/2)
            startX = row
            startY = int((grid.gridSize/2) - checkDiff)
            endX = row
            endY = int((grid.gridSize/2) + checkDiff) - 1
            grid.setLine(startX,startY,endX,endY, 1)
            #print("Row Clue:" + str(hint))
            grid.print()
    row += 1

col = 0
for clue in colClues:

    # Deal with single clues first
    if len(clue) == 1:
        hint = clue[0]
        if hint > (grid.gridSize/2):
            checkDiff = hint - (grid.gridSize/2)
            startX = int((grid.gridSize/2) - checkDiff)
            startY = col

            endX = int((grid.gridSize/2) + checkDiff) - 1
            endY = col

            grid.setLine(startX,startY,endX,endY, 1)
            #print("Col Clue:" + str(hint))
            grid.print()
    col += 1


# Now Cross out Squares where we can starting with the singletons
for y in range (grid.gridSize):
    for x in range (grid.gridSize):
        if grid.get(x,y) == 1:
            if len(colClues[y]) == 1:
                if colClues[y] == 1:
                    grid.setValue(x-1,y,2)
                    grid.setValue(x+1,y,2)
            else:
                if colClues[y][0] == 1:
                    grid.setValue(x-1,y,2)
                    grid.setValue(x+1,y,2)

# Fill in the Xs for lines where there is 1 clue and space ie (2) .....#.... = XXXX.#.XXX
y = 0
for clue in colClues:
    if clue == 1:
        hint = clue[0]
        x = grid.findFilledInCellRow(y)
        if x != 0:
            if x - hint > 0:
                startX = x - hint
                startY = y
                endX = x - 1
                endY = y
                grid.setLine(startX,startY,endX,endY,2)
                startX = x + hint
                startY = y
                endX = grid.gridSize
                endY = y
                grid.setLine(startX,startY,endX,endY,2)
    y += 1



grid.print()
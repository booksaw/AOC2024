grid = []

posY = 0
posX = 0
lineNo = 0

for line in open("d6/input.txt"):
    grid.append(list(line.replace("\n", "")))
    if "^" in line:    
        posY = lineNo
        posX = line.index("^")
    lineNo += 1

facing = [-1, 0]

class Grid:
    def __init__(self, grid):
        self.grid = [row[:] for row in grid]

    def turnRight(self, facing):
        return [facing[1], facing[0] * -1]

    def isObstacle(self, y, x):
        return self.grid[y][x] == "#"

    def hasTravelled(self, y, x):
        return self.grid[y][x] == "X" or self.grid[y][x] == "^"

    def isOffGrid(self, y, x): 
        if y < 0 or x < 0 or len(self.grid) <= y or len(self.grid[y]) <= x:
            return True
        return False
    
    def setElement(self, y, x, ele):
        self.grid[y][x] = ele

    def nextPosition(self, y , x, facing):
        return (y + facing[0], x + facing[1])

    def printGrid(self):
        for line in self.grid:
            print(''.join(line))

print(posY, posX)
print()

def testGrid(grid, posX, posY, facing):
    turnsSinceNew = 0
    while True:
        newY, newX = grid.nextPosition(posY, posX, facing)
        if grid.isOffGrid(newY, newX):
            break
        elif grid.isObstacle(newY, newX):
            facing = grid.turnRight(facing)
            continue
        elif not grid.hasTravelled(newY, newX):
            grid.setElement(newY, newX, 'X')
            turnsSinceNew = 0
        else:
            turnsSinceNew += 1
            if turnsSinceNew > len(grid.grid) ** 2:
                return False
        posY = newY
        posX = newX
    return True

grid[posY][posX] = "1"

totalCount = 0

for i in range(len(grid)):
    print("Progress: ", i/len(grid) * 100)
    for j in range(len(grid[i])):
        if grid[i][j] == ".":
            gridCopy = [row[:] for row in grid]
            gridCopy[i][j] = "#"
            fail = False
            if not testGrid(Grid(gridCopy), posX, posY, facing):
                totalCount += 1



print("Valid placements:", totalCount)

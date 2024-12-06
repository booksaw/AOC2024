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
independentCount = 1


def turnRight(facing):
    return [facing[1], facing[0] * -1]

def isObstacle(y, x):
    return grid[y][x] == "#"

def hasTravelled(y, x):
    return grid[y][x] == "X" or grid[y][x] == "^"

def isOffGrid(y, x): 
    if y < 0 or x < 0 or len(grid) <= y or len(grid[y]) <= x:
        return True
    return False

def nextPosition(y , x, facing):
    return (y + facing[0], x + facing[1])

def printGrid():
    for line in grid:
        print(''.join(line))

# printGrid()
print(posY, posX)
print()

for i in range(50000):
    newY, newX = nextPosition(posY, posX, facing)
    # print(newY, newX)
    if isOffGrid(newY, newX):
        break
    elif isObstacle(newY, newX):
        facing = turnRight(facing)
        continue
    elif not hasTravelled(newY, newX):
        independentCount += 1
        grid[newY][newX] = 'X'
    posY = newY
    posX = newX


grid[posY][posX] = "1"
printGrid()
print("Unique Squares:", independentCount)

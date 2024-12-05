search = []

for line in open("d4/input.txt"):
    search.append(list(line.replace("\n", "")))

foundCount = 0
# search for horizontal occurrences
for row in range(1, len(search) -1 ):
    for column in range(1, len(search[row]) -1):
        if(search[row][column] == 'A'):
            foundX = 0
            for x in range(-1, 2, 1):
                for y in range(-1, 2, 1):
                    if abs(x) + abs(y) == 2 and 'M' == search[row + x][column + y] and 'S' == search[row - x][column - y]:
                        foundX += 1
            if foundX == 2: 
                foundCount += 1
                print("diagonal", row, column)


print(foundCount)

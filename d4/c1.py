search = []

for line in open("d4/input.txt"):
    search.append(list(line.replace("\n", "")))

searchString = ['X', 'M', 'A', 'S']

foundCount = 0
# search for horizontal occurrences
for row in range(0, len(search)):
    for column in range(0, len(search[row])):

        if(search[row][column] == searchString[0]):
            for x in range(-1, 2, 1):
                for y in range(-1, 2, 1):
                    try: 
                        for i in range(1, len(searchString)):
                            # print(row, column, x, y, i)
                            if row + (x * i) < 0 or column + (y * i) < 0 or searchString[i] != search[row + (x * i)][column + (y * i)]:
                                # print("fail")
                                break
                            elif i == len(searchString)-1: 
                                foundCount += 1
                                # print("Success")
                    except Exception as e:
                        print(e)


print(foundCount)
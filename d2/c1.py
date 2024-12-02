safeCount = 0
with open("d2/input.txt") as file:
    for line in file:
        arr = line.split(" ")
        asc = None
        prev = None
        fail = False
        for i in arr:
            i = int(i)
            if prev == None:
                prev = i
                continue
            if (i >= prev and asc == False) or (i <= prev and asc == True) or (abs(i-prev) > 3) or (i == prev):
                fail = True
                break
            asc = (i > prev)
            prev = i
        if fail == False: safeCount += 1 
print (safeCount)
# this is a horrible and really inefficient way of solving this problem
# The solution I have used is turning brute force up to its maximum
import numpy as np

def isSafeCombo(arr):
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
    if (not fail): print("Array is safe: ", arr)
    return not fail

safeCount = 0
with open("d2/input.txt") as file:
    for line in file:
        arr = line.replace("\n", "").split(" ")
        if isSafeCombo(arr):
            safeCount += 1
        else:
            for i in range(0, len(arr)):
                print(arr, i)
                newArr = arr.copy()
                newArr.pop(i)
                if isSafeCombo(newArr):
                    safeCount += 1
                    break
print (safeCount)
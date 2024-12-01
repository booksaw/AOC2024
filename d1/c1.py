import numpy as np
import pandas as pd

inputArr = pd.read_csv('d1/c1input.txt', sep='   ', header=None)

print("input Arr", inputArr)

leftv, rightv = np.hsplit(inputArr, 2)
leftv = np.sort(leftv, axis=0)
rightv = np.sort(rightv, axis=0)

print("Left values:", leftv)
print("Right values:", rightv)

resultArr = abs(leftv - rightv)

print("ResultArr:", resultArr)

result = np.sum(resultArr)

print("Result:", result)
import numpy as np
import pandas as pd

inputArr = pd.read_csv('d1/c1input.txt', sep='   ', header=None)

print("input Arr", inputArr)

leftv, rightv = np.hsplit(inputArr, 2)
leftv = np.sort(leftv, axis=0)
rightv = np.sort(rightv, axis=0)

print("Left values:", leftv)
print("Right values:", rightv)

rightvUnique, rightvCounts = np.unique(rightv, return_counts=True)
rightVUniqueCounts = dict(zip(rightvUnique, rightvCounts))

total = 0
for ele in leftv:
    if(ele[0] in rightVUniqueCounts):
        total += ele[0] * rightVUniqueCounts[ele[0]]

print("Total:", total)
# CCC '15 S1
numsList = []

import sys
data = sys.stdin.readline


for i in range(0, int(data()), 1):
    nums = int(input())
    
    if nums > 0:
        numsList.append(nums)
    
    elif nums == 0:
        numsList.pop()
    
finalSum = sum(numsList)
print(finalSum)

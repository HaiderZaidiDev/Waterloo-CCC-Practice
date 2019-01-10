# CCC '15 S1
numsList = []

for i in range(0, int(input()), 1):
    nums = int(input())
    
    if nums > 0:
        numsList.append(nums)
    
    elif nums == 0:
        numsList.pop()
    
finalSum = sum(numsList)
print(finalSum)

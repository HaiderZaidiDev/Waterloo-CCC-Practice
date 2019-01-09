numbers = int(input())
numsList[]

for nums in numbers:
  if nums > 0:
    numsList.append(nums)
  else:
    numsList.pop()

totalSum = sum(numsList)
print(totalSum)

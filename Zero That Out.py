numsList = []

for i in range(input()):
  nums = input()
  
  if nums > 0:
    numsList.append(nums)
  else:
    numsList.pop(nums)

totalSum = sum(numsList)
print(totalSum)

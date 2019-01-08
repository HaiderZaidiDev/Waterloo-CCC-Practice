#--- CodeChef ATM Beginner Prompt
# https://www.codechef.com/problems/HS08TEST

atmInfo = input().split()

withdrawAMNT = float(atmInfo[0])
accBalance = float(atmInfo[1])

if withdrawAMNT % 5 != 0:
  print(accBalance) 
elif withdrawAMNT > accBalance - 0.5:
  print(accBalance)

else:
  print(accBalance - withdrawAMNT - 0.5)
  

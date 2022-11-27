# exercise one of three
# sum of n natural numbers
# ask a user for natural numbers
# print total from 1 to n 

n = int(input("Enter a number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i +=1
print(sum)
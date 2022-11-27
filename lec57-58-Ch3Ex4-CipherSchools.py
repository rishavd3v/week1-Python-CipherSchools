# problem
# ask user to input a number containing more than one digit
# example - 1237
# calculate 1+2+3+7

#solution

n = input("Enter a number: ")
sum = 0
i = 0
while i<len(n):
    sum += int(n[i])
    i += 1
print(sum)

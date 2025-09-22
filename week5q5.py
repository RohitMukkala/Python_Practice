"""Write a Python program to calculate sum of digits of a number."""

s = int(input("Enter a number: "))
sum = 0
while s>0:
    sum+=s%10
    s//=10

print(sum)
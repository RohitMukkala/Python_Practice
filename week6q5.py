"""Write a Python program to calculate factorial of a number"""
n = int(input("Enter a number: "))
s = 1
while n>0:
    s=s*n
    n-=1

print(s)
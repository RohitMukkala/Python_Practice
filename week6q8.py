"""Write a Python program to print Fibonacci series up to n terms"""

n = int(input("Enter a number: "))

a = 0
b=1
series = []
for _ in range(n):
    series.append(a)
    a,b=b,b+a

print(series)
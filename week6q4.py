"""Write a Python program to find all factors of a number."""

n = int(input("Enter a number: "))

factorials = []
for i in range(1,n+1):
    if n%i==0:
        factorials.append(i)

print(factorials)
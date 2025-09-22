"""Write a Python program to count number of digits in a number."""

n = int(input("Enter a number: "))
count = 0

# Convert negative numbers to positive
n = abs(n)

# Special case for zero
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10  # Remove the last digit of the number

print("Number of digits:", count)

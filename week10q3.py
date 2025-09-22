def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Get input from the user
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

result = gcd(a, b)
print(f"The GCD of {a} and {b} is: {result}")

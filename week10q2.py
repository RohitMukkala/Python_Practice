def sum_series(n):
    total = 0
    while n > 0:
        total += n
        n -= 2
    return total

# Get input from the user
n = int(input("Enter a positive integer n: "))
if n > 0:
    result = sum_series(n)
    print(f"The sum of the series is: {result}")
else:
    print("Please enter a positive integer greater than 0.")

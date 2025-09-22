def harmonic_sum(n):
    if n <= 1:
        return 0  
    
    total = 0.0
    for i in range(1, n):
        total += 1 / i
    return total

n = int(input("Enter a positive integer n: "))
if n > 0:
    result = harmonic_sum(n)
    print(f"The harmonic sum of {n-1} is: {result}")
else:
    print("Please enter a positive integer greater than 0.")

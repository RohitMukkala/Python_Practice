def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

number = int(input("Enter a non-negative integer: "))
if number >= 0:
    result = sum_of_digits(number)
    print(f"The sum of the digits is: {result}")
else:
    print("Please enter a non-negative integer.")

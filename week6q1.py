"""Write a Python program to check whether a number is palindrome or not."""

original_number = int(input("Enter a number: "))
temp_number = original_number  
reversed_number = 0

while temp_number > 0:
    reversed_number = reversed_number * 10 + temp_number % 10
    temp_number //= 10

if original_number == reversed_number:
    print(f"The number {original_number} is a palindromic number.")
else:
    print(f"The number {original_number} is not a palindromic number.")

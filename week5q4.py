"""Write a Python program to find first and last digit of a number"""

s = int(input("ENTER a number: "))

last_digit = s%10
first_digit = s
while first_digit>=10:
    first_digit//=10

print(f"First digit is '{first_digit}' , last digit is '{last_digit}'.")
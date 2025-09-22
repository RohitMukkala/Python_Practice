"""Write a python program to input any character and check whether it is alphabet, digit or special character."""

char = input("Enter any character: ")

if len(char) != 1:
    print("Please enter a single character.")
else:
    ascii_value = ord(char)

    if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
        print(f"'{char}' is an alphabet.")
    elif 48 <= ascii_value <= 57:
        print(f"'{char}' is a digit.")
    else:
        print(f"'{char}' is a special character.")

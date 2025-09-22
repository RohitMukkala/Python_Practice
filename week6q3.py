"""Write a Python program to print all ASCII character with their values."""

# Printing ASCII characters with their values
print("ASCII Character Table")
print("----------------------")
print("Char  |  ASCII Value")
print("----------------------")

# Loop through ASCII values from 0 to 127
for ascii_value in range(128):
    # Convert ASCII value to character using chr() function
    character = chr(ascii_value)
    # Print character and its ASCII value
    print(f"  {character}   |    {ascii_value}")

print("----------------------")
